# Xuleta de Docker

> Consulta ràpida. La teoria completa està en la [secció de Docker](../docker/index.md).

## Contenidors

```bash
docker run -d --name web -p 8080:80 nginx:1.27      # segon pla, nom, port FORA:DINS
docker run -it --rm ubuntu bash                     # entrar en un contenidor de prova
docker run -d -e VAR=valor -v vol:/dades imatge     # variable d'entorn i volum
docker ps                    # en marxa
docker ps -a                 # tots
docker stop / start / restart NOM
docker rm NOM / docker rm -f NOM                    # esborrar (forçat si està en marxa)
docker logs -f NOM                                  # registres en directe
docker exec -it NOM bash                            # entrar en un que ja funciona (o sh)
docker inspect NOM                                  # tota la informació
docker stats                                        # CPU i memòria
docker cp fitxer NOM:/ruta / docker cp NOM:/ruta .  # copiar fitxers
```

| Opció de `run` | Fa |
| -------------- | -- |
| `-d` | segon pla |
| `-it` | interactiu amb terminal |
| `--name` | nom del contenidor |
| `-p 8080:80` | port **FORA:DINS** |
| `-e VAR=x` | variable d'entorn |
| `-v vol:/ruta` | volum |
| `-v "$(pwd)/dir":/ruta` | bind mount (carpeta teua) |
| `--network xarxa` | connectar a una xarxa |
| `--rm` | esborrar en acabar |
| `--restart unless-stopped` | tornar a arrancar sol |

## Imatges

```bash
docker pull nginx:1.27       # descarregar (nom:etiqueta; sense etiqueta = latest)
docker images                # llistar
docker rmi nginx:1.27        # esborrar
docker image prune -a        # esborrar les que no s'usen
docker build -t nom:1.0 .    # construir amb el Dockerfile (¡el punt!)
docker tag nom:1.0 usuari/nom:1.0 && docker push usuari/nom:1.0
```

## Volums i xarxes

```bash
docker volume create / ls / inspect / rm / prune
docker network create xarxa
docker network ls / inspect / connect / disconnect / rm
```

- En una **xarxa creada per tu**, els contenidors es troben **pel nom**.
- Dades de bases de dades → **volum** · codi que edites → **bind mount**.

## Compose

```yaml
services:
  web:
    build: .                      # o image: nginx:1.27
    ports: ["8080:80"]
    environment:
      DB_HOST: bd
      DB_PASSWORD: ${DB_PASSWORD}
    volumes:
      - ./src:/var/www/html
    depends_on: [bd]
  bd:
    image: mariadb:11.4
    environment:
      MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - dades_bd:/var/lib/mysql
volumes:
  dades_bd:
```

```bash
docker compose up -d              # arrancar (en la carpeta del compose.yaml)
docker compose up -d --build      # reconstruint les imatges
docker compose ps / logs -f / exec servei bash
docker compose stop / start / restart
docker compose down               # parar i esborrar (els volums es queden)
docker compose down -v            # ⚠️ també els volums
docker compose config             # comprovar el fitxer
```

- `.env` amb les contrasenyes (en `.gitignore`) · `.env.example` com a plantilla (sí es puja)
- YAML: **espais, mai tabuladors**

## Dockerfile

```dockerfile
FROM php:8.3-apache               # imatge base (sempre primer)
WORKDIR /app                      # carpeta de treball
RUN apt-get update && apt-get install -y curl    # en CONSTRUIR
COPY src/ /var/www/html/          # copiar fitxers
ENV TZ=Europe/Madrid              # variable d'entorn
EXPOSE 80                         # documentar el port
CMD ["apache2-foreground"]        # en ARRANCAR
```

## Carpetes de dades habituals

| Imatge | Carpeta |
| ------ | ------- |
| `mariadb` / `mysql` | `/var/lib/mysql` |
| `postgres` | `/var/lib/postgresql/data` |
| `nginx` | `/usr/share/nginx/html` |
| `httpd` | `/usr/local/apache2/htdocs` |
| `php:*-apache` / `wordpress` | `/var/www/html` |

## Netejar

```bash
docker system df                  # quant ocupa
docker container prune            # contenidors parats
docker image prune -a             # imatges sense ús
docker system prune               # una mica de tot (no toca volums)
```
