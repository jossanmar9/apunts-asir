# 8. Excepcions

Quan alguna cosa va malament, Python llança una **excepció**. Si ningú la captura, el programa s'atura i mostra el *traceback*. Llig-lo **de baix a dalt**: l'última línia diu quin error és i on.

```console
Traceback (most recent call last):
  File "calc.py", line 2, in <module>
    n = int(input("Número: "))
ValueError: invalid literal for int() with base 10: 'hola'
```

## `try` / `except`

```python
try:
    n = int(input("Número: "))
    print(100 / n)
except ValueError:
    print("No és un número")
except ZeroDivisionError:
    print("No es pot dividir per zero")
```

```python
try:
    ...
except (ValueError, TypeError) as e:     # diversos tipus, i el missatge en e
    print(f"Error: {e}")
else:
    print("Ha anat bé")                  # només si NO hi ha hagut excepció
finally:
    print("Açò s'executa sempre")        # tancar connexions, netejar...
```

## Les més habituals

| Excepció | Quan |
| -------- | ---- |
| `ValueError` | valor incorrecte: `int("abc")` |
| `TypeError` | tipus incorrecte: `"a" + 1` |
| `KeyError` | clau inexistent en un diccionari |
| `IndexError` | posició fora d'una llista |
| `ZeroDivisionError` | dividir per zero |
| `FileNotFoundError` | el fitxer no existix |
| `PermissionError` | sense permisos |
| `KeyboardInterrupt` | l'usuari ha premut ++ctrl+c++ |

## Patró: demanar fins que siga vàlid

```python
def demana_enter(missatge, minim=None, maxim=None):
    while True:
        try:
            n = int(input(missatge))
        except ValueError:
            print("Escriu un número enter")
            continue
        if (minim is not None and n < minim) or (maxim is not None and n > maxim):
            print(f"Ha d'estar entre {minim} i {maxim}")
            continue
        return n

port = demana_enter("Port: ", 1, 65535)
```

## Patró: fitxers que poden no existir

```python
import sys

try:
    with open(sys.argv[1]) as f:
        dades = f.read()
except IndexError:
    sys.exit(f"Ús: {sys.argv[0]} <fitxer>")
except FileNotFoundError:
    sys.exit(f"No existix: {sys.argv[1]}")
except PermissionError:
    sys.exit(f"Sense permís per a llegir {sys.argv[1]}")
```

`sys.exit("missatge")` escriu el missatge a stderr i ix amb codi 1.

## Llançar les teues excepcions

```python
def configura_port(port):
    if not 1 <= port <= 65535:
        raise ValueError(f"Port fora de rang: {port}")
    ...
```

!!! warning "No captures-ho tot a cegues"
    `except:` o `except Exception:` sense fer res amaga errors de veritat (fins i tot de lletra). Captura només el que esperes i saps tractar.
