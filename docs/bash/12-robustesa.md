# 12. Scripts robustos

Un script "robust" és el que **no es trenca** quan l'usuari s'equivoca: si falten arguments, si el fitxer no existix, si escriu text on havia d'anar un número... En lloc de fer coses estranyes, avisa i acaba.

En els exàmens, **comprovar els arguments sol puntuar**.

## Comprovar els arguments al principi

La idea: abans de fer res, comprova que tens tot el que necessites. Si falta alguna cosa, explica com s'usa i ix.

```bash title="neteja.sh"
#!/bin/bash
# Esborra els fitxers d'una carpeta que tinguen més de N dies
# Ús: ./neteja.sh <carpeta> <dies>

# 1. Hi ha exactament 2 arguments?
if [ $# -ne 2 ]; then
    echo "Ús: $0 <carpeta> <dies>" >&2
    exit 1
fi

# 2. El primer és una carpeta que existix?
if [ ! -d "$1" ]; then
    echo "Error: '$1' no és una carpeta" >&2
    exit 2
fi

# 3. El segon és un número?
if ! [[ $2 =~ ^[0-9]+$ ]]; then
    echo "Error: els dies han de ser un número" >&2
    exit 3
fi

# Tot correcte: ja podem treballar
carpeta=$1
dies=$2
find "$carpeta" -type f -mtime +"$dies" -print -delete
```

**Per què així:**

- Els missatges d'error van a `>&2` (el canal d'errors).
- Cada error ix amb un número diferent (`exit 1`, `exit 2`...). Així, si un altre script el crida, pot saber què ha fallat.
- Guardar `$1` i `$2` en variables amb nom (`carpeta`, `dies`) fa que la resta de l'script s'entenga millor.

### Forma curta

Les mateixes comprovacions es poden escriure en una línia cadascuna:

```bash
[ $# -eq 2 ]          || { echo "Ús: $0 <carpeta> <dies>" >&2; exit 1; }
[ -d "$1" ]           || { echo "No és una carpeta: $1" >&2; exit 2; }
[[ $2 =~ ^[0-9]+$ ]]  || { echo "Els dies han de ser un número" >&2; exit 3; }
```

Es llig: "*o es complix açò, o mostra l'error i ix*".

### Altres comprovacions habituals

```bash
# És root?
if [ "$EUID" -ne 0 ]; then
    echo "Has d'executar-lo com a root (sudo)" >&2
    exit 1
fi

# Està instal·lat un programa?
if ! command -v rsync > /dev/null; then
    echo "Cal instal·lar rsync" >&2
    exit 1
fi

# Es pot llegir el fitxer?
[ -r "$fitxer" ] || { echo "No es pot llegir $fitxer" >&2; exit 1; }
```

## `set`: fer que Bash siga més estricte

Per defecte, Bash és molt permissiu: si una ordre falla, continua amb la següent com si res. Això pot ser perillós. Amb esta línia al principi de l'script, Bash para en el primer problema:

```bash
set -euo pipefail
```

| Opció | Què fa |
| ----- | ------ |
| `-e` | Para l'script si una ordre falla |
| `-u` | Para si uses una variable que no existix (detecta errors de lletra) |
| `-o pipefail` | En una tuberia (<code>a &#124; b</code>), considera error si **qualsevol** part falla |

!!! example "Per què importa"
    ```bash
    cd /carpeta/que/no/existix
    rm -rf *
    ```
    Sense `set -e`, si el `cd` falla, el `rm` s'executa en la carpeta **on estaves**. Amb `set -e`, l'script para en el `cd` i no esborra res.

## Trobar errors (depurar)

Quan un script no fa el que esperes:

### 1. Mira què està fent: `bash -x`

```bash
bash -x script.sh
```

Mostra cada ordre abans d'executar-la, **amb els valors reals** de les variables (les línies que comencen per `+`):

```console
+ nom=Ana
+ '[' Ana = Pep ']'
+ echo 'No és Pep'
No és Pep
```

Així veus de seguida si una variable està buida o té un valor que no esperaves.

### 2. Mostra el valor d'una variable

```bash
echo "DEBUG: nom=[$nom]" >&2
```

Els `[ ]` serveixen per a veure si hi ha espais amagats o si està buida (`nom=[]`).

### 3. Comprova la sintaxi sense executar

```bash
bash -n script.sh       # si no diu res, la sintaxi és correcta
```

### 4. ShellCheck

És un programa que revisa l'script i et diu els errors típics (cometes que falten, variables mal escrites...):

```bash
sudo apt install shellcheck
shellcheck script.sh
```

També es pot usar en línia: <https://www.shellcheck.net/>

## Plantilla per a començar qualsevol script

```bash title="plantilla.sh"
#!/bin/bash
# nom.sh — Què fa l'script en una línia
# Ús: ./nom.sh <argument1> [argument2]

# Funció per a mostrar errors i eixir
error() {
    echo "ERROR: $*" >&2
    exit 1
}

# 1. Comprovar arguments
[ $# -ge 1 ] || error "Ús: $0 <argument1> [argument2]"

# 2. Guardar arguments en variables amb nom clar
arg1=$1
arg2=${2:-valor_per_defecte}     # opcional

# 3. Fer la feina
echo "Treballant amb $arg1 i $arg2..."

# 4. Acabar bé
exit 0
```

!!! success "Per a l'examen"
    - **Comprova sempre** el nombre d'arguments: `[ $# -eq N ] || { echo "Ús: ..." >&2; exit 1; }`
    - Comprova que els fitxers/carpetes existixen: `-f`, `-d`
    - Comprova que els números són números: `[[ $x =~ ^[0-9]+$ ]]`
    - Errors a stderr: `echo "..." >&2` i `exit 1`
    - Si no funciona: `bash -x script.sh`
