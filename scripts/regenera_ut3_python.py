"""Regenera los 50 ejercicios de Python UT3 ajustados al temario 3.1–3.5."""
from pathlib import Path

UT3 = [
("Control de acceso por edad", "Pide una edad y muestra ACCESO si es mayor o igual que 18; en caso contrario, DENEGADO."),
("Estado de temperatura", "Pide una temperatura y clasifícala como BAJO CERO, CERO o SOBRE CERO."),
("Puerto web", "Pide un puerto y muestra WEB si es 80 o 443, SSH si es 22 y OTRO en cualquier otro caso."),
("Espacio de disco", "Pide los GB libres. Muestra CRÍTICO si son menos de 5, AVISO si son menos de 15 y CORRECTO en otro caso."),
("Horario permitido", "Pide una hora de 0 a 23 y muestra si está dentro del horario de soporte de 8 a 18 usando and."),
("Archivo de configuración", "Pide un nombre de archivo y muestra ACEPTADO si termina en .conf o .ini; en otro caso, RECHAZADO."),
("Usuario especial", "Pide un usuario y muestra PRIVILEGIADO si es root o administrator; en otro caso, ESTÁNDAR."),
("Asignación condicional", "Pide una nota y guarda en una variable el texto APTO o NO APTO mediante una asignación condicional. Después muéstrala."),
("Nombre no vacío", "Pide un nombre, aplica strip() y utiliza directamente su valor verdadero o falso para indicar si se ha escrito algo."),
("Acceso con dos requisitos", "Pide edad y si tiene autorización (s/n). Permite el acceso únicamente si es mayor de edad y tiene autorización."),
("Contador del 1 al 10", "Muestra los números del 1 al 10 utilizando while."),
("Cuenta atrás", "Pide un entero positivo y muestra una cuenta atrás hasta 0 utilizando while."),
("Contraseña repetida", "Pide una contraseña hasta que el usuario escriba 'python'. Después muestra ACCESO CONCEDIDO."),
("Validar entero positivo", "Pide un número como texto y repite la entrada mientras no sea un número positivo usando isdigit() y while."),
("Salir con break", "Crea un while True que pida comandos. Termina con break cuando el usuario escriba salir."),
("Saltar el cinco", "Muestra del 1 al 10 con while, pero utiliza continue para no mostrar el número 5."),
("Suma hasta cero", "Pide números enteros y acumula su suma. El programa termina cuando se introduce 0."),
("Tres intentos", "Permite introducir una clave como máximo tres veces usando while. Termina antes con break si la clave es correcta."),
("Buscar sin break", "Pide números hasta introducir uno mayor que 100. Usa while con else para mostrar que el bucle terminó de forma normal."),
("Menú sencillo", "Muestra un menú con opciones 1, 2 y 0 dentro de un while. Repite hasta elegir 0 y usa if/elif para responder a cada opción."),
("Recorrer palabra", "Pide una palabra y muestra cada carácter en una línea utilizando for."),
("Números del 0 al 9", "Muestra los números del 0 al 9 utilizando for y range()."),
("Números del 1 al 20", "Muestra los números del 1 al 20 utilizando range(inicio, fin)."),
("Pares hasta 30", "Muestra los números pares del 2 al 30 usando el paso de range()."),
("Cuenta atrás con range", "Muestra del 10 al 0 utilizando range() con paso negativo."),
("Repetir mensaje", "Pide un mensaje y muéstralo cinco veces usando for y _ como variable no utilizada."),
("Enumerar servidores", "Recorre la lista ['web', 'db', 'dns'] con enumerate(..., 1) y muestra número y nombre."),
("Buscar error", "Recorre ['OK', 'OK', 'ERROR', 'OK'] y usa break para detenerte al encontrar ERROR."),
("Omitir temporal", "Recorre una lista de nombres de archivo y utiliza continue para no mostrar los que terminan en .tmp."),
("Buscar puerto con else", "Recorre [22, 53, 80, 443] buscando el puerto 3306. Usa for con else para indicar que no se encontró."),
("Tabla de multiplicar", "Pide un número y muestra su tabla del 1 al 10 con for y range()."),
("Coordenadas de rack", "Usa dos bucles for anidados para mostrar combinaciones de rack 1–3 y posición 1–4."),
("Localizar un ValueError", "Escribe un pequeño programa que intente convertir 'abc' con int(). Ejecútalo, identifica el tipo de error y corrige el dato para que funcione."),
("Depurar con f-string", "Pide una edad como texto, muestra print(f'DEBUG: {edad=}') antes de convertirla a int() y comprueba qué ocurre con una entrada no numérica."),
("Capturar conversión", "Pide un número y captura únicamente ValueError con try/except para mostrar un mensaje claro si la conversión falla."),
("Comprobar con assert", "Crea una variable edad con un valor negativo y usa assert para comprobar que sea mayor o igual que cero. Observa el error y después corrige el valor."),
("Versión de Python", "Importa sys y muestra sys.version y sys.platform."),
("Argumento de usuario", "Importa sys. Si no existe sys.argv[1], muestra el uso del programa; si existe, saluda al nombre recibido."),
("Variable PATH", "Importa os y muestra el valor de la variable de entorno PATH con os.getenv()."),
("Fecha actual", "Importa datetime y muestra la fecha y hora actuales usando datetime.datetime.now()."),
("Backup de ayer", "Importa datetime y genera un nombre backup_YYYY_MM_DD.zip correspondiente a ayer usando datetime.timedelta()."),
("Información del sistema", "Importa platform y muestra sistema operativo, versión y procesador."),
("Directorio actual", "Importa pathlib y muestra el directorio actual con pathlib.Path.cwd()."),
("Crear carpeta logs", "Importa pathlib. Comprueba si existe la carpeta logs y créala si no existe."),
("Listar archivos Python", "Importa pathlib y recorre la carpeta actual con iterdir(). Muestra solo los archivos cuya extensión sea .py."),
("Tamaño de un archivo", "Importa pathlib, comprueba si existe informe.log y, si existe, muestra su tamaño con stat().st_size."),
("Buscar logs recursivamente", "Importa pathlib y utiliza rglob('*.log') para mostrar archivos .log de la carpeta actual y sus subcarpetas."),
("Uso de disco", "Importa shutil, consulta disk_usage('/') y muestra el porcentaje de espacio utilizado."),
("Copiar backup", "Importa pathlib y shutil. Si existe backup.zip, crea la carpeta copias si hace falta y copia allí el archivo."),
("Inventario Python", "Importa datetime, pathlib y platform. Muestra sistema, fecha actual y cuántos archivos .py hay en la carpeta actual combinando for e if."),
]

BASE = Path("docs/ejercicios/python")
DIR = BASE / "ut3"
DIR.mkdir(parents=True, exist_ok=True)

for antiguo in DIR.glob("ejercicio_*.py"):
    antiguo.unlink()

lineas = [
    "# UT3 · Ejercicios adicionales revisados",
    "",
    "50 ejercicios ajustados a los contenidos de los temas 3.1–3.5: condicionales, `while`, `for`, depuración y librerías de administración.",
    "",
    "!!! note \"Organización\"",
    "    **1–10:** condicionales · **11–20:** `while` · **21–32:** `for` y `range()` · **33–36:** depuración · **37–50:** librerías sysadmin.",
    "",
]

for numero, (titulo, enunciado) in enumerate(UT3, 1):
    nombre = f"ejercicio_{numero:02d}.py"
    lineas.extend([
        f"## Ejercicio {numero:02d} · {titulo}",
        enunciado,
        "",
        f"[:material-language-python: Abrir {nombre}](ut3/{nombre}){{ .md-button }}",
        "",
    ])
    (DIR / nombre).write_text(
        f'# Ejercicio {numero:02d} · {titulo}\n# {enunciado}\n\n# Escribe aquí tu solución.\n',
        encoding="utf-8",
    )

(BASE / "ut3.md").write_text("\n".join(lineas), encoding="utf-8")
print(f"Generados {len(UT3)} ejercicios revisados de UT3")
