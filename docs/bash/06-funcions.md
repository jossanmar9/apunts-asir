# 6. Funcions

## Definir i cridar

```bash
saluda() {
    echo "Hola, $1"
}

saluda "Pep"      # es crida SENSE parèntesis
```

La funció s'ha de definir **abans** de cridar-la. Dins, `$1`, `$2`, `$#`, `"$@"` són els arguments **de la funció**, no els de l'script.

## Tornar valors: dues maneres

=== "Tornar dades → `echo` + `$( )`"

    ```bash
    bytes_a_mb() {
        echo $(( $1 / 1024 / 1024 ))
    }

    mida=$(bytes_a_mb 52428800)
    echo "$mida MB"      # 50 MB
    ```

=== "Tornar èxit/error → `return`"

    ```bash
    existix_usuari() {
        id "$1" &> /dev/null    # el codi d'id és el de la funció
    }

    if existix_usuari "pep"; then
        echo "Sí"
    fi
    ```

`return` només accepta números de 0 a 255 i serveix per a dir **si ha anat bé**, no per a tornar resultats. Si no poses `return`, la funció torna el codi de la seua última ordre.

## Variables locals

Per defecte, les variables d'una funció són **globals** i poden xafar les de l'script. Usa `local`:

```bash
total=100
suma() {
    local total=0
    for n in "$@"; do (( total += n )); done
    echo "$total"
}
echo "$(suma 1 2 3)"   # 6
echo "$total"          # 100 (no s'ha tocat)
```

## Funcions útils per a qualsevol script

```bash
error() {                   # missatge a stderr i ix
    echo "ERROR: $*" >&2
    exit 1
}

log() {                     # missatge amb hora
    echo "[$(date +%T)] $*"
}

confirma() {                # torna 0 si l'usuari diu sí
    read -r -p "$1 (s/n) " r
    [[ $r =~ ^[sS] ]]
}

[ $# -ge 1 ] || error "falta el directori"
confirma "Esborrar $1?" && rm -r "$1" && log "Esborrat $1"
```

## Biblioteques: `source`

Guarda les funcions en un fitxer i carrega-les des de diversos scripts:

```bash title="lib.sh"
error() { echo "ERROR: $*" >&2; exit 1; }
es_root() { (( EUID == 0 )); }
```

```bash title="crea_usuari.sh"
#!/bin/bash
source "$(dirname "$0")/lib.sh"
es_root || error "cal executar-lo com a root"
```

`dirname "$0"` és el directori on està l'script, així funciona encara que l'executes des d'un altre lloc.
