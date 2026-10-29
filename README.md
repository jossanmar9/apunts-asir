# Apuntes ASIR

Apuntes desarrollados en **castellano** a partir del material de clase de **IAW, ASO, Python y Sostenibilidad**, organizados por módulo, unidad y tema. Incluyen explicaciones desde cero, ejemplos propios, repaso y ejercicios adicionales para practicar sin reproducir las tareas de clase. **Git y GitHub tienen una sección independiente.**

🌐 **[Web de Apuntes ASIR](https://jossanmar9.github.io/apunts-asir/)**

## Contenido

| Sección | Contenido | Apuntes |
| --- | --- | --- |
| IAW · Implantación de aplicaciones web | UT1: entorno web · UT2: programación PHP | [Índice de IAW](docs/iaw/index.md) |
| ASO · Administración de sistemas operativos | UT1: Bash · UT2: procesos, servicios, automatización y monitorización | [Índice de ASO](docs/aso/index.md) |
| Introducción a Python | UT1: entorno y datos · UT2: objetos y cadenas · UT3: control, depuración y bibliotecas | [Índice de Python](docs/python-classe/index.md) |
| Git y GitHub | Repositorios, commits, remoto y SSH | [Git y GitHub](docs/git-github/index.md) |
| Sostenibilidad aplicada al sistema productivo | ASG, retos, ODS, economía circular, huellas y plan de sostenibilidad | [Índice de Sostenibilidad](docs/sostenibilidad/index.md) |
| Cómo estudiar | Método de estudio y consejos para aprender | [Cómo estudiar](docs/estudiar/index.md) |

## Ejercicios adicionales

El repositorio incluye colecciones de ejercicios propias, separadas del material para practicar o entregar en clase. El objetivo es poder repetir cada concepto muchas veces antes de pasar a ejercicios que combinen varias técnicas.

### Python

| Unidad | Organización | Total |
| --- | --- | ---: |
| UT1 | Introducción, tipos, operadores y entrada/salida | 50 |
| UT2 | Cadenas, métodos, slicing y formato | 50 |
| UT3 | 20 condicionales + 20 `while` + 20 `for`/`range()` + 20 depuración + 20 bibliotecas + 20 mixtos | 120 |

La **UT3 de Python** sigue deliberadamente una estructura de práctica por bloques. Los primeros 100 ejercicios permiten trabajar por separado los cinco bloques de los temas 3.1–3.5 y los ejercicios 101–120 obligan a combinar contenidos, por ejemplo bucles con condicionales, validación de datos, `pathlib`, fechas o información del sistema.

Los generadores se conservan en `scripts/` para poder regenerar los archivos de ejercicios de forma reproducible. Los `.py` generados contienen el enunciado y un espacio para escribir la solución.

## Criterio de los apuntes

Cada tema desarrolla los conceptos para un estudiante que empieza: qué significan, cómo funcionan, para qué se utilizan, ejemplos sencillos, errores habituales y repaso. Las tablas y resúmenes sirven de apoyo, pero no sustituyen la explicación.

Los casos didácticos y los ejercicios adicionales son distintos de los ejercicios de clase para practicar o entregar; no se crean simples variantes cambiando nombres o números. Cuando un tema incluye ejercicios dentro de los propios apuntes, se mantienen las pistas y soluciones plegadas para poder intentarlos antes de consultar la respuesta.

En los ejemplos de Python se prioriza una sintaxis sencilla y coherente con lo visto en clase. Para módulos se prefiere, cuando resulta adecuado, `import datetime` y `import pathlib`, accediendo después a sus elementos mediante el nombre del módulo.

En ASO se utiliza Bash con la cabecera `#!/bin/bash`, siguiendo el formato de clase. Para mostrar mensajes se utiliza `echo`.

## Material de Sostenibilidad

Se han añadido las seis unidades de *Sostenibilidad aplicada al sistema productivo* (Juan Jesús García Navarro y Antonio Ramón Álvarez Sánchez, Editex, edición 2024), a partir del PDF facilitado por el estudiante. El repositorio contiene apuntes y ejercicios propios, no una copia del libro. Consulta el [índice de Sostenibilidad](docs/sostenibilidad/index.md).

## Fuentes y actualización

Fuentes principales de clase:

- [IAW — victoria-nr](https://victoria-nr.github.io/iaw-alumnos/)
- [ASO — angelabserrano](https://angelabserrano.github.io/aso/)
- [Introducción a Python — victoria-nr](https://victoria-nr.github.io/python-intro-alumnos/)

Los apuntes y ejemplos son de redacción propia a partir del material facilitado y de las fuentes de clase. No existe sincronización automática con esas webs: la actualización se realiza cuando se revisa material nuevo.

Al actualizar una unidad se sigue este criterio:

1. Revisar la teoría y los enunciados de clase para identificar exactamente los conceptos publicados.
2. Actualizar los apuntes en castellano sin adelantar innecesariamente contenidos de unidades posteriores.
3. Mantener ejemplos y ejercicios propios distintos de las tareas asignadas.
4. Comprobar los ejemplos ejecutables y la compilación de MkDocs.
5. Actualizar índices, generadores y documentación cuando cambie la cobertura.

Consulta también [la cobertura por unidades](docs/classe.md). Los originales y materiales que no deben publicarse se conservan fuera de `docs/` cuando corresponde.

## Estructura

```text
docs/
├── index.md              portada
├── iaw/                  teoría de IAW
├── aso/                  teoría de ASO
├── git-github/           Git y GitHub
├── python-classe/        teoría de Python UT1–UT3
├── ejercicios/           ejercicios adicionales por módulo
├── sostenibilidad/       apuntes y ejercicios de Sostenibilidad
├── estudiar/             método y consejos de estudio
├── classe.md             fuentes y cobertura del temario
└── assets/               estilos de la web
scripts/
├── regenera_ejercicios_python.py
├── regenera_ut3_python.py
├── regenera_ejercicios_aso.py
├── regenera_ejercicios_iaw.py
└── revisar_apuntes.py
archivo/                  material anterior/original fuera de la web
mkdocs.yml                configuración y navegación
```

## Trabajar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abre `http://127.0.0.1:8000`. Para comprobar la compilación:

```bash
mkdocs build --strict
```

## Revisar los ejemplos

Con Python 3, Bash, PHP, Git y `bc` instalados:

```bash
mkdocs build --strict --site-dir /tmp/asir-revision-web
python3 scripts/revisar_apuntes.py --site-dir /tmp/asir-revision-web
```

El comprobador revisa sintaxis, ejecuta ejemplos en carpetas temporales y comprueba enlaces, tablas y ejercicios desplegables de la web generada. Las comprobaciones adicionales `--http` y `--docker` prueban los formularios mediante un servidor local y el entorno Nginx/PHP en un proyecto Docker temporal independiente.

## Publicación

Los cambios se realizan sobre `main`. Después de actualizar y revisar el contenido, GitHub Actions regenera cuando corresponde los ejercicios y publica la web en GitHub Pages.
