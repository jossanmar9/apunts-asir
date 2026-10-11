# 2. Contenidors

## Crear i executar un contenidor: `docker run`

```bash
docker run ubuntu echo "Hola món"
```

```console
Hola món
```

Què ha passat:

1. Docker ha descarregat la imatge `ubuntu` (si no la tenia).
2. Ha creat un contenidor a partir d'ella.
3. Ha executat l'ordre `echo "Hola món"` dins.
4. Quan l'ordre ha acabat, **el contenidor s'ha parat** (però continua existint).

!!! note "Un contenidor viu mentre viu el seu procés"
    Un contenidor no és una màquina que està sempre encesa. Executa **un procés principal**, i quan eixe procés acaba, el contenidor es para. Per això un contenidor amb `echo` dura un segon, i un amb un servidor web (que no acaba mai) es queda funcionant.

## Les opcions més importants de `docker run`

```bash
docker run [OPCIONS] IMATGE [ORDRE]
```

| Opció | Què fa | Exemple |
| ----- | ------ | ------- |
| `--name nom` | posa nom al contenidor (si no, n'inventa un) | `--name web1` |
| `-d` | l'executa **en segon pla** (*detached*) | servidors |
| `-it` | **interactiu** amb terminal: per a entrar-hi i escriure | `docker run -it ubuntu bash` |
| `-p amfitrió:contenidor` | **publica un port**: connecta un port del teu equip amb el del contenidor | `-p 8080:80` |
| `-e VAR=valor` | defineix una **variable d'entorn** | `-e MARIADB_ROOT_PASSWORD=1234` |
| `-v origen:destí` | munta un **volum** o carpeta ([tema 4](04-emmagatzematge.md)) | `-v dades:/var/lib/mysql` |
| `--rm` | **esborra** el contenidor quan acaba | proves ràpides |
| `--network xarxa` | el connecta a una xarxa ([tema 5](05-xarxes.md)) | `--network red1` |
| `--restart always` | el torna a arrancar si es para o si reinicies l'equip | serveis |

### Exemple: un servidor web

```bash
docker run -d --name web1 -p 8080:80 nginx
```

| Tros | Significa |
| ---- | --------- |
| `-d` | en segon pla (el terminal queda lliure) |
| `--name web1` | el contenidor es dirà `web1` |
| `-p 8080:80` | el port **8080 del teu equip** porta al port **80 del contenidor** |
| `nginx` | la imatge del servidor web Nginx |

Obri el navegador en `http://localhost:8080` i veuràs la pàgina de benvinguda de Nginx.

!!! tip "Com recordar `-p`"
    **Fora:dins**. L'esquerra és el teu equip; la dreta, el contenidor. `-p 8080:80` → entres per 8080 i arribes al 80 de dins.

### Exemple: entrar dins d'un contenidor

```bash
docker run -it --name prova ubuntu bash
```

```console
root@3f2a1b4c5d6e:/#
```

Ara estàs **dins** del contenidor, com si fora un Ubuntu acabat d'instal·lar. Escriu `exit` per a eixir (el contenidor es pararà).

### Exemple: variables d'entorn

Moltes imatges es configuren amb variables. La de MariaDB **obliga** a posar la contrasenya de root:

```bash
docker run -d --name bd -e MARIADB_ROOT_PASSWORD=secret mariadb
```

Quines variables accepta cada imatge? Està explicat en la seua pàgina de **Docker Hub** ([hub.docker.com](https://hub.docker.com)).

## Veure els contenidors

```bash
docker ps          # els que estan en marxa
docker ps -a       # TOTS, també els parats
```

```console
CONTAINER ID   IMAGE    COMMAND                  STATUS          PORTS                  NAMES
a1b2c3d4e5f6   nginx    "/docker-entrypoint.…"   Up 2 minutes    0.0.0.0:8080->80/tcp   web1
```

Per a referir-te a un contenidor pots usar el **nom** (`web1`) o l'**ID** (n'hi ha prou amb els primers caràcters: `a1b2`).

## Gestionar contenidors

| Vull... | Ordre |
| ------- | ----- |
| parar-lo | `docker stop web1` |
| arrancar-lo (si estava parat) | `docker start web1` |
| reiniciar-lo | `docker restart web1` |
| esborrar-lo (ha d'estar parat) | `docker rm web1` |
| esborrar-lo encara que estiga en marxa | `docker rm -f web1` |
| esborrar tots els parats | `docker container prune` |
| canviar-li el nom | `docker rename vell nou` |

## Veure què passa dins

```bash
docker logs web1             # el que ha mostrat el contenidor (els seus registres)
docker logs -f web1          # els va mostrant en directe (Ctrl+C per a eixir)
docker exec -it web1 bash    # obrir un terminal DINS d'un contenidor que ja està en marxa
docker exec web1 ls /etc     # executar una ordre dins sense entrar
docker top web1              # processos que hi ha dins
docker stats                 # CPU i memòria de cada contenidor, en directe
docker inspect web1          # tota la informació (IP, volums, variables...) en JSON
```

!!! tip "`docker exec` és la clau"
    Per a "entrar" en un contenidor que ja funciona (per exemple, a la base de dades), usa `docker exec -it NOM bash`. Si la imatge no té `bash` (les basades en Alpine), prova `sh`.

### `run` o `exec`?

| | `docker run` | `docker exec` |
| - | ------------ | ------------- |
| Què fa | **crea** un contenidor nou | executa una ordre en un contenidor **que ja existix i està en marxa** |
| Quan | la primera vegada | per a entrar o fer coses dins |

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `The container name "/web1" is already in use` | Ja hi ha un contenidor amb eixe nom (encara que estiga parat) | `docker rm -f web1` o tria un altre nom |
| `port is already allocated` | El port del teu equip ja l'usa un altre programa o contenidor | Canvia el de l'esquerra: `-p 8081:80` |
| El contenidor es para just després d'arrancar | El procés principal ha acabat o ha fallat | `docker logs nom` per a veure l'error |
| MariaDB es para sola | Falta la variable obligatòria de contrasenya | `-e MARIADB_ROOT_PASSWORD=...` |
| `docker exec` dona `is not running` | El contenidor està parat | `docker start nom` abans |
| `exec: "bash": executable file not found` | La imatge no porta bash | Usa `sh` |
| `-p 80:8080` i no funciona | Has posat els ports al revés | **fora:dins** → `-p 8080:80` |

!!! success "Per a l'examen"
    ```bash
    docker run -d --name web -p 8080:80 nginx      # servidor en segon pla
    docker run -it --rm ubuntu bash                # entrar en un contenidor de prova
    docker run -d -e VAR=valor imatge              # amb variable d'entorn
    docker ps / docker ps -a                       # en marxa / tots
    docker stop / start / restart / rm -f NOM
    docker logs -f NOM                             # veure registres
    docker exec -it NOM bash                       # entrar en un que ja funciona
    docker inspect NOM                             # tota la informació
    ```
    - `-p FORA:DINS` · `-d` segon pla · `-it` interactiu · `--rm` esborrar en acabar
    - El contenidor viu **mentre viu el seu procés principal**
