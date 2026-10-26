# UT1 · 1. Programar y preparar el entorno

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Intérprete** | Programa que procesa y ejecuta el código Python. |
| **Bytecode** | Representación intermedia que utiliza habitualmente CPython al ejecutar el código. |
| **Entorno virtual** | Conjunto aislado de intérprete y paquetes de un proyecto, sin virtualizar una máquina completa. |
| **Cmdlet** | Comando propio de PowerShell, como `Get-Command`. |
| **Política de ejecución** | Configuración de PowerShell que afecta a la ejecución de scripts; puede afectar a la activación de un entorno. |

## Programar es concretar una secuencia

Un programa expresa pasos sin ambigüedades. Antes del código, define qué entra, qué hay que transformar y qué debe salir. Python es un lenguaje de alto nivel: permite representar esos pasos sin escribir directamente instrucciones de la CPU.

En el uso habitual con CPython, el código fuente `.py` se transforma en bytecode y se ejecuta en la máquina virtual de Python. El editor donde escribes no es el intérprete que ejecuta. Un comentario con `#` explica el motivo de una decisión; Python no lo ejecuta.

## Ejemplo resuelto: estimar una lectura de audio

**Problema propio:** una grabación contiene 840 palabras y se lee a 140 palabras por minuto. Queremos estimar su duración.

1. Entrada: cantidad de palabras y ritmo de lectura.
2. Transformación: dividir palabras entre palabras por minuto.
3. Salida: duración estimada en minutos.

Guarda `audio.py`:

```python
palabras = 840
ritmo = 140
# Suponemos un ritmo constante, sin pausas adicionales.
minutos = palabras / ritmo
print(f"Duración estimada: {minutos:.1f} minutos")
```

Ejecuta `python3 audio.py` en Linux o `py audio.py` en un Windows con el lanzador instalado. **Resultado esperado:** `Duración estimada: 6.0 minutos`. Si duplicas las palabras y mantienes el ritmo, la duración también se duplica. Es una comprobación de sentido, además de comprobar que el programa no falla.

## Entorno de trabajo paso a paso

En Linux, dentro de una carpeta nueva:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python audio.py
python -m pip --version
deactivate
```

En PowerShell, la activación correspondiente es `.\.venv\Scripts\Activate.ps1`. Puede estar condicionada por la política de ejecución de tu equipo. En VS Code selecciona el intérprete del proyecto con **Python: Select Interpreter**. Si el terminal funciona y el botón de ejecución no, comprueba que ambos utilizan el mismo intérprete.

Un entorno virtual aísla paquetes del proyecto, pero no es una máquina virtual. `python -m pip install NOMBRE_PAQUETE` instala con el Python que has elegido; no necesitas instalar nada para los ejemplos de esta sección, que utilizan la biblioteca estándar.

## ¿Qué es cada herramienta?

| Herramienta | Función |
| --- | --- |
| VS Code | Editor ampliable con ejecución y depuración |
| Thonny / PyCharm | Entornos de desarrollo de Python con distintos enfoques |
| Jupyter | Cuadernos con texto, código y resultados |
| Anaconda | Distribución y herramientas muy utilizadas en trabajo científico |
| pip | Instalación de paquetes |
| uv | Herramienta alternativa para gestionar proyectos, paquetes y entornos |
| pyenv | Gestión de versiones de Python |
| pdb | Depurador de terminal |

## Depurar es observar

Pon un punto de interrupción en `minutos = ...` y ejecuta el depurador. Antes de la línea, existen `palabras` y `ritmo`; después, también `minutos`. El resaltado suele indicar la próxima instrucción, no una instrucción ya ejecutada. Mira VARIABLES y vigila `palabras / ritmo` en WATCH.

| Error | Revisión |
| --- | --- |
| No se encuentra `audio.py` | Carpeta de trabajo y nombre del archivo. |
| `NameError` con `Print` | Python distingue mayúsculas; es `print`. |
| Paquete instalado pero no importable | Intérprete del editor y del terminal. |

## Consola interactiva, archivo y directorio de trabajo

`python3` sin un archivo abre normalmente la consola interactiva: escribes una expresión y ves su resultado. `python3 audio.py` ejecuta un archivo. No copies el prompt `>>>` dentro del programa: es la marca de la consola, no código Python.

El directorio de trabajo es la carpeta desde la que se resuelven las rutas relativas. Abrir un archivo en el editor no cambia necesariamente el directorio del terminal. Esto explica muchos errores de «archivo no encontrado».

En Windows, PowerShell es una shell cuyos comandos propios se llaman cmdlets, como `Get-Command`. Su política de ejecución puede afectar al script de activación del entorno virtual; no es un sistema que sustituya a los permisos ni al control de seguridad del equipo. Si no puedes activar el entorno, puedes seleccionar directamente su intérprete en VS Code o ejecutar `.\.venv\Scripts\python.exe audio.py`.

!!! success "Para repasar"
    Explica entrada, transformación y salida antes del código. Después identifica qué programa edita y qué programa ejecuta.

---

Fuentes del temario: [01-introduccion-python](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/01-introduccion-python/), [02-entorno-vscode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/02-entorno-vscode/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
