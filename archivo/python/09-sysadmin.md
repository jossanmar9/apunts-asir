# 9. Python per a sysadmin

Este tema recull les eines de Python més útils per a administrar sistemes: rebre arguments, executar ordres, copiar fitxers, treballar amb dates, buscar patrons en logs...

## Rebre arguments: `sys.argv`

Igual que un script de Bash rep `$1`, `$2`..., un programa de Python pot rebre arguments:

```bash
python3 copia.py /home/ana /backup
```

Dins del programa estan en la llista `sys.argv`:

```python
import sys

print(sys.argv)          # ['copia.py', '/home/ana', '/backup']
origen = sys.argv[1]     # '/home/ana'   (com $1)
desti = sys.argv[2]      # '/backup'     (com $2)
```

| Python | Bash | Significa |
| ------ | ---- | --------- |
| `sys.argv[0]` | `$0` | nom del programa |
| `sys.argv[1]` | `$1` | primer argument |
| `len(sys.argv) - 1` | `$#` | quants arguments |

Comprovar que n'hi ha prou:

```python
if len(sys.argv) != 3:
    sys.exit(f"Ús: {sys.argv[0]} <origen> <destí>")
```

## Arguments professionals: `argparse`

Per a programes amb opcions (`-v`, `--dies 7`...), `argparse` ho fa tot sol: comprova els arguments i genera l'ajuda `-h` automàticament.

```python title="neteja.py"
import argparse

parser = argparse.ArgumentParser(description="Esborra fitxers antics")
parser.add_argument("carpeta", help="on buscar")                       # obligatori
parser.add_argument("-d", "--dies", type=int, default=30,              # opcional amb valor
                    help="antiguitat mínima en dies")
parser.add_argument("-s", "--simula", action="store_true",             # opcional sí/no
                    help="només mostra, no esborra")
args = parser.parse_args()

print(args.carpeta)    # el que s'ha passat
print(args.dies)       # 30 si no s'ha indicat
print(args.simula)     # True si s'ha posat -s
```

```console
$ python3 neteja.py /tmp -d 7 -s
$ python3 neteja.py -h          ← mostra l'ajuda automàticament
```

## Executar ordres del sistema: `subprocess`

```python
import subprocess

resultat = subprocess.run(["df", "-h"], capture_output=True, text=True)

print(resultat.stdout)       # el que ha mostrat l'ordre
print(resultat.returncode)   # 0 si ha anat bé (com $? en Bash)
```

| Paràmetre | Per a què |
| --------- | --------- |
| `["df", "-h"]` | l'ordre i els seus arguments, **cada un en un element** de la llista |
| `capture_output=True` | guarda l'eixida en compte de mostrar-la |
| `text=True` | l'eixida com a text (si no, ve en bytes) |
| `check=True` | si l'ordre falla, llança una excepció |

### Exemple: comprovar si uns serveis estan actius

```python
import subprocess

def servei_actiu(nom):
    r = subprocess.run(["systemctl", "is-active", "--quiet", nom])
    return r.returncode == 0         # 0 vol dir actiu

for servei in ["ssh", "cron", "nginx"]:
    if servei_actiu(servei):
        print(f"{servei}: actiu")
    else:
        print(f"{servei}: parat")
```

!!! danger "No uses `shell=True` amb dades de l'usuari"
    `subprocess.run(f"rm -rf {carpeta}", shell=True)` és perillós: si `carpeta` val `"x; rm -rf /"`, s'executaria tot. Passa sempre l'ordre com a **llista**: `["rm", "-rf", carpeta]`.

## Fitxers i carpetes: `shutil` i `os`

```python
import shutil
import os

shutil.copy("a.txt", "b.txt")            # copiar un fitxer
shutil.copytree("dades", "dades_copia")  # copiar una carpeta sencera
shutil.move("a.txt", "/tmp/")            # moure
shutil.rmtree("carpeta_vella")           # ⚠️ esborrar una carpeta amb tot el contingut

shutil.make_archive("backup", "gztar", "dades")   # crea backup.tar.gz amb la carpeta dades
shutil.which("rsync")                    # on està l'ordre rsync (None si no està)

total, usat, lliure = shutil.disk_usage("/")       # espai en disc (en bytes)
print(f"Disc ple al {usat / total:.0%}")

os.getenv("HOME")                        # una variable d'entorn
os.getuid() == 0                         # sóc root?
```

## Dates i hores: `datetime`

```python
from datetime import datetime, timedelta

ara = datetime.now()                       # data i hora actuals
print(ara.strftime("%d/%m/%Y %H:%M"))      # 10/10/2026 18:30

nom = f"backup_{ara:%Y%m%d}.tar.gz"        # backup_20261010.tar.gz
fa_una_setmana = ara - timedelta(days=7)   # restar dies
```

| Codi | Significa | Exemple |
| ---- | --------- | ------- |
| `%Y` | any (4 xifres) | 2026 |
| `%m` | mes | 10 |
| `%d` | dia | 10 |
| `%H` | hora | 18 |
| `%M` | minuts | 30 |
| `%S` | segons | 05 |

## Buscar patrons en text: `re`

Les **expressions regulars** (vegeu el [tema 11 de Bash](../bash/11-find-grep-xargs.md#patrons-buscar-formes-no-paraules-exactes)) també funcionen en Python, amb el mòdul `re`:

```python
import re

linia = "Failed password for root from 203.0.113.5 port 52211"

ips = re.findall(r"\d+\.\d+\.\d+\.\d+", linia)     # busca totes les IPs
print(ips)        # ['203.0.113.5']

if re.search(r"Failed password", linia):            # conté el patró?
    print("Intent fallit")
```

| Patró | Significa |
| ----- | --------- |
| `\d` | un dígit |
| `\d+` | un o més dígits |
| `\.` | un punt (literal) |
| `\s` | un espai |
| `\S+` | una "paraula" (tot el que no siga espai) |

La `r` davant de les cometes (`r"..."`) fa que les `\` no s'interpreten com a caràcters especials. Posa-la sempre amb `re`.

## Exemple complet: analitzar intents d'accés SSH fallits

Llig el log del sistema i mostra quines IPs han intentat entrar per SSH sense èxit:

```python title="ssh_fallits.py"
#!/usr/bin/env python3
"""Mostra les IPs amb més intents de login SSH fallits."""
import re
import sys
from collections import Counter

# Fitxer de log: el que es passe per argument o /var/log/auth.log
fitxer = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"

# Patró que busca: "Failed password for USUARI from IP"
patro = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+)")

ips = Counter()          # comptador d'IPs
usuaris = Counter()      # comptador d'usuaris provats

try:
    with open(fitxer, encoding="utf-8", errors="replace") as f:
        for linia in f:
            coincidencia = patro.search(linia)
            if coincidencia:
                usuari, ip = coincidencia.groups()    # els dos trossos entre ( )
                ips[ip] += 1
                usuaris[usuari] += 1
except (FileNotFoundError, PermissionError) as e:
    sys.exit(f"No puc llegir el log: {e}")

print(f"Total d'intents fallits: {sum(ips.values())}\n")

print("IPs amb més intents:")
for ip, n in ips.most_common(5):
    print(f"  {ip:<18}{n:>6}")

print("Usuaris més provats:")
for usuari, n in usuaris.most_common(5):
    print(f"  {usuari:<18}{n:>6}")
```

```console
$ sudo python3 ssh_fallits.py
Total d'intents fallits: 3

IPs amb més intents:
  203.0.113.5            2
  198.51.100.7           1
Usuaris més provats:
  root                   2
  admin                  1
```

**Com funciona:**

- Els parèntesis `( )` del patró marquen els trossos que volem traure (usuari i IP). `.groups()` els torna.
- `(?:invalid user )?` vol dir "*pot haver-hi el text 'invalid user ' o no*", sense guardar-lo.
- `Counter` és un diccionari que compta: `ips[ip] += 1` suma 1 a eixa IP.
- `most_common(5)` torna les 5 que més es repetixen.

!!! success "Per a l'examen"
    ```python
    import sys
    sys.argv[1]                         # primer argument ($1)
    sys.exit("missatge d'error")        # acabar amb error

    import subprocess
    r = subprocess.run(["ordre", "arg"], capture_output=True, text=True)
    r.stdout   r.returncode             # eixida · 0 = bé

    import shutil
    shutil.copy(a, b)  shutil.move(a, b)  shutil.rmtree(d)
    shutil.disk_usage("/")

    from datetime import datetime
    f"{datetime.now():%Y-%m-%d}"

    import re
    re.findall(r"\d+", text)   re.search(r"patró", text)
    ```
