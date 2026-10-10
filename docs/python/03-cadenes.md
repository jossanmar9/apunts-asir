# 3. Cadenes

Una **cadena** (`str`, de *string*) és un text. Es pot escriure amb cometes simples o dobles, és igual:

```python
nom = "Ana"
cognom = 'Puig'
frase = "L'apòstrof no molesta si uses cometes dobles"
```

Per a textos de diverses línies, tres cometes:

```python
missatge = """Primera línia
Segona línia"""
```

### Caràcters especials

| S'escriu | Significa |
| -------- | --------- |
| `\n` | salt de línia |
| `\t` | tabulador |
| `\\` | una barra `\` |
| `\"` | unes cometes dins del text |

```python
print("Línia 1\nLínia 2")
```

## Unir i repetir

```python
"Hola" + " " + "món"      # "Hola món"     → unir (concatenar)
"-" * 20                  # "--------------------" → repetir
```

## Llargària: `len`

```python
len("Python")       # 6 → quantes lletres té
```

## Accedir a les lletres: índexs

Cada lletra té una posició, **començant per 0**. També es pot comptar des del final amb números negatius:

```
 P  y  t  h  o  n
 0  1  2  3  4  5      ← des del principi
-6 -5 -4 -3 -2 -1      ← des del final
```

```python
s = "Python"
s[0]       # 'P'  → la primera
s[1]       # 'y'  → la segona
s[-1]      # 'n'  → l'última
s[-2]      # 'o'  → la penúltima
```

## Traure un tros: slicing

Amb `[inici:final]` agafes un tros. **El final no s'inclou**.

```python
s = "Python"
s[0:4]     # 'Pyth' → posicions 0, 1, 2 i 3 (la 4 NO)
s[2:]      # 'thon' → des de la 2 fins al final
s[:2]      # 'Py'   → des del principi fins a la 2 (sense incloure-la)
s[::-1]    # 'nohtyP' → tot al revés
```

!!! tip "Com recordar-ho"
    `s[:3]` són **els 3 primers**. `s[3:]` és **tot menys els 3 primers**.

!!! note "Les cadenes no es poden modificar"
    `s[0] = "J"` dona error. Per a "canviar" una cadena, cal crear-ne una de nova: `s = "J" + s[1:]`.

## Comprovar si conté alguna cosa: `in`

```python
"err" in "error de disc"      # True
"ssh" in "nginx"              # False
```

## Recórrer lletra a lletra

```python
for lletra in "hola":
    print(lletra)
```

## Mètodes: funcions de les cadenes

Les cadenes porten funcions incloses. S'usen amb un punt: `text.metode()`.

| Mètode | Què fa | Exemple | Resultat |
| ------ | ------ | ------- | -------- |
| `.upper()` | a majúscules | `"hola".upper()` | `'HOLA'` |
| `.lower()` | a minúscules | `"HOLA".lower()` | `'hola'` |
| `.title()` | primera lletra de cada paraula en majúscula | `"maria josep".title()` | `'Maria Josep'` |
| `.strip()` | lleva espais i salts de línia del principi i del final | `"  hola \n".strip()` | `'hola'` |
| `.replace(a, b)` | canvia `a` per `b` | `"1.000".replace(".", "")` | `'1000'` |
| `.split()` | talla en paraules → llista | `"a b c".split()` | `['a', 'b', 'c']` |
| `.split(":")` | talla pel caràcter indicat | `"a:b:c".split(":")` | `['a', 'b', 'c']` |
| `"-".join(llista)` | uneix una llista amb el separador | `"-".join(["a", "b"])` | `'a-b'` |
| `.startswith(x)` | comença per x? | `"hola".startswith("ho")` | `True` |
| `.endswith(x)` | acaba en x? | `"f.log".endswith(".log")` | `True` |
| `.count(x)` | quantes vegades apareix x | `"banana".count("a")` | `3` |
| `.find(x)` | posició de x (−1 si no hi és) | `"hola".find("l")` | `2` |
| `.isdigit()` | són tot dígits? | `"123".isdigit()` | `True` |

!!! warning "Els mètodes no canvien la variable"
    ```python
    nom = "  ana  "
    nom.strip()          # torna "ana" però nom continua sent "  ana  "
    nom = nom.strip()    # ✅ guarda el resultat
    ```

### `split` i `join`: els més útils per a fitxers

`split` talla un text en trossos. Imprescindible per a llegir fitxers amb camps separats:

```python
linia = "ana:x:1000:1000:Ana Puig:/home/ana:/bin/bash"
camps = linia.split(":")
# camps = ['ana', 'x', '1000', '1000', 'Ana Puig', '/home/ana', '/bin/bash']

usuari = camps[0]          # 'ana'
uid = int(camps[2])        # 1000 (convertit a número)
shell = camps[-1]          # '/bin/bash' (l'últim)
print(f"{usuari} té l'UID {uid} i usa {shell}")
```

`join` fa el contrari: uneix una llista en un text.

```python
serveis = ["ssh", "nginx", "cron"]
print(", ".join(serveis))     # ssh, nginx, cron
```

## f-strings: posar variables dins del text

Una **f-string** és una cadena amb una `f` davant. Dins, el que posis entre `{ }` es canvia pel seu valor:

```python
nom = "Pep"
nota = 7.456
print(f"{nom} ha tret un {nota}")       # Pep ha tret un 7.456
print(f"El doble és {nota * 2}")        # es poden fer operacions dins
```

### Donar format als números i alinear

Després del nom, amb `:` pots indicar el format:

```python
nota = 7.456
f"{nota:.2f}"       # '7.46'     → 2 decimals
f"{nota:.0f}"       # '7'        → sense decimals
f"{0.256:.1%}"      # '25.6%'    → com a percentatge
f"{42:05d}"         # '00042'    → amb zeros davant fins a 5 xifres
```

Per a fer **taules alineades**:

```python
f"{'Pep':<10}|"     # 'Pep       |'  → alinea a l'esquerra en 10 espais
f"{'Pep':>10}|"     # '       Pep|'  → a la dreta
f"{'Pep':^10}|"     # '   Pep    |'  → centrat
```

```python
for usuari, uid in [("root", 0), ("ana", 1000), ("www-data", 33)]:
    print(f"{usuari:<12}{uid:>6}")
```

```console
root             0
ana           1000
www-data        33
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `IndexError: string index out of range` | Has demanat una posició que no existix | Recorda que va de 0 a `len(s) - 1` |
| `TypeError: 'str' object does not support item assignment` | Has intentat canviar una lletra | Crea una cadena nova |
| `.strip()` "no fa res" | No has guardat el resultat | `s = s.strip()` |
| `f"..."` mostra `{nom}` literal | T'has oblidat la `f` | `f"Hola {nom}"` |

!!! success "Per a l'examen"
    ```python
    len(s)              # llargària
    s[0], s[-1]         # primera, última
    s[:3], s[3:]        # 3 primers, la resta
    s[::-1]             # al revés
    "x" in s            # conté?
    s.upper() s.lower() s.strip() s.replace(a, b)
    s.split(":")        # text → llista
    ", ".join(llista)   # llista → text
    f"{var:.2f}"        # 2 decimals
    f"{var:<10}"        # alinear
    ```

    - Posicions **des de 0** · el final del slicing **no s'inclou**
    - Els mètodes **no canvien** la variable: `s = s.strip()`
