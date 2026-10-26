# Apunts ASIR

Resums dels apunts de classe d’**IAW, ASO i Python**, organitzats per mòdul, unitat i tema, amb explicacions des de zero i exemples propis resolts pas a pas. Serveixen per a estudiar i com a guia mentre es fan els treballs.

🌐 **[Web d’Apunts ASIR](https://jossanmar9.github.io/apunts-asir/)**

## Estudiar des del repositori

| Mòdul | Unitats amb resum | Apunts |
| --- | --- | --- |
| IAW · Implantació d’aplicacions web | UT1: entorn web · UT2: programació PHP | [Índex d’IAW](docs/iaw/index.md) |
| ASO · Administració de sistemes operatius | UT0: Git · UT1: Bash | [Índex d’ASO](docs/aso/index.md) |
| Introducció a Python | UT1: entorn i dades · UT2: objectes i cadenes · UT3: control i biblioteques | [Índex de Python](docs/python-classe/index.md) |
| Com estudiar | Mètode d’estudi i consells per a aprendre | [Com estudiar](docs/estudiar/index.md) |

Cada tema inclou teoria explicada, exemples nous amb el raonament i el resultat esperat, errors habituals i un resum de repàs. Els casos didàctics **no són els exercicis de classe per a practicar o entregar**, ni versions amb només noms o xifres canviats.

## Fonts i criteri d’actualització

- [IAW — victoria-nr](https://victoria-nr.github.io/iaw-alumnos/)
- [ASO — angelabserrano](https://angelabserrano.github.io/aso/)
- [Introducció a Python — victoria-nr](https://victoria-nr.github.io/python-intro-alumnos/)

Última consulta: **26/10/2026**. Consulta la [cobertura per unitats](docs/classe.md). Els resums i exemples són redacció pròpia; les fonts de teoria s’enllacen en cada tema.

**Actualització manual, quan ho demane l’estudiant.** Quan s’anuncien materials nous:

1. Revisa la teoria i els enunciats nous per identificar conceptes i evitar resoldre els exercicis assignats.
2. Actualitza el mòdul i la unitat corresponents amb explicacions clares i casos didàctics diferents, no simples canvis de noms o dades.
3. Explica entrada, passos, resultat i errors. Distingeix el que està publicat del que només està planificat.
4. Comprova els exemples executables i la compilació; actualitza fonts, data i cobertura.

No hi ha sincronització automàtica amb els webs de classe.

## Estructura

```text
docs/
├── index.md          portada per mòduls
├── iaw/              UT1 i UT2, amb 8 temes
├── aso/              UT0 i UT1, amb 6 temes
├── python-classe/    UT1 a UT3, amb 8 temes
├── estudiar/         mètode i consells d’estudi
├── classe.md         fonts i cobertura del temari
├── bash/, python/, powershell/, git/, docker/, php/
│                     apunts anteriors, accessibles en Complements
├── xuletes/          resums de consulta ràpida
└── bibliografia.md   bibliografia complementària
mkdocs.yml            configuració i menú de la web
```

## Treballar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Obri `http://127.0.0.1:8000`. Per comprovar la compilació: `mkdocs build --strict`.

## Publicar canvis

Edita els `.md` dins de `docs/` i registra qualsevol pàgina nova en `nav:` de `mkdocs.yml`. Després de revisar i provar, un commit enviat a `main` activa l’Action que publica la web en GitHub Pages.
