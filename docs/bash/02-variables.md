# 2. Variables i paràmetres

## Variables

```bash
nom="Jose"            # guardar: SENSE espais al voltant de =
echo "$nom"           # llegir: amb $
echo "Hola ${nom}s"   # claus quan va enganxada a altre text
```

!!! danger "L'error número 1"
    `nom = "Jose"` no és una assignació: Bash intenta executar una ordre anomenada `nom` amb els arguments `=` i `Jose`.

- Els noms distingixen majúscules: `nom` i `NOM` són diferents.
- Per convenció, **majúscules per a variables d'entorn** (`PATH`, `HOME`) i minúscules per a les teues.
- Una variable que no existix val buit, i Bash no avisa (llevat que uses `set -u`, vegeu el [tema 12](12-robustesa.md)).

### Capturar l'eixida d'una ordre

```bash
data=$(date +%F)                 # 2026-10-10
usuaris=$(wc -l < /etc/passwd)   # número de línies
echo "Còpia del $data"
```

La forma antiga amb cometes invertides `` `date` `` també funciona, però `$( )` es pot niar i es llig millor.

### Variables d'entorn útils

| Variable | Valor |
| -------- | ----- |
| `$USER` | usuari actual |
| `$HOME` | directori personal |
| `$PWD` | directori actual |
| `$HOSTNAME` | nom de la màquina |
| `$PATH` | on es busquen les ordres |
| `$RANDOM` | número aleatori 0–32767 |
| `$SECONDS` | segons des que ha començat l'script |

Per a que un programa fill veja una variable, cal exportar-la: `export EDITOR=nano`.

## Cometes: la diferència important

```bash
nom="Pep"
echo "Hola $nom"     # Hola Pep        → dobles: SÍ expandixen $
echo 'Hola $nom'     # Hola $nom       → simples: tot literal
echo "Preu: \$5"     # Preu: $5        → \ escapa un caràcter
```

**Posa sempre cometes dobles a les variables.** Sense elles, Bash parteix el valor pels espais i expandix comodins:

```bash
fitxer="informe final.txt"
rm $fitxer       # intenta esborrar "informe" i "final.txt" ❌
rm "$fitxer"     # esborra "informe final.txt" ✅
```

## Paràmetres posicionals

Són els arguments que passes en executar l'script.

```bash
./servei.sh apache2 restart
#           └─ $1 ─┘ └─$2──┘
```

| Variable | Significat |
| -------- | ---------- |
| `$0` | nom de l'script |
| `$1` … `$9` | arguments 1 a 9 |
| `${10}` | a partir del 10, amb claus |
| `$#` | **quants** arguments hi ha |
| `"$@"` | tots, **cadascun com a paraula separada** (el que vols quasi sempre) |
| `"$*"` | tots junts en **una sola** cadena |
| `$?` | codi d'eixida de l'última ordre |
| `$$` | PID de l'script |

```bash title="args.sh"
#!/bin/bash
echo "Script: $0"
echo "Has passat $# arguments"
for arg in "$@"; do
    echo " - $arg"
done
```

```console
$ ./args.sh uno "dos tres" quatre
Script: ./args.sh
Has passat 3 arguments
 - uno
 - dos tres
 - quatre
```

### `shift`

Descarta `$1` i desplaça la resta: `$2` passa a ser `$1`, etc. Útil quan el primer argument és una opció i la resta són dades.

```bash
operacio=$1
shift                 # ara "$@" només conté els números
echo "Opció: $operacio. Números: $*"
```

## Valors per defecte

```bash
dir=${1:-/var/log}          # si $1 està buit, usa /var/log
port=${PORT:=8080}          # i a més l'assigna a PORT
: "${1:?Falta el directori}" # si està buit, error i ix
```

## Constants

```bash
readonly BACKUP_DIR="/backup"
BACKUP_DIR="/tmp"   # error: variable de només lectura
```
