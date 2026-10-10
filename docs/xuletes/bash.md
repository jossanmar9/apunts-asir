# Xuleta de Bash

> Consulta ràpida. La teoria completa està en la [secció de Bash](../bash/index.md).

---

## ⚠️ Les 5 regles d'or

| ❌ Malament | ✅ Bé | Per què |
|---|---|---|
| `[-z "$1"]` | `[ -z "$1" ]` | `[` és una **ordre**: necessita espais al voltant |
| `num = 5` | `num=5` | En l'assignació, **mai** espais al voltant del `=` |
| `[ num -lt 70 ]` | `[ "$num" -lt 70 ]` | **Sense `$` per a guardar, amb `$` per a llegir** |
| `elif [ ... ]` | `elif [ ... ]; then` | Cada `if` i `elif` necessita el seu `then` |
| `echo "$nom"` sense haver-la creat | crear-la abans | Una variable que no existix val **buit**, i Bash no avisa |

Posa sempre cometes a les variables, `"$var"`. T'estalvia errors estranys amb valors buits i espais.

---

## 📄 Estructura d'un script

```bash
#!/bin/bash
# Comentari: què fa el script

echo "Hola món"
```

```bash
chmod +x script.sh     # donar permís d'execució (una sola vegada)
./script.sh            # executar-lo
bash script.sh         # executar-lo sense permís d'execució
```

---

## 📦 Variables

```bash
nom="Ana"                 # guardar (sense espais!)
echo "$nom"                # llegir (amb $)
echo "Hola ${nom}!"        # amb claus quan va enganxada a altre text

data=$(date +%F)           # guardar el RESULTAT d'una ordre → $( )
suma=$(( 3 + 4 ))          # guardar el resultat d'un CÀLCUL → $(( ))
```

| Sintaxi | Serveix per a | Exemple |
|---|---|---|
| `$var` | llegir una variable | `echo "$nom"` |
| `$( ordre )` | resultat d'una ordre | `n=$(grep -c ERROR f.log)` |
| `$(( expr ))` | càlcul amb enters | `p=$(( $1 * 100 / $2 ))` |

**Variables d'entorn:** `$HOME`, `$USER`, `$PWD`, `$PATH`, `$SHELL`, `$LANG`

---

## 🎯 Paràmetres posicionals

```bash
./script.sh apache2 80
#           └─ $1 ─┘ └$2┘
```

| Variable | Significat |
|---|---|
| `$0` | nom del script |
| `$1` … `$9` | primer … novè argument |
| `$#` | **quants** arguments hi ha |
| `"$@"` | tots els arguments, **cadascun per separat** (el que normalment vols) |
| `"$*"` | tots els arguments **junts en un sol text** |
| `$?` | codi d'eixida de l'última ordre (0 = tot bé) |

**Comprovar els arguments al principi**
```bash
if [ $# -ne 2 ]; then
    echo "Ús: $0 <usats> <totals>"
    exit 1
fi
```

---

## ⌨️ Llegir del teclat

```bash
read -p "Com et dius? " nom
echo "Hola $nom"
```
Si l'enunciat diu **"com a argument"** o **"paràmetre posicional"**, usa `$1` i **no** `read`.

---

## 🔢 Aritmètica

```bash
echo $(( 10 + 3 ))   # 13
echo $(( 10 - 3 ))   # 7
echo $(( 10 * 3 ))   # 30
echo $(( 10 / 3 ))   # 3   ← només enters, retalla decimals
echo $(( 10 % 3 ))   # 1   ← residu (mòdul)

i=$(( i + 1 ))       # sumar 1 a una variable (comptador)
```

**Percentatges: multiplica ABANS de dividir**
```bash
echo $(( 35 / 100 * 100 ))   # 0   ❌
echo $(( 35 * 100 / 100 ))   # 35  ✅
```

**Decimals amb `bc`**
```bash
z=$(echo "4.1+5.2" | bc)          # 9.3
echo "scale=2; 10/3" | bc         # 3.33
```

---

## ❓ Condicionals: `if`

```bash
if [ CONDICIÓ ]; then
    ...
elif [ ALTRA_CONDICIÓ ]; then
    ...
else
    ...
fi
```

Amb `elif`, l'ordre importa: quan arribes a l'`elif`, ja saps que la condició anterior era **falsa**, així que no cal tornar-la a comprovar.

```bash
if [ "$p" -lt 70 ]; then echo "OK"
elif [ "$p" -lt 90 ]; then echo "AVISO"      # ja sé que p >= 70
else echo "CRÍTICO"                          # ja sé que p >= 90
fi
```

### Comparar NÚMEROS

| Operador | Significa | Recorda-ho |
|---|---|---|
| `-eq` | igual | **eq**ual |
| `-ne` | diferent | **n**ot **e**qual |
| `-lt` | menor que | **l**ess **t**han |
| `-le` | menor o igual | **l**ess or **e**qual |
| `-gt` | major que | **g**reater **t**han |
| `-ge` | major o igual | **g**reater or **e**qual |

Dins de `[ ]`, `<` i `>` **no** serveixen per a comparar números.

### Comparar TEXT

| Operador | Significa |
|---|---|
| `[ "$a" = "$b" ]` | textos iguals |
| `[ "$a" != "$b" ]` | textos diferents |
| `[ -z "$a" ]` | text **buit** (*zero length*) |
| `[ -n "$a" ]` | text **no** buit |
| `[ -v nom ]` | la variable està definida (sense `$`) |

### Comprovar FITXERS

| Operador | És cert si… |
|---|---|
| `-e` | existix (el que siga) |
| `-f` | és un **fitxer** normal |
| `-d` | és un **directori** |
| `-r` / `-w` / `-x` | té permís de lectura / escriptura / execució |
| `-s` | existix i **no** està buit |
| `-h` o `-L` | és un enllaç simbòlic |
| `-b` / `-c` | és un dispositiu de blocs / de caràcters |

### Combinar condicions

```bash
[ "$a" -gt 0 ] && [ "$a" -lt 10 ]    # I (AND)
[ "$a" -eq 0 ] || [ "$a" -eq 1 ]     # O (OR)
[ "$a" -gt 0 -a "$a" -lt 10 ]        # I dins del mateix [ ]
[ "$a" -eq 0 -o "$a" -eq 1 ]         # O dins del mateix [ ]
[ ! -f "$f" ]                        # NO (negació)
```

### `[ ]` vs `[[ ]]`
`[[ ]]` és la versió millorada de Bash: tolera variables sense cometes, permet `&&` i `||` dins i expressions regulars amb `=~`.
```bash
if [[ $email =~ ^.+@.+\..+$ ]]; then echo "Email vàlid"; fi
```

---

## 🔀 `case` (molts casos sobre la mateixa variable)

```bash
case "$1" in
    start)          echo "Arrancant..." ;;
    stop)           echo "Parant..." ;;
    restart|reload) echo "Reiniciant..." ;;
    *)              echo "Opció no vàlida" ;;
esac
```
`*)` vol dir "qualsevol altra cosa", com l'`else`. Cada cas acaba en `;;`.

---

## 🔁 Bucles

### `for` sobre una llista
```bash
for fruita in poma pera plàtan; do
    echo "$fruita"
done
```
A cada volta, la variable agafa el **valor següent** de la llista.

### `for` sobre fitxers ⭐
```bash
for entrada in ~/prueba_bash/*; do          # totes les entrades
    nombre=$(basename "$entrada")
    if [ -d "$entrada" ]; then
        echo "$nombre directorio"
    elif [ -f "$entrada" ]; then
        echo "$nombre fichero"
    fi
done
```

```bash
for fichero in "$1"/*.log; do                # només els .log de la carpeta $1
    nombre=$(basename "$fichero")
    errores=$(grep -c ERROR "$fichero")
    echo "$nombre → $errores ERROR"
done
```

`*` **no** entra a les subcarpetes. Per a buscar també dins d'elles:
```bash
for fichero in $(find "$1" -name "*.log"); do ...; done
```

### `for` estil C (comptar)
```bash
for (( i=1; i<=5; i++ )); do
    echo "Volta $i"
done
```

### `while` (mentre la condició siga certa)
```bash
i=1
while [[ $i -le 5 ]]; do
    echo "$i"
    i=$(( i + 1 ))        # si oblides açò → bucle infinit
done
```

### `until` (fins que la condició siga certa)
```bash
until [[ $port -ge 1 && $port -le 65535 ]]; do
    read -p "Port (1-65535): " port
done
```

| Ordre | Què fa dins d'un bucle |
|---|---|
| `continue` | salta a la **volta següent** |
| `break` | **ix** del bucle |

---

## 🧩 Funcions

```bash
saludar() {
    echo "Hola $1"            # $1 = primer argument DE LA FUNCIÓ
}

saludar "Ana"                # cridar-la (sense parèntesis!)
```
També es pot declarar com `function saludar() { ... }`.

**Tornar un TEXT o un número → `echo` + `$( )`**
```bash
doble() { echo $(( $1 * 2 )); }
resultat=$(doble 5)           # resultat = 10
```

**Tornar ÈXIT o ERROR → `return` (0 = bé, 1-255 = error)**
```bash
es_par() {
    if [ $(( $1 % 2 )) -eq 0 ]; then return 0; else return 1; fi
}

es_par 4
echo "Código devuelto: $?"    # 0

if es_par 7; then echo "Par"; else echo "Impar"; fi
```

**Funcions en un altre fitxer**
```bash
source ./funciones.sh
```

---

## 🧵 Arrays

```bash
serveis=(apache2 ssh mysql)
echo "${serveis[0]}"          # apache2 (es compta des de 0)
echo "${serveis[-1]}"         # mysql (l'últim)
echo "${serveis[@]}"          # tots
echo "${#serveis[@]}"         # quants n'hi ha → 3

for s in "${serveis[@]}"; do echo "$s"; done
```

---

## ✂️ Manipular text de variables

```bash
ruta="/home/ana/datos/app1.log"

echo "${#ruta}"          # longitud del text → 25
echo "${ruta:0:5}"       # des de la posició 0, 5 caràcters → /home
echo "${ruta##*/}"       # lleva tot fins a l'última /  → app1.log
echo "${ruta%/*}"        # lleva des de l'última /      → /home/ana/datos
echo "${ruta%.log}"      # lleva el sufix .log          → /home/ana/datos/app1
echo "${ruta/log/txt}"   # canvia la primera "log" per "txt"
```

| Patró | Lleva… |
|---|---|
| `${var#patró}` | per **davant**, el tros **més curt** |
| `${var##patró}` | per **davant**, el tros **més llarg** |
| `${var%patró}` | per **darrere**, el tros **més curt** |
| `${var%%patró}` | per **darrere**, el tros **més llarg** |

Per a recordar-ho: `#` lleva per **davant** i `%` per **darrere** (al teclat, `#` va abans que `%`).

---

## 🛠️ Ordres útils

| Ordre | Què fa | Exemple |
|---|---|---|
| `basename` | nom del fitxer **sense la ruta** | `basename /a/b/app.log` → `app.log` |
| `grep PATRÓ f` | mostra les línies que contenen PATRÓ | `grep ERROR app.log` |
| `grep -c` | **compta** les línies que coincidixen | `grep -c ERROR app.log` → `2` |
| `cut -d: -f1` | talla per camps | `cut -d: -f1 /etc/passwd` → usuaris |
| `sort` | ordena línies | `sort noms.txt` |
| `uniq -c` | lleva repetits i compta (sobre text ordenat) | `sort f \| uniq -c` |
| `tr` | canvia caràcters | `echo hola \| tr a-z A-Z` → `HOLA` |
| `awk` | processa columnes | `awk '{print $1}' access.log` |
| `sed` | busca i substituïx | `sed 's/vell/nou/g' f` |
| `find` | busca fitxers, també en subcarpetes | `find /var/log -name "*.log"` |
| `xargs` | passa una llista com a arguments d'una ordre | `find . -name "*.tmp" \| xargs rm` |

La tuberia `|` passa l'eixida d'una ordre com a entrada de la següent.

---

## 🐞 Depurar

```bash
bash -x script.sh       # mostra cada ordre amb els valors reals
bash -v script.sh       # mostra cada línia tal com està escrita
set -x  ...  set +x     # activa/desactiva la traça dins del script
```
**ShellCheck** (<https://www.shellcheck.net/>) detecta errors típics: enganxa-hi l'script o instal·la'l amb `sudo apt install shellcheck`.

**Truc:** si alguna cosa no funciona, posa `echo "DEBUG: var=$var"` just abans per a veure què val realment.
