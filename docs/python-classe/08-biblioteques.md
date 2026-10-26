# UT3 · 3. Biblioteques per a administració de sistemes

## Importar una eina, no memoritzar un catàleg

La biblioteca estàndard ja ve amb Python. `import sys` dona accés amb el prefix `sys.`; `from pathlib import Path` importa directament el nom `Path`. Un nom de fitxer com `random.py` o `sys.py` en el teu projecte pot causar confusions amb imports: usa noms propis.

| Mòdul | Què consultes o fas |
| --- | --- |
| sys | `argv`, `version`, `platform`, `exit` |
| os | Entorn amb `getenv`, directori amb `getcwd`, contingut amb `listdir` |
| platform | `system`, `release`, `processor` |
| datetime | Dates, hores, diferències i format |
| pathlib | Construcció de rutes i propietats dels fitxers |
| shutil | Còpies, moviments i ús del disc |
| random / time | Simulacions aleatòries / pauses |

## Exemple resolt: calendari de calibratge

**Problema nou:** a partir d'una data fixa, preparar tres dates de revisió cada dos dies. Usar una data fixa permet comprovar el resultat sense dependre del dia en què executes el codi.

```python
from datetime import date, timedelta
inici = date(2026, 10, 26)
for numero in range(3):
    revisio = inici + timedelta(days=numero * 2)
    print(f"R{numero + 1:02d} | {revisio:%d/%m/%Y}")
```

**Resultat esperat:**

```text
R01 | 26/10/2026
R02 | 28/10/2026
R03 | 30/10/2026
```

`timedelta` representa una duració i sap travessar canvis de mes. `%d`, `%m` i `%Y` formaten dia, mes i any. `date.today()` i `datetime.now()` consulten el rellotge; `weekday()` numera dilluns com a 0 i diumenge com a 6. Una data/hora sense zona no incorpora automàticament les regles d'una altra zona horària.

## Exemple resolt: resum de documents Markdown

**Objectiu nou:** llegir una carpeta passada com a argument i sumar la mida dels fitxers `.md` immediats. No modifica el contingut.

Desa `documents.py`:

```python
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Ús: python documents.py carpeta")
    sys.exit(1)

carpeta = Path(sys.argv[1])
if not carpeta.is_dir():
    print("Cal indicar una carpeta existent")
    sys.exit(2)

quantitat = 0
bytes_total = 0
for ruta in sorted(carpeta.iterdir()):
    if ruta.is_file() and ruta.suffix.lower() == ".md":
        quantitat += 1
        bytes_total += ruta.stat().st_size
        print(ruta.name)
print(f"Documents: {quantitat}; bytes: {bytes_total}")
```

`sys.argv[0]` és el script i `[1]` la carpeta. `Path` representa una ruta; `/` combina components sense concatenar separadors manualment. `iterdir()` recorre el nivell immediat i `stat().st_size` consulta bytes. L'ordre es fa explícit amb `sorted`.

**Prova controlada:** crea una carpeta amb `a.md` de tres bytes (`abc`) i `b.md` de dos bytes (`xy`), sense salts finals, i un `imatge.txt` qualsevol. L'eixida enumera `a.md`, `b.md` i acaba amb `Documents: 2; bytes: 5`. La mida en bytes no sempre coincideix amb el nombre de caràcters en UTF-8.

## Rutes i operacions que necessiten atenció

`Path.cwd()` consulta el directori actual; `exists`, `is_file` i `is_dir` comproven; `parent`, `name` i `suffix` descriuen la ruta. `mkdir(parents=True, exist_ok=True)` crea carpetes intermèdies i tolera una carpeta ja existent. `glob('*.md')` busca en el nivell actual i `rglob('*.md')` ho fa recursivament. `rename` pot moure o substituir segons el sistema; `rmdir` només elimina un directori buit.

`shutil.copy` copia fitxers i pot sobreescriure; `move` els mou; `rmtree` elimina un arbre complet. Abans d'usar-les, defineix origen, destí i què faràs si ja existeix. `shutil.disk_usage(Path.cwd())` retorna total, usat i lliure en bytes per al sistema de fitxers corresponent; no totes les plataformes comparteixen una ruta com `/`.

`os.getenv('NOM', 'alternativa')` consulta una variable d'entorn. `platform.system()` pot retornar `Linux`, `Windows` o `Darwin`; `processor()` pot retornar text buit. No deduïsques el gestor de paquets exacte només del nom Linux: hi ha distribucions diferents.

`random.randint(1, 6)` simula un dau; `time.sleep(0.1)` pausa el procés. No cal esperar realment minuts per a provar un bucle: usa dades fixes i pauses curtes durant el laboratori.

## Errors típics

| Símptoma | Revisió |
| --- | --- |
| No troba la carpeta | El punt de partida de les rutes relatives és el directori de treball. |
| La mida és diferent de la prevista | Bytes, salts de línia i codificació del fitxer. |
| Falla `stat()` malgrat la comprovació | Permisos o canvis del fitxer entre comprovar i llegir. |
| No inclou subcarpetes | `iterdir` no és un recorregut recursiu. |

!!! success "Per a repassar"
    Tria el mòdul per la tasca, consulta el tipus que retorna cada operació i prova primer amb un conjunt menut de fitxers coneguts.

---

Fonts del temari: [05-librerias-sysadmin](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/05-librerias-sysadmin/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
