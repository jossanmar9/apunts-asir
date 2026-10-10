# 4. Control de flux

Normalment un programa s'executa línia a línia, de dalt a baix. Amb el **control de flux** canvies això:

- **Condicionals** (`if`): executar una cosa **només si** es complix una condició.
- **Bucles** (`for`, `while`): **repetir** una cosa diverses vegades.

## `if`: prendre decisions

```python
edat = int(input("Edat: "))

if edat >= 18:
    print("Eres major d'edat")
else:
    print("Eres menor d'edat")
```

Com es llig: "*si edat és major o igual que 18, mostra... ; si no, mostra...*".

**Fixa't en:**

- Els **dos punts** `:` al final de la línia de l'`if` i de l'`else`.
- Les línies de dins tenen **4 espais** davant. Així sap Python què està dins de l'`if`.

### Diverses opcions: `elif`

```python
nota = float(input("Nota: "))

if nota < 5:
    print("Suspés")
elif nota < 7:
    print("Aprovat")
elif nota < 9:
    print("Notable")
else:
    print("Excel·lent")
```

Python comprova les condicions de dalt a baix i executa **només la primera certa**. Quan arriba a `elif nota < 7`, ja sap que la nota no és menor que 5.

### Comprovar si un valor és un d'uns quants

```python
resposta = input("Continuar? ")
if resposta in ("s", "si", "sí", "S"):
    print("Continuem")
```

### `if` en una línia

```python
estat = "aprovat" if nota >= 5 else "suspés"
```

## `match`: moltes opcions d'una variable

Equivalent al `case` de Bash (Python 3.10 o posterior):

```python
opcio = input("Opció: ")

match opcio:
    case "1":
        print("Has triat la primera")
    case "2" | "3":
        print("Has triat la segona o la tercera")
    case _:
        print("Opció no vàlida")
```

`case _:` és "qualsevol altra cosa", com l'`else`.

## Bucles

### `for`: per a cada element

```python
for servei in ["ssh", "nginx", "cron"]:
    print(f"Comprovant {servei}")
```

```console
Comprovant ssh
Comprovant nginx
Comprovant cron
```

La variable `servei` agafa cada valor de la llista, un per volta, i s'executa el bloc de dins.

`for` pot recórrer qualsevol col·lecció: una llista, les lletres d'un text, les línies d'un fitxer...

```python
for lletra in "hola":
    print(lletra)
```

### `range`: repetir N vegades o comptar

```python
for i in range(5):
    print(i)          # 0 1 2 3 4  (5 voltes, comença en 0)
```

| S'escriu | Genera | |
| -------- | ------ | - |
| `range(5)` | 0, 1, 2, 3, 4 | 5 números des de 0 |
| `range(1, 6)` | 1, 2, 3, 4, 5 | des de 1 fins a 6 **sense incloure'l** |
| `range(0, 20, 5)` | 0, 5, 10, 15 | de 5 en 5 |
| `range(10, 0, -1)` | 10, 9, ... 1 | cap enrere |

!!! warning "El final no s'inclou"
    `range(1, 10)` va de 1 a **9**. Per a arribar a 10: `range(1, 11)`.

```python
# Taula de multiplicar del 7
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
```

### `enumerate`: tindre també la posició

```python
noms = ["Ana", "Pep", "Laura"]
for num, nom in enumerate(noms, start=1):
    print(f"{num}. {nom}")
```

```console
1. Ana
2. Pep
3. Laura
```

### `while`: mentre siga cert

```python
compte = 5
while compte > 0:
    print(compte)
    compte -= 1        # resta 1 (si no, no acabaria mai)
print("Ja!")
```

`while` s'usa quan **no saps quantes voltes** faràs. Per exemple, preguntar fins que la resposta siga vàlida:

```python
clau = ""
while clau != "secret":
    clau = input("Contrasenya: ")
print("Correcta!")
```

!!! danger "Bucle infinit"
    Si la condició del `while` no deixa mai de ser certa, el programa no acaba. Per a parar-lo: ++ctrl+c++.

## `break` i `continue`

| Paraula | Què fa |
| ------- | ------ |
| `break` | **ix del bucle** immediatament |
| `continue` | deixa la volta actual i **passa a la següent** |

```python
for n in range(1, 11):
    if n % 2 == 0:
        continue          # si és parell, salta'l
    if n > 7:
        break             # si passa de 7, acaba
    print(n)
# mostra: 1 3 5 7
```

### El patró més útil: repetir fins que l'usuari escriga bé

```python
while True:                              # bucle "infinit"...
    text = input("Escriu un número: ")
    if text.isdigit():                   # si és un número...
        numero = int(text)
        break                            # ...ix del bucle
    print("Això no és un número")
print(f"Has escrit {numero}")
```

## Bucles dins de bucles

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(fila * columna, end=" ")   # end=" " → no baixa de línia
    print()                              # baixa de línia al final de cada fila
```

```console
1 2 3
2 4 6
3 6 9
```

Per cada volta del bucle de fora, el de dins fa **totes** les seues voltes.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `SyntaxError: expected ':'` | Falten els dos punts | `if x > 5:` · `for x in y:` |
| `IndentationError` | El bloc no té els espais correctes | 4 espais dins de cada bloc |
| `range(1, 10)` no arriba a 10 | El final no s'inclou | `range(1, 11)` |
| El `while` no acaba mai | La condició sempre és certa | Canvia la variable dins del bucle |
| `if x = 5:` | `=` guarda, `==` compara | `if x == 5:` |

!!! success "Per a l'examen"
    ```python
    if cond:
        ...
    elif cond:
        ...
    else:
        ...

    for x in llista:
        ...
    for i in range(1, 11):     # 1..10
        ...
    while cond:
        ...
    while True:                # repetir fins a break
        if ok: break
    ```

    - **`:` al final** i **4 espais** dins de cada bloc
    - `range(a, b)` → de `a` a `b-1`
    - `break` ix · `continue` passa a la següent
