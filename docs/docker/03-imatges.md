# 3. Imatges

## Què és una imatge

Una **imatge** és una plantilla de **només lectura** amb tot el necessari per a executar una aplicació: el sistema de fitxers base, els programes, les llibreries i la configuració. A partir d'ella es creen els contenidors.

## Docker Hub: d'on venen les imatges

[Docker Hub](https://hub.docker.com) és el registre públic d'imatges. Hi ha de dos tipus:

| Tipus | Nom | Exemple | Fiabilitat |
| ----- | --- | ------- | ---------- |
| **Oficials** | només el nom | `nginx`, `mariadb`, `php`, `python` | mantingudes per Docker o pel projecte ✅ |
| **D'usuaris** | `usuari/nom` | `bitnami/wordpress`, `ana/la-meua-app` | depén de qui la mantinga ⚠️ |

!!! tip "Llig sempre la pàgina de la imatge"
    En Docker Hub, cada imatge explica quins **ports** usa, quines **variables d'entorn** accepta i on guarda les **dades**. És el que necessitaràs per a fer el `docker run` o el `compose.yaml`.

## Etiquetes (tags): les versions

Una imatge té el format **`nom:etiqueta`**. L'etiqueta normalment indica la versió:

```bash
docker pull nginx:1.27          # una versió concreta
docker pull mariadb:11.4
docker pull php:8.3-apache      # PHP 8.3 amb Apache inclòs
docker pull python:3.12-slim    # versió reduïda
docker pull nginx               # sense etiqueta = nginx:latest
```

| Etiqueta típica | Significa |
| --------------- | --------- |
| `latest` | l'última (és la que s'agafa si no poses res) |
| `1.27`, `11.4` | una versió concreta |
| `-alpine` | basada en Alpine Linux: molt menuda (pocs MB) |
| `-slim` | versió reduïda (sense coses supèrflues) |

!!! warning "Evita `latest` en projectes"
    `latest` canvia cada vegada que hi ha una versió nova. El que hui funciona, demà pot trencar-se. En un `compose.yaml` d'una pràctica, posa sempre la versió: `mariadb:11.4`, no `mariadb`.

## Gestionar imatges

| Vull... | Ordre |
| ------- | ----- |
| descarregar una imatge | `docker pull nginx:1.27` |
| veure les que tinc | `docker images` |
| buscar en Docker Hub | `docker search wordpress` |
| esborrar una imatge | `docker rmi nginx:1.27` |
| esborrar les que no usa cap contenidor | `docker image prune -a` |
| veure les capes d'una imatge | `docker history nginx` |
| veure'n tota la informació | `docker inspect nginx` |

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        1.27      a1b2c3d4e5f6   2 weeks ago   192MB
mariadb      11.4      b2c3d4e5f6a7   3 weeks ago   407MB
```

!!! note "No es pot esborrar una imatge que usa un contenidor"
    Si `docker rmi` diu que la imatge està en ús, primer esborra els contenidors creats a partir d'ella (`docker ps -a` per a veure'ls).

## Capes: per què les imatges ocupen menys del que sembla

Una imatge està feta de **capes** posades una damunt de l'altra (sistema base, després un programa, després la configuració...). Si dues imatges comparteixen capes (per exemple, totes dues parteixen de Debian), eixes capes es guarden **una sola vegada**.

Quan crees un contenidor, Docker afig una **capa d'escriptura** damunt de la imatge. Tots els canvis que fas dins del contenidor van a eixa capa. Per això:

- La imatge **no canvia mai**: diversos contenidors poden usar-la alhora.
- Si **esborres el contenidor**, la seua capa d'escriptura (i els canvis) **es perden**. Ho solucionen els volums ([tema 4](04-emmagatzematge.md)).

## Netejar espai

Docker pot acabar ocupant molt de disc:

```bash
docker system df          # quant ocupen imatges, contenidors i volums
docker system prune       # esborra contenidors parats, xarxes sense ús i imatges "penjades"
docker system prune -a    # a més, totes les imatges que no use cap contenidor
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `manifest unknown` / `not found` | L'etiqueta no existix | Mira en Docker Hub quines etiquetes hi ha |
| `pull access denied` | El nom està mal escrit o la imatge és privada | Revisa el nom (`usuari/imatge`) |
| `image is being used by stopped container` | Hi ha contenidors creats amb eixa imatge | Esborra'ls abans o usa `docker rmi -f` |
| El disc s'ompli | Imatges i contenidors vells | `docker system prune -a` |

!!! success "Per a l'examen"
    - Format: **`nom:etiqueta`** · sense etiqueta = `latest`
    - Oficials: `nginx` · d'usuaris: `usuari/nom`
    - `docker pull` · `docker images` · `docker rmi` · `docker image prune -a`
    - La imatge és de **només lectura**; els canvis van a la capa del contenidor i **es perden en esborrar-lo**
    - En projectes, **fixa la versió** (`mariadb:11.4`)
