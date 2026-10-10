# 3. Cadenes

## Crear-les

```python
s1 = 'cometes simples'
s2 = "cometes dobles: l'apòstrof no molesta"
s3 = """diverses
línies"""
ruta = r"C:\Users\nou"     # raw: les \ no s'interpreten
```

Seqüències d'escapament: `\n` (salt de línia), `\t` (tabulador), `\\` (barra), `\"`.

## Índexs i slicing

```
 p  y  t  h  o  n
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
```

```python
s = "python"
s[0]       # 'p'
s[-1]      # 'n'  (l'últim)
s[0:4]     # 'pyth'  (del 0 al 3: el final NO s'inclou)
s[4:]      # 'on'    (des del 4 fins al final)
s[:4]      # 'pyth'
s[::2]     # 'pto'   (de 2 en 2)
s[::-1]    # 'nohtyp' (al revés)
len(s)     # 6
```

Les cadenes són **inmutables**: `s[0] = "J"` dona error. Cal crear-ne una de nova: `s = "J" + s[1:]`.

## Operacions

```python
"ab" + "cd"        # 'abcd'
"-" * 20           # '--------------------'
"err" in "error"   # True
for c in "hola":   # recórrer lletra a lletra
    print(c)
```

## Mètodes més útils

| Mètode | Exemple | Resultat |
| ------ | ------- | -------- |
| `upper()` / `lower()` | `"Hola".upper()` | `'HOLA'` |
| `capitalize()` / `title()` | `"maria josep".title()` | `'Maria Josep'` |
| `strip()` | `"  hola\n".strip()` | `'hola'` |
| `split(sep)` | `"a:b:c".split(":")` | `['a', 'b', 'c']` |
| `split()` | `"a  b   c".split()` | `['a', 'b', 'c']` (qualsevol espai) |
| `sep.join(llista)` | `", ".join(["a", "b"])` | `'a, b'` |
| `replace(a, b)` | `"1.000".replace(".", "")` | `'1000'` |
| `startswith()` / `endswith()` | `f.endswith(".log")` | `True`/`False` |
| `find(x)` | `"hola".find("l")` | `2` (−1 si no hi és) |
| `count(x)` | `"banana".count("a")` | `3` |
| `isdigit()` | `"123".isdigit()` | `True` |
| `isalpha()` / `isalnum()` | `"abc1".isalnum()` | `True` |
| `zfill(n)` | `"7".zfill(3)` | `'007'` |
| `center(n, c)` | `"TÍTOL".center(20, "=")` | `'=======TÍTOL========'` |

Els mètodes no modifiquen la cadena, en tornen una de nova: `s = s.strip()`.

### Exemple: processar una línia de `/etc/passwd`

```python
linia = "ana:x:1000:1000:Ana Puig:/home/ana:/bin/bash"
camps = linia.split(":")
usuari, uid, shell = camps[0], int(camps[2]), camps[-1]
print(f"{usuari} ({uid}) usa {shell}")
```

## f-strings: el format modern

```python
nom, nota, preu = "Pep", 7.456, 1234.5

f"{nom} ha tret {nota}"         # 'Pep ha tret 7.456'
f"{nota:.2f}"                   # '7.46'    → 2 decimals
f"{preu:,.2f}"                  # '1,234.50' → separador de milers
f"{nom:<10}|"                   # 'Pep       |' → alinea a l'esquerra en 10
f"{nom:>10}|"                   # '       Pep|' → a la dreta
f"{nom:^10}|"                   # '   Pep    |' → centrat
f"{42:05d}"                     # '00042'
f"{0.256:.1%}"                  # '25.6%'
f"{2 + 3 = }"                   # '2 + 3 = 5' → útil per a depurar
```

Taula alineada:

```python
for usuari, uid in [("root", 0), ("ana", 1000), ("www-data", 33)]:
    print(f"{usuari:<12}{uid:>6}")
```

## Unicode

```python
ord("A")      # 65
chr(65)       # 'A'
len("cafè")   # 4 (compta caràcters, no bytes)
"cafè".encode()          # b'caf\xc3\xa8' (bytes UTF-8)
b"caf\xc3\xa8".decode()  # 'cafè'
```
