# 3. Aritmètica i comparacions

## Aritmètica entera: `$(( ))`

```bash
a=17; b=5
echo $(( a + b ))   # 22
echo $(( a - b ))   # 12
echo $(( a * b ))   # 85
echo $(( a / b ))   # 3   ← divisió ENTERA, retalla decimals
echo $(( a % b ))   # 2   ← residu
echo $(( a ** 2 ))  # 289 ← potència
```

Dins de `$(( ))` no cal posar `$` davant de les variables. Per a modificar una variable:

```bash
i=0
(( i++ ))            # i = 1
(( i += 5 ))         # i = 6
i=$(( i * 2 ))       # i = 12
```

!!! warning "Percentatges: multiplica abans de dividir"
    `$(( 35 / 100 * 100 ))` dona **0** perquè `35/100` ja és 0 en enters.
    `$(( 35 * 100 / 100 ))` dona **35**.

## Decimals: `bc`

Bash no sap fer decimals. Per a això s'usa `bc`:

```bash
echo "scale=2; 10 / 3" | bc          # 3.33
mitjana=$(echo "scale=1; ($a + $b) / 2" | bc)
echo "4.5 > 3.2" | bc                # 1 (cert) o 0 (fals)
```

`scale` és el nombre de decimals. Per a mostrar-los amb format, `printf "%.2f\n" "$mitjana"`.

## Comparacions: `test`, `[ ]` i `[[ ]]`

`[ ... ]` és una **ordre** (equivalent a `test`). Per això necessita espais: `[ "$a" -gt 5 ]`. Torna 0 si la condició és certa.

### Números

| Operador | Significa | Mnemotècnia |
| -------- | --------- | ----------- |
| `-eq` | igual | **eq**ual |
| `-ne` | diferent | **n**ot **e**qual |
| `-lt` | menor | **l**ess **t**han |
| `-le` | menor o igual | **l**ess or **e**qual |
| `-gt` | major | **g**reater **t**han |
| `-ge` | major o igual | **g**reater or **e**qual |

Alternativa més natural per a números: `(( a > 5 ))`, `(( a == b ))`.

### Text

| Expressió | Cert si… |
| --------- | -------- |
| `[ "$a" = "$b" ]` | iguals (dins `[[ ]]` també `==`) |
| `[ "$a" != "$b" ]` | diferents |
| `[ -z "$a" ]` | buit (*zero length*) |
| `[ -n "$a" ]` | no buit |

!!! danger "`<` i `>` dins de `[ ]` NO comparen números"
    `[ 10 > 5 ]` crea un fitxer anomenat `5`. Usa `-gt` o `(( ))`.

### Fitxers

| Expressió | Cert si… |
| --------- | -------- |
| `-e f` | existix |
| `-f f` | és un fitxer normal |
| `-d f` | és un directori |
| `-s f` | existix i no està buit |
| `-r` `-w` `-x` | es pot llegir / escriure / executar |
| `-L f` | és un enllaç simbòlic |
| `f1 -nt f2` | f1 és més nou que f2 |

### Combinar

```bash
[ "$a" -gt 0 ] && [ "$a" -lt 10 ]     # I
[ "$a" -eq 0 ] || [ "$a" -eq 1 ]      # O
[ ! -d "$dir" ]                       # NO
[[ $a -gt 0 && $a -lt 10 ]]           # dins de [[ ]] es pot posar && i ||
```

### `[[ ]]`: la versió de Bash

- No parteix les variables per espais (però posa cometes igualment, és bon hàbit).
- Permet `&&`, `||`, `<`, `>` (aquestes dues comparen **text** alfabèticament).
- Patrons: `[[ $fitxer == *.log ]]`
- Expressions regulars: `[[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]`

```bash
if [[ $1 =~ ^[0-9]+$ ]]; then
    echo "$1 és un número enter positiu"
fi
```

## Comprovar si una variable és un número

```bash
es_numero() { [[ $1 =~ ^-?[0-9]+$ ]]; }

if ! es_numero "$1"; then
    echo "Error: '$1' no és un número" >&2
    exit 1
fi
```
