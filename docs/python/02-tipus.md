# 2. Tipus i variables

## Variables

```python
nom = "Ana"         # str
edat = 30           # int
alcada = 1.78       # float
actiu = True        # bool
res = None          # "no hi ha valor"
```

No es declara el tipus: la variable agafa el del valor. `type(x)` et diu quin és.

```python
a, b = 1, 2          # assignació múltiple
a, b = b, a          # intercanviar valors
x = y = 0            # el mateix valor a diverses
```

## Números

| Operador | Exemple | Resultat |
| -------- | ------- | -------- |
| `+ - *` | `7 * 3` | `21` |
| `/` | `7 / 2` | `3.5` (sempre float) |
| `//` | `7 // 2` | `3` (divisió entera) |
| `%` | `7 % 2` | `1` (residu) |
| `**` | `2 ** 10` | `1024` (potència) |

```python
x = 10
x += 5        # x = 15  (també -=, *=, /=, //=)
abs(-4)       # 4
round(3.14159, 2)   # 3.14
max(3, 8, 1)  # 8
min(3, 8, 1)  # 1
divmod(17, 5) # (3, 2) → quocient i residu alhora
```

Els enters no tenen límit de mida (`2 ** 1000` funciona). Els float tenen errors de precisió:

```python
0.1 + 0.2            # 0.30000000000000004
round(0.1 + 0.2, 2)  # 0.3
```

Per a arrels i altres funcions matemàtiques: `import math` → `math.sqrt(16)`, `math.pi`, `math.ceil(2.1)`.

### Bases (útil per a xarxes)

```python
bin(192)           # '0b11000000'
hex(255)           # '0xff'
int("11000000", 2) # 192
int("ff", 16)      # 255
f"{10:08b}"        # '00001010' → 8 bits amb zeros
```

## Booleans i comparacions

```python
5 > 3          # True
5 == 5.0       # True
"a" != "b"     # True
1 <= x <= 10   # es poden encadenar
```

Operadors lògics: `and`, `or`, `not`.

Es consideren **falsos**: `False`, `0`, `0.0`, `""`, `[]`, `{}`, `None`. Tot la resta és cert.

```python
nom = input("Nom: ")
if not nom:
    print("No has escrit res")
```

## Entrada i eixida

```python
nom = input("Nom: ")          # sempre torna un str!
edat = int(input("Edat: "))   # cal convertir per a operar
preu = float(input("Preu: "))

print("Hola", nom)                    # separa amb espai
print("a", "b", "c", sep="-")         # a-b-c
print("sense salt", end="")           # no baixa de línia
print(f"{nom} té {edat} anys")        # f-string (vegeu cadenes)
```

!!! danger "L'error clàssic"
    ```python
    n = input("Número: ")
    print(n * 2)        # si escrius 5, mostra 55 (repetix el text)
    print(int(n) * 2)   # 10
    ```

## Conversions

| Funció | Exemple | Resultat |
| ------ | ------- | -------- |
| `int()` | `int("42")`, `int(3.9)` | `42`, `3` (trunca) |
| `float()` | `float("3.5")` | `3.5` |
| `str()` | `str(42)` | `'42'` |
| `bool()` | `bool("")`, `bool("no")` | `False`, `True` |

Si el text no és un número, `int("hola")` llança `ValueError` (vegeu [excepcions](08-excepcions.md)).

## Mutabilitat

- **Inmutables**: `int`, `float`, `bool`, `str`, `tuple`. "Modificar-los" crea un objecte nou.
- **Mutables**: `list`, `dict`, `set`. Es poden canviar per dins, i això té conseqüències quan dues variables apunten al mateix objecte (vegeu [estructures](05-estructures.md#compte-amb-les-copies)).
