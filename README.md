# Apunts ASIR

Apunts propis de **Bash** i **Python** amb exemples, exercicis resolts i xuletes, publicats com a web amb [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

🌐 **Web:** https://jossanmar9.github.io/apunts-asir/

## Estructura

```
docs/
├── index.md          portada
├── bash/             12 temes + mètode + problemes resolts
├── python/           10 temes + exercicis resolts
├── xuletes/          Bash, Linux, Python, Git, PowerShell
└── bibliografia.md
mkdocs.yml            configuració i menú
```

## Treballar en local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000, es refresca en guardar
```

## Afegir o canviar apunts

1. Edita o crea un `.md` dins de `docs/`.
2. Si és una pàgina nova, afig-la al menú (`nav:`) de `mkdocs.yml`.
3. `git add . && git commit -m "..." && git push` → l'Action publica la web en un minut o dos.

### Coses útils de Markdown

```markdown
!!! tip "Títol"          caixa destacada (note, tip, warning, danger, example)
    Contingut sagnat

??? success "Solució"    caixa plegada
    Contingut sagnat

=== "Linux"              pestanyes
    ...
=== "Windows"
    ...

++ctrl+c++               tecles
```
