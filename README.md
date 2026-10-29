# Apuntes ASIR

Repositorio personal de apuntes y material de práctica de **ASIR**, desarrollado en **castellano** a partir del temario y los materiales utilizados en clase.

La idea no es sustituir los apuntes originales, sino convertirlos en material de estudio más cómodo: explicaciones desarrolladas desde cero, ejemplos propios, errores habituales, repasos y un banco de ejercicios adicionales para practicar cada concepto.

🌐 **[Web de Apuntes ASIR](https://jossanmar9.github.io/apunts-asir/)**

## Contenido actual

| Sección | Contenido disponible |
| --- | --- |
| **IAW · Implantación de aplicaciones web** | UT1: entorno de implantación web · UT2: programación web en servidor con PHP |
| **ASO · Administración de sistemas operativos** | UT1: Bash · UT2: procesos, control de procesos, systemd, automatización y monitorización |
| **Introducción a Python** | UT1: introducción, entorno, datos, números y cadenas · UT2: objetos, métodos de cadenas, f-strings y Unicode · UT3: condicionales, `while`, `for`, depuración y bibliotecas para administración |
| **Git y GitHub** | Repositorios, commits, remoto y SSH |
| **Sostenibilidad aplicada al sistema productivo** | ASG, retos, ODS, economía circular, huellas y plan de sostenibilidad |
| **Cómo estudiar** | Método de estudio y consejos de aprendizaje |

Los índices de cada módulo están dentro de `docs/` y la navegación completa está disponible en la web de MkDocs.

## Ejercicios adicionales

Además de la teoría, el repositorio contiene un **banco propio de ejercicios adicionales**. No son copias de los ejercicios de practicar o entregar de clase: los enunciados se preparan específicamente para reforzar los contenidos ya vistos.

Actualmente hay **500 ejercicios adicionales**:

| Módulo | Unidad | Ejercicios | Organización |
| --- | --- | ---: | --- |
| **Python** | UT1 | 50 | 20 básicos + 20 intermedios + 10 de repaso |
| **Python** | UT2 | 50 | 20 básicos + 20 intermedios + 10 de repaso |
| **Python** | UT3 | 120 | 20 por cada bloque del temario + 20 mixtos |
| **ASO** | UT1 · Bash | 120 | práctica progresiva de Bash |
| **ASO** | UT2 · Procesos, servicios y automatización | 50 | práctica de los contenidos de la unidad |
| **IAW** | UT1 · Entorno de implantación web | 60 | práctica del entorno y herramientas de implantación |
| **IAW** | UT2 · PHP | 50 | práctica de programación web en servidor |

### Python UT3

UT3 tiene más ejercicios porque reúne varios bloques diferentes. En lugar de repartir solo 50 ejercicios entre todos ellos, cada parte dispone de práctica suficiente antes de mezclarlas:

| Ejercicios | Bloque |
| ---: | --- |
| 1–20 | Condicionales |
| 21–40 | `while` |
| 41–60 | `for` y `range()` |
| 61–80 | Depuración y errores |
| 81–100 | Bibliotecas para administración: `sys`, `os`, `datetime`, `platform`, `pathlib` y `shutil` |
| 101–120 | Ejercicios mixtos |

Los **20 ejercicios mixtos** son el último paso: combinan contenidos de varios bloques para evitar practicar cada herramienta de forma aislada. Pueden mezclar, por ejemplo, condicionales y bucles, validación de entradas, recorrido de archivos, fechas o información del sistema.

### Cómo trabajar los ejercicios

La intención es seguir una progresión sencilla:

1. Estudiar primero el tema correspondiente.
2. Resolver los ejercicios específicos de ese contenido sin consultar la solución de otros ejercicios.
3. Volver a los apuntes cuando aparezca una duda.
4. Hacer los ejercicios de repaso o mixtos cuando los conceptos individuales ya estén asentados.

Los ejercicios de Python se generan también como archivos `.py` independientes con el enunciado y espacio para escribir la solución. Los generadores se conservan en `scripts/` para que el banco pueda regenerarse de forma reproducible.

## Criterio de los apuntes

Los apuntes están pensados para estudiar desde un nivel inicial. Cada tema intenta explicar **qué es cada concepto, cómo funciona, para qué sirve y cómo se utiliza**, en lugar de limitarse a tablas o resúmenes.

Como criterio general:

- la teoría sigue el contenido publicado en clase;
- las explicaciones están redactadas en castellano;
- los ejemplos son propios y sencillos;
- los ejercicios adicionales son diferentes de las tareas de practicar o entregar;
- no se adelantan innecesariamente conceptos de unidades posteriores;
- se incluyen errores habituales y ejemplos de ejecución cuando ayudan a entender el tema;
- las tablas y resúmenes sirven como repaso, no como sustituto de la explicación.

En Python se mantiene una sintaxis sencilla y cercana a la utilizada en clase. Cuando resulta adecuado se prefiere `import datetime` y `import pathlib`, utilizando después `datetime.datetime`, `pathlib.Path`, etc.

En ASO los scripts utilizan `#!/bin/bash` y `echo`, siguiendo el formato empleado en clase.

## Fuentes de clase

Las principales fuentes utilizadas para comprobar el temario son:

- [IAW — victoria-nr](https://victoria-nr.github.io/iaw-alumnos/)
- [ASO — angelabserrano](https://angelabserrano.github.io/aso/)
- [Introducción a Python — victoria-nr](https://victoria-nr.github.io/python-intro-alumnos/)

También se utiliza el material facilitado en clase para revisar la cobertura de cada unidad. Los apuntes, ejemplos y ejercicios del repositorio son de redacción propia.

No existe una sincronización automática con las fuentes: cuando aparece material nuevo se revisa la unidad correspondiente, se actualiza la teoría y después se comprueba si el banco de ejercicios necesita ampliarse o modificarse.

## Estructura del repositorio

```text
docs/
├── index.md              portada de la web
├── iaw/                  apuntes de IAW
├── aso/                  apuntes de ASO
├── python-classe/        apuntes de Python UT1–UT3
├── git-github/           Git y GitHub
├── sostenibilidad/       apuntes de Sostenibilidad
├── ejercicios/
│   ├── python/           ejercicios adicionales de Python
│   ├── aso/              ejercicios adicionales de ASO
│   └── iaw/              ejercicios adicionales de IAW
├── estudiar/             método y consejos de estudio
├── classe.md             fuentes y cobertura del temario
└── assets/               recursos de la web

scripts/
├── regenera_ejercicios_python.py
├── regenera_ut3_python.py
├── regenera_ejercicios_aso.py
├── regenera_ejercicios_iaw.py
└── revisar_apuntes.py

archivo/                  material anterior conservado fuera de la web
mkdocs.yml                configuración y navegación de MkDocs
```

## Regeneración de ejercicios

Los generadores permiten reconstruir los archivos de ejercicios sin tener que mantener manualmente cientos de ficheros individuales.

```bash
python3 scripts/regenera_ejercicios_python.py
python3 scripts/regenera_ut3_python.py
python3 scripts/regenera_ejercicios_aso.py
python3 scripts/regenera_ejercicios_iaw.py
```

Los workflows de GitHub Actions ejecutan las regeneraciones correspondientes cuando cambian sus generadores.

## Trabajar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

La web estará disponible en `http://127.0.0.1:8000`.

Para comprobar que MkDocs puede generar toda la documentación:

```bash
mkdocs build --strict
```

## Revisar los ejemplos

Con Python 3, Bash, PHP, Git y `bc` instalados:

```bash
mkdocs build --strict --site-dir /tmp/asir-revision-web
python3 scripts/revisar_apuntes.py --site-dir /tmp/asir-revision-web
```

El comprobador revisa sintaxis, ejecuta los ejemplos preparados para ello y comprueba elementos de la web generada. Las opciones adicionales `--http` y `--docker` permiten probar también los casos que necesitan un servidor local o el entorno Docker de IAW.

## Actualización del temario

Cuando se publica contenido nuevo en clase:

1. se revisa primero el material original;
2. se actualiza la teoría de la unidad correspondiente;
3. se comprueba que los ejemplos utilizan únicamente contenidos ya estudiados;
4. se revisan los ejercicios adicionales para evitar duplicados y contenidos adelantados;
5. se actualizan índices, navegación y documentación si cambia la cobertura;
6. se comprueba la generación de la web antes de considerar terminada la actualización.

## Publicación

El repositorio utiliza `main` como rama de trabajo. GitHub Actions se encarga de las tareas automatizadas de regeneración y de publicar la documentación con GitHub Pages.