# Apuntes ASIR

Resúmenes en **castellano** de los apuntes de clase de **IAW, ASO y Python**, organizados por módulo, unidad y tema, con explicaciones desde cero y ejemplos propios resueltos paso a paso. **Git y GitHub tiene una sección independiente.** Sirven para estudiar y como guía mientras haces los trabajos.

🌐 **[Web de Apuntes ASIR](https://jossanmar9.github.io/apunts-asir/)**

## Estudiar desde el repositorio

| Sección | Contenido | Apuntes |
| --- | --- | --- |
| IAW · Implantación de aplicaciones web | UT1: entorno web · UT2: programación PHP | [Índice de IAW](docs/iaw/index.md) |
| ASO · Administración de sistemas operativos | UT1: Bash | [Índice de ASO](docs/aso/index.md) |
| Introducción a Python | UT1: entorno y datos · UT2: objetos y cadenas · UT3: control y bibliotecas | [Índice de Python](docs/python-classe/index.md) |
| Git y GitHub | Tema independiente: repositorios, commits, remoto y SSH | [Git y GitHub](docs/git-github/index.md) |
| Cómo estudiar | Método de estudio y consejos para aprender | [Cómo estudiar](docs/estudiar/index.md) |

Cada tema incluye teoría explicada, ejemplos propios con el razonamiento y el resultado esperado, errores habituales y un resumen de repaso. Los casos didácticos **no son los ejercicios de clase para practicar o entregar**, ni versiones con solo los nombres o los datos cambiados.

## Fuentes y criterio de actualización

- [IAW — victoria-nr](https://victoria-nr.github.io/iaw-alumnos/)
- [ASO — angelabserrano](https://angelabserrano.github.io/aso/)
- [Introducción a Python — victoria-nr](https://victoria-nr.github.io/python-intro-alumnos/)

Última consulta: **26/10/2026**. Traducción al castellano: **27/10/2026**. Consulta la [cobertura por unidades](docs/classe.md). Los resúmenes y ejemplos son de redacción propia; las fuentes de teoría se enlazan en cada tema.

**Actualización manual, cuando lo solicite el estudiante.** Cuando se anuncien materiales nuevos:

1. Revisa la teoría y los enunciados nuevos para identificar conceptos y evitar resolver los ejercicios asignados.
2. Actualiza el módulo y la unidad correspondientes con explicaciones claras en castellano y casos didácticos diferentes, no simples cambios de nombres o datos.
3. Explica entrada, pasos, resultado y errores. Distingue lo publicado de lo que solo está planificado.
4. Comprueba los ejemplos ejecutables y la compilación; actualiza fuentes, fecha y cobertura.

No hay sincronización automática con las webs de clase. Los apuntes anteriores se conservan en **Complementos (valenciano)**.

## Estructura

```text
docs/
├── index.md          portada por módulos y temas independientes
├── iaw/              UT1 y UT2, con 8 temas
├── aso/              UT1 Bash, con 5 temas
├── git-github/       tema independiente de Git y GitHub
├── python-classe/    UT1 a UT3, con 8 temas
├── estudiar/         método y consejos de estudio en castellano
├── classe.md         fuentes y cobertura del temario
├── bash/, python/, powershell/, git/, docker/, php/
│                     apuntes anteriores en valenciano
├── xuletes/          resúmenes anteriores de consulta rápida
└── bibliografia.md   bibliografía complementaria
mkdocs.yml            configuración y menú de la web
```

La antigua página de Git en ASO conserva un enlace a la nueva sección para que los enlaces publicados sigan siendo útiles.

## Trabajar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abre `http://127.0.0.1:8000`. Para comprobar la compilación: `mkdocs build --strict`.

## Publicar cambios

Edita los `.md` dentro de `docs/` y registra cualquier página nueva en `nav:` de `mkdocs.yml`. Después de revisar y probar, un commit enviado a `main` activa la Action que publica la web en GitHub Pages.
