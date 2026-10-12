# 7. Desplegar aplicacions

**Desplegar** és posar una aplicació en un servidor perquè la puguen usar els usuaris. En IAW, sovint no es programa l'aplicació: s'**instal·la** una que ja existix (WordPress, Moodle, Nextcloud) o la que ha fet l'equip de desenvolupament.

## Què necessita una aplicació PHP

| Peça | En Debian/Ubuntu |
| ---- | ---------------- |
| Servidor web | `apache2` (amb `libapache2-mod-php`) o `nginx` (amb `php-fpm`) |
| PHP i les **extensions** que demane | `php`, `php-pgsql`, `php-mysql`, `php-mbstring`, `php-xml`, `php-curl`, `php-gd`, `php-zip`, `php-intl` |
| Base de dades | `postgresql` o `mariadb-server` |
| Una base de dades i un usuari per a l'aplicació | `CREATE DATABASE` + `CREATE USER` + `GRANT` |
| Un nom (DNS) i HTTPS | un registre DNS que apunte al servidor i un certificat (Let's Encrypt: `sudo certbot --apache`) |

```bash
php -m                       # extensions carregades
php --ini                    # quin php.ini s'usa (el de la CLI és diferent del d'Apache!)
```

## Desplegar l'aplicació CRUD en Apache

```bash
# 1. Paquets
sudo apt install apache2 libapache2-mod-php php-pgsql postgresql

# 2. Base de dades i usuari
sudo -u postgres createdb institut
sudo -u postgres psql -d institut -f institut.sql
sudo -u postgres psql -d institut -c "CREATE ROLE app LOGIN PASSWORD 'una-contrasenya-llarga';"
sudo -u postgres psql -d institut -c "GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app;"
sudo -u postgres psql -d institut -c "GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app;"

# 3. El codi
sudo mkdir -p /var/www/alumnes
sudo unzip crud-alumnes.zip -d /var/www/alumnes
sudo nano /var/www/alumnes/config.php          # port 5432 i la contrasenya bona

# 4. Permisos: de root, i que Apache només puga LLEGIR
sudo chown -R root:www-data /var/www/alumnes
sudo find /var/www/alumnes -type d -exec chmod 750 {} +
sudo find /var/www/alumnes -type f -exec chmod 640 {} +
```

```text title="/etc/apache2/sites-available/alumnes.conf"
<VirtualHost *:80>
    ServerName alumnes.institut.local
    DocumentRoot /var/www/alumnes

    <Directory /var/www/alumnes>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>

    <Files "config.php">
        Require all denied
    </Files>

    ErrorLog ${APACHE_LOG_DIR}/alumnes_error.log
    CustomLog ${APACHE_LOG_DIR}/alumnes_access.log combined
</VirtualHost>
```

```bash
sudo a2ensite alumnes
sudo apache2ctl configtest && sudo systemctl reload apache2
curl -I http://alumnes.institut.local
```

!!! danger "Els permisos"
    - El servidor web (**`www-data`**) ha de poder **llegir** el codi, però **no modificar-lo**: si hi ha una vulnerabilitat, l'atacant no podrà canviar els fitxers.
    - Només les carpetes on l'aplicació ha d'**escriure** (pujades, memòria cau) han de ser de `www-data` amb escriptura. I que no s'hi puga executar PHP.
    - **Mai** `chmod 777`.

!!! tip "La configuració fora del `DocumentRoot`"
    Encara millor que bloquejar `config.php`: posar-lo **fora** de la carpeta pública (per exemple, `/etc/alumnes/config.php` o `/var/www/alumnes-config/`), i que la web només tinga la carpeta `public/` com a `DocumentRoot`. Així ho fan els *frameworks*.

### `php.ini` de producció

En `/etc/php/8.3/apache2/php.ini` (o `fpm/php.ini`):

```ini
display_errors = Off
log_errors = On
expose_php = Off
upload_max_filesize = 10M
post_max_size = 12M
memory_limit = 256M
session.cookie_httponly = 1
session.cookie_secure = 1
date.timezone = Europe/Madrid
```

```bash
sudo systemctl restart apache2        # (o php8.3-fpm)
```

## Amb Nginx i PHP-FPM

```nginx title="/etc/nginx/sites-available/alumnes"
server {
    listen 80;
    server_name alumnes.institut.local;
    root /var/www/alumnes;
    index index.php;

    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
    }
    location = /config.php { deny all; }
}
```

Nginx no executa PHP: li passa els `.php` a PHP-FPM pel *socket* (`fastcgi_pass`).

## Amb Docker

Tot l'entorn (PHP + Apache + PostgreSQL) en dos fitxers. Vegeu [Docker Compose](../docker/06-compose.md).

```dockerfile title="Dockerfile"
FROM php:8.3-apache
RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq-dev \
    && docker-php-ext-install pdo_pgsql \
    && rm -rf /var/lib/apt/lists/*
```

```yaml title="compose.yaml"
services:
  web:
    build: .
    ports:
      - "8080:80"
    volumes:
      - ./src:/var/www/html
    environment:
      DB_DSN: "pgsql:host=bd;port=5432;dbname=institut"
      DB_USER: app
      DB_PASS: canvia-la
    depends_on:
      - bd

  bd:
    image: postgres:16
    environment:
      POSTGRES_DB: institut
      POSTGRES_USER: app
      POSTGRES_PASSWORD: canvia-la
    volumes:
      - dades:/var/lib/postgresql/data
      - ./institut.sql:/docker-entrypoint-initdb.d/institut.sql:ro

volumes:
  dades:
```

I en `config.php`, llegir les variables d'entorn (amb valors per defecte per a treballar sense Docker):

```php title="config.php"
<?php
return [
    "dsn"  => getenv("DB_DSN")  ?: "pgsql:host=127.0.0.1;port=5432;dbname=institut",
    "user" => getenv("DB_USER") ?: "app",
    "clau" => getenv("DB_PASS") ?: "canvia-la",
];
```

```bash
docker compose up -d --build
docker compose logs -f web
# http://localhost:8080
```

- El nom del servei (`bd`) és el **nom de host** de la base de dades dins de la xarxa de Compose.
- Els fitxers `.sql` de `/docker-entrypoint-initdb.d/` s'executen **la primera vegada** que es crea el volum.

## Instal·lar un CMS: WordPress

Un **CMS** (*Content Management System*) és una aplicació per a fer webs sense programar: WordPress, Joomla, Drupal. Altres aplicacions habituals: **Moodle** (aula virtual), **Nextcloud** (núvol de fitxers), **PrestaShop** (botiga).

=== "En el servidor (Apache + MariaDB)"

    ```bash
    sudo apt install apache2 mariadb-server php libapache2-mod-php php-mysql php-xml php-mbstring php-curl php-gd php-zip php-intl
    sudo mysql_secure_installation
    sudo mariadb
    ```
    ```sql
    CREATE DATABASE wordpress CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
    CREATE USER 'wp'@'localhost' IDENTIFIED BY 'una-contrasenya-llarga';
    GRANT ALL PRIVILEGES ON wordpress.* TO 'wp'@'localhost';
    FLUSH PRIVILEGES;
    ```
    ```bash
    cd /tmp && wget https://wordpress.org/latest.tar.gz && tar -xzf latest.tar.gz
    sudo mv wordpress /var/www/wordpress
    sudo chown -R www-data:www-data /var/www/wordpress       # WordPress s'actualitza sol: necessita escriure
    ```
    Un `VirtualHost` amb `DocumentRoot /var/www/wordpress` i `AllowOverride All` (usa `.htaccess` per a les URL), `a2enmod rewrite`, i obrir la web: l'**instal·lador** demana les dades de la base de dades i crea `wp-config.php`.

=== "Amb Docker"

    ```yaml title="compose.yaml"
    services:
      wordpress:
        image: wordpress:6
        ports:
          - "8081:80"
        environment:
          WORDPRESS_DB_HOST: bd
          WORDPRESS_DB_USER: wp
          WORDPRESS_DB_PASSWORD: canvia-la
          WORDPRESS_DB_NAME: wordpress
        volumes:
          - wp:/var/www/html
        depends_on:
          - bd
      bd:
        image: mariadb:11
        environment:
          MARIADB_DATABASE: wordpress
          MARIADB_USER: wp
          MARIADB_PASSWORD: canvia-la
          MARIADB_RANDOM_ROOT_PASSWORD: "1"
        volumes:
          - bd:/var/lib/mysql
    volumes:
      wp:
      bd:
    ```

**Després d'instal·lar un CMS:** actualitzacions (del nucli i dels *plugins*: és per on entren la majoria d'atacs), còpies de seguretat de **la base de dades i els fitxers**, HTTPS, i pocs *plugins* (i de fonts de confiança).

## Composer: les dependències

Les aplicacions PHP modernes usen **Composer** per a descarregar les biblioteques que necessiten (com `pip` en Python o `npm` en JavaScript).

```bash
sudo apt install composer
composer install --no-dev --optimize-autoloader    # en producció: instal·la el que diu composer.lock
composer require monolog/monolog                   # afegir una dependència (en desenvolupament)
```

Es descarreguen en `vendor/` (que **no** es puja a Git ni ha de ser accessible des de la web).

## Desplegar amb Git

```bash
cd /var/www/alumnes
sudo -u desplegament git pull          # baixar l'última versió
composer install --no-dev
sudo systemctl reload php8.3-fpm       # (si cal)
```

Vegeu [Git](../git/index.md). En equips més grans, ho fa automàticament una eina d'**integració i desplegament continus** (CI/CD): GitHub Actions, GitLab CI.

## Errors típics

| Problema | Per què | Solució |
| -------- | ------- | ------- |
| **500** i pàgina en blanc | Error de PHP amb `display_errors = Off` | `tail /var/log/apache2/error.log` |
| `could not find driver` | Falta `php-pgsql` (o `php-mysql`) **per a Apache/FPM** | Instal·la'l i reinicia Apache o PHP-FPM (`php -m` de la CLI pot dir que sí: és un altre `php.ini`) |
| `Permission denied` en guardar fitxers | `www-data` no pot escriure en eixa carpeta | `chown www-data` **només** d'eixa carpeta |
| Les URL amigables de WordPress donen 404 | Falta `a2enmod rewrite` o `AllowOverride All` | Activa'ls |
| WordPress demana dades FTP per a actualitzar | No pot escriure en la seua carpeta | Propietari `www-data` |
| `Connection refused` a la BD des de Docker | Has posat `localhost` en el DSN | El **nom del servei**: `host=bd` |
| Es veu el codi de `config.php` | El servidor no executa PHP, o és un fitxer de còpia (`config.php.bak`) | PHP instal·lat; esborra les còpies; configuració fora del `DocumentRoot` |

!!! success "Per a l'examen"
    - Servidor web + PHP (+ **extensions**) + BD + usuari de BD propi + DNS + HTTPS
    - Codi **de root, llegible per `www-data`** · escriptura només on cal · mai `777` · `config.php` protegit o fora del `DocumentRoot`
    - `php.ini` de producció: `display_errors = Off`, `log_errors = On`, `expose_php = Off`
    - Docker: imatge `php:8.3-apache` + `docker-php-ext-install pdo_pgsql` · BD per **nom de servei** · variables d'entorn
    - CMS: BD + usuari + fitxers + instal·lador web · **actualitzacions** i **còpies** (BD i fitxers)
    - Composer: `composer install --no-dev` · `vendor/` fora de Git
