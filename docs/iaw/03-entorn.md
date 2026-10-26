# UT1 · 3. Docker Compose i un entorn que pots reconstruir

## Conceptes abans de copiar configuracions

Una **imatge** és la base amb què es crea un contenidor. Un **contenidor** és una instància d'eixa imatge, que pot estar parada o executant-se. Un **servei de Compose** descriu com crear-lo: imatge, configuració, xarxa, muntatges i ports.

Un muntatge de carpeta (*bind mount*) connecta una ruta del teu equip amb una del contenidor. Un volum amb nom és emmagatzematge gestionat per Docker; és adequat per a dades que han de sobreviure a la substitució del contenidor.

## Laboratori resolt: cartellera d'un cineclub

Aquest exemple nou aïlla la comunicació Nginx–PHP, sense reproduir la pràctica de desplegament de classe. Necessites Docker amb Compose. Crea una carpeta de proves amb aquesta estructura:

```text
cineclub/
├── compose.yaml
├── .env.example
├── .env
├── .gitignore
├── web.conf
└── public/
    └── index.php
```

`compose.yaml`:

```yaml
services:
  cartellera:
    image: nginx:stable-alpine
    ports:
      - "127.0.0.1:${WEB_PORT:-8092}:80"
    volumes:
      - ./public:/srv/cineclub:ro
      - ./web.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - motor
  motor:
    image: php:8.3-fpm-alpine
    volumes:
      - ./public:/srv/cineclub:ro
```

`web.conf`:

```nginx
server {
    listen 80;
    root /srv/cineclub;
    index index.php;
    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        try_files $uri =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass motor:9000;
    }
}
```

`public/index.php`:

```php
<?php
$titol = 'Sessió de curtmetratges';
?>
<h1><?= htmlspecialchars($titol, ENT_QUOTES, 'UTF-8') ?></h1>
<p>El motor PHP ha generat aquesta cartellera.</p>
```

`.env.example` i la còpia local `.env`:

```dotenv
WEB_PORT=8092
```

`.gitignore`:

```gitignore
.env
```

### Per què funciona?

1. El navegador connecta al port **8092 de l'amfitrió**, publicat cap al **80 de Nginx**. El prefix `127.0.0.1` limita l'accés al mateix equip.
2. Nginx busca `index.php` a `/srv/cineclub`.
3. `motor` és el nom DNS del servei PHP dins de la xarxa de Compose. Des de Nginx, `localhost` seria el contenidor de Nginx, no PHP.
4. Els dos contenidors veuen el mateix codi en la mateixa ruta; PHP pot obrir el fitxer que Nginx li indica.
5. `:ro` permet llegir el muntatge, però impedeix escriure-hi des del contenidor.

### Ordres i comprovació

Des de la carpeta `cineclub`:

```bash
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
curl -i http://localhost:8092/
docker compose logs --tail=30 cartellera motor
docker compose down
```

**Resultat esperat:** estat HTTP 200 i una cartellera amb «Sessió de curtmetratges». `config` comprova i resol la configuració; `ps` mostra l'estat; `logs` ajuda a investigar. `down` elimina els contenidors i la xarxa del projecte. `depends_on` ordena l'arrancada, però amb aquesta forma no garanteix que una aplicació estiga preparada per a atendre peticions.

## I si afegim una base de dades?

MariaDB seria un altre servei, per exemple `arxiu`. PHP connectaria a `arxiu:3306`, no al port de l'amfitrió. Un volum com `dades_arxiu:/var/lib/mysql` conservaria la informació. Els scripts de `/docker-entrypoint-initdb.d/` s'apliquen en la inicialització d'un directori de dades buit; no es tornen a executar simplement perquè edites el SQL.

Un Dockerfile permet derivar una imatge, per exemple amb `FROM php:8.3-fpm-alpine` i `RUN docker-php-ext-install pdo_mysql` per a disposar del controlador PDO de MySQL/MariaDB. Després Compose usa `build:` i cal reconstruir la imatge. La connexió i les consultes es treballen als [apunts complementaris de PDO](../php/05-pdo.md).

## `.env`, `environment` i `env_file`

Compose pot llegir `.env` per a substituir `${WEB_PORT}` en el YAML. Això **no introdueix automàticament totes les variables dins de PHP**. `environment:` passa variables concretes al servei; `env_file:` carrega un fitxer de variables dins del contenidor. Un `.env.example` documenta els noms amb valors de prova; les credencials reals no han d'anar al repositori.

Les etiquetes d'imatge d'aquest exemple són mòbils. Per a repetir exactament una versió cal registrar-ne una versió immutable o el digest, a més del procediment.

| Símptoma | Què revises primer |
| --- | --- |
| Port ocupat | Canvia `WEB_PORT` i recrea el servei. |
| 404 | Fitxer, `root`, ruta del muntatge i URL. |
| 502 | Estat de `motor`, nom DNS i port FastCGI. |
| PHP no veu una variable | `environment` o `env_file`, no només `.env`. |
| Dades desaparegudes | Volum usat i si s'ha eliminat. `down -v` elimina volums. |

!!! success "Per a repassar"
    Explica cada costat d'un port i d'un muntatge. Per a reconstruir el projecte necessites codi, configuració, variables documentades i passos de verificació.

---

Font del temari: [apunts originals de UT1](https://victoria-nr.github.io/iaw-alumnos/UT1/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
