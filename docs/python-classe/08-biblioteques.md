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

## Para qué sirve importar un módulo

Un módulo reúne código que puedes reutilizar. `import pathlib` da acceso a sus nombres con el prefijo, como `pathlib.Path`. `from pathlib import Path` permite usar directamente `Path`. No son dos bibliotecas distintas ni necesitas instalar una de ellas por usar otra forma de importación.

La biblioteca estándar se distribuye con Python e incluye las herramientas que utilizamos aquí. Otras bibliotecas externas requieren instalación. Antes de ejecutar `pip`, comprueba cuál es el caso y qué intérprete está activo.

Evita que tu archivo tenga el mismo nombre que un módulo que quieres importar. Un `random.py` dentro del proyecto puede interferir con la búsqueda de módulos y dar mensajes desconcertantes. Cambiar el contenido de la biblioteca no es lo primero que debes intentar ante ese problema.

## Construir una ruta es distinto de abrir un archivo

`Path('fichas') / 'azul.txt'` representa una ruta. Crear ese objeto no crea automáticamente la carpeta ni el archivo. Después puedes preguntar si existe, si es archivo o directorio, o intentar una operación con ella.

Una ruta relativa parte del directorio de trabajo del proceso. Si ejecutas el mismo script desde otra carpeta, puede referirse a otro lugar. Por eso conviene observar `Path.cwd()` cuando no encuentras lo que esperabas. La carpeta donde está guardado el script y el directorio desde el que se ejecuta no son necesariamente el mismo.

`name`, `parent` y `suffix` describen partes de la ruta. `is_file()` consulta si corresponde a un archivo; `stat()` obtiene información del recurso. Una propiedad del nombre no demuestra que el recurso exista: puedes preguntar el sufijo de una ruta que todavía no se ha creado.

## Recorrer el nivel actual o recorrer subcarpetas

`iterdir()` enumera las entradas inmediatas. No baja automáticamente por todas las carpetas. `glob` permite seleccionar con un patrón y `rglob` realiza una búsqueda recursiva con el patrón indicado.

Al recorrer, comprueba si cada entrada es del tipo que necesitas. Una carpeta también tiene nombre y puede terminar en un texto parecido a una extensión; no debes sumar su tamaño como si fuera uno de los documentos del informe.

No dependas del orden que encuentres al listar para explicar una salida exacta. Si el ejercicio necesita un orden concreto, aplica `sorted` u otra regla explícita. Así la presentación tiene un criterio que puedes justificar.

## Leer texto y entender cuándo se cierra

Abrir un archivo crea un recurso que necesita cerrarse. `with` delimita el trabajo con él y realiza el cierre al salir del bloque. Dentro puedes recorrer líneas, leer todo el texto o escribir según el modo elegido.

El modo `r` lee, `w` crea o sustituye contenido y `a` añade al final. Elegir mal el modo puede borrar datos aunque el programa no dé ninguna excepción. Expresa la codificación, por ejemplo `encoding='utf-8'`, para no depender de una interpretación distinta entre equipos.

Un salto de línea puede formar parte del texto leído. `strip()` lo elimina, pero también elimina otros espacios de los extremos. Si esos espacios tienen significado en tu formato, utiliza una operación más específica en lugar de limpiar por costumbre.

## Copiar no es lo mismo que mover

Copiar deja el origen y crea o sustituye un destino; mover cambia la ubicación o el nombre del recurso. Antes de operar, decide qué pasa si el destino existe y qué debe conservarse. Una comprobación previa no garantiza que nada cambie entre comprobar y actuar, así que las operaciones aún pueden fallar.

Para estudiar estas funciones, utiliza una carpeta pequeña de laboratorio. Es más fácil justificar qué ocurrió con dos archivos conocidos que con un árbol grande cuyo estado inicial no has revisado. Las funciones que eliminan árboles no son necesarias para aprender a construir una ruta.

## Fechas: separar el dato del texto que lo representa

Una fecha no es simplemente una cadena como `27/10/2026`. El objeto permite hacer operaciones de calendario; el formato decide cómo mostrarlo. `timedelta` expresa una duración y evita calcular cambios de mes con restas manuales de números.

El calendario del ejemplo empieza en una fecha fijada para que puedas seguir sus tres resultados a mano. Al usar `today()` o `now()`, el punto de partida procede del reloj y la salida varía. Debes distinguir qué es una diferencia esperable por la fecha del sistema y qué sería un error de tu fórmula.

## Problema explicado paso a paso: calendario de calibración

A partir de una fecha fija, preparar tres fechas de revisión cada dos días. Utilizar una fecha fija permite comprobar el resultado sin depender del día en que ejecutes el código.

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

## Problema explicado paso a paso: resumen de documentos Markdown

Leer una carpeta pasada como argumento y sumar el tamaño de los archivos `.md` inmediatos. No modifica el contenido.

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

## Leer y escribir un archivo con cierre automático

```python
from pathlib import Path
ruta = Path("nota-laboratorio.txt")
with ruta.open("w", encoding="utf-8") as archivo:
    archivo.write("Vitrina revisada\n")
with ruta.open(encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())
```

Se crea o sobrescribe `nota-laboratorio.txt` y se muestra `Vitrina revisada`. `with` garantiza el cierre al salir del bloque, incluso si aparece una excepción. El modo `w` sustituye el contenido; `a` añade. Practica con una ruta de laboratorio, no con un archivo que necesites conservar.

## Argumentos con ayuda automática

Como ampliación de `sys.argv`, `argparse` define opciones y genera `-h`:

```python
import argparse
parser = argparse.ArgumentParser(description="Configura un informe de prueba")
parser.add_argument("carpeta")
parser.add_argument("--limite", type=int, default=3)
args = parser.parse_args()
print(f"Carpeta: {args.carpeta}; límite: {args.limite}")
```

Guárdalo como `opciones.py`. `python opciones.py fichas --limite 5` muestra `Carpeta: fichas; límite: 5`. `--limite muchas` produce un error de argumentos. El programa aún no inspecciona la carpeta: solo demuestra cómo interpretar la llamada.

Para ejecutar otro programa, `subprocess.run` acepta una lista con el comando y cada argumento por separado. `capture_output=True` captura stdout y stderr, `text=True` devuelve texto y `returncode` permite revisar el estado. Evita construir una orden de shell concatenando datos externos. El módulo `re` proporciona `search`, `findall` y patrones compilados; recuerda diferenciar una coincidencia de formato de una validación completa del dato.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Construye una ruta sin crear archivos

Construye con `Path` la ruta relativa `material/sonidos/aviso.wav`. Muestra por separado su nombre, su sufijo y el nombre de su carpeta padre. El programa debe funcionar aunque esa ruta todavía no exista.

??? tip "Pista"
    Construir una ruta y consultar sus componentes no exige abrir el recurso.

??? success "Solución paso a paso"
    ```python
    from pathlib import Path
    ruta = Path("material") / "sonidos" / "aviso.wav"
    print(ruta.name)
    print(ruta.suffix)
    print(ruta.parent.name)
    ```

    Las salidas son `aviso.wav`, `.wav` y `sonidos`. No se ha creado ninguna carpeta ni comprobado que exista el archivo: solo se han interpretado componentes de su dirección.

### 2. Calcula una devolución con calendario

Una herramienta se presta el 30 de abril de 2026 durante tres días. Calcula con `date` y `timedelta` la fecha de devolución y muéstrala como día/mes/año. No calcules el cambio de mes manualmente.

??? tip "Pista"
    Suma una duración al objeto de fecha, no al texto que lo representa.

??? success "Solución paso a paso"
    ```python
    from datetime import date, timedelta
    prestamo = date(2026, 4, 30)
    devolucion = prestamo + timedelta(days=3)
    print(f"Devolución: {devolucion:%d/%m/%Y}")
    ```

    La salida es `Devolución: 03/05/2026`. El objeto de calendario realiza el cambio de mes y el formato decide cómo presentarlo.

### 3. Lee una lista sin perder su orden

Crea `recordatorios.txt` en una carpeta de pruebas con dos líneas: `revisar batería` y `guardar cables`. Léelo con `with`, numera las líneas desde 1 y muestra cada recordatorio sin añadir líneas vacías entre ellos. No escribas los recordatorios dentro del programa lector.

??? tip "Pista"
    El archivo se cierra al salir de `with`; `enumerate` permite numerar el recorrido.

??? success "Solución paso a paso"
    ```python
    from pathlib import Path
    ruta = Path("recordatorios.txt")
    with ruta.open(encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, start=1):
            print(f"{numero}. {linea.rstrip()}")
    ```

    Se muestran `1. revisar batería` y `2. guardar cables`. `rstrip` elimina el salto ya leído antes de que `print` añada el suyo. En este formato no se necesitan espacios al final de las notas.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Módulo y biblioteca** | Unidad importable de código y conjunto de herramientas; una biblioteca puede contener varios módulos. |
| **Ruta y sistema de archivos** | Dirección de un recurso y organización en la que se guarda. |
| **CSV y JSON** | Representaciones de datos tabulares y estructurados; requieren lectores adecuados a cada formato. |
| **Gestor de contexto** | Objeto usado con `with` para gestionar entrada, salida y liberación de recursos. |

!!! success "Para repasar"
    Elige el módulo según la tarea, consulta el tipo que devuelve cada operación y prueba primero con un conjunto pequeño de archivos conocidos.

---

Fuentes del temario: [05-librerias-sysadmin](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/05-librerias-sysadmin/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
