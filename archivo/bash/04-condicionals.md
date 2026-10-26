# 4. Condicionals

## Prendre decisions: `if`

Un condicional fa que l'script faça una cosa **només si** es complix una condició. És com dir en valencià: "*si plou, agafa el paraigua; si no, agafa les ulleres de sol*".

### L'estructura

```bash
if [ CONDICIÓ ]; then
    # ordres si la condició és CERTA
else
    # ordres si la condició és FALSA
fi
```

- `if` = si
- `then` = aleshores
- `else` = si no (és opcional)
- `fi` = final de l'if (és `if` al revés)

### Exemple pas a pas

```bash title="edat.sh"
#!/bin/bash
read -p "Quants anys tens? " edat       # demana un número (read: tema 8)

if [ "$edat" -ge 18 ]; then             # si edat és major o igual que 18...
    echo "Eres major d'edat"            # ...mostra açò
else                                    # si no...
    echo "Eres menor d'edat"            # ...mostra açò altre
fi                                      # final de l'if
```

!!! note "Els espais de davant (indentació)"
    Les ordres de dins de l'`if` es posen amb uns espais davant. Bash no ho necessita, però fa que el codi es llija molt millor i que vegis on comença i on acaba cada bloc.

### Diverses opcions: `elif`

Quan hi ha més de dos camins, s'usa `elif` ("else if" = "si no, si..."):

```bash
if [ "$nota" -lt 5 ]; then
    echo "Suspés"
elif [ "$nota" -lt 7 ]; then
    echo "Aprovat"
elif [ "$nota" -lt 9 ]; then
    echo "Notable"
else
    echo "Excel·lent"
fi
```

Bash comprova les condicions **de dalt a baix** i executa **només la primera** que siga certa. Per això, quan arriba al segon `elif` ja sap que la nota no és menor que 5 ni que 7: no cal tornar-ho a comprovar.

## La condició pot ser qualsevol ordre

Recorda el **codi d'eixida** del [tema 1](01-primer-script.md): 0 si va bé, altre número si falla. L'`if` en realitat mira eixe codi. Per tant, pots posar **qualsevol ordre** com a condició, no només `[ ]`:

```bash
if grep -q "^ana:" /etc/passwd; then
    echo "L'usuari ana existix"
fi
```

- `grep -q` busca el text sense mostrar res: només diu si l'ha trobat (codi 0) o no (codi 1).

```bash
if ping -c1 8.8.8.8 &> /dev/null; then
    echo "Hi ha connexió a Internet"
else
    echo "No hi ha connexió"
fi
```

- `ping -c1` fa un sol ping. `&> /dev/null` amaga el que mostra ([tema 7](07-redireccions.md)).

## Moltes opcions sobre la mateixa variable: `case`

Quan has de comparar **una mateixa variable** amb molts valors, una cadena d'`elif` es fa llarga. `case` és més clar:

```bash
case "$1" in
    start)
        echo "Arrancant el servei..."
        ;;
    stop)
        echo "Parant el servei..."
        ;;
    restart)
        echo "Reiniciant..."
        ;;
    *)
        echo "Opció no vàlida. Usa: start, stop o restart"
        ;;
esac
```

Com es llig:

| Part | Significa |
| ---- | --------- |
| `case "$1" in` | mira què val `$1` |
| `start)` | si val `start`, fes el que hi ha a sota... |
| `;;` | ...fins ací (final d'esta opció) |
| `*)` | si no coincidix amb cap anterior (com l'`else`) |
| `esac` | final del case (`case` al revés) |

Trucs útils:

```bash
case "$resposta" in
    s|S|si|SI)  echo "Has dit que sí" ;;     # | separa diverses opcions
    n|N|no|NO)  echo "Has dit que no" ;;
    *)          echo "No t'entenc" ;;
esac

case "$fitxer" in
    *.jpg|*.png) echo "És una imatge" ;;     # * = qualsevol cosa
    *.txt)       echo "És un text" ;;
esac
```

## Condicionals curts: `&&` i `||`

Per a coses senzilles, hi ha una forma abreujada:

| S'escriu | Significa |
| -------- | --------- |
| `A && B` | fes A, i **si ha anat bé**, fes B |
| <code>A &#124;&#124; B</code> | fes A, i **si ha fallat**, fes B |

```bash
mkdir /tmp/prova && echo "Carpeta creada"       # només mostra el missatge si mkdir funciona
[ -d "$dir" ] || mkdir "$dir"                   # si la carpeta NO existix, crea-la
[ $# -eq 1 ] || { echo "Falta un argument"; exit 1; }   # si no hi ha 1 argument, error i ix
```

Les claus `{ ...; }` agrupen diverses ordres. Cal el `;` abans de `}`.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `syntax error near unexpected token 'else'` | Falta el `then` | `if [ ... ]; then` |
| `syntax error: unexpected end of file` | Falta el `fi` (o `done`, `esac`) | Tanca cada bloc |
| `[: missing ']'` | Falten espais | `[ "$a" -eq 1 ]` |
| `elif` sense `then` | Cada `elif` necessita el seu | `elif [ ... ]; then` |
| Al `case` s'executen dues opcions | Falta `;;` | Acaba cada opció amb `;;` |

!!! success "Per a l'examen"
    ```bash
    if [ cond ]; then
        ...
    elif [ cond ]; then
        ...
    else
        ...
    fi
    ```
    ```bash
    case "$var" in
        opcio1) ... ;;
        a|b)    ... ;;
        *)      ... ;;
    esac
    ```

    - La condició pot ser qualsevol ordre: `if grep -q "x" fitxer; then`
    - `A && B` → B si A va bé · `A || B` → B si A falla
