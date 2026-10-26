# 3. Aritmètica i comparacions

## Fer comptes: `$(( ))`

Bash no fa comptes si no li ho demanes. Si escrius `echo 2+3`, mostra el text `2+3`. Per a calcular, cal posar l'operació dins de `$(( ))`:

```bash
echo 2+3          # mostra: 2+3   (és només text)
echo $(( 2+3 ))   # mostra: 5     (ara sí calcula)
```

| Operació | Símbol | Exemple | Resultat |
| -------- | ------ | ------- | -------- |
| Sumar | `+` | `$(( 17 + 5 ))` | `22` |
| Restar | `-` | `$(( 17 - 5 ))` | `12` |
| Multiplicar | `*` | `$(( 17 * 5 ))` | `85` |
| Dividir | `/` | `$(( 17 / 5 ))` | `3` ⚠️ |
| Residu | `%` | `$(( 17 % 5 ))` | `2` |
| Potència | `**` | `$(( 2 ** 3 ))` | `8` |

!!! warning "La divisió només dona enters"
    `17 / 5` hauria de ser 3,4, però Bash **talla els decimals** i dona `3`. Bash només sap treballar amb números enters.

**El residu** (`%`) és el que sobra en una divisió. És molt útil per a saber si un número és **parell**: si `n % 2` dona 0, és parell.

### Amb variables

Dins de `$(( ))` no cal posar `$` davant de les variables (però si el poses també funciona):

```bash
a=10
b=3
suma=$(( a + b ))       # 13
echo "La suma és $suma"
```

### Sumar a una variable (comptadors)

```bash
i=0
i=$(( i + 1 ))   # i val 1
(( i++ ))        # forma curta: suma 1 → i val 2
(( i += 5 ))     # suma 5 → i val 7
```

### Percentatges: compte amb l'ordre

```bash
echo $(( 35 / 100 * 100 ))   # 0  ❌ perquè 35/100 = 0 (es tallen els decimals)
echo $(( 35 * 100 / 100 ))   # 35 ✅ multiplica primer, divideix després
```

**Regla: per a percentatges, multiplica per 100 abans de dividir.**

## Decimals: `bc`

Si necessites decimals, usa la calculadora `bc`:

```bash
echo "scale=2; 10 / 3" | bc        # 3.33
```

- `scale=2` vol dir "vull 2 decimals".
- El `|` passa l'operació a `bc` (les tuberies s'expliquen en el [tema 7](07-redireccions.md)).

Guardar-ho en una variable:

```bash
mitjana=$(echo "scale=2; ($a + $b) / 2" | bc)
```

## Comparar: `[ ]`

Per a preguntar "és major?", "són iguals?", "existix el fitxer?", s'usen els **claudàtors** `[ ]`.

```bash
[ 5 -gt 3 ]      # és 5 major que 3? → sí
```

`[ ]` no mostra res. El que fa és deixar el codi d'eixida (`$?`): **0 si és cert**, 1 si és fals. Normalment s'usa dins d'un `if` ([tema 4](04-condicionals.md)):

```bash
if [ "$edat" -ge 18 ]; then
    echo "Major d'edat"
fi
```

!!! danger "Els espais dins de `[ ]` són obligatoris"
    ```bash
    [5 -gt 3]        # ❌ error
    [ 5 -gt 3 ]      # ✅ espai després de [ i abans de ]
    ```
    `[` és en realitat una ordre, i com qualsevol ordre necessita espais per a separar-se dels arguments.

### Comparar números

No s'usen `<` i `>`, sinó unes abreviatures en anglés:

| Operador | Significa | Ve de l'anglés |
| -------- | --------- | -------------- |
| `-eq` | igual | **eq**ual |
| `-ne` | diferent | **n**ot **e**qual |
| `-lt` | menor que | **l**ess **t**han |
| `-le` | menor o igual | **l**ess or **e**qual |
| `-gt` | major que | **g**reater **t**han |
| `-ge` | major o igual | **g**reater or **e**qual |

```bash
[ "$nota" -ge 5 ]       # nota >= 5
[ "$a" -eq "$b" ]       # a == b
```

!!! danger "No uses `>` dins de `[ ]`"
    `[ 10 > 5 ]` **no compara**: crea un fitxer anomenat `5`. Dins de `[ ]`, `>` vol dir "guardar en un fitxer". Usa `-gt`.

Alternativa més còmoda per a números: `(( ))` sí que entén `<`, `>`, `==`:

```bash
if (( nota >= 5 )); then echo "Aprovat"; fi
```

### Comparar textos

| Expressió | És cert si... |
| --------- | ------------- |
| `[ "$a" = "$b" ]` | els dos textos són iguals |
| `[ "$a" != "$b" ]` | són diferents |
| `[ -z "$a" ]` | el text està **buit** |
| `[ -n "$a" ]` | el text **no** està buit |

```bash
if [ -z "$1" ]; then
    echo "No m'has passat cap argument"
fi
```

### Comprovar fitxers i carpetes

| Expressió | És cert si... |
| --------- | ------------- |
| `[ -e "$f" ]` | existix (fitxer o carpeta) |
| `[ -f "$f" ]` | existix i és un **fitxer** |
| `[ -d "$f" ]` | existix i és una **carpeta** (directori) |
| `[ -s "$f" ]` | existix i **no està buit** |
| `[ -r "$f" ]` | es pot **llegir** |
| `[ -w "$f" ]` | es pot **escriure** |
| `[ -x "$f" ]` | es pot **executar** |

```bash
if [ -f /etc/passwd ]; then
    echo "El fitxer existix"
fi
```

### Combinar condicions

| Vull... | S'escriu |
| ------- | -------- |
| les dues coses (I) | `[ cond1 ] && [ cond2 ]` |
| una o l'altra (O) | <code>[ cond1 ] &#124;&#124; [ cond2 ]</code> |
| el contrari (NO) | `[ ! cond ]` |

```bash
[ "$n" -gt 0 ] && [ "$n" -lt 10 ]   # n està entre 1 i 9
[ ! -d "$dir" ]                     # dir NO és una carpeta
```

### `[[ ]]`: la versió millorada

Bash té també els dobles claudàtors `[[ ]]`, que són més flexibles:

- Permeten `&&` i `||` dins: `[[ $n -gt 0 && $n -lt 10 ]]`
- Permeten comparar amb patrons: `[[ $fitxer == *.log ]]` (acaba en .log?)
- Permeten **expressions regulars** amb `=~` (vegeu baix)

## Comprovar si una dada és un número

Molt útil per a validar el que escriu l'usuari:

```bash
if [[ $1 =~ ^[0-9]+$ ]]; then
    echo "$1 és un número"
else
    echo "$1 NO és un número"
fi
```

Què vol dir `^[0-9]+$`:

| Tros | Significa |
| ---- | --------- |
| `^` | des del principi |
| `[0-9]` | un dígit |
| `+` | un o més dels anteriors |
| `$` | fins al final |

És a dir: "*des del principi fins al final, només dígits*". Per a acceptar també negatius: `^-?[0-9]+$` (el `-?` vol dir "pot haver-hi un guió o no").

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `echo 2+3` mostra `2+3` | Falta dir-li que calcule | `echo $(( 2+3 ))` |
| `10 / 3` dona `3` | Bash només fa enters | Usa `bc` per a decimals |
| `[: missing ']'` | Falten espais | `[ "$a" -gt 5 ]` |
| `[ 10 > 5 ]` crea un fitxer | `>` és redirecció | Usa `-gt` |
| `integer expression expected` | La variable no té un número (està buida o té text) | Comprova-la abans |
| `[ $a = "x" ]` dona error si `a` està buida | Sense cometes desapareix | `[ "$a" = "x" ]` |

!!! success "Per a l'examen"
    - Comptes: `$(( a + b ))` · residu `%` · **només enters**
    - Decimals: `echo "scale=2; 10/3" | bc`
    - Percentatge: **multiplica abans de dividir**
    - Números: `-eq -ne -lt -le -gt -ge` (o `(( a > b ))`)
    - Textos: `=`, `!=`, `-z` (buit), `-n` (no buit)
    - Fitxers: `-e` existix, `-f` fitxer, `-d` carpeta
    - **Espais dins de `[ ]` obligatoris**
    - És número?: `[[ $x =~ ^[0-9]+$ ]]`
