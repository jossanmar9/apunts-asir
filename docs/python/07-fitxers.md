# 7. Fitxers, pathlib i glob

## Obrir fitxers amb `with`

```python
with open("notes.txt", encoding="utf-8") as f:
    contingut = f.read()
# en eixir del bloc el fitxer es tanca sol, encara que hi haja un error
```

| Mode | Què fa |
| ---- | ------ |
| `"r"` | llegir (per defecte) |
| `"w"` | escriure: **esborra** el que hi havia |
| `"a"` | afegir al final |
| `"x"` | crear; error si ja existix |
| `"rb"`, `"wb"` | binari (imatges, fitxers comprimits...) |

## Llegir

```python
with open("/etc/hosts") as f:
    tot = f.read()             # tot en un str
with open("/etc/hosts") as f:
    linies = f.readlines()     # llista de línies (amb \n)
with open("/etc/hosts") as f:
    for linia in f:            # ⭐ línia a línia (no carrega tot en memòria)
        print(linia.rstrip("\n"))
```

Per a logs grans, recórrer línia a línia és la manera correcta.

## Escriure

```python
with open("informe.txt", "w", encoding="utf-8") as f:
    f.write("Informe del servidor\n")
    for s in serveis:
        f.write(f"- {s}\n")

with open("app.log", "a") as f:        # afegir
    print("Nova entrada", file=f)      # print també pot escriure en fitxers
```

## CSV

```python
import csv

with open("usuaris.csv", newline="", encoding="utf-8") as f:
    for fila in csv.DictReader(f):          # cada fila és un dict
        print(fila["nom"], fila["grup"])

with open("eixida.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["nom", "uid"])
    w.writerow(["jose", 1000])
```

Amb separador `;` (Excel en castellà/valencià): `csv.reader(f, delimiter=";")`.

## JSON

```python
import json

with open("config.json") as f:
    config = json.load(f)          # JSON → dict/list
print(config["servidor"]["port"])

config["debug"] = False
with open("config.json", "w") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

text = json.dumps({"a": 1})        # dict → str
dades = json.loads('{"a": 1}')     # str → dict
```

## `pathlib`: rutes com a objectes

```python
from pathlib import Path

p = Path("/var/log/nginx/access.log")
p.name          # 'access.log'
p.stem          # 'access'
p.suffix        # '.log'
p.parent        # Path('/var/log/nginx')
p.exists()      # True/False
p.is_file(), p.is_dir()
p.stat().st_size       # mida en bytes

Path.home()            # /home/jose
Path.cwd()             # directori actual
backup = Path.home() / "backup" / "2026"   # / uneix rutes
backup.mkdir(parents=True, exist_ok=True)  # com mkdir -p

text = Path("notes.txt").read_text(encoding="utf-8")
Path("eixida.txt").write_text("hola\n", encoding="utf-8")
```

### Recórrer i buscar

```python
carpeta = Path("/etc")
for f in carpeta.iterdir():            # contingut directe
    print(f.name)

list(carpeta.glob("*.conf"))           # .conf de /etc
list(carpeta.rglob("*.conf"))          # .conf de /etc i subdirectoris
```

## `glob`: patrons de noms

```python
import glob

glob.glob("/var/log/*.log")
glob.glob("/var/log/**/*.log", recursive=True)   # ** = qualsevol subdirectori
glob.glob("informe_202[0-6]_*.pdf")
```

| Patró | Significa |
| ----- | --------- |
| `*` | qualsevol cosa (dins d'un directori) |
| `**` | qualsevol nombre de directoris (amb `recursive=True` o `rglob`) |
| `?` | un caràcter |
| `[abc]` / `[0-9]` | un d'eixos caràcters |

`pathlib` i `glob` fan el mateix; `pathlib` és més modern i torna objectes `Path` en compte de cadenes.

## Exemple: els 5 fitxers més grans

```python
from pathlib import Path

def mida_llegible(bytes_):
    for unitat in ("B", "KiB", "MiB", "GiB"):
        if bytes_ < 1024:
            return f"{bytes_:.1f} {unitat}"
        bytes_ /= 1024
    return f"{bytes_:.1f} TiB"

fitxers = [f for f in Path.home().rglob("*") if f.is_file()]
for f in sorted(fitxers, key=lambda f: f.stat().st_size, reverse=True)[:5]:
    print(f"{mida_llegible(f.stat().st_size):>10}  {f}")
```
