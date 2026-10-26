# 10. Processar text

Una gran part de l'administració de sistemes és **treballar amb text**: llegir logs, traure columnes de fitxers de configuració, comptar coses, ordenar... Este tema explica les eines per a fer-ho.

## Retallar el valor d'una variable

Bash pot llevar trossos d'una variable sense usar cap altra ordre. Per exemple, traure només el nom d'un fitxer d'una ruta:

```bash
ruta="/var/log/nginx/access.log.gz"

echo "${ruta##*/}"         # access.log.gz          → només el nom del fitxer
echo "${ruta%/*}"          # /var/log/nginx         → només la carpeta
echo "${ruta%.gz}"         # /var/log/nginx/access.log → sense l'extensió .gz
echo "${#ruta}"            # 28                     → quants caràcters té
echo "${ruta:0:8}"         # /var/log               → 8 caràcters des de la posició 0
```

### Com recordar-ho

- `#` lleva **pel principi** (per l'esquerra).
- `%` lleva **pel final** (per la dreta).
- Un símbol (`#` o `%`) lleva el tros **més curt** possible; dos (`##` o `%%`), el **més llarg**.

| Expressió | Lleva | Exemple amb `a.tar.gz` |
| --------- | ----- | ---------------------- |
| `${v#*.}` | pel principi, fins al primer `.` | `tar.gz` |
| `${v##*.}` | pel principi, fins a l'últim `.` | `gz` |
| `${v%.*}` | pel final, des de l'últim `.` | `a.tar` |
| `${v%%.*}` | pel final, des del primer `.` | `a` |

Truc: en el teclat, `#` està a l'esquerra de `%`, igual que el principi està a l'esquerra del final.

### Canviar text i majúscules

```bash
text="hola món hola"
echo "${text/hola/adéu}"    # adéu món hola  → canvia la primera
echo "${text//hola/adéu}"   # adéu món adéu  → canvia totes
echo "${text^^}"            # HOLA MÓN HOLA  → a majúscules
```

## `cut`: traure columnes

`cut` agafa una part de cada línia. Ideal per a fitxers amb camps separats per un caràcter:

```bash
cut -d: -f1 /etc/passwd        # el camp 1 → els noms d'usuari
cut -d: -f1,7 /etc/passwd      # els camps 1 i 7 → usuari i shell
cut -c1-5 fitxer.txt           # els caràcters 1 a 5 de cada línia
```

| Opció | Significa |
| ----- | --------- |
| `-d:` | el separador és `:` (*delimiter*) |
| `-f1` | vull el camp 1 (*field*) |
| `-c1-5` | vull els caràcters 1 a 5 |

!!! warning "`cut` i els espais"
    Si les columnes estan separades per **diversos** espais, `cut -d' '` no funciona bé (compta cada espai com un separador). En eixe cas usa `awk` o comprimix els espais abans amb `tr -s ' '`.

## `tr`: canviar o esborrar caràcters

```bash
echo "hola" | tr 'a-z' 'A-Z'      # HOLA → canvia minúscules per majúscules
echo "a   b    c" | tr -s ' '     # a b c → deixa un sol espai on n'hi ha diversos
echo "600-11-22-33" | tr -d '-'   # 600112233 → esborra els guions
```

## Ordenar, comptar i llevar repetits

```bash
sort noms.txt           # ordena alfabèticament
sort -n numeros.txt     # ordena com a números (sense -n, "10" aniria abans que "9")
sort -r noms.txt        # ordre invers
sort -u noms.txt        # ordena i lleva repetits

wc -l fitxer.txt        # quantes línies
wc -w fitxer.txt        # quantes paraules

head -5 fitxer.txt      # les 5 primeres línies
tail -5 fitxer.txt      # les 5 últimes
tail -f /var/log/syslog # va mostrant les línies noves en directe (++ctrl+c++ per a eixir)
```

### `uniq`: llevar repetits i comptar

`uniq` lleva les línies repetides **que estan seguides**. Per això quasi sempre va després de `sort`:

```bash
sort noms.txt | uniq          # cada nom una vegada
sort noms.txt | uniq -c       # cada nom amb quantes vegades apareix
```

### La combinació estrella: el "rànquing"

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -rn
```

1. `cut` trau la columna 7 (el shell de cada usuari).
2. `sort` els ordena (perquè els iguals queden junts).
3. `uniq -c` compta quants n'hi ha de cada.
4. `sort -rn` ordena pel compte, de major a menor.

Resultat: quins shells s'usen més. Canviant el `cut` serveix per a fer el rànquing de **qualsevol cosa** (IPs que més accedixen, usuaris amb més errors...).

## `awk`: treballar amb columnes

`awk` és més potent que `cut`. Separa cada línia en columnes per espais (encara que n'hi haja molts) i les anomena `$1`, `$2`, `$3`...

```bash
echo "ana 30 València" | awk '{print $1}'      # ana
echo "ana 30 València" | awk '{print $3, $1}'  # València ana
```

Exemples útils:

```bash
df -h | awk '{print $5, $6}'                     # % d'ús i punt de muntatge
awk -F: '{print $1}' /etc/passwd                 # -F: canvia el separador a :
awk -F: '$3 >= 1000 {print $1}' /etc/passwd      # només els usuaris amb UID >= 1000
awk '{suma += $2} END {print suma}' notes.txt    # suma la columna 2
```

| Cosa | Significa |
| ---- | --------- |
| `$1`, `$2`... | columna 1, 2... |
| `$0` | la línia sencera |
| `$NF` | l'última columna |
| `NR` | el número de línia |
| `-F:` | el separador és `:` |
| `condició {acció}` | fes l'acció només en les línies que complixen la condició |
| `END {...}` | fes açò al final, després de llegir-ho tot |

## `sed`: buscar i substituir

```bash
sed 's/vell/nou/' fitxer        # canvia la primera aparició de cada línia
sed 's/vell/nou/g' fitxer       # canvia totes (g = global)
sed -i 's/vell/nou/g' fitxer    # -i: modifica el fitxer de veritat
sed '/^#/d' fitxer              # esborra les línies que comencen per #
sed -n '5,10p' fitxer           # mostra només les línies 5 a 10
```

`s/vell/nou/` es llig: "*substituïx `vell` per `nou`*".

!!! warning "`sed -i` modifica el fitxer"
    Sense `-i`, `sed` només mostra el resultat per pantalla i el fitxer no canvia. Prova sempre primer sense `-i`.

## `printf`: mostrar dades alineades

`echo` mostra el text tal qual. `printf` permet donar-li format, per exemple per a fer taules:

```bash
printf "%-10s %5s\n" "USUARI" "UID"
printf "%-10s %5d\n" "root" 0
printf "%-10s %5d\n" "ana" 1000
```

```console
USUARI       UID
root           0
ana         1000
```

| Format | Significa |
| ------ | --------- |
| `%s` | un text |
| `%d` | un número enter |
| `%.2f` | un número amb 2 decimals |
| `%-10s` | text en 10 espais, alineat a l'**esquerra** |
| `%5d` | número en 5 espais, alineat a la **dreta** |
| `\n` | salt de línia (`printf` no el posa sol) |

!!! success "Per a l'examen"
    | Vull... | S'escriu |
    | ------- | -------- |
    | nom del fitxer d'una ruta | `${ruta##*/}` o `basename "$ruta"` |
    | carpeta d'una ruta | `${ruta%/*}` o `dirname "$ruta"` |
    | llevar extensió | `${f%.txt}` |
    | columna N separada per `:` | `cut -d: -fN` |
    | columna N separada per espais | `awk '{print $N}'` |
    | majúscules | `tr 'a-z' 'A-Z'` |
    | ordenar números | `sort -n` |
    | comptar repetits | <code>sort &#124; uniq -c</code> |
    | rànquing | <code>... &#124; sort &#124; uniq -c &#124; sort -rn</code> |
    | substituir en fitxer | `sed -i 's/vell/nou/g' f` |
    | sumar una columna | `awk '{s+=$2} END {print s}'` |
