# UT3 · 3. Bibliotecas para administración de sistemas

## Importar una herramienta, no memorizar un catálogo

La biblioteca estándar ya viene con Python. `import sys` permite acceder con el prefijo `sys.`; `from pathlib import Path` importa directamente el nombre `Path`. Un nombre de archivo como `random.py` o `sys.py` en tu proyecto puede causar confusiones con imports: utiliza nombres propios.

| Módulo | Qué consultas o haces |
| --- | --- |
| sys | `argv`, `version`, `platform`, `exit` |
| os | Entorno con `getenv`, directorio con `getcwd`, contenido con `listdir` |
| platform | `system`, `release`, `processor` |
| datetime | Fechas, horas, diferencias y formato |
| pathlib | Construcción de rutas y propiedades de los archivos |
| shutil | Copias, movimientos y uso del disco |
| random / time | Simulaciones aleatorias / pausas |

## Ejemplo resuelto: calendario de calibración

**Problema propio:** a partir de una fecha fija, preparar tres fechas de revisión cada dos días. Utilizar una fecha fija permite comprobar el resultado sin depender del día en que ejecutes el código.

```python
from datetime import date, timedelta
inicio = date(2026, 10, 26)
for numero in range(3):
    revision = inicio + timedelta(days=numero * 2)
    print(f"R{numero + 1:02d} | {revision:%d/%m/%Y}")
```

**Resultado esperado:**

```text
R01 | 26/10/2026
R02 | 28/10/2026
R03 | 30/10/2026
```

`timedelta` representa una duración y sabe atravesar cambios de mes. `%d`, `%m` y `%Y` formatean día, mes y año. `date.today()` y `datetime.now()` consultan el reloj; `weekday()` numera el lunes como 0 y el domingo como 6. Una fecha/hora sin zona no incorpora automáticamente las reglas de otra zona horaria.

## Ejemplo resuelto: resumen de documentos Markdown

**Objetivo propio:** leer una carpeta pasada como argumento y sumar el tamaño de los archivos `.md` inmediatos. No modifica el contenido.

Guarda `documentos.py`:

```python
import sys
from pathlib import Path

if len(sys.argv) != 2:
    print("Uso: python documentos.py carpeta")
    sys.exit(1)

carpeta = Path(sys.argv[1])
if not carpeta.is_dir():
    print("Debes indicar una carpeta existente")
    sys.exit(2)

cantidad = 0
bytes_total = 0
for ruta in sorted(carpeta.iterdir()):
    if ruta.is_file() and ruta.suffix.lower() == ".md":
        cantidad += 1
        bytes_total += ruta.stat().st_size
        print(ruta.name)
print(f"Documentos: {cantidad}; bytes: {bytes_total}")
```

`sys.argv[0]` es el script y `[1]` la carpeta. `Path` representa una ruta; `/` combina componentes sin concatenar separadores manualmente. `iterdir()` recorre el nivel inmediato y `stat().st_size` consulta bytes. El orden se hace explícito con `sorted`.

**Prueba controlada:** crea una carpeta con `a.md` de tres bytes (`abc`) y `b.md` de dos bytes (`xy`), sin saltos finales, y un `imagen.txt` cualquiera. La salida enumera `a.md`, `b.md` y termina con `Documentos: 2; bytes: 5`. El tamaño en bytes no siempre coincide con el número de caracteres en UTF-8.

## Rutas y operaciones que necesitan atención

`Path.cwd()` consulta el directorio actual; `exists`, `is_file` e `is_dir` comprueban; `parent`, `name` y `suffix` describen la ruta. `mkdir(parents=True, exist_ok=True)` crea carpetas intermedias y tolera una carpeta ya existente. `glob('*.md')` busca en el nivel actual y `rglob('*.md')` lo hace recursivamente. `rename` puede mover o sustituir según el sistema; `rmdir` solo elimina un directorio vacío.

`shutil.copy` copia archivos y puede sobrescribir; `move` los mueve; `rmtree` elimina un árbol completo. Antes de utilizarlas, define origen, destino y qué harás si ya existe. `shutil.disk_usage(Path.cwd())` devuelve total, usado y libre en bytes para el sistema de archivos correspondiente; no todas las plataformas comparten una ruta como `/`.

`os.getenv('NOMBRE', 'alternativa')` consulta una variable de entorno. `platform.system()` puede devolver `Linux`, `Windows` o `Darwin`; `processor()` puede devolver texto vacío. No deduzcas el gestor de paquetes exacto solo del nombre Linux: hay distribuciones diferentes.

`random.randint(1, 6)` simula un dado; `time.sleep(0.1)` pausa el proceso. No necesitas esperar minutos reales para probar un bucle: utiliza datos fijos y pausas cortas durante el laboratorio.

## Errores típicos

| Síntoma | Revisión |
| --- | --- |
| No encuentra la carpeta | El punto de partida de las rutas relativas es el directorio de trabajo. |
| El tamaño difiere del previsto | Bytes, saltos de línea y codificación del archivo. |
| Falla `stat()` pese a la comprobación | Permisos o cambios del archivo entre comprobar y leer. |
| No incluye subcarpetas | `iterdir` no es un recorrido recursivo. |

!!! success "Para repasar"
    Elige el módulo según la tarea, consulta el tipo que devuelve cada operación y prueba primero con un conjunto pequeño de archivos conocidos.

---

Fuentes del temario: [05-librerias-sysadmin](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/05-librerias-sysadmin/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
