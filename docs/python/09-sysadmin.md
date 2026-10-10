# 9. Python per a sysadmin

## Arguments de línia d'ordres

### `sys.argv` (senzill)

```python
import sys

if len(sys.argv) != 2:
    sys.exit(f"Ús: {sys.argv[0]} <directori>")
directori = sys.argv[1]       # sys.argv[0] és el nom de l'script
```

### `argparse` (professional)

Genera l'ajuda (`-h`) i valida els tipus automàticament:

```python title="neteja.py"
import argparse

parser = argparse.ArgumentParser(description="Esborra fitxers antics")
parser.add_argument("directori", help="on buscar")
parser.add_argument("-d", "--dies", type=int, default=30, help="antiguitat mínima")
parser.add_argument("-n", "--simula", action="store_true", help="no esborra, només mostra")
args = parser.parse_args()

print(args.directori, args.dies, args.simula)
```

```console
$ python3 neteja.py /tmp -d 7 --simula
$ python3 neteja.py -h
```

## Executar ordres: `subprocess`

```python
import subprocess

r = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
print(r.returncode)    # 0 si ha anat bé
print(r.stdout)        # l'eixida
print(r.stderr)        # els errors

subprocess.run(["systemctl", "restart", "nginx"], check=True)  # check: excepció si falla
```

!!! danger "Passa la llista d'arguments, no una cadena amb `shell=True`"
    `subprocess.run(f"rm -rf {dir}", shell=True)` és perillós: si `dir` conté `; rm -rf /` s'executa. Amb `["rm", "-rf", dir]` cada element és un argument i no s'interpreta.

```python
def servei_actiu(nom):
    r = subprocess.run(["systemctl", "is-active", "--quiet", nom])
    return r.returncode == 0

for s in ["ssh", "nginx", "cron"]:
    print(f"{s:<8} {'✅' if servei_actiu(s) else '❌'}")
```

## Sistema: `os`, `shutil`, `platform`

```python
import os, shutil, platform

os.getenv("HOME")                # variable d'entorn
os.environ.get("EDITOR", "nano")
os.getcwd(); os.chdir("/tmp")
os.getuid() == 0                 # és root?
os.cpu_count()
platform.system(), platform.release(), platform.node()

shutil.copy("a.txt", "b.txt")            # copiar fitxer
shutil.copytree("dir", "dir_backup")     # copiar directori
shutil.move("a.txt", "/tmp/")
shutil.rmtree("dir_vell")                # esborrar directori sencer (compte!)
shutil.make_archive("backup", "gztar", "dades")   # crea backup.tar.gz
shutil.which("rsync")                    # ruta de l'ordre o None

total, usat, lliure = shutil.disk_usage("/")
print(f"Disc: {usat / total:.0%} usat")
```

## Dates: `datetime`

```python
from datetime import datetime, timedelta

ara = datetime.now()
ara.strftime("%Y-%m-%d %H:%M")          # '2026-10-10 17:30'
f"backup_{ara:%Y%m%d_%H%M}.tar.gz"      # dins d'un f-string
fa_una_setmana = ara - timedelta(days=7)
datetime.strptime("10/10/2026", "%d/%m/%Y")   # text → data
datetime.fromtimestamp(os.path.getmtime("f.txt"))   # data de modificació
```

## Expressions regulars: `re`

```python
import re

linia = "Oct 10 17:30:01 srv sshd[1234]: Failed password for root from 203.0.113.5 port 52211"

m = re.search(r"Failed password for (\S+) from (\d+\.\d+\.\d+\.\d+)", linia)
if m:
    usuari, ip = m.groups()     # ('root', '203.0.113.5')

re.findall(r"\d+\.\d+\.\d+\.\d+", text)        # totes les IPs
re.sub(r"\s+", " ", text)                       # comprimir espais
re.fullmatch(r"[a-z][a-z0-9_]{2,15}", usuari)   # validar un nom d'usuari
```

## Registres: `logging`

Millor que `print` per a scripts que s'executen sols (cron, systemd):

```python
import logging

logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logging.info("Començant còpia")
logging.warning("Queda poc espai")
logging.error("No s'ha pogut connectar")
```

## Exemple complet: analitzar intents d'accés SSH fallits

```python title="ssh_fallits.py"
#!/usr/bin/env python3
"""Mostra les IPs amb més intents de login SSH fallits."""
import argparse
import re
import sys
from collections import Counter

PATRO = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\S+)")

def analitza(fitxer):
    ips, usuaris = Counter(), Counter()
    with open(fitxer, encoding="utf-8", errors="replace") as f:
        for linia in f:
            if m := PATRO.search(linia):
                usuari, ip = m.groups()
                usuaris[usuari] += 1
                ips[ip] += 1
    return ips, usuaris

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("log", nargs="?", default="/var/log/auth.log")
    p.add_argument("-n", "--top", type=int, default=5)
    args = p.parse_args()

    try:
        ips, usuaris = analitza(args.log)
    except (FileNotFoundError, PermissionError) as e:
        sys.exit(f"No puc llegir el log: {e}")

    print(f"Total d'intents fallits: {sum(ips.values())}\n")
    print("IPs:")
    for ip, n in ips.most_common(args.top):
        print(f"  {ip:<18}{n:>6}")
    print("Usuaris provats:")
    for u, n in usuaris.most_common(args.top):
        print(f"  {u:<18}{n:>6}")

if __name__ == "__main__":
    main()
```

```console
$ sudo python3 ssh_fallits.py -n 3
```

En sistemes amb `journald` sense `auth.log`: `journalctl -u ssh --no-pager > ssh.log` i passa-li eixe fitxer.
