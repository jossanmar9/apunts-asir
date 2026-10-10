# 5. Bucles

Un **bucle** repetix unes ordres diverses vegades. Serveix per a coses com "*per a cada fitxer de la carpeta, fes açò*" o "*mentre l'usuari no escriga un número vàlid, torna-li a preguntar*".

Hi ha tres tipus:

| Bucle | Quan usar-lo |
| ----- | ------------ |
| `for` | Saps sobre **què** vols repetir: una llista, uns fitxers, del 1 al 10... |
| `while` | Repetix **mentre** una condició siga certa |
| `until` | Repetix **fins que** una condició siga certa |

## `for`: per a cada element d'una llista

```bash
for fruita in poma pera plàtan; do
    echo "M'agrada la $fruita"
done
```

```console
M'agrada la poma
M'agrada la pera
M'agrada la plàtan
```

**Com funciona:** la variable `fruita` agafa el primer valor (`poma`) i s'executen les ordres entre `do` i `done`. Després agafa el segon (`pera`) i torna a executar-les. I així fins al final de la llista.

| Part | Significa |
| ---- | --------- |
| `for fruita in ...` | per a cada valor de la llista, guarda'l en `fruita` |
| `do` | comença el que es repetix |
| `done` | acaba el que es repetix |

### D'on pot vindre la llista

```bash
for i in 1 2 3 4 5; do ...; done          # una llista escrita a mà
for i in {1..10}; do ...; done            # del 1 al 10
for i in {0..100..10}; do ...; done       # del 0 al 100 de 10 en 10
for f in *.txt; do ...; done              # tots els .txt de la carpeta actual
for f in /var/log/*.log; do ...; done     # tots els .log d'una altra carpeta
for arg in "$@"; do ...; done             # tots els arguments de l'script
```

### Exemple: recórrer fitxers

```bash
for fitxer in /etc/*.conf; do
    echo "Fitxer: $fitxer"
done
```

L'asterisc `*` vol dir "qualsevol cosa". Bash el canvia per la llista de tots els fitxers que coincidixen.

!!! warning "Si no hi ha cap fitxer"
    Si no hi ha cap `.conf`, el bucle s'executa **una vegada** amb el text literal `/etc/*.conf`. Per a evitar-ho, comprova que existix:
    ```bash
    for f in /etc/*.conf; do
        [ -e "$f" ] || continue      # si no existix, salta a la següent volta
        echo "$f"
    done
    ```

### `for` per a comptar (estil C)

```bash
for (( i=1; i<=10; i++ )); do
    echo "7 x $i = $(( 7 * i ))"
done
```

Dins dels parèntesis hi ha tres parts separades per `;`:

1. `i=1` → valor inicial
2. `i<=10` → es repetix mentre açò siga cert
3. `i++` → què es fa al final de cada volta (sumar 1)

## `while`: mentre siga cert

```bash
compte=5
while [ "$compte" -gt 0 ]; do     # mentre compte siga major que 0...
    echo "$compte..."
    sleep 1                       # espera 1 segon
    compte=$(( compte - 1 ))      # resta 1 (si no, no acabaria mai!)
done
echo "Ja!"
```

```console
5...
4...
3...
2...
1...
Ja!
```

!!! danger "Bucle infinit"
    Si oblides canviar la variable de la condició (ací, `compte`), la condició sempre serà certa i el bucle no acabarà mai. Per a parar-lo: ++ctrl+c++.

## `until`: fins que siga cert

És el contrari del `while`: repetix **mentre la condició siga falsa**. Molt útil per a tornar a preguntar fins que l'usuari escriga una cosa vàlida:

```bash
until [[ $resposta == "s" || $resposta == "n" ]]; do
    read -p "Vols continuar? (s/n) " resposta
done
```

## Llegir un fitxer línia a línia ⭐

Esta és una de les coses que més es fan en scripts d'administració:

```bash
while read -r linia; do
    echo "He llegit: $linia"
done < fitxer.txt
```

**Com funciona:**

- `< fitxer.txt` (al final, després de `done`) fa que el bucle llija del fitxer.
- A cada volta, `read` agafa **una línia** i la guarda en `linia`.
- Quan s'acaben les línies, `read` falla i el bucle acaba.
- `-r` fa que les barres `\` es lligen tal qual (posa-la sempre).

### Fitxers amb camps separats

Molts fitxers del sistema tenen camps separats per un caràcter. Per exemple, `/etc/passwd` usa `:`:

```
ana:x:1000:1000:Ana Puig:/home/ana:/bin/bash
 1  2  3    4      5        6          7
```

Amb `IFS=:` li dius a `read` que talle per `:` i pots guardar cada camp en una variable:

```bash
while IFS=: read -r usuari clau uid gid nom home shell; do
    echo "L'usuari $usuari té la carpeta $home"
done < /etc/passwd
```

- `IFS` és el caràcter que s'usa per a separar. Per defecte són els espais.
- Si un camp no t'interessa, pots posar `_` com a nom: `read -r usuari _ uid _ _ home shell`.

!!! danger "Evita `cat fitxer | while read`"
    Funciona, però les variables que modifiques dins del bucle **es perden** en acabar:
    ```bash
    total=0
    cat numeros.txt | while read -r n; do total=$(( total + n )); done
    echo "$total"       # mostra 0 ❌

    total=0
    while read -r n; do total=$(( total + n )); done < numeros.txt
    echo "$total"       # mostra la suma correcta ✅
    ```

## Controlar el bucle: `break` i `continue`

| Ordre | Què fa |
| ----- | ------ |
| `continue` | Deixa la volta actual i **passa a la següent** |
| `break` | **Ix del bucle** del tot |

```bash
for n in {1..10}; do
    if [ $(( n % 2 )) -eq 0 ]; then
        continue            # si és parell, salta'l
    fi
    if [ "$n" -gt 7 ]; then
        break               # si passa de 7, acaba
    fi
    echo "$n"
done
# mostra: 1 3 5 7
```

## Menú que es repetix

Combinació típica: un bucle infinit (`while true`) amb un `case`, i `break` per a eixir:

```bash
while true; do
    echo "1) Veure la data"
    echo "2) Veure l'espai en disc"
    echo "3) Eixir"
    read -p "Tria: " opcio
    case $opcio in
        1) date ;;
        2) df -h ;;
        3) break ;;
        *) echo "Opció no vàlida" ;;
    esac
done
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `syntax error near unexpected token 'done'` | Falta el `do` | `for x in ...; do` |
| `unexpected end of file` | Falta el `done` | Tanca el bucle |
| No acaba mai | La condició del `while` no canvia | Modifica la variable dins del bucle |
| La variable val 0 després del bucle | Has usat <code>cat f &#124; while</code> | Usa `while ...; done < f` |
| `for f in $(ls)` falla amb noms amb espais | `$(ls)` talla pels espais | Usa `for f in *` |

!!! success "Per a l'examen"
    ```bash
    for x in a b c; do ...; done          # llista
    for i in {1..10}; do ...; done        # rang
    for f in *.log; do ...; done          # fitxers
    for (( i=1; i<=10; i++ )); do ...; done

    while [ cond ]; do ...; done          # mentre siga cert
    until [ cond ]; do ...; done          # fins que siga cert

    while IFS=: read -r a b c; do         # llegir fitxer línia a línia
        ...
    done < fitxer
    ```

    - `continue` → següent volta · `break` → ix del bucle
    - **Recorda canviar la variable** dins del `while`
