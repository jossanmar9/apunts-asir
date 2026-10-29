# UT3 · 3.5 Librerías útiles para administradores de sistemas

## De los ejercicios a pequeños scripts de administración

Python incluye una biblioteca estándar amplia. Muchas herramientas ya vienen con Python y podemos utilizarlas mediante `import`.

```python
import platform

print(platform.system())
```

El objetivo de este tema no es memorizar todas las funciones, sino saber qué librerías existen, importarlas, entender ejemplos sencillos y consultar documentación cuando sea necesario.

!!! note "Forma de importar utilizada en estos apuntes"
    Para mantener una forma consistente y fácil de reconocer utilizaremos normalmente `import modulo`, por ejemplo `import datetime` y `import pathlib`. El material de clase también muestra importaciones concretas como `from pathlib import Path`; ambas formas existen, pero aquí priorizamos la primera.

## `sys`: intérprete y argumentos

`sys` permite consultar información del intérprete y trabajar con los argumentos con los que se ha iniciado un script.

```python
import sys

print(sys.version)
print(sys.platform)
```

Elementos importantes del temario:

- `sys.version`: versión de Python.
- `sys.platform`: plataforma.
- `sys.exit()`: termina el programa.
- `sys.argv`: argumentos recibidos en la línea de comandos.

### Argumentos de un script

```python
import sys

if len(sys.argv) < 2:
    print("Uso: python saluda.py nombre")
else:
    print(f"Hola, {sys.argv[1]}")
```

Ejecución:

```bash
python saluda.py Ana
```

`sys.argv[0]` contiene el nombre del script y `sys.argv[1]` el primer argumento.

## `os`: sistema operativo y variables de entorno

El temario presenta `os` para interactuar con el sistema operativo.

```python
import os

print(os.getcwd())
print(os.listdir("."))
print(os.getenv("PATH"))
```

También dispone de operaciones como `os.mkdir()`. Para trabajar con rutas y directorios, el propio material recomienda utilizar normalmente `pathlib`, que ofrece una interfaz más moderna.

## `datetime`: fechas y horas

Utilizaremos el módulo completo:

```python
import datetime

ahora = datetime.datetime.now()
print(ahora)
```

La fecha actual puede obtenerse con:

```python
import datetime

hoy = datetime.date.today()
print(hoy)
```

### Sumar o restar tiempo

```python
import datetime

hoy = datetime.datetime.now()
ayer = hoy - datetime.timedelta(days=1)
print(ayer)
```

### `strftime()`

Permite dar formato a una fecha:

```python
import datetime

hoy = datetime.datetime.now()
print(hoy.strftime("%Y-%m-%d"))
```

Podemos crear un nombre de copia de seguridad:

```python
import datetime

hoy = datetime.datetime.now()
nombre_backup = f"backup_{hoy.strftime('%Y_%m_%d')}.zip"
print(nombre_backup)
```

### Hora y día de la semana

```python
import datetime

hora = datetime.datetime.now().hour

if hora < 14:
    print("Buenos días")
else:
    print("Buenas tardes")
```

```python
import datetime

dia = datetime.datetime.now().weekday()
print(dia)
```

`weekday()` devuelve `0` para lunes y `6` para domingo.

## `platform`: información del sistema

```python
import platform

print("Sistema operativo:", platform.system())
print("Versión:", platform.release())
print("Procesador:", platform.processor())
```

Podemos combinarlo con condicionales:

```python
import platform

if platform.system() == "Windows":
    print("Configurando entorno para Windows...")
```

## `pathlib`: rutas de forma moderna

`pathlib` permite trabajar con rutas mediante objetos `Path`.

```python
import pathlib

ruta = pathlib.Path.cwd()
print(ruta)
```

Operaciones y propiedades que aparecen en el material:

| Elemento | Uso |
| --- | --- |
| `Path.cwd()` | directorio actual |
| `iterdir()` | recorrer elementos de un directorio |
| `exists()` | comprobar si existe |
| `is_dir()` | comprobar si es directorio |
| `is_file()` | comprobar si es archivo |
| `mkdir()` | crear directorio |
| `rmdir()` | eliminar directorio |
| `rename()` | renombrar |
| `stat()` | consultar información de la ruta |
| `suffix` | extensión final |
| `parent` | ruta padre |

### Construir rutas

```python
import pathlib

ruta = pathlib.Path.cwd()
carpeta = ruta / "ejercicios"

if not carpeta.exists():
    carpeta.mkdir()
    print("Carpeta creada")
else:
    print("La carpeta ya existe")
```

El operador `/` permite construir una ruta a partir de sus partes.

### Crear carpetas anidadas

```python
import pathlib

ruta = pathlib.Path("backups") / "2026" / "10" / "dia_29"
ruta.mkdir(parents=True, exist_ok=True)
print(ruta)
```

- `parents=True` crea los directorios intermedios necesarios.
- `exist_ok=True` evita un error si la carpeta ya existe.

### Consultar información de un archivo

```python
import pathlib

archivo = pathlib.Path("informe.log")

if archivo.exists():
    datos = archivo.stat()
    print(datos.st_size)
    print(datos.st_mtime)
```

### Recorrer una carpeta

```python
import pathlib

for elemento in pathlib.Path(".").iterdir():
    print(elemento.name)
```

### Filtrar por extensión

```python
import pathlib

for archivo in pathlib.Path(".").iterdir():
    if archivo.is_file() and archivo.suffix == ".py":
        print(archivo.name)
```

Aquí se combinan objetos, métodos, `for` y `if`.

## `shutil`: operaciones de alto nivel con archivos

El material introduce `shutil` para copiar, mover o eliminar archivos y carpetas y consultar el uso de disco.

```python
import shutil
```

Funciones destacadas:

- `shutil.copy(origen, destino)`.
- `shutil.move(origen, destino)`.
- `shutil.rmtree(carpeta)`.
- `shutil.disk_usage(ruta)`.

### Copiar un archivo

```python
import pathlib
import shutil

origen = pathlib.Path("backup.zip")
destino = pathlib.Path("copias") / "backup.zip"

destino.parent.mkdir(exist_ok=True)

if origen.exists():
    shutil.copy(origen, destino)
    print("Backup copiado")
```

### Uso de disco

```python
import shutil

total, usado, libre = shutil.disk_usage("/")
porcentaje = usado / total * 100
print(f"Uso: {porcentaje:.2f}%")
```

`total`, `usado` y `libre` están expresados en bytes.

## `random` y `time`

El temario también utiliza estas librerías en algunos ejercicios:

```python
import random
import time

numero = random.randint(1, 100)
simbolo = random.choice("!#$%&*")

print(numero)
print(simbolo)
time.sleep(1)
```

- `random.randint(a, b)` devuelve un entero entre ambos límites.
- `random.choice(secuencia)` selecciona un elemento.
- `time.sleep(segundos)` pausa la ejecución.

## `zfill()` para numeración

Aunque no es una librería, el tema recuerda `zfill()` para generar nombres numerados:

```python
for numero in range(1, 4):
    print(str(numero).zfill(2))
```

Salida:

```text
01
02
03
```

## `glob()` y `rglob()`

`pathlib` permite buscar archivos mediante patrones.

```python
import pathlib

for archivo in pathlib.Path(".").glob("*.py"):
    print(archivo.name)
```

Busca archivos `.py` en la carpeta actual.

Para una búsqueda recursiva:

```python
import pathlib

for archivo in pathlib.Path(".").rglob("*.log"):
    print(archivo)
```

## Ejemplo integrador

El ejemplo final combina conceptos de toda la unidad:

```python
import datetime
import pathlib
import platform

print(f"Sistema: {platform.system()}")
print(f"Fecha: {datetime.datetime.now():%Y-%m-%d}")

carpeta = pathlib.Path(".")
contador_py = 0

for archivo in carpeta.iterdir():
    if archivo.is_file() and archivo.suffix == ".py":
        contador_py += 1

print(f"Archivos Python encontrados: {contador_py}")
```

Aquí aparecen:

- variables;
- condicionales;
- bucles;
- librerías;
- rutas;
- f-strings.

## Qué debes memorizar y qué no

El material indica expresamente que **no tienes que memorizar todas las funciones de estas librerías**. Lo importante es:

- saber que existen;
- saber importarlas;
- saber utilizarlas;
- reconocer ejemplos;
- consultar documentación;
- adaptar código sencillo;
- entender qué hace tu script.

## Comprueba que sabes...

- Utilizar `import modulo`.
- Consultar `sys.version`, `sys.platform` y `sys.argv`.
- Entender para qué sirve `sys.exit()`.
- Consultar una variable de entorno con `os.getenv()`.
- Obtener fecha y hora con `datetime`.
- Utilizar `timedelta` y `strftime()`.
- Consultar información básica con `platform`.
- Crear y combinar rutas con `pathlib.Path`.
- Utilizar `exists()`, `is_file()`, `is_dir()` e `iterdir()`.
- Consultar `suffix`, `parent` y `stat()`.
- Crear directorios con `mkdir()`.
- Utilizar `shutil.copy()` y `shutil.disk_usage()`.
- Reconocer `random.randint()`, `random.choice()` y `time.sleep()`.
- Buscar archivos con `glob()` y `rglob()`.
- Combinar librerías con condicionales y bucles.

!!! success "Para el examen"
    No intentes memorizar la biblioteca estándar completa. Aprende a reconocer **qué módulo resuelve cada tipo de problema** y practica pequeños scripts que combinen `if`, `for` y rutas.

---

Fuente principal: material de clase **Introducción a Python 3.5 · Librerías útiles para administradores de sistemas**.