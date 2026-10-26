# 5. Xarxes

Quan una aplicació té diverses peces (per exemple, una web i la seua base de dades), cada una va en un contenidor. Necessiten **parlar entre elles**. Per a això estan les xarxes de Docker.

## Tipus de xarxes

| Xarxa | Què és | Quan |
| ----- | ------ | ---- |
| `bridge` (per defecte) | la xarxa on van els contenidors si no dius res | proves |
| **bridge definida per tu** | una xarxa que crees tu amb `docker network create` | ⭐ **sempre que tingues diversos contenidors** |
| `host` | el contenidor usa directament la xarxa de l'equip, sense aïllament | casos especials |
| `none` | sense xarxa | contenidors aïllats |

!!! danger "La gran diferència: el DNS"
    En la xarxa `bridge` per defecte, els contenidors **no es poden trobar pel nom**, només per IP (i la IP canvia cada vegada).

    En una **xarxa creada per tu**, Docker posa un DNS intern: cada contenidor es pot connectar a un altre **pel seu nom**. Per exemple, la web es connecta a la base de dades escrivint `bd` com a servidor.

## Gestionar xarxes

```bash
docker network create la_meua_xarxa         # crear
docker network ls                           # llistar
docker network inspect la_meua_xarxa        # veure quins contenidors hi ha i les IP
docker network connect la_meua_xarxa web1   # connectar un contenidor que ja existix
docker network disconnect la_meua_xarxa web1
docker network rm la_meua_xarxa             # esborrar
```

## Exemple: WordPress + MariaDB amb `docker run`

WordPress necessita una base de dades. Cada peça en un contenidor, i tots dos en la mateixa xarxa:

```bash
# 1. Crear la xarxa
docker network create xarxa_wp

# 2. La base de dades
docker run -d --name bd \
    --network xarxa_wp \
    -v dades_bd:/var/lib/mysql \
    -e MARIADB_DATABASE=wordpress \
    -e MARIADB_USER=wp \
    -e MARIADB_PASSWORD=wp_secret \
    -e MARIADB_ROOT_PASSWORD=root_secret \
    mariadb:11.4

# 3. WordPress, que es connecta a la base de dades pel NOM "bd"
docker run -d --name wp \
    --network xarxa_wp \
    -v dades_wp:/var/www/html \
    -e WORDPRESS_DB_HOST=bd \
    -e WORDPRESS_DB_USER=wp \
    -e WORDPRESS_DB_PASSWORD=wp_secret \
    -e WORDPRESS_DB_NAME=wordpress \
    -p 8080:80 \
    wordpress:6
```

Obri `http://localhost:8080` i tindràs l'instal·lador de WordPress.

**Fixa't en:**

- `WORDPRESS_DB_HOST=bd` → WordPress busca el servidor de base de dades pel nom del contenidor. Funciona perquè estan en una xarxa creada per nosaltres.
- La base de dades **no té `-p`**: no cal obrir-la a l'exterior. WordPress hi arriba per la xarxa interna. Així és més segur.
- Les dades de tots dos van en volums: es poden esborrar i tornar a crear els contenidors sense perdre res.
- La `\` al final de línia permet escriure una ordre llarga en diverses línies.

Escriure tot açò cada vegada és pesat i fàcil d'equivocar-se. Per això existix **Docker Compose** ([tema 6](06-compose.md)), que fa el mateix amb un fitxer.

## Comprovar la connexió entre contenidors

```bash
docker exec -it wp bash
# dins del contenidor:
getent hosts bd           # a quina IP resol el nom "bd"
```

O amb un contenidor temporal en la mateixa xarxa:

```bash
docker run --rm -it --network xarxa_wp alpine ping -c2 bd
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `Unknown host 'bd'` / `could not translate host name` | Els contenidors no estan en la mateixa xarxa, o és la `bridge` per defecte | Crea una xarxa i posa'ls en ella amb `--network` |
| La web diu *Error establishing a database connection* | Nom, usuari o contrasenya diferents entre els dos contenidors | Revisa que les variables coincidixen |
| La base de dades encara està arrancant | La web intenta connectar-se abans d'hora | Espera uns segons i recarrega |
| `network ... has active endpoints` en esborrar | Hi ha contenidors connectats | Para'ls o desconnecta'ls abans |

!!! success "Per a l'examen"
    - Diversos contenidors que han de parlar → **xarxa creada per tu**: `docker network create nom`
    - En eixa xarxa, els contenidors es troben **pel nom** (DNS intern)
    - `--network nom` en `docker run`
    - Només publica (`-p`) el que s'ha de veure des de fora: la web sí, la base de dades no
    - `docker network ls / inspect / connect / rm`
