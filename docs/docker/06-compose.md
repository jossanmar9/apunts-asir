# 6. Docker Compose

## Què és

**Docker Compose** permet definir **tots els contenidors d'una aplicació** (amb els seus ports, volums, variables i xarxes) en **un sol fitxer**: `compose.yaml`. Després s'arranca tot amb una ordre.

| Sense Compose | Amb Compose |
| ------------- | ----------- |
| Diversos `docker run` llargs, en l'ordre correcte | Un fitxer `compose.yaml` |
| Crear xarxes i volums a mà | Es creen sols |
| Fàcil equivocar-se | Repetible: sempre igual |
| Difícil de compartir | Puges el fitxer a Git i qualsevol l'arranca |

Per això a IAW us demanen un **entorn reproduïble** amb `compose.yaml`: qui clone el vostre repositori ha de poder arrancar la pràctica amb `docker compose up -d`.

## El format YAML en 1 minut

El fitxer està en **YAML**: un format de text on l'estructura es marca amb **espais**.

```yaml
clau: valor                 # una parella clau: valor
llista:                     # una llista: cada element comença per "- "
  - element1
  - element2
objecte:                    # un objecte: les claus de dins, 2 espais més a la dreta
  nom: web
  port: 80
```

!!! danger "Les regles que trenquen tot"
    - **Espais, mai tabuladors.**
    - La indentació ha de ser **coherent** (normalment 2 espais per nivell).
    - Després de `:` i de `-` va **un espai**.

## Un `compose.yaml` comentat

El mateix WordPress + MariaDB del [tema 5](05-xarxes.md), ara amb Compose:

```yaml title="compose.yaml"
services:                         # la llista de contenidors (cada un és un "servei")

  bd:                             # nom del servei: els altres el troben amb este nom
    image: mariadb:11.4           # la imatge (amb versió fixa)
    restart: unless-stopped       # tornar-lo a arrancar si es para
    environment:                  # variables d'entorn
      MARIADB_DATABASE: wordpress
      MARIADB_USER: wp
      MARIADB_PASSWORD: wp_secret
      MARIADB_ROOT_PASSWORD: root_secret
    volumes:
      - dades_bd:/var/lib/mysql   # volum per a no perdre la base de dades

  wordpress:
    image: wordpress:6
    restart: unless-stopped
    depends_on:                   # arranca després de "bd"
      - bd
    environment:
      WORDPRESS_DB_HOST: bd       # el nom del servei de la base de dades
      WORDPRESS_DB_USER: wp
      WORDPRESS_DB_PASSWORD: wp_secret
      WORDPRESS_DB_NAME: wordpress
    ports:
      - "8080:80"                 # FORA:DINS, entre cometes
    volumes:
      - dades_wp:/var/www/html

volumes:                          # els volums que s'usen dalt, declarats ací
  dades_bd:
  dades_wp:
```

**No cal crear cap xarxa**: Compose crea automàticament una xarxa per al projecte i hi connecta tots els serveis. Cada servei es troba pel seu **nom** (`bd`, `wordpress`).

### Les claus més usades d'un servei

| Clau | Per a què | Exemple |
| ---- | --------- | ------- |
| `image` | quina imatge usar | `nginx:1.27` |
| `build` | construir la imatge amb un Dockerfile ([tema 7](07-dockerfile.md)) | `build: .` |
| `container_name` | nom fix per al contenidor (opcional) | `container_name: web` |
| `ports` | publicar ports | `- "8080:80"` |
| `environment` | variables d'entorn | `TZ: Europe/Madrid` |
| `env_file` | llegir les variables d'un fitxer | `env_file: .env` |
| `volumes` | volums i bind mounts | `- ./src:/var/www/html` |
| `depends_on` | arrancar després d'un altre servei | `- bd` |
| `restart` | què fer si es para | `unless-stopped` |
| `networks` | xarxes concretes (normalment no cal) | `- interna` |
| `healthcheck` | com comprovar que el servei està bé | vegeu baix |

!!! note "`version:` ja no cal"
    En molts exemples antics veuràs `version: '3.8'` al principi. Les versions actuals de Compose l'ignoren: no cal posar-lo.

## Les ordres

**Totes s'executen en la carpeta on està el `compose.yaml`.**

| Vull... | Ordre |
| ------- | ----- |
| **arrancar-ho tot** (i crear el que falte) | `docker compose up -d` |
| veure l'estat | `docker compose ps` |
| veure els registres | `docker compose logs` · `docker compose logs -f bd` |
| entrar en un servei | `docker compose exec bd bash` |
| parar (sense esborrar) | `docker compose stop` |
| tornar a arrancar | `docker compose start` · `docker compose restart` |
| **parar i esborrar** contenidors i xarxa | `docker compose down` |
| esborrar-ho tot, **també els volums** (⚠️ perds les dades) | `docker compose down -v` |
| aplicar canvis del `compose.yaml` | `docker compose up -d` (de nou) |
| tornar a construir les imatges | `docker compose up -d --build` |
| comprovar que el fitxer és correcte | `docker compose config` |

!!! tip "`docker compose config`"
    Mostra el fitxer tal com l'entén Docker, amb les variables substituïdes. Si hi ha un error de format, t'ho diu. Executa'l sempre que alguna cosa no arranque.

## Variables i el fitxer `.env` ⭐

No és bona idea escriure les contrasenyes directament en el `compose.yaml` (i menys pujar-les a GitHub). La solució: posar-les en un fitxer `.env` en la mateixa carpeta, i referir-s'hi amb `${NOM}`:

```text title=".env"
DB_NAME=wordpress
DB_USER=wp
DB_PASSWORD=wp_secret
DB_ROOT_PASSWORD=root_secret
WEB_PORT=8080
```

```yaml title="compose.yaml"
services:
  bd:
    image: mariadb:11.4
    environment:
      MARIADB_DATABASE: ${DB_NAME}
      MARIADB_USER: ${DB_USER}
      MARIADB_PASSWORD: ${DB_PASSWORD}
      MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    volumes:
      - dades_bd:/var/lib/mysql

  wordpress:
    image: wordpress:6
    depends_on:
      - bd
    environment:
      WORDPRESS_DB_HOST: bd
      WORDPRESS_DB_NAME: ${DB_NAME}
      WORDPRESS_DB_USER: ${DB_USER}
      WORDPRESS_DB_PASSWORD: ${DB_PASSWORD}
    ports:
      - "${WEB_PORT:-8080}:80"      # si WEB_PORT no està definida, 8080
    volumes:
      - dades_wp:/var/www/html

volumes:
  dades_bd:
  dades_wp:
```

Compose llig el `.env` automàticament en fer `docker compose up`.

### `.env` i `.env.example`: com es puja a Git

| Fitxer | Conté | Es puja a Git? |
| ------ | ----- | -------------- |
| `.env` | les contrasenyes **de veritat** | ❌ **NO**: posa'l en el `.gitignore` |
| `.env.example` | les mateixes variables amb valors d'exemple | ✅ sí |

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

Qui clone el repositori fa:

```bash
cp .env.example .env      # crea el seu .env
nano .env                 # posa les seues contrasenyes
docker compose up -d
```

## Esperar que la base de dades estiga llesta: `healthcheck`

`depends_on` només espera que el contenidor **arranque**, no que la base de dades **estiga llesta** per a acceptar connexions (pot tardar uns segons). Si l'aplicació falla per això, es pot afegir una comprovació:

```yaml
services:
  bd:
    image: mariadb:11.4
    environment:
      MARIADB_ROOT_PASSWORD: ${DB_ROOT_PASSWORD}
    healthcheck:
      test: ["CMD", "healthcheck.sh", "--connect", "--innodb_initialized"]
      interval: 5s
      timeout: 5s
      retries: 10

  web:
    image: php:8.3-apache
    depends_on:
      bd:
        condition: service_healthy     # espera que el healthcheck de bd diga que està bé
```

(`healthcheck.sh` ve inclòs en la imatge oficial de MariaDB.)

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `no configuration file provided: not found` | No estàs en la carpeta del `compose.yaml` | `cd` a la carpeta |
| `yaml: line X: did not find expected key` | Error d'indentació o un tabulador | Revisa els espais en eixa línia; `docker compose config` |
| `variable is not set. Defaulting to a blank string` | Falta la variable en el `.env` (o no hi ha `.env`) | `cp .env.example .env` i omple'l |
| Canvie el `compose.yaml` i no es nota | Cal tornar a aplicar-lo | `docker compose up -d` |
| He perdut la base de dades | Has fet `down -v` | `-v` esborra els volums: usa només `down` |
| L'app no connecta amb la BD en el primer arranc | La BD encara no estava llesta | Espera o afig `healthcheck` + `condition: service_healthy` |
| He pujat el `.env` amb contrasenyes a GitHub | Faltava en el `.gitignore` | Afig-lo, `git rm --cached .env`, i **canvia les contrasenyes** |

!!! success "Per a l'examen"
    ```yaml
    services:
      nom_servei:
        image: imatge:versio
        ports: ["FORA:DINS"]
        environment:
          VAR: ${VAR_DEL_ENV}
        volumes:
          - volum:/carpeta/dins
          - ./local:/carpeta/dins
        depends_on: [altre_servei]
        restart: unless-stopped
    volumes:
      volum:
    ```
    ```bash
    docker compose up -d        # arrancar
    docker compose ps / logs -f / exec servei bash
    docker compose down         # parar i esborrar (els volums es queden)
    docker compose down -v      # ⚠️ també esborra els volums
    docker compose config       # comprovar el fitxer
    ```
    - Els serveis es troben **pel nom del servei**
    - Contrasenyes en `.env` (no es puja) · plantilla en `.env.example` (sí es puja)
    - **Espais, no tabuladors** en el YAML
