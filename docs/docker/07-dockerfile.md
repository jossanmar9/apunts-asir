# 7. Crear imatges: Dockerfile

Fins ara has usat imatges que ja existien. Però de vegades cal una imatge **pròpia**: per exemple, PHP amb una extensió concreta, o la teua aplicació ja copiada dins.

Les imatges es fan amb un fitxer de text anomenat **`Dockerfile`** (sense extensió, amb `D` majúscula): una llista d'instruccions que Docker segueix, pas a pas, per a construir-la.

## Un Dockerfile comentat

Una imatge amb una web estàtica servida per Nginx:

```dockerfile title="Dockerfile"
# 1. Partir d'una imatge que ja existix
FROM nginx:1.27-alpine

# 2. Copiar la nostra web dins de la imatge
COPY web/ /usr/share/nginx/html/

# 3. Documentar quin port usa
EXPOSE 80
```

Estructura de la carpeta:

```text
projecte/
├── Dockerfile
└── web/
    └── index.html
```

Construir la imatge i provar-la:

```bash
docker build -t la-meua-web:1.0 .          # construir (el . és la carpeta actual)
docker run -d -p 8080:80 la-meua-web:1.0   # crear un contenidor amb ella
```

- `-t nom:etiqueta` posa nom a la imatge.
- El `.` final és el **context**: la carpeta amb els fitxers que es poden copiar dins. **No t'oblides del punt.**

## Les instruccions

| Instrucció | Què fa | Exemple |
| ---------- | ------ | ------- |
| `FROM` | imatge de partida. **Sempre la primera** | `FROM python:3.12-slim` |
| `RUN` | executa una ordre **mentre es construïx** la imatge (instal·lar coses) | `RUN apt-get update && apt-get install -y curl` |
| `COPY` | copia fitxers del teu equip a la imatge | `COPY src/ /var/www/html/` |
| `WORKDIR` | la carpeta de treball per a les instruccions següents (com un `cd`) | `WORKDIR /app` |
| `ENV` | defineix una variable d'entorn | `ENV TZ=Europe/Madrid` |
| `ARG` | una variable que només existix mentre es construïx | `ARG VERSIO=1.0` |
| `EXPOSE` | documenta el port que usa (no el publica: això ho fa `-p`) | `EXPOSE 80` |
| `USER` | amb quin usuari s'executa el que ve després | `USER www-data` |
| `CMD` | l'ordre que s'executa **quan arranca el contenidor** | `CMD ["python", "app.py"]` |
| `ENTRYPOINT` | com `CMD`, però més difícil de canviar en fer `docker run` | `ENTRYPOINT ["nginx"]` |

!!! warning "`RUN` o `CMD`?"
    - **`RUN`** s'executa **una vegada, en construir** la imatge (per a instal·lar).
    - **`CMD`** s'executa **cada vegada que arranca** un contenidor (per a llançar l'aplicació).
    - Només hi pot haver **un** `CMD` (si n'hi ha diversos, val l'últim).

## Exemple: PHP amb Apache i l'extensió de MariaDB

La imatge oficial `php:8.3-apache` no porta l'extensió per a connectar amb MySQL/MariaDB amb PDO. És un cas típic per a fer una imatge pròpia:

```dockerfile title="Dockerfile"
FROM php:8.3-apache

# Instal·lar les extensions de PHP per a MariaDB/MySQL
RUN docker-php-ext-install pdo pdo_mysql mysqli

# Copiar l'aplicació
COPY src/ /var/www/html/
```

`docker-php-ext-install` és una ferramenta que porten les imatges oficials de PHP per a afegir extensions.

## Exemple: una aplicació Python

```dockerfile title="Dockerfile"
FROM python:3.12-slim

WORKDIR /app

# Primer només les dependències (així Docker les reaprofita si no canvien)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Després el codi
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

!!! tip "L'ordre importa: la memòria cau"
    Docker guarda cada pas (capa) en memòria cau. Si tornes a construir i un pas no ha canviat, el reaprofita i va molt més ràpid. Per això es copia **primer** `requirements.txt` i s'instal·la, i **després** el codi: si només canvies el codi, no torna a instal·lar les llibreries.

## `.dockerignore`

Igual que `.gitignore`, indica què **no** s'ha de copiar a la imatge:

```text title=".dockerignore"
.git
.env
.venv
__pycache__
*.log
```

## Construir des de Compose

En lloc d'`image:`, posa `build:` amb la carpeta on està el Dockerfile:

```yaml title="compose.yaml"
services:
  web:
    build: .                 # construïx la imatge amb el Dockerfile d'esta carpeta
    ports:
      - "8080:80"
```

```bash
docker compose up -d --build     # --build: torna a construir si has canviat el Dockerfile
```

## Pujar la imatge a Docker Hub

```bash
docker login                                       # amb el teu compte de Docker Hub
docker tag la-meua-web:1.0 USUARI/la-meua-web:1.0  # el nom ha de començar pel teu usuari
docker push USUARI/la-meua-web:1.0
```

Ara qualsevol pot fer `docker pull USUARI/la-meua-web:1.0`.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `"docker build" requires exactly 1 argument` | Falta el `.` al final | `docker build -t nom .` |
| `COPY failed: file not found` | El fitxer no està dins de la carpeta del context, o està en `.dockerignore` | Revisa la ruta relativa al `Dockerfile` |
| He canviat el codi i el contenidor no ho mostra | El contenidor usa la imatge vella | Torna a construir: `docker compose up -d --build` |
| `E: Unable to locate package` en un `RUN apt-get install` | Falta `apt-get update` en el mateix `RUN` | `RUN apt-get update && apt-get install -y paquet` |
| L'`apt-get install` es queda esperant | Pregunta "Do you want to continue?" | Afig `-y` |
| `could not find driver` en PHP amb PDO | Falta l'extensió | `RUN docker-php-ext-install pdo_mysql` |

!!! success "Per a l'examen"
    ```dockerfile
    FROM imatge:versio            # sempre primer
    WORKDIR /app                  # carpeta de treball
    RUN ordre                     # en CONSTRUIR (instal·lar)
    COPY origen destí             # copiar fitxers
    ENV VAR=valor
    EXPOSE 80                     # documentar el port
    CMD ["programa", "arg"]       # en ARRANCAR el contenidor
    ```
    ```bash
    docker build -t nom:versio .        # ¡el punt!
    docker compose up -d --build        # amb build: en el compose.yaml
    docker tag nom usuari/nom && docker push usuari/nom
    ```
