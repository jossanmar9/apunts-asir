# UT1 · 1. Programar y preparar el entorno

## Programar es concretar una secuencia

Un programa expresa pasos sin ambigüedades. Antes del código, define qué entra, qué hay que transformar y qué debe salir. Python es un lenguaje de alto nivel: permite representar esos pasos sin escribir directamente instrucciones de la CPU.

En el uso habitual con CPython, el código fuente `.py` se transforma en bytecode y se ejecuta en la máquina virtual de Python. El editor donde escribes no es el intérprete que ejecuta. Un comentario con `#` explica el motivo de una decisión; Python no lo ejecuta.

## Qué necesitas para escribir y ejecutar tu primer programa

Necesitas un lugar donde escribir el código y un programa que lo ejecute. El editor guarda texto en un archivo; el intérprete de Python entiende ese texto como instrucciones. Puedes cambiar de editor sin cambiar el lenguaje, y puedes abrir un `.py` sin que eso signifique que se esté ejecutando.

El terminal permite pedir la ejecución escribiendo un comando. Si estás en la carpeta del archivo, `python3 audio.py` indica qué intérprete y qué archivo utilizar. Si el sistema tiene otro nombre de comando, compruébalo con la opción `--version`; no confundas un comando que falta con un fallo dentro de tu programa.

La consola interactiva sirve para probar expresiones pequeñas. Al escribir `python3` sin archivo aparece normalmente `>>>`. Ese signo indica que espera una instrucción; no forma parte del código que debes guardar. Una expresión puede mostrar su resultado automáticamente en esa consola, mientras en un archivo utilizarás `print` para presentarlo.

## Qué significa ejecutar de arriba abajo

Python empieza por las instrucciones que corresponden al programa y va evaluándolas en orden. Si una línea necesita una variable que todavía no has definido, no la busca automáticamente más abajo para adivinar lo que querías hacer.

```python
cantidad = 3
print(cantidad)
cantidad = 5
print(cantidad)
```

El resultado son dos líneas: 3 y 5. La primera impresión utiliza el valor de ese momento. Cambiarlo después no reescribe lo que ya apareció en pantalla. Esta idea sencilla es la base para seguir programas con decisiones y bucles.

Un comentario explica el código a las personas. No se ejecuta y no arregla una instrucción incorrecta. Es más útil escribir por qué una estimación supone un ritmo constante que repetir «divide dos números» encima de una división visible.

## Los errores de escritura también tienen una explicación

Python distingue mayúsculas: `print` es un nombre y `Print` otro. Las cadenas necesitan comillas para distinguir un texto literal del nombre de una variable. Al escribir `print("cantidad")` muestras la palabra; al escribir `print(cantidad)` muestras su valor.

Los bloques se delimitan con indentación. Tras una línea que abre bloque con `:`, las instrucciones interiores llevan un nivel adicional, normalmente cuatro espacios. No se trata de decorar el código: indica a qué estructura pertenece cada instrucción. Evita mezclar espacios y tabuladores.

## Por qué preparar un entorno virtual

Distintos proyectos pueden necesitar paquetes distintos. Instalar todo junto dificulta saber qué necesita cada uno y puede producir incompatibilidades. Un entorno virtual crea un lugar separado para los paquetes del proyecto; no instala un sistema operativo completo ni requiere otra máquina.

La creación de `.venv` se hace una vez para ese entorno. La activación modifica el entorno del terminal actual para utilizar sus herramientas. Al cerrar el terminal, en una sesión nueva tendrás que activarlo otra vez o seleccionar directamente su intérprete.

`python -m pip` ejecuta el instalador asociado a ese Python. Esta forma reduce la confusión entre el intérprete que ejecuta y el que recibe los paquetes. Si un editor utiliza otro Python, puede no ver lo que acabas de instalar: revisa su selección antes de reinstalar lo mismo varias veces.

## Cómo aprovechar el depurador al estudiar

Pon una pausa antes de una operación y mira los valores disponibles. Avanza una línea y explica qué cambió. El objetivo no es pulsar botones hasta que termine: es relacionar la instrucción con su efecto.

Si todavía no se ha ejecutado una asignación, su variable puede no existir. Si una línea no modifica un valor, no esperes que cambie solo por avanzar. Con programas pequeños puedes hacer lo mismo en papel y comparar después tu tabla con lo que muestra el depurador.

## Problema explicado paso a paso: estimar una lectura de audio

Una grabación contiene 840 palabras y se lee a 140 palabras por minuto. Queremos estimar su duración.

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

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Intérprete** | Programa que procesa y ejecuta el código Python. |
| **Bytecode** | Representación intermedia que utiliza habitualmente CPython al ejecutar el código. |
| **Entorno virtual** | Conjunto aislado de intérprete y paquetes de un proyecto, sin virtualizar una máquina completa. |
| **Cmdlet** | Comando propio de PowerShell, como `Get-Command`. |
| **Política de ejecución** | Configuración de PowerShell que afecta a la ejecución de scripts; puede afectar a la activación de un entorno. |

!!! success "Para repasar"
    Explica entrada, transformación y salida antes del código. Después identifica qué programa edita y qué programa ejecuta.

---

Fuentes del temario: [01-introduccion-python](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/01-introduccion-python/), [02-entorno-vscode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/02-entorno-vscode/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
