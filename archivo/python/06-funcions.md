# 6. Funcions i mòduls

## Què és una funció

Una **funció** és un tros de codi amb nom que fa una tasca concreta. La crees una vegada i la uses (la **crides**) quantes vegades vulgues.

Ja n'has usat moltes: `print()`, `input()`, `len()`... Ara aprendràs a crear les teues.

**Per què?**

- Per a **no repetir codi**.
- Per a **dividir** un problema gran en trossos menuts i clars.

## Crear-la i cridar-la

```python
def saluda():                 # def = "definir una funció"
    print("Hola!")
    print("Benvingut")

saluda()                      # cridar-la
saluda()                      # i una altra vegada
```

- `def` + nom + `()` + `:`
- El codi de dins amb 4 espais.
- Per a cridar-la: el nom **amb parèntesis**.

## Paràmetres: passar-li dades

```python
def saluda(nom):              # nom és un PARÀMETRE: una variable que rep la dada
    print(f"Hola, {nom}!")

saluda("Ana")                 # Hola, Ana!
saluda("Pep")                 # Hola, Pep!
```

Poden ser diversos:

```python
def area_rectangle(base, altura):
    print(base * altura)

area_rectangle(3, 4)          # 12
```

## `return`: tornar un resultat

Fins ara les funcions mostraven el resultat amb `print`. Però normalment volem que **tornen** el resultat per a poder usar-lo després. Per a això està `return`:

```python
def area_rectangle(base, altura):
    return base * altura      # torna el resultat a qui l'ha cridada

a = area_rectangle(3, 4)      # a = 12
print(f"L'àrea és {a}")
total = area_rectangle(3, 4) + area_rectangle(2, 5)   # 12 + 10 = 22
```

### `print` o `return`?

| | `print` | `return` |
| - | ------- | -------- |
| Què fa | **mostra** el valor per pantalla | **torna** el valor perquè el pugues usar |
| Puc guardar el resultat? | No | Sí: `x = funcio()` |
| Quan usar-lo | per a mostrar missatges | per a calcular coses |

!!! warning "`return` acaba la funció"
    El que hi haja després d'un `return` no s'executa.

Si una funció no té `return`, torna `None` (res).

### Tornar diversos valors

```python
def estadistiques(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

minim, maxim, mitjana = estadistiques([4, 8, 15])
```

## Valors per defecte

```python
def connecta(host, port=22, usuari="root"):
    print(f"ssh {usuari}@{host} -p {port}")

connecta("10.0.0.1")                      # usa port=22 i usuari=root
connecta("10.0.0.1", 2222)                # canvia el port
connecta("10.0.0.1", usuari="ana")        # canvia només l'usuari (pel nom)
```

Els paràmetres amb valor per defecte van **sempre després** dels que no en tenen.

## Les variables de dins són locals

Una variable creada **dins** d'una funció només existix dins:

```python
def calcula():
    resultat = 42

calcula()
print(resultat)     # ❌ NameError: fora no existix
```

Per a traure un valor de la funció, usa `return`:

```python
def calcula():
    resultat = 42
    return resultat

r = calcula()
print(r)            # 42 ✅
```

## Documentar la funció

La primera línia entre `"""` explica què fa. Es pot veure amb `help(funcio)`:

```python
def es_parell(n):
    """Torna True si n és parell."""
    return n % 2 == 0
```

## Funcions recursives

Una funció **recursiva** es crida a si mateixa. Ha de tindre un **cas base** que pare, o no acabaria mai:

```python
def factorial(n):
    if n <= 1:                     # cas base: ací para
        return 1
    return n * factorial(n - 1)    # es crida amb un número més menut

factorial(4)    # 4 * 3 * 2 * 1 = 24
```

## Funcions `lambda`

Una funció curta, sense nom, d'una sola línia. S'usa sobretot per a ordenar:

```python
usuaris = [("pep", 1001), ("ana", 1000), ("root", 0)]
ordenats = sorted(usuaris, key=lambda u: u[1])     # ordena pel segon element (UID)
```

`lambda u: u[1]` vol dir "*una funció que rep `u` i torna `u[1]`*".

## Mòduls: usar codi ja fet

Un **mòdul** és un fitxer amb funcions que pots usar. Python en porta molts inclosos. Per a usar-los, cal **importar-los**:

```python
import math                   # importa tot el mòdul
print(math.sqrt(16))          # 4.0 → s'usa amb mòdul.funció

from math import sqrt         # importa només una funció
print(sqrt(16))               # 4.0 → s'usa directament

import datetime as dt         # importa amb un nom més curt
print(dt.date.today())
```

### Mòduls més útils

| Mòdul | Per a què |
| ----- | --------- |
| `math` | funcions matemàtiques |
| `random` | números a l'atzar |
| `os`, `sys` | coses del sistema |
| `pathlib` | treballar amb rutes i fitxers |
| `shutil` | copiar, moure, esborrar fitxers |
| `subprocess` | executar ordres del sistema |
| `datetime` | dates i hores |
| `json`, `csv` | llegir i escriure eixos formats |

```python
import random
random.randint(1, 100)              # número a l'atzar entre 1 i 100
random.choice(["roig", "verd"])     # un element a l'atzar
```

### Crear els teus propis mòduls

Qualsevol fitxer `.py` és un mòdul. Si tens `utils.py`:

```python title="utils.py"
def es_parell(n):
    return n % 2 == 0
```

el pots usar des d'un altre fitxer de la mateixa carpeta:

```python
from utils import es_parell
print(es_parell(4))     # True
```

### `if __name__ == "__main__":`

Veuràs molt esta línia al final dels programes:

```python
def main():
    print("Programa principal")

if __name__ == "__main__":
    main()
```

Vol dir: "*executa `main()` només si estic executant este fitxer directament*". Si un altre fitxer l'importa, `main()` no s'executa. Així un fitxer pot ser programa i mòdul alhora.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `NameError` en cridar la funció | La crides abans de definir-la | Posa el `def` abans |
| La funció torna `None` | Falta el `return` (o has usat `print`) | Afig `return valor` |
| `TypeError: missing 1 required positional argument` | No li has passat totes les dades | Revisa els paràmetres |
| `NameError` amb una variable de la funció | Les variables de dins són locals | Usa `return` |
| `ModuleNotFoundError` | El mòdul no està instal·lat o el nom és incorrecte | `pip install` dins d'un `venv` |

!!! success "Per a l'examen"
    ```python
    def nom(param1, param2=valor_defecte):
        """Què fa."""
        ...
        return resultat

    x = nom(1)               # cridar-la i guardar el resultat
    a, b = funcio()          # si torna diversos valors

    import modul             # modul.funcio()
    from modul import funcio # funcio()
    ```

    - `return` **torna** el valor · `print` només el **mostra**
    - Les variables de dins **no existixen fora**
