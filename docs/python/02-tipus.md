# 2. Tipus i variables

## Variables

Una **variable** és un nom que apunta a un valor. Serveix per a guardar dades i usar-les després.

```python
nom = "Ana"
edat = 30
print(nom)        # Ana
print(edat + 1)   # 31
```

El signe `=` vol dir **"guarda"**, no "és igual". `edat = 30` es llig "*guarda 30 en edat*".

A diferència de Bash, en Python **sí que pots posar espais** al voltant de `=` (de fet, és el costum) i **no cal `$`** per a llegir la variable.

## Tipus de dades

Cada valor és d'un **tipus**. Els bàsics són:

| Tipus | Nom en Python | Exemples | Per a què |
| ----- | ------------- | -------- | --------- |
| Número enter | `int` | `5`, `-3`, `1000` | comptar coses |
| Número decimal | `float` | `3.14`, `0.5`, `-2.0` | preus, mesures |
| Text | `str` | `"hola"`, `'Ana'` | noms, missatges |
| Sí / No | `bool` | `True`, `False` | condicions |
| Res | `None` | `None` | "encara no té valor" |

```python
quantitat = 5          # int
preu = 19.99           # float
producte = "Ratolí"    # str (el text va entre cometes)
disponible = True      # bool (amb majúscula: True / False)
```

!!! note "Decimals amb punt"
    En Python els decimals s'escriuen amb **punt**: `3.14`, no `3,14`.

Per a saber de quin tipus és un valor: `type(x)`.

```python
type(5)        # <class 'int'>
type("hola")   # <class 'str'>
```

## Operacions amb números

| Operació | Símbol | Exemple | Resultat |
| -------- | ------ | ------- | -------- |
| Sumar | `+` | `7 + 2` | `9` |
| Restar | `-` | `7 - 2` | `5` |
| Multiplicar | `*` | `7 * 2` | `14` |
| Dividir | `/` | `7 / 2` | `3.5` |
| Divisió entera | `//` | `7 // 2` | `3` (sense decimals) |
| Residu | `%` | `7 % 2` | `1` (el que sobra) |
| Potència | `**` | `2 ** 3` | `8` |

El **residu** (`%`) serveix per a saber si un número és parell: si `n % 2 == 0`, és parell.

### Abreviatures per a modificar una variable

```python
x = 10
x = x + 5    # x val 15
x += 5       # forma curta del mateix → x val 20
x -= 3       # x val 17
x *= 2       # x val 34
```

### Funcions útils amb números

```python
abs(-4)            # 4       → valor absolut (sense signe)
round(3.14159, 2)  # 3.14    → arredonir a 2 decimals
max(3, 8, 1)       # 8       → el major
min(3, 8, 1)       # 1       → el menor
```

Per a arrels i altres coses matemàtiques:

```python
import math
math.sqrt(16)      # 4.0     → arrel quadrada
math.pi            # 3.14159...
```

## Mostrar dades: `print`

```python
print("Hola")                    # Hola
print("Tinc", 30, "anys")        # Tinc 30 anys  (separa amb espais)
print("a", "b", sep="-")         # a-b           (sep canvia el separador)
```

La forma més còmoda de mesclar text i variables és amb una **f-string** (una `f` davant de les cometes i les variables entre `{ }`):

```python
nom = "Ana"
edat = 30
print(f"{nom} té {edat} anys")   # Ana té 30 anys
```

## Demanar dades: `input`

```python
nom = input("Com et dius? ")
print(f"Hola, {nom}")
```

`input` mostra el missatge, espera que l'usuari escriga i prema ++enter++, i torna el que ha escrit.

!!! danger "L'error més típic: `input` sempre torna TEXT"
    ```python
    n = input("Escriu un número: ")    # l'usuari escriu 5
    print(n * 2)                       # 55   ❌ repetix el text "5" dues vegades
    ```
    Encara que l'usuari escriga un número, `input` el torna com a text (`"5"`). Per a fer comptes, cal **convertir-lo**:
    ```python
    n = int(input("Escriu un número: "))    # converteix a enter
    print(n * 2)                            # 10   ✅
    ```

## Convertir entre tipus

| Funció | Converteix a | Exemple | Resultat |
| ------ | ------------ | ------- | -------- |
| `int()` | enter | `int("42")` | `42` |
| `float()` | decimal | `float("3.5")` | `3.5` |
| `str()` | text | `str(42)` | `"42"` |

```python
edat = int(input("Edat: "))        # per a números enters
preu = float(input("Preu: "))      # per a números amb decimals
missatge = "Tens " + str(edat) + " anys"   # per a unir text amb un número
```

Si el text no és un número (`int("hola")`), dona l'error `ValueError`. En el [tema 8](08-excepcions.md) veuràs com controlar-ho.

## Comparacions i booleans

Una **comparació** dona `True` (cert) o `False` (fals):

| Operador | Significa | Exemple | Resultat |
| -------- | --------- | ------- | -------- |
| `==` | igual | `5 == 5` | `True` |
| `!=` | diferent | `5 != 3` | `True` |
| `<` | menor | `5 < 3` | `False` |
| `>` | major | `5 > 3` | `True` |
| `<=` | menor o igual | `5 <= 5` | `True` |
| `>=` | major o igual | `3 >= 5` | `False` |

!!! warning "`=` i `==` són diferents"
    - `=` **guarda** un valor: `x = 5`
    - `==` **compara**: `x == 5` (val `True` o `False`)

Per a combinar condicions:

| Operador | Significa | Exemple |
| -------- | --------- | ------- |
| `and` | les dues | `edat >= 18 and edat < 65` |
| `or` | almenys una | `dia == "dissabte" or dia == "diumenge"` |
| `not` | el contrari | `not actiu` |

Python també permet escriure `18 <= edat < 65`, com en matemàtiques.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `"5" * 2` dona `"55"` | Era text, no número | `int(input(...))` |
| `TypeError: can only concatenate str (not "int")` | Unes text i número amb `+` | Usa una f-string: `f"Tens {edat} anys"` |
| `ValueError: invalid literal for int()` | Has convertit un text que no és número | Comprova què escriu l'usuari |
| `if x = 5:` dona `SyntaxError` | Per a comparar és `==` | `if x == 5:` |
| `true` no funciona | Va amb majúscula | `True` / `False` |

!!! success "Per a l'examen"
    - Guardar: `var = valor` (espais permesos, sense `$`)
    - Tipus: `int` (enter), `float` (decimal, amb **punt**), `str` (text), `bool` (`True`/`False`)
    - `input()` torna **sempre text** → `int(input(...))` per a números
    - Mostrar: `print(f"Text {variable}")`
    - `/` divisió normal · `//` divisió entera · `%` residu · `**` potència
    - `=` guarda · `==` compara
    - `and`, `or`, `not`
