# UT1 · 1.2 Entorno de desarrollo

## Qué debes aprender

Para programar no basta con conocer la sintaxis de Python. Necesitamos herramientas para **escribir, ejecutar, probar y depurar** programas.

## Editor, IDE y terminal

Un entorno de desarrollo puede incluir:

- resaltado de sintaxis;
- autocompletado;
- ejecución de programas;
- depuración paso a paso;
- explorador de archivos;
- integración con Git;
- extensiones.

| Herramienta | Uso habitual |
| --- | --- |
| Thonny | Entorno sencillo para empezar |
| Visual Studio Code | Editor profesional, flexible y extensible |
| PyCharm | IDE especializado en Python |
| Jupyter Notebook | Cuadernos con texto, código y resultados |
| Anaconda | Distribución utilizada especialmente en ciencia de datos |

En el módulo se utiliza principalmente **VS Code**, porque permite trabajar con Python, terminal, Git, extensiones y repositorios en un entorno parecido al profesional.

## Comprobar Python

Desde una terminal:

```bash
python --version
```

En sistemas donde el comando es `python3`:

```bash
python3 --version
```

Si aparece una versión de Python, el intérprete está disponible.

## Ejecutar un archivo `.py`

Si tenemos `programa.py`:

```bash
python programa.py
```

O, según el sistema:

```bash
python3 programa.py
```

También puede ejecutarse desde VS Code. El editor sirve para escribir el archivo; **el intérprete de Python es quien ejecuta el código**.

## Extensiones útiles de VS Code

El material de clase destaca:

- Python;
- Pylance;
- Ruff;
- extensiones para Markdown.

No hace falta dominar todas desde el principio. Lo esencial es saber crear un `.py`, ejecutarlo y leer los errores.

## Entornos virtuales

Un entorno virtual permite aislar las librerías de un proyecto de las de otros proyectos.

Crear uno:

```bash
python -m venv .venv
```

Activarlo en Linux/macOS:

```bash
source .venv/bin/activate
```

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Cuando está activo, los paquetes instalados quedan asociados a ese entorno.

!!! note "No confundas"
    Un entorno virtual de Python **no es una máquina virtual**. Su objetivo es separar intérprete/dependencias del proyecto, no virtualizar un sistema operativo completo.

## `pip`, `uv` y `pyenv`

`pip` es la herramienta clásica para instalar paquetes:

```bash
pip install requests
```

Una forma útil de asegurarte de que utilizas el `pip` asociado al Python actual es:

```bash
python -m pip install requests
```

El temario también presenta otras herramientas que debes reconocer:

- **uv**: gestión rápida de paquetes y entornos;
- **pyenv**: permite gestionar distintas versiones de Python;
- **pyenv-virtualenv**: combina versiones y entornos virtuales;
- **Anaconda**: distribución con muchas herramientas científicas preinstaladas.

No es necesario dominar estas herramientas ahora: debes saber **para qué sirven**.

## Depuración

Depurar significa ejecutar y observar un programa para entender qué ocurre.

En VS Code puedes colocar un **breakpoint** o punto de interrupción. Cuando la ejecución se detiene puedes observar:

- **VARIABLES**: valores existentes en ese momento;
- **WATCH**: expresiones que quieres vigilar.

El resaltado durante la depuración suele indicar la **siguiente línea que se ejecutará**.

También existe `pdb`:

```python
import pdb

nombre = "Ana"
pdb.set_trace()
print(nombre)
```

En este nivel basta con reconocer que depurar es observar el programa paso a paso, no cambiar cosas al azar hasta que funcione.

## Jupyter Notebook

Jupyter permite mezclar en un mismo documento:

- texto;
- código;
- resultados;
- gráficos;
- explicaciones.

Es muy útil en análisis de datos y enseñanza. En el módulo se priorizan archivos `.py` para practicar un flujo de desarrollo convencional.

## Entornos online

El material también menciona plataformas como Replit, que permiten programar desde el navegador. Son útiles para pruebas rápidas, aunque el entorno principal del módulo es local con VS Code.

## Organización del proyecto

Una estructura sencilla puede ser:

```text
mi-proyecto-python/
├── README.md
├── ejercicios/
│   ├── ejercicio_01.py
│   └── ejercicio_02.py
└── pruebas/
```

Organizar los archivos desde el principio evita terminar con decenas de scripts mezclados sin saber para qué sirve cada uno.

## Ejemplo práctico

```bash
mkdir practica-python
cd practica-python
python3 -m venv .venv
source .venv/bin/activate
python --version
```

Después creamos `hola.py`:

```python
print("Entorno preparado")
```

Y ejecutamos:

```bash
python hola.py
```

## Comprueba que sabes...

- Explicar qué es un entorno de desarrollo.
- Diferenciar editor, IDE, terminal e intérprete.
- Reconocer VS Code, Thonny, PyCharm, Jupyter y Anaconda.
- Comprobar la versión de Python.
- Ejecutar un archivo `.py`.
- Explicar para qué sirve un entorno virtual.
- Saber que `pip` instala paquetes.
- Reconocer `uv`, `pyenv` y `pdb`.
- Explicar qué es un breakpoint y para qué sirven VARIABLES y WATCH.

!!! success "Para el examen"
    Recuerda especialmente la diferencia entre **escribir código** (editor), **ejecutarlo** (intérprete) y **aislar dependencias** (entorno virtual).

---

Fuente principal: material de clase **Introducción a Python 1.2 · Entorno de desarrollo: Python, VS Code y herramientas básicas**, consultado el 29/10/2026. Las aclaraciones prácticas están señaladas dentro del desarrollo del mismo contenido.