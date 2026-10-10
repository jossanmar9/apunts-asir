# Xuleta de Python

> Consulta ràpida. La teoria completa està en la [secció de Python](../python/index.md).

## Bàsics

```python
nom = input("Nom: ")              # sempre str
n = int(input("Número: "))        # convertir
print(f"{nom} té {n} anys")       # f-string
print(f"{3.14159:.2f}")           # 3.14
print(f"{'text':<10}|{42:>5}")    # alinear
```

| Operador | Significa |
| -------- | --------- |
| `/` `//` `%` `**` | divisió, divisió entera, residu, potència |
| `==` `!=` `<` `<=` | comparacions |
| `and` `or` `not` | lògics |
| `in` / `not in` | pertany a |
| `is None` | comprovar si és None |

## Control de flux

```python
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

valor = "sí" if cond else "no"

for i in range(1, 11): ...           # 1..10
for i, v in enumerate(llista): ...    # índex i valor
for a, b in zip(l1, l2): ...          # dues llistes alhora
while cond: ...
break / continue / pass
```

## Cadenes

```python
s[0]  s[-1]  s[2:5]  s[::-1]
s.strip()  s.lower()  s.upper()  s.title()
s.split(":")  ",".join(llista)  s.replace("a", "b")
s.startswith("x")  s.endswith(".log")  s.isdigit()
"err" in s  len(s)  s.count("a")  s.find("x")
```

## Llistes

```python
l = [3, 1, 2]
l.append(4)  l.insert(0, 9)  l.extend([5, 6])
l.remove(9)  l.pop()  del l[0]
l.sort()  sorted(l, reverse=True)  sorted(l, key=len)
sum(l)  max(l)  min(l)  len(l)
[x * 2 for x in l if x > 1]          # comprensió
copia = l.copy()                     # NO copia = l
```

## Diccionaris i conjunts

```python
d = {"ssh": 22, "http": 80}
d["dns"] = 53          d.get("ftp", 21)      "ssh" in d
del d["http"]          d.pop("dns", None)
for k, v in d.items(): ...
{k: v for k, v in d.items() if v < 100}

from collections import Counter
Counter(llista).most_common(3)

a | b   a & b   a - b               # unió, intersecció, diferència
set(llista)                         # llevar duplicats
```

## Funcions

```python
def f(obligatori, opcional=10, *args, **kwargs):
    """Documentació."""
    return a, b                      # torna una tupla

x, y = f(1)
sorted(dades, key=lambda d: d[1])

if __name__ == "__main__":
    main()
```

## Fitxers

```python
with open("f.txt", encoding="utf-8") as f:     # "w" escriure, "a" afegir
    for linia in f:
        linia = linia.rstrip("\n")

from pathlib import Path
p = Path("/var/log/syslog")
p.name  p.stem  p.suffix  p.parent  p.exists()  p.is_dir()
Path.home() / "backup"                         # unir rutes
p.read_text()  p.write_text("...")
Path("/etc").glob("*.conf")   Path(".").rglob("*.py")

import json, csv
json.load(f)  json.dump(dades, f, indent=2, ensure_ascii=False)
csv.DictReader(f)  csv.writer(f).writerow([...])
```

## Excepcions

```python
try:
    n = int(text)
except ValueError as e:
    print(f"Error: {e}")
else:
    ...                  # si no hi ha hagut error
finally:
    ...                  # sempre

raise ValueError("missatge")
sys.exit("missatge d'error")     # ix amb codi 1
```

## Sistema

```python
import sys, os, shutil, subprocess
sys.argv                                   # arguments
os.getenv("HOME")   os.getuid() == 0       # és root?
shutil.copy(a, b)   shutil.move(a, b)   shutil.rmtree(d)
shutil.disk_usage("/")   shutil.which("rsync")
r = subprocess.run(["ls", "-l"], capture_output=True, text=True)
r.returncode   r.stdout

from datetime import datetime, timedelta
f"{datetime.now():%Y-%m-%d_%H%M}"
datetime.now() - timedelta(days=7)

import re
re.search(r"(\d+)\.(\d+)", s).groups()
re.findall(r"\d+\.\d+\.\d+\.\d+", text)
```

## Entorns virtuals

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install paquet
pip freeze > requirements.txt
deactivate
```
