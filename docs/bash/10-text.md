# 10. Processar text

## Retallar variables sense ordres externes

```bash
ruta="/var/log/nginx/access.log.gz"

echo "${#ruta}"            # 28 → longitud
echo "${ruta:0:8}"         # /var/log → des de la posició 0, 8 caràcters
echo "${ruta##*/}"         # access.log.gz → com basename
echo "${ruta%/*}"          # /var/log/nginx → com dirname
echo "${ruta%%.*}"         # /var/log/nginx/access → lleva totes les extensions
echo "${ruta%.gz}"         # /var/log/nginx/access.log → lleva un sufix
echo "${ruta/log/LOG}"     # canvia la primera aparició
echo "${ruta//log/LOG}"    # canvia totes
echo "${nom^^}" "${nom,,}" # MAJÚSCULES / minúscules
```

| Patró | Lleva... |
| ----- | -------- |
| `${v#pat}` | pel **principi**, el tros **més curt** |
| `${v##pat}` | pel **principi**, el tros **més llarg** |
| `${v%pat}` | pel **final**, el tros **més curt** |
| `${v%%pat}` | pel **final**, el tros **més llarg** |

Truc: al teclat `#` va abans que `%`, igual que el principi va abans que el final.

## `cut`: columnes

```bash
cut -d: -f1 /etc/passwd          # camp 1 separat per :
cut -d: -f1,6 /etc/passwd        # camps 1 i 6
cut -d' ' -f2- fitxer            # del 2 fins al final
cut -c1-10 fitxer                # caràcters 1 a 10
```

`cut` només accepta **un** caràcter de separació. Si hi ha diversos espais seguits, comprimix-los abans amb `tr -s ' '` o usa `awk`.

## `tr`: canviar o esborrar caràcters

```bash
echo "hola" | tr 'a-z' 'A-Z'     # HOLA
echo "a  b    c" | tr -s ' '     # a b c (comprimix repetits)
echo "tel: 600-11-22" | tr -d -c '0-9\n'   # 6001122 (esborra el que NO és dígit)
tr ':' '\n' <<< "$PATH"          # un directori per línia
```

## `sort`, `uniq`, `wc`, `head`, `tail`

```bash
sort fitxer              # alfabètic
sort -n                  # numèric
sort -rn                 # numèric invers
sort -t: -k3 -n /etc/passwd   # per la columna 3 (separador :)
sort -h                  # mides humanes (1K, 2M, 3G)
sort -u                  # sense repetits

uniq                     # lleva repetits CONSECUTIUS (ordena abans!)
uniq -c                  # compta quantes vegades
sort | uniq -c | sort -rn | head    # el "top" de qualsevol cosa

wc -l f                  # línies   (wc -l < f → només el número)
head -n 5  /  tail -n 5  /  tail -f log
```

## `awk`: columnes amb potència

`awk` separa cada línia en camps (`$1`, `$2`... `$NF` és l'últim) per espais, encara que n'hi haja diversos.

```bash
awk '{print $1}' access.log                     # primera columna
awk -F: '$3 >= 1000 {print $1}' /etc/passwd     # usuaris "humans"
awk '{s += $5} END {print s}' fitxer            # suma la columna 5
df -h | awk 'NR > 1 {print $5, $6}'             # salta la capçalera
awk -F: '{print NR": "$1}' /etc/passwd          # numera les línies
```

| Variable | Significat |
| -------- | ---------- |
| `$0` | la línia sencera |
| `$1`… | camps |
| `NF` | nombre de camps; `$NF` l'últim |
| `NR` | número de línia |
| `-F` | separador |

## `sed`: buscar i substituir

```bash
sed 's/vell/nou/' f          # primera aparició de cada línia
sed 's/vell/nou/g' f         # totes
sed -i 's/^#Port 22/Port 2222/' /etc/ssh/sshd_config   # edita el fitxer
sed -i.bak '...' f           # i guarda còpia en f.bak
sed -n '5,10p' f             # només les línies 5 a 10
sed '/^#/d; /^$/d' f         # esborra comentaris i línies buides
```

## `printf`: eixida amb format

```bash
printf "%-15s %5s\n" "USUARI" "UID"
printf "%-15s %5d\n" "pep" 1001
printf "%.2f\n" 3.14159       # 3.14
printf "%03d\n" 7             # 007
```

`%-15s` = text alineat a l'esquerra en 15 caràcters. Ideal per a fer taules.
