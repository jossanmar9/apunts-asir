# 7. Fitxers, pathlib i glob

## Obrir un fitxer: `open` amb `with`

Per a treballar amb un fitxer cal **obrir-lo**, fer el que siga i **tancar-lo**. La manera correcta en Python és amb `with`, que el tanca sol en acabar:

```python
with open("notes.txt") as f:      # obri el fitxer i el guarda en la variable f
    contingut = f.read()          # llig tot el contingut
print(contingut)                  # ací el fitxer ja està tancat
```

### Modes d'obertura

El segon paràmetre d'`open` diu què vols fer:

| Mode | Per a | Si el fitxer existix | Si no existix |
| ---- | ----- | -------------------- | ------------- |
| `"r"` | **llegir** (per defecte) | el llig | error |
| `"w"` | **escriure** | ⚠️ **l'esborra** i comença de zero | el crea |
| `"a"` | **afegir** al final | escriu al final | el crea |

```python
open("f.txt")          # llegir
open("f.txt", "w")     # escriure (esborra el que hi havia!)
open("f.txt", "a")     # afegir al final
```

!!! tip "Accents"
    Si el fitxer té accents o caràcters especials, afig `encoding="utf-8"`: `open("f.txt", encoding="utf-8")`.

## Llegir

Tres maneres:

```python
with open("noms.txt") as f:
    tot = f.read()             # 1. tot el fitxer en un sol text

with open("noms.txt") as f:
    linies = f.readlines()     # 2. una llista amb una línia per element

with open("noms.txt") as f:
    for linia in f:            # 3. ⭐ línia a línia (la millor per a fitxers grans)
        print(linia.strip())
```

!!! note "Per què `.strip()`?"
    Cada línia porta al final un salt de línia (`\n`) invisible. Si no el lleves, `print` en posaria dos i es veurien línies en blanc. `.strip()` el lleva.

### Exemple: llegir `/etc/passwd`

```python
with open("/etc/passwd") as f:
    for linia in f:
        camps = linia.strip().split(":")    # talla per :
        usuari = camps[0]
        uid = int(camps[2])
        if uid >= 1000:
            print(usuari)
```

## Escriure

```python
with open("informe.txt", "w") as f:
    f.write("Informe del servidor\n")       # \n per a baixar de línia
    f.write("Tot correcte\n")
```

`write` **no** posa el salt de línia sol: cal afegir `\n`.

Alternativa: `print` també pot escriure en un fitxer:

```python
with open("informe.txt", "a") as f:
    print("Una línia més", file=f)          # print sí que posa el salt de línia
```

## Fitxers CSV

Un **CSV** és un fitxer de text amb dades en columnes separades per comes (com una fulla de càlcul). Exemple `usuaris.csv`:

```text
nom,grup,uid
ana,asir,1000
pep,smx,1001
```

Llegir-lo:

```python
import csv

with open("usuaris.csv") as f:
    for fila in csv.DictReader(f):         # cada fila és un diccionari
        print(fila["nom"], fila["grup"])   # accedixes per nom de columna
```

Escriure'l:

```python
with open("eixida.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nom", "uid"])             # capçalera
    w.writerow(["ana", 1000])              # dades
```

Si el separador és `;` en compte de `,`: `csv.DictReader(f, delimiter=";")`.

## Fitxers JSON

**JSON** és un format molt usat per a configuracions i APIs. S'assembla molt als diccionaris i llistes de Python:

```json
{
  "servidor": "web01",
  "port": 80,
  "serveis": ["nginx", "php"]
}
```

```python
import json

with open("config.json") as f:
    config = json.load(f)                  # JSON → diccionari de Python
print(config["port"])                      # 80

config["port"] = 8080                      # canviar un valor
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)         # diccionari → JSON (indent: amb format bonic)
```

## `pathlib`: treballar amb rutes

`pathlib` permet manejar rutes de fitxers de forma còmoda:

```python
from pathlib import Path

p = Path("/var/log/nginx/access.log")
p.name          # 'access.log'       → nom del fitxer
p.stem          # 'access'           → nom sense extensió
p.suffix        # '.log'             → extensió
p.parent        # /var/log/nginx     → la carpeta on està
p.exists()      # True o False       → existix?
p.is_file()     # és un fitxer?
p.is_dir()      # és una carpeta?
```

### Construir rutes

```python
Path.home()                         # la teua carpeta personal: /home/ana
carpeta = Path.home() / "backup"    # / uneix trossos de ruta → /home/ana/backup
carpeta.mkdir(exist_ok=True)        # crear la carpeta (sense error si ja existix)
```

### Llegir i escriure d'una vegada

```python
text = Path("notes.txt").read_text()
Path("eixida.txt").write_text("hola\n")
```

### Llistar i buscar fitxers

```python
carpeta = Path("/etc")

for f in carpeta.iterdir():         # tot el que hi ha dins
    print(f.name)

for f in carpeta.glob("*.conf"):    # només els .conf
    print(f)

for f in carpeta.rglob("*.conf"):   # els .conf de dins i de totes les subcarpetes
    print(f)
```

## `glob`: buscar fitxers per patró

El mòdul `glob` fa el mateix que `Path.glob` però torna textos:

```python
import glob

glob.glob("/var/log/*.log")                         # els .log de /var/log
glob.glob("/var/log/**/*.log", recursive=True)      # també en subcarpetes
```

| Patró | Significa |
| ----- | --------- |
| `*` | qualsevol cosa |
| `?` | un sol caràcter |
| `**` | qualsevol nombre de subcarpetes |
| `[0-9]` | un dígit |

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `FileNotFoundError` | El fitxer no existix o la ruta està mal | Comprova la ruta amb `Path(...).exists()` |
| `PermissionError` | No tens permís | Executa amb `sudo` o canvia de fitxer |
| He perdut el contingut del fitxer | L'has obert amb `"w"` | Usa `"a"` per a afegir |
| Les línies ixen amb línies en blanc enmig | Les línies porten `\n` | `linia.strip()` |
| `UnicodeDecodeError` | Accents | `open(f, encoding="utf-8")` |
| `write()` ho posa tot en una línia | `write` no afig `\n` | `f.write("text\n")` |

!!! success "Per a l'examen"
    ```python
    with open("f.txt") as f:              # llegir
        for linia in f:
            linia = linia.strip()

    with open("f.txt", "w") as f:         # escriure ("a" per afegir)
        f.write("text\n")

    import csv
    for fila in csv.DictReader(f): fila["columna"]

    import json
    dades = json.load(f)    json.dump(dades, f, indent=2)

    from pathlib import Path
    p = Path("ruta")
    p.name  p.suffix  p.parent  p.exists()
    Path.home() / "carpeta"
    p.glob("*.txt")   p.rglob("*.txt")
    ```

    - `"w"` **esborra** · `"a"` **afig**
    - `.strip()` per a llevar el `\n`
