#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'docs' / 'ejercicios' / 'aso'

for unit, total in [('ut1', 120), ('ut2', 50)]:
    md = BASE / f'{unit}.md'
    text = md.read_text(encoding='utf-8')
    out = []
    found = 0
    folder = BASE / unit
    folder.mkdir(parents=True, exist_ok=True)
    for line in text.splitlines():
        # Remove old generated links, making regeneration idempotent.
        if line.startswith('[🐚 Abrir ejercicio_'):
            continue
        out.append(line)
        m = re.match(r'^(\d+)\.\s+(.+)$', line)
        if not m:
            continue
        n = int(m.group(1))
        if not 1 <= n <= total:
            continue
        found += 1
        statement = re.sub(r'\*\*', '', m.group(2)).strip()
        filename = f'ejercicio_{n:03d}.sh'
        content = '#!/bin/bash\n\n# ASO · ' + unit.upper() + f' · Ejercicio {n:03d}\n# ' + statement + '\n\n# Escribe tu solución a partir de aquí:\n\n'
        (folder / filename).write_text(content, encoding='utf-8')
        out.append(f'[🐚 Abrir {filename}]({unit}/{filename}){{ .md-button }}')
        out.append('')
    if found != total:
        raise SystemExit(f'{unit}: esperados {total}, encontrados {found}')
    md.write_text('\n'.join(out).rstrip() + '\n', encoding='utf-8')

# Add ASO to exercise landing page if absent.
idx = ROOT / 'docs' / 'ejercicios' / 'index.md'
text = idx.read_text(encoding='utf-8')
if 'aso/index.md' not in text:
    text += '\n## ASO\n\n- [UT1 · Bash — 120 ejercicios](aso/ut1.md)\n- [UT2 · Procesos, servicios y automatización — 50 ejercicios](aso/ut2.md)\n'
    idx.write_text(text, encoding='utf-8')

# Add ASO exercise navigation to mkdocs if absent.
mk = ROOT / 'mkdocs.yml'
y = mk.read_text(encoding='utf-8')
needle = '      - "Python":\n          - ejercicios/python/index.md\n          - "UT1 · Introducción y tipos": ejercicios/python/ut1.md\n          - "UT2 · Cadenas": ejercicios/python/ut2.md\n          - "UT3 · Condicionales y sysadmin": ejercicios/python/ut3.md\n'
addition = needle + '      - "ASO":\n          - ejercicios/aso/index.md\n          - "UT1 · Bash · 120": ejercicios/aso/ut1.md\n          - "UT2 · Procesos, servicios y automatización · 50": ejercicios/aso/ut2.md\n'
if 'ejercicios/aso/index.md' not in y:
    if needle not in y:
        raise SystemExit('No se encontró el bloque Ejercicios/Python en mkdocs.yml')
    mk.write_text(y.replace(needle, addition), encoding='utf-8')
