# UT1 · 1. Programar i preparar l'entorn

## Programar és concretar una seqüència

Un programa expressa passos sense ambigüitats. Abans del codi, defineix què entra, què cal transformar i què ha d'eixir. Python és un llenguatge d'alt nivell: permet representar eixos passos sense escriure directament instruccions de la CPU.

En l'ús habitual amb CPython, el codi font `.py` es transforma en bytecode i s'executa en la màquina virtual de Python. L'editor on escrius no és l'intèrpret que executa. Un comentari amb `#` explica el motiu d'una decisió; Python no l'executa.

## Exemple resolt: estimar una lectura d'àudio

**Problema nou:** una gravació conté 840 paraules i es llig a 140 paraules per minut. Volem estimar-ne la duració.

1. Entrada: quantitat de paraules i ritme de lectura.
2. Transformació: dividir paraules entre paraules per minut.
3. Eixida: duració estimada en minuts.

Desa `audio.py`:

```python
paraules = 840
ritme = 140
# Suposem un ritme constant, sense pauses addicionals.
minuts = paraules / ritme
print(f"Duració estimada: {minuts:.1f} minuts")
```

Executa `python3 audio.py` en Linux o `py audio.py` en un Windows amb el llançador instal·lat. **Resultat esperat:** `Duració estimada: 6.0 minuts`. Si dobles les paraules i mantens el ritme, la duració també es dobla. És una comprovació de sentit, a més de comprovar que el programa no falla.

## Entorn de treball pas a pas

En Linux, dins d'una carpeta nova:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python audio.py
python -m pip --version
deactivate
```

En PowerShell, l'activació corresponent és `.\.venv\Scripts\Activate.ps1`. Pot estar condicionada per la política d'execució del teu equip. A VS Code selecciona l'intèrpret del projecte amb **Python: Select Interpreter**. Si el terminal funciona i el botó d'execució no, comprova que tots dos usen el mateix intèrpret.

Un entorn virtual aïlla paquets del projecte, però no és una màquina virtual. `python -m pip install NOM_PAQUET` instal·la amb el Python que has triat; no necessites instal·lar res per als exemples d'aquesta secció, que usen la biblioteca estàndard.

## Què és cada eina?

| Eina | Funció |
| --- | --- |
| VS Code | Editor ampliable amb execució i depuració |
| Thonny / PyCharm | Entorns de desenvolupament de Python amb diferents enfocaments |
| Jupyter | Quaderns amb text, codi i resultats |
| Anaconda | Distribució i eines molt utilitzades en treball científic |
| pip | Instal·lació de paquets |
| uv | Eina alternativa per a gestionar projectes, paquets i entorns |
| pyenv | Gestió de versions de Python |
| pdb | Depurador de terminal |

## Depurar és observar

Posa un punt d'interrupció en `minuts = ...` i executa el depurador. Abans de la línia, existeixen `paraules` i `ritme`; després, també `minuts`. El ressaltat sol indicar la pròxima instrucció, no una instrucció ja executada. Mira VARIABLES i vigila `paraules / ritme` en WATCH.

| Error | Revisió |
| --- | --- |
| No es troba `audio.py` | Carpeta de treball i nom del fitxer. |
| `NameError` amb `Print` | Python distingeix majúscules; és `print`. |
| Paquet instal·lat però no importable | Intèrpret de l'editor i del terminal. |

!!! success "Per a repassar"
    Explica entrada, transformació i eixida abans del codi. Després identifica quin programa edita i quin programa executa.

---

Fonts del temari: [01-introduccion-python](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/01-introduccion-python/), [02-entorno-vscode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/02-entorno-vscode/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
