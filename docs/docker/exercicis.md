# Exercicis resolts

Fes-los en ordre: cada un usa coses de l'anterior. Per a cada exercici, crea una carpeta nova.

!!! tip "Abans de començar"
    Comprova que Docker funciona amb `docker run hello-world`. Si algun contenidor no arranca, el primer que has de mirar és `docker logs NOM` (o `docker compose logs`).

## Nivell bàsic

### 1. La teua pàgina web en un contenidor

Servix una pàgina `index.html` feta per tu amb Nginx en el port 8080. Has de poder editar la pàgina i veure el canvi sense reiniciar el contenidor.

??? success "Solució"

    ```bash
    # 1. Crear la pàgina
    mkdir -p ~/docker/ex1/web && cd ~/docker/ex1
    echo "<h1>La meua primera web amb Docker</h1>" > web/index.html

    # 2. Arrancar Nginx amb un bind mount de la carpeta web
    docker run -d --name ex1 -p 8080:80 \
        -v "$(pwd)/web":/usr/share/nginx/html:ro \
        nginx:1.27-alpine

    # 3. Comprovar-ho
    curl http://localhost:8080          # o obri-ho en el navegador

    # 4. Editar la pàgina i tornar a comprovar: el canvi es veu al moment
    echo "<h1>Pàgina modificada</h1>" > web/index.html
    curl http://localhost:8080

    # 5. Netejar
    docker rm -f ex1
    ```

    - `-v "$(pwd)/web":/usr/share/nginx/html` connecta la teua carpeta amb la carpeta on Nginx busca la web.
    - `:ro` perquè Nginx només ha de llegir.
    - Com que és un **bind mount**, els canvis en el teu equip es veuen immediatament dins.

### 2. MariaDB que no perd les dades

Arranca un MariaDB amb una base de dades `institut` i un volum. Crea una taula amb dades, esborra el contenidor, torna'l a crear i comprova que les dades continuen.

??? success "Solució"

    ```bash
    # 1. Arrancar MariaDB amb un volum
    docker run -d --name bd \
        -e MARIADB_ROOT_PASSWORD=secret \
        -e MARIADB_DATABASE=institut \
        -v dades_institut:/var/lib/mysql \
        mariadb:11.4

    # 2. Esperar uns segons que arranque i entrar al client de MariaDB
    docker logs bd | tail -3            # ha de dir "ready for connections"
    docker exec -it bd mariadb -u root -psecret institut
    ```

    Dins del client de MariaDB:

    ```sql
    CREATE TABLE alumnes (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(50));
    INSERT INTO alumnes (nom) VALUES ('Ana'), ('Pep');
    SELECT * FROM alumnes;
    exit
    ```

    ```bash
    # 3. Esborrar el contenidor (el volum NO s'esborra)
    docker rm -f bd
    docker volume ls                    # dades_institut continua ací

    # 4. Tornar a crear-lo amb el MATEIX volum
    docker run -d --name bd \
        -e MARIADB_ROOT_PASSWORD=secret \
        -v dades_institut:/var/lib/mysql \
        mariadb:11.4

    # 5. Les dades hi són
    docker exec -it bd mariadb -u root -psecret institut -e "SELECT * FROM alumnes;"

    # 6. Netejar del tot
    docker rm -f bd && docker volume rm dades_institut
    ```

    La segona vegada no cal posar `MARIADB_DATABASE`: la base de dades ja existix dins del volum. Les variables de configuració inicial només s'apliquen quan el volum està **buit**.

### 3. Dos contenidors que parlen: MariaDB + Adminer

Arranca un MariaDB i un **Adminer** (un gestor web de bases de dades) en una xarxa pròpia, de manera que des del navegador pugues gestionar la base de dades. La base de dades **no** s'ha de publicar a l'exterior.

??? success "Solució"

    ```bash
    docker network create xarxa_ex3

    docker run -d --name bd --network xarxa_ex3 \
        -e MARIADB_ROOT_PASSWORD=secret \
        mariadb:11.4

    docker run -d --name adminer --network xarxa_ex3 \
        -p 8081:8080 \
        adminer:4
    ```

    Obri `http://localhost:8081` i entra amb: **Servidor** `bd`, **Usuari** `root`, **Contrasenya** `secret`.

    - Adminer troba la base de dades pel **nom del contenidor** (`bd`) perquè estan en la mateixa xarxa creada per nosaltres.
    - Només Adminer té `-p`. La base de dades queda tancada dins de la xarxa de Docker.

    ```bash
    # Netejar
    docker rm -f bd adminer && docker network rm xarxa_ex3
    ```

## Docker Compose

### 4. WordPress amb Compose i `.env`

Desplega WordPress + MariaDB + Adminer amb un `compose.yaml`. Les contrasenyes han d'estar en un `.env` que **no** es puje a Git, i ha d'haver-hi un `.env.example` com a plantilla.

??? success "Solució"

    Estructura:

    ```text
    ex4/
    ├── compose.yaml
    ├── .env.example
    ├── .env            ← no es puja
    └── .gitignore
    ```

    ```yaml title="compose.yaml"
    services:
      bd:
        image: mariadb:11.4
        restart: unless-stopped
        environment:
          MARIADB_DATABASE: ${DB_NAME}
          MARIADB_USER: ${DB_USER}
          MARIADB_PASSWORD: ${DB_PASSWORD}
          MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
        volumes:
          - dades_bd:/var/lib/mysql

      wordpress:
        image: wordpress:6
        restart: unless-stopped
        depends_on:
          - bd
        environment:
          WORDPRESS_DB_HOST: bd
          WORDPRESS_DB_NAME: ${DB_NAME}
          WORDPRESS_DB_USER: ${DB_USER}
          WORDPRESS_DB_PASSWORD: ${DB_PASSWORD}
        ports:
          - "${WEB_PORT:-8080}:80"
        volumes:
          - dades_wp:/var/www/html

      adminer:
        image: adminer:4
        restart: unless-stopped
        depends_on:
          - bd
        ports:
          - "8081:8080"

    volumes:
      dades_bd:
      dades_wp:
    ```

    ```text title=".env.example"
    DB_NAME=wordpress
    DB_USER=wp
    DB_PASSWORD=canvia_esta_contrasenya
    DB_ROOT_PASSWORD=canvia_esta_tambe
    WEB_PORT=8080
    ```

    ```text title=".gitignore"
    .env
    ```

    ```bash
    cp .env.example .env        # i edita'l amb les contrasenyes
    docker compose up -d
    docker compose ps
    ```

    - WordPress: `http://localhost:8080` · Adminer: `http://localhost:8081` (servidor `bd`).
    - No cal crear cap xarxa: Compose en crea una per al projecte.
    - `${WEB_PORT:-8080}` usa 8080 si la variable no està en el `.env`.

### 5. Entorn PHP + MariaDB reproduïble (estil IAW)

Crea un entorn de desenvolupament per a una aplicació PHP que llig contactes d'una base de dades MariaDB amb PDO. Requisits:

- Qualsevol persona que clone el repositori l'ha d'arrancar amb `cp .env.example .env` i `docker compose up -d --build`.
- El codi PHP s'ha de poder editar sense reconstruir res.
- La base de dades s'ha de crear **automàticament** amb una taula i dades d'exemple.
- La web no ha d'intentar connectar-se fins que la base de dades estiga llesta.
- Un gestor web (Adminer) per a veure la base de dades.

??? success "Solució"

    Estructura:

    ```text
    agenda/
    ├── compose.yaml
    ├── Dockerfile
    ├── .env.example
    ├── .gitignore
    ├── README.md
    ├── bd/
    │   └── 01-esquema.sql
    └── src/
        └── index.php
    ```

    ```yaml title="compose.yaml"
    services:
      web:
        build: .                                  # imatge pròpia amb el Dockerfile d'esta carpeta
        restart: unless-stopped
        ports:
          - "${WEB_PORT:-8080}:80"
        environment:                              # l'aplicació PHP llegirà estes variables
          DB_HOST: bd
          DB_NAME: ${DB_NAME}
          DB_USER: ${DB_USER}
          DB_PASSWORD: ${DB_PASSWORD}
        volumes:
          - ./src:/var/www/html                   # bind mount: edites el codi i es veu al moment
        depends_on:
          bd:
            condition: service_healthy            # espera que MariaDB estiga llesta

      bd:
        image: mariadb:11.4
        restart: unless-stopped
        environment:
          MARIADB_DATABASE: ${DB_NAME}
          MARIADB_USER: ${DB_USER}
          MARIADB_PASSWORD: ${DB_PASSWORD}
          MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
        volumes:
          - dades_bd:/var/lib/mysql               # les dades no es perden
          - ./bd:/docker-entrypoint-initdb.d:ro   # scripts .sql que s'executen la PRIMERA vegada
        healthcheck:
          test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
          interval: 5s
          timeout: 5s
          retries: 10

      adminer:
        image: adminer:4                          # gestor web de la base de dades
        restart: unless-stopped
        ports:
          - "8081:8080"
        depends_on:
          - bd

    volumes:
      dades_bd:
    ```

    ```dockerfile title="Dockerfile"
    FROM php:8.3-apache

    # Extensió PDO per a MariaDB/MySQL (la imatge oficial no la porta)
    RUN docker-php-ext-install pdo_mysql
    ```

    ```text title=".env.example"
    # Copia este fitxer com a .env i canvia les contrasenyes
    DB_NAME=agenda
    DB_USER=app
    DB_PASSWORD=canvia_esta_contrasenya
    DB_ROOT_PASSWORD=canvia_esta_tambe
    WEB_PORT=8080
    ```

    ```sql title="bd/01-esquema.sql"
    -- S'executa automàticament la primera vegada que arranca MariaDB
    CREATE TABLE IF NOT EXISTS contactes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(100) NOT NULL,
        telefon VARCHAR(20)
    );

    INSERT INTO contactes (nom, telefon) VALUES
        ('Ana Puig', '600111222'),
        ('Pep Roig', '611222333');
    ```

    ```php title="src/index.php"
    <?php
    // Les dades de connexió venen de les variables d'entorn del compose.yaml
    $host = getenv('DB_HOST');
    $bd   = getenv('DB_NAME');
    $usu  = getenv('DB_USER');
    $clau = getenv('DB_PASSWORD');

    try {
        $pdo = new PDO("mysql:host=$host;dbname=$bd;charset=utf8mb4", $usu, $clau, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        ]);
        $contactes = $pdo->query('SELECT nom, telefon FROM contactes ORDER BY nom')->fetchAll();
    } catch (PDOException $e) {
        http_response_code(500);
        exit('Error de connexió: ' . htmlspecialchars($e->getMessage()));
    }
    ?>
    <!doctype html>
    <html lang="ca">
    <head><meta charset="utf-8"><title>Agenda</title></head>
    <body>
        <h1>Agenda</h1>
        <ul>
            <?php foreach ($contactes as $c): ?>
                <li><?= htmlspecialchars($c['nom']) ?> — <?= htmlspecialchars($c['telefon']) ?></li>
            <?php endforeach; ?>
        </ul>
    </body>
    </html>
    ```

    ```markdown title="README.md"
    # Agenda amb PHP + MariaDB

    ## Arrancar

        cp .env.example .env     # i canvia les contrasenyes
        docker compose up -d --build

    - Aplicació: http://localhost:8080
    - Adminer (gestor de la BD): http://localhost:8081 — servidor `bd`, usuari i contrasenya del `.env`

    ## Parar

        docker compose down          # les dades es conserven
        docker compose down -v       # esborra també la base de dades
    ```

    **Les claus de l'exercici:**

    - **`build: .`** → la imatge de PHP es construïx amb el `Dockerfile`, que afig l'extensió `pdo_mysql`. Sense ella, PHP diu *could not find driver*.
    - **`./src:/var/www/html`** → bind mount: edites `index.php` en el teu equip i només cal recarregar el navegador.
    - **`./bd:/docker-entrypoint-initdb.d`** → la imatge de MariaDB executa automàticament els `.sql` d'eixa carpeta **la primera vegada** (quan el volum està buit). Si canvies l'SQL i vols que es torne a executar: `docker compose down -v` i `up` de nou.
    - **`healthcheck` + `condition: service_healthy`** → la web espera que MariaDB estiga realment llesta.
    - **`getenv('DB_HOST')`** → el PHP no té contrasenyes escrites: les llig de les variables que li passa Compose, que al seu torn venen del `.env`.
    - El servidor de la base de dades és **`bd`**, el nom del servei.

## Crear imatges

### 6. Imatge pròpia d'una aplicació Python

Crea una imatge amb un servidor web fet en Python que mostre un missatge configurable amb una variable d'entorn. Construïx-la, executa dos contenidors amb missatges diferents i comprova que cada un mostra el seu.

??? success "Solució"

    ```python title="app.py"
    """Servidor web mínim que mostra el nom de l'equip i l'hora."""
    import os
    import socket
    from datetime import datetime
    from http.server import BaseHTTPRequestHandler, HTTPServer

    MISSATGE = os.getenv("MISSATGE", "Hola des de Docker!")   # es pot canviar amb -e


    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            cos = (f"<h1>{MISSATGE}</h1>"
                   f"<p>Contenidor: {socket.gethostname()}</p>"
                   f"<p>Hora: {datetime.now():%H:%M:%S}</p>")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(cos.encode())


    if __name__ == "__main__":
        print("Escoltant en el port 8000")
        HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()
    ```

    ```dockerfile title="Dockerfile"
    FROM python:3.12-slim

    WORKDIR /app
    COPY app.py .

    ENV MISSATGE="Hola des de Docker!"
    EXPOSE 8000

    CMD ["python", "app.py"]
    ```

    ```bash
    docker build -t salutacio:1.0 .

    docker run -d --name s1 -p 8001:8000 salutacio:1.0
    docker run -d --name s2 -p 8002:8000 -e MISSATGE="Bon dia, ASIR" salutacio:1.0

    curl http://localhost:8001      # Hola des de Docker!
    curl http://localhost:8002      # Bon dia, ASIR

    docker rm -f s1 s2
    ```

    - Una mateixa imatge, dos contenidors: cada un en un port del teu equip diferent (8001 i 8002), però tots dos usen el 8000 de dins.
    - `ENV` en el Dockerfile dona un valor per defecte; `-e` el canvia en arrancar.
    - *Contenidor:* mostra l'ID del contenidor, que és el seu nom de host.

## Per a sysadmin

### 7. Script de còpia de seguretat d'una base de dades en Docker

Fes un script de Bash que faça un *dump* comprimit de totes les bases de dades d'un contenidor MariaDB, amb la data al nom, i que conserve només les 7 últimes còpies.

??? success "Solució"

    ```bash title="backup_bd.sh"
    #!/bin/bash
    # Còpia de seguretat de la base de dades d'un contenidor MariaDB, conservant les 7 últimes
    # Ús: ./backup_bd.sh <contenidor> <carpeta_destí>
    set -euo pipefail

    [ $# -eq 2 ] || { echo "Ús: $0 <contenidor> <carpeta_destí>" >&2; exit 1; }
    contenidor=$1
    desti=$2
    conserva=7

    # Comprovem que el contenidor està en marxa
    if ! docker ps --format '{{.Names}}' | grep -qx "$contenidor"; then
        echo "El contenidor '$contenidor' no està en marxa" >&2
        exit 1
    fi

    mkdir -p "$desti"
    fitxer="$desti/${contenidor}_$(date +%Y%m%d_%H%M%S).sql.gz"

    # Fem el dump DINS del contenidor (la contrasenya ja està en la seua variable d'entorn)
    # i el comprimim FORA, en el nostre equip
    docker exec "$contenidor" sh -c 'mariadb-dump -u root -p"$MARIADB_ROOT_PASSWORD" --all-databases' | gzip > "$fitxer"
    echo "Creat $fitxer ($(du -h "$fitxer" | cut -f1))"

    # Rotació: esborrem les més velles i deixem les $conserva últimes
    ls -1t "$desti/${contenidor}"_*.sql.gz | tail -n +$((conserva + 1)) | while read -r vella; do
        rm -- "$vella"
        echo "Esborrada $vella"
    done
    ```

    ```bash
    ./backup_bd.sh bd ~/copies_bd
    # Creat /home/ana/copies_bd/bd_20261011_204512.sql.gz (4,0K)
    ```

    - `sh -c '... $MARIADB_ROOT_PASSWORD'` amb cometes **simples**: la variable s'expandix **dins** del contenidor, on existix. Així la contrasenya no apareix en el script.
    - El `|` entre `docker exec` i `gzip` passa el dump del contenidor al teu equip.
    - `ls -1t` ordena per data (els més nous primer) i `tail -n +8` dona de la 8a en avant: les que sobren.
    - Per a fer-lo cada nit: `crontab -e` → `0 3 * * * /ruta/backup_bd.sh bd /copies`.
    - Per a **restaurar**: `gunzip -c copia.sql.gz | docker exec -i bd sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD"'`.

### 8. El disc s'ha omplit

Un servidor amb Docker es queda sense espai. Esbrina quant ocupa Docker i allibera espai sense perdre les dades de les bases de dades.

??? success "Solució"

    ```bash
    docker system df                 # quant ocupen imatges, contenidors, volums i memòria cau
    docker ps -a                     # contenidors parats que ja no serveixen?
    docker container prune           # esborra els contenidors parats
    docker image prune -a            # esborra les imatges que no usa cap contenidor
    docker builder prune             # esborra la memòria cau de construccions
    docker system df                 # comprova quant has guanyat
    ```

    !!! danger "No uses `docker volume prune` ni `docker system prune --volumes` sense pensar"
        Esborren els volums que no estiguen en ús en eixe moment. Si una base de dades està parada, **el seu volum s'esborraria** i perdries les dades.
