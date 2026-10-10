# 12. Scripts robustos

## Validar els arguments al principi

Comprova-ho tot **abans** de fer res. Un bon esquema:

```bash
#!/bin/bash
# Ús: ./neteja.sh <directori> <dies>

us() {
    echo "Ús: $0 <directori> <dies>" >&2
    exit 1
}

[ $# -eq 2 ]              || us
[ -d "$1" ]               || { echo "No existix el directori $1" >&2; exit 2; }
[[ $2 =~ ^[0-9]+$ ]]      || { echo "Els dies han de ser un número" >&2; exit 3; }

dir=$1
dies=$2
find "$dir" -type f -mtime +"$dies" -print -delete
```

Codis d'eixida diferents per a cada error ajuden a saber què ha fallat des d'un altre script.

### Comprovacions habituals

```bash
(( EUID == 0 )) || { echo "Cal ser root" >&2; exit 1; }
command -v rsync &> /dev/null || { echo "Instal·la rsync" >&2; exit 1; }
[ -r "$fitxer" ] || { echo "No es pot llegir $fitxer" >&2; exit 1; }
```

## `set`: opcions del shell

```bash
set -euo pipefail
```

| Opció | Efecte |
| ----- | ------ |
| `-e` | ix en el moment que una ordre falla |
| `-u` | error si uses una variable no definida (adéu als errors de lletra) |
| `-o pipefail` | una tuberia falla si **qualsevol** part falla |
| `-x` | mostra cada ordre abans d'executar-la (depurar) |

!!! note "Matisos de `-e`"
    No s'activa en ordres dins d'un `if`, ni a l'esquerra de `&&`/`||`. Si vols permetre que una ordre falle: `ordre || true`.

## `trap`: fer neteja en acabar

```bash
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT          # s'executa sempre en eixir

trap 'echo "Interromput"; exit 130' INT   # en prémer Ctrl+C
```

`mktemp` crea un fitxer temporal amb nom únic (no inventes noms com `/tmp/fitxer`).

## Depurar

```bash
bash -x script.sh          # mostra cada línia amb els valors reals
bash -n script.sh          # només comprova la sintaxi, no l'executa
set -x ... set +x          # traça només un tros
echo "DEBUG: var=[$var]" >&2   # els [] mostren espais amagats
```

**ShellCheck** troba la majoria d'errors típics (cometes, `[ ]` mal posats, variables sense usar):

```bash
sudo apt install shellcheck
shellcheck script.sh
```

## Plantilla per a començar

```bash title="plantilla.sh"
#!/bin/bash
# nom.sh — descripció curta
# Ús: ./nom.sh <arg1> [arg2]
set -euo pipefail

error() { echo "ERROR: $*" >&2; exit 1; }
log()   { echo "[$(date +'%F %T')] $*"; }

main() {
    [ $# -ge 1 ] || error "Ús: $0 <arg1> [arg2]"
    local arg1=$1
    local arg2=${2:-valor_per_defecte}

    log "Començant amb $arg1 i $arg2"
    # ... feina ...
    log "Fet"
}

main "$@"
```

Posar el codi en `main` i cridar-la al final obliga a definir abans totes les funcions i deixa l'script més ordenat.
