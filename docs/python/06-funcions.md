# 6. Funcions i mòduls

## Definir una funció

```python
def area_rectangle(base, altura):
    """Torna l'àrea d'un rectangle."""
    return base * altura

print(area_rectangle(3, 4))   # 12
```

- `return` torna el valor i acaba la funció. Sense `return`, torna `None`.
- La primera línia entre `"""` és la documentació: la veus amb `help(area_rectangle)`.

### Tornar diversos valors

```python
def estadistiques(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

minim, maxim, mitjana = estadistiques([4, 8, 15])
```

## Paràmetres

```python
def connecta(host, port=22, usuari="root"):     # valors per defecte
    print(f"ssh {usuari}@{host} -p {port}")

connecta("10.0.0.1")                     # port=22, usuari=root
connecta("10.0.0.1", 2222)               # per posició
connecta("10.0.0.1", usuari="ana")       # per nom
```

Els paràmetres amb valor per defecte van sempre després dels obligatoris.

### Nombre variable d'arguments

```python
def suma(*nums):            # nums és una tupla
    return sum(nums)
suma(1, 2, 3, 4)            # 10

def mostra(**opcions):      # opcions és un diccionari
    for k, v in opcions.items():
        print(f"{k} = {v}")
mostra(port=80, ssl=True)
```

!!! danger "No uses una llista com a valor per defecte"
    ```python
    def afig(x, llista=[]):     # ❌ la llista es comparteix entre crides
        llista.append(x)
        return llista

    afig(1)    # [1]
    afig(2)    # [1, 2]  😱 recorda la crida anterior

    def afig(x, llista=None):   # ✅
        if llista is None:
            llista = []
        llista.append(x)
        return llista
    ```

## Àmbit de les variables

Les variables creades dins d'una funció són **locals**: no existixen fora.

```python
total = 0
def suma_u():
    total = total + 1    # ❌ UnboundLocalError
```

Pots **llegir** variables globals, però per a modificar-les cal `global total`. Millor: passa-les com a paràmetre i torna el resultat.

## Funcions lambda

Funcions anònimes d'una línia, sobretot per a `sorted`, `max`, `filter`:

```python
usuaris = [("pep", 1001), ("ana", 1000), ("root", 0)]
sorted(usuaris, key=lambda u: u[1])        # ordenar per UID
max(usuaris, key=lambda u: u[1])           # ('pep', 1001)
```

## Indicacions de tipus (opcional)

```python
def es_port_valid(port: int) -> bool:
    return 1 <= port <= 65535
```

No canvien el funcionament, però ajuden a llegir el codi i l'editor t'avisa d'errors.

## Funcions recursives

Una funció que es crida a si mateixa. Necessita un **cas base** que pare:

```python
def factorial(n):
    if n <= 1:          # cas base
        return 1
    return n * factorial(n - 1)
```

## Mòduls

Un mòdul és un fitxer `.py`. Per a usar el que hi ha dins:

```python
import math
math.sqrt(16)

from math import sqrt, pi
sqrt(16)

import datetime as dt
dt.date.today()
```

### Els teus propis mòduls

```python title="utils.py"
def es_ip_valida(ip):
    parts = ip.split(".")
    return len(parts) == 4 and all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)
```

```python title="main.py"
from utils import es_ip_valida
print(es_ip_valida("192.168.1.300"))   # False
```

### `if __name__ == "__main__":`

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

El codi de dins només s'executa si llances el fitxer directament (`python3 utils.py`), **no** quan un altre fitxer el importa. Així un mateix fitxer pot ser script i mòdul alhora.

### Mòduls de la biblioteca estàndard que més usaràs

| Mòdul | Per a què |
| ----- | --------- |
| `os`, `sys` | sistema, variables d'entorn, arguments |
| `pathlib`, `glob`, `shutil` | rutes, buscar fitxers, copiar/moure |
| `subprocess` | executar ordres del sistema |
| `datetime`, `time` | dates i esperes |
| `json`, `csv` | formats de dades |
| `re` | expressions regulars |
| `argparse` | opcions de línia d'ordres |
| `logging` | registres |
| `random` | números aleatoris |
| `collections` | `Counter`, `defaultdict` |

Vegeu els temes [7](07-fitxers.md) i [9](09-sysadmin.md).
