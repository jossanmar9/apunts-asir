# 8. Excepcions

## Què és una excepció

Quan alguna cosa va malament mentre el programa s'executa (dividir per zero, obrir un fitxer que no existix, convertir "hola" a número...), Python **llança una excepció**: para el programa i mostra un missatge d'error.

```python
n = int(input("Número: "))      # l'usuari escriu: hola
```

```console
Traceback (most recent call last):
  File "prova.py", line 1, in <module>
    n = int(input("Número: "))
ValueError: invalid literal for int() with base 10: 'hola'
```

### Com llegir el missatge d'error

Llig-lo **de baix a dalt**:

1. **L'última línia** diu el **tipus d'error** (`ValueError`) i què ha passat.
2. Una mica més amunt diu **en quin fitxer i línia** (`line 1`).

Amb això ja saps on mirar.

## Controlar els errors: `try` / `except`

En compte de deixar que el programa pete, pots **preveure** l'error i decidir què fer:

```python
try:
    n = int(input("Número: "))      # prova a fer açò...
    print(f"El doble és {n * 2}")
except ValueError:                  # ...i si dona ValueError, fes açò altre
    print("Això no és un número")
```

**Com funciona:**

1. Python intenta executar el bloc `try`.
2. Si tot va bé, se salta l'`except`.
3. Si hi ha un error del tipus indicat, para el `try` i executa l'`except`. El programa **no peta**.

### Diversos errors possibles

```python
try:
    a = int(input("Número: "))
    b = int(input("Divisor: "))
    print(a / b)
except ValueError:
    print("Has d'escriure números")
except ZeroDivisionError:
    print("No es pot dividir per zero")
```

### Veure el missatge de l'error

```python
try:
    ...
except ValueError as e:
    print(f"Error: {e}")
```

### `else` i `finally` (opcionals)

```python
try:
    n = int(input("Número: "))
except ValueError:
    print("No és un número")
else:
    print("Perfecte")                # només si NO hi ha hagut error
finally:
    print("Açò s'executa sempre")    # haja error o no
```

## Els errors més habituals

| Error | Quan passa | Exemple |
| ----- | ---------- | ------- |
| `ValueError` | el valor no és vàlid | `int("hola")` |
| `TypeError` | operació entre tipus incompatibles | `"a" + 1` |
| `ZeroDivisionError` | dividir per zero | `5 / 0` |
| `IndexError` | posició que no existix en una llista | `[1, 2][5]` |
| `KeyError` | clau que no existix en un diccionari | `{"a": 1}["b"]` |
| `FileNotFoundError` | el fitxer no existix | `open("no.txt")` |
| `PermissionError` | no tens permís | `open("/etc/shadow")` |
| `NameError` | variable que no existix (o mal escrita) | `print(nmo)` |

## Patró: preguntar fins que siga vàlid

Combinant `while True` amb `try`:

```python
while True:
    try:
        edat = int(input("Edat: "))
        break                         # si arriba ací, és vàlid: ix del bucle
    except ValueError:
        print("Escriu un número, per favor")

print(f"Tens {edat} anys")
```

## Patró: fitxers que poden no existir

```python
nom = input("Quin fitxer vols llegir? ")
try:
    with open(nom) as f:
        print(f.read())
except FileNotFoundError:
    print(f"No existix el fitxer {nom}")
except PermissionError:
    print(f"No tens permís per a llegir {nom}")
```

## Llançar els teus propis errors: `raise`

Si detectes una situació incorrecta, pots llançar tu un error:

```python
def posa_edat(edat):
    if edat < 0:
        raise ValueError("L'edat no pot ser negativa")
    ...
```

## Acabar el programa amb un error: `sys.exit`

```python
import sys

if not fitxer_existix:
    sys.exit("Error: no trobe el fitxer")    # mostra el missatge i acaba
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| L'`except` no captura l'error | Has posat un tipus diferent | Mira l'última línia del missatge i usa eixe tipus |
| `except:` sense tipus amaga errors reals | Captura **tot**, fins i tot errors de lletra | Indica sempre el tipus: `except ValueError:` |
| El programa continua amb una variable buida | Després de l'`except` no has parat ni tornat a preguntar | Usa un bucle o `sys.exit()` |

!!! success "Per a l'examen"
    ```python
    try:
        ...                        # el que pot fallar
    except ValueError:             # int("hola")
        ...
    except FileNotFoundError:      # fitxer que no existix
        ...

    while True:                    # preguntar fins que siga vàlid
        try:
            n = int(input("> "))
            break
        except ValueError:
            print("No és un número")
    ```

    - Missatge d'error: **llig l'última línia** (tipus) i la línia del codi
    - Indica **sempre** el tipus d'error en l'`except`
