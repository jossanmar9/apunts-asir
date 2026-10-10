# 2. Variables i paràmetres

## Què és una variable

Una **variable** és una caixa amb nom on guardes un valor per a usar-lo després.

```bash
nom="Ana"           # guarde "Ana" en la caixa que es diu nom
echo "$nom"         # traure el que hi ha dins → mostra: Ana
```

Hi ha dues accions diferents:

| Acció | Com s'escriu | Exemple |
| ----- | ------------ | ------- |
| **Guardar** un valor | `nom=valor` (sense `$`) | `edat=30` |
| **Llegir** el valor | `$nom` (amb `$`) | `echo "$edat"` |

Recorda: **sense `$` per a guardar, amb `$` per a llegir.**

!!! danger "L'error número 1: espais al voltant de `=`"
    ```bash
    nom = "Ana"     # ❌ ERROR
    nom="Ana"       # ✅ BÉ
    ```
    Amb espais, Bash pensa que `nom` és una ordre i intenta executar-la. Dona l'error `nom: command not found`.

### Regles dels noms

- Poden tindre lletres, números i `_`, però **no poden començar per número**.
- Majúscules i minúscules són diferents: `nom` i `NOM` són dues variables distintes.
- Costum: les teues variables en **minúscules**. Les majúscules les usa el sistema (`HOME`, `PATH`...).

### Claus `{ }`: quan el nom va enganxat a altre text

```bash
fitxer="informe"
echo "$fitxer_2026.txt"     # ❌ busca una variable anomenada "fitxer_2026"
echo "${fitxer}_2026.txt"   # ✅ informe_2026.txt
```

Les claus diuen a Bash on acaba el nom de la variable.

## Guardar el resultat d'una ordre

Amb `$( ordre )` executes l'ordre i guardes el que mostra:

```bash
data=$(date +%F)                  # data = 2026-10-10
linies=$(wc -l < /etc/passwd)     # quantes línies té el fitxer
echo "Hui és $data i hi ha $linies usuaris"
```

## Variables que ja existixen (variables d'entorn)

El sistema ja en té algunes creades. Les pots usar sense crear-les:

| Variable | Què conté | Exemple de valor |
| -------- | --------- | ---------------- |
| `$USER` | el teu usuari | `ana` |
| `$HOME` | la teua carpeta personal | `/home/ana` |
| `$PWD` | la carpeta on estàs ara | `/home/ana/scripts` |
| `$HOSTNAME` | el nom de l'ordinador | `servidor01` |
| `$RANDOM` | un número a l'atzar (0–32767) | `18234` |

## Cometes: dobles, simples o cap

Este és un punt que confon molt. Mira la diferència:

```bash
nom="Pep"
echo "Hola $nom"     # Hola Pep     ← cometes DOBLES: canvia $nom pel valor
echo 'Hola $nom'     # Hola $nom    ← cometes SIMPLES: ho mostra tal qual
echo "Preu: \$5"     # Preu: $5     ← \ fa que el $ es mostre com a lletra
```

| Cometes | Què fan | Quan usar-les |
| ------- | ------- | ------------- |
| `"dobles"` | Canvien les variables pel seu valor | **Quasi sempre** |
| `'simples'` | Ho deixen tot literal | Quan vols que `$` es mostre tal qual |

### Per què cal posar cometes a les variables

```bash
fitxer="informe final.txt"     # el nom té un espai
rm $fitxer       # ❌ Bash veu DOS fitxers: "informe" i "final.txt"
rm "$fitxer"     # ✅ esborra "informe final.txt"
```

Sense cometes, Bash talla el valor per cada espai. **Regla: posa sempre `"$variable"` entre cometes dobles.**

## Paràmetres: dades que passes en executar l'script

Pots passar informació a l'script quan l'executes, escrivint-la darrere del nom. Cada paraula és un **argument** (o **paràmetre**):

```bash
./servei.sh apache2 restart
#           ──┬───  ───┬───
#            $1       $2
```

Dins de l'script, cada argument està en una variable especial:

| Variable | Què conté | En l'exemple |
| -------- | --------- | ------------ |
| `$0` | el nom de l'script | `./servei.sh` |
| `$1` | el primer argument | `apache2` |
| `$2` | el segon argument | `restart` |
| `$#` | **quants** arguments hi ha | `2` |
| `"$@"` | tots els arguments, un per un | `apache2` `restart` |

A partir del 10 cal claus: `${10}`.

### Exemple complet

```bash title="args.sh"
#!/bin/bash
echo "M'has executat com: $0"
echo "M'has passat $# arguments"
echo "El primer és: $1"
echo "Tots, un per línia:"
for arg in "$@"; do        # recorre els arguments un a un (bucles: tema 5)
    echo " - $arg"
done
```

```console
$ ./args.sh poma "pera verda" plàtan
M'has executat com: ./args.sh
M'has passat 3 arguments
El primer és: poma
Tots, un per línia:
 - poma
 - pera verda
 - plàtan
```

Fixa't que `"pera verda"`, en anar entre cometes, compta com **un sol** argument.

### `"$@"` o `"$*"`?

- `"$@"` → cada argument per separat. **És el que vols quasi sempre.**
- `"$*"` → tots junts en un sol text.

### `shift`: llevar el primer argument

`shift` esborra `$1` i fa córrer la resta: el que era `$2` passa a ser `$1`, etc. S'usa quan el primer argument és una opció i la resta són dades:

```bash
# ./calcula.sh sumar 4 5 6
operacio=$1     # sumar
shift           # ara $1=4, $2=5, $3=6 i "$@" = 4 5 6
```

## Valors per defecte

Si l'usuari no passa un argument, pots usar un valor per defecte:

```bash
dir=${1:-/var/log}    # si no hi ha $1, usa /var/log
```

Es llig: "*`dir` val `$1`, i si està buit, `/var/log`*".

## Constants

Una variable que no es pot canviar:

```bash
readonly BACKUP_DIR="/backup"
BACKUP_DIR="/tmp"   # error: és de només lectura
```

## Errors típics

| Error | Què passa | Solució |
| ----- | --------- | ------- |
| `nom = "Ana"` | `nom: command not found` | Sense espais: `nom="Ana"` |
| `echo nom` | Mostra la paraula "nom" | Falta el `$`: `echo "$nom"` |
| `$nom="Ana"` | Error estrany | Per a guardar, **sense** `$` |
| Variable buida sense saber per què | Has escrit el nom diferent (`$nmo`) | Revisa el nom lletra a lletra |
| `rm $fitxer` esborra coses que no tocava | El nom tenia espais | `rm "$fitxer"` |

!!! success "Per a l'examen"
    - Guardar: `var=valor` (**sense espais, sense `$`**)
    - Llegir: `"$var"` (**amb `$` i cometes dobles**)
    - Resultat d'una ordre: `var=$(ordre)`
    - `$1`, `$2`... arguments · `$#` quants · `"$@"` tots · `$0` nom de l'script
    - Valor per defecte: `${1:-valor}`
    - `"dobles"` expandixen variables, `'simples'` no
