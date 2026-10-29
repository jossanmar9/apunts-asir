"""Regenera 120 ejercicios adicionales de Python UT3 ajustados al temario 3.1–3.5."""
import pathlib

CONDICIONALES = [
("Mayor de edad", "Pide una edad y muestra si la persona es mayor o menor de edad."),
("Positivo, negativo o cero", "Pide un número y clasifícalo como positivo, negativo o cero."),
("Par o impar", "Pide un entero e indica si es par o impar."),
("Múltiplo de cinco", "Pide un entero e indica si es múltiplo de 5."),
("Intervalo permitido", "Pide un número e indica si está entre 10 y 20, ambos incluidos."),
("Nota válida", "Pide una nota e indica si está dentro del intervalo válido de 0 a 10."),
("Calificación", "Pide una nota de 0 a 10 y clasifícala como insuficiente, suficiente, bien, notable o sobresaliente."),
("Puerto conocido", "Pide un puerto y muestra SSH para 22, WEB para 80 o 443 y OTRO en cualquier otro caso."),
("Puerto válido", "Pide un entero e indica si es un puerto válido entre 1 y 65535."),
("Puerto privilegiado", "Pide un puerto válido e indica si es privilegiado, menor de 1024, o no privilegiado."),
("Uso de CPU", "Pide el porcentaje de CPU y clasifícalo como NORMAL, ALTO o CRÍTICO usando dos umbrales."),
("Uso de memoria", "Pide el porcentaje de RAM utilizada y clasifícalo en BAJO, MEDIO o ALTO."),
("Espacio libre", "Pide los GB libres de un disco y muestra un aviso si quedan menos de 10 GB."),
("Temperatura de CPU", "Pide una temperatura y clasifícala como NORMAL, CALIENTE o CRÍTICA."),
("Horario de soporte", "Pide una hora de 0 a 23 e indica si está dentro del horario de soporte de 8 a 18 usando and."),
("Extensión permitida", "Pide un nombre de archivo y acepta solo los que terminen en .txt, .log o .conf."),
("Entorno por hostname", "Pide un hostname y muestra PRODUCCIÓN si empieza por PROD-, PRUEBAS si empieza por TEST- y DESCONOCIDO en otro caso."),
("Usuario especial", "Pide un usuario y muestra PRIVILEGIADO si es root o administrator; en otro caso, ESTÁNDAR."),
("Asignación condicional", "Pide una nota y guarda APTO o NO APTO en una variable mediante una asignación condicional."),
("Acceso con requisitos", "Pide edad y autorización (s/n). Permite el acceso únicamente si es mayor de edad y tiene autorización."),
]

WHILE = [
("Contador ascendente", "Muestra los números del 1 al 10 utilizando while."),
("Cuenta atrás", "Pide un entero positivo y muestra una cuenta atrás hasta 0 utilizando while."),
("Pares con while", "Muestra los números pares del 2 al 20 utilizando while."),
("Contraseña repetida", "Pide una contraseña hasta que el usuario escriba 'python'."),
("Validar positivo", "Pide un número como texto y repite la entrada mientras no sea un entero positivo usando isdigit()."),
("Comando salir", "Crea un while True que pida comandos y termine con break cuando se escriba salir."),
("Saltar el cinco", "Muestra del 1 al 10 con while y utiliza continue para no mostrar el número 5."),
("Suma hasta cero", "Pide enteros y acumula su suma hasta que se introduzca 0."),
("Tres intentos", "Permite introducir una clave como máximo tres veces y termina antes con break si es correcta."),
("Menú sencillo", "Muestra un menú con opciones 1, 2 y 0 dentro de un while y repite hasta elegir 0."),
("Acumular hasta cien", "Pide números y súmalos hasta que el total sea igual o superior a 100."),
("Primer múltiplo", "Pide enteros hasta introducir uno que sea múltiplo de 7."),
("Confirmación", "Pregunta '¿Continuar? (s/n)' hasta recibir una respuesta válida."),
("PIN limitado", "Permite tres intentos para introducir un PIN correcto y muestra si se agotaron los intentos."),
("Contar entradas", "Pide palabras hasta escribir fin y muestra cuántas palabras se introdujeron antes."),
("Media hasta cero", "Pide números hasta introducir 0 y calcula la media de los anteriores."),
("Solo impares", "Recorre con while los números del 1 al 20 y usa continue para mostrar solo los impares."),
("Buscar mayor que cien", "Pide números hasta introducir uno mayor que 100 y utiliza while con else al finalizar normalmente."),
("Repetir ruta", "Pide una ruta hasta que el usuario introduzca una cadena que empiece por '/'."),
("Descenso configurable", "Pide un número inicial positivo y un paso positivo y haz una cuenta atrás con while hasta llegar a 0 o menos."),
]

FOR = [
("Recorrer palabra", "Pide una palabra y muestra cada carácter en una línea utilizando for."),
("Cero a nueve", "Muestra los números del 0 al 9 utilizando for y range()."),
("Uno a veinte", "Muestra los números del 1 al 20 utilizando range(inicio, fin)."),
("Pares hasta treinta", "Muestra los pares del 2 al 30 usando el paso de range()."),
("Cuenta atrás con range", "Muestra del 10 al 0 utilizando range() con paso negativo."),
("Repetir mensaje", "Pide un mensaje y muéstralo cinco veces usando for y _ como variable no utilizada."),
("Enumerar servidores", "Recorre ['web', 'db', 'dns'] con enumerate(..., 1) y muestra número y nombre."),
("Buscar error", "Recorre ['OK', 'OK', 'ERROR', 'OK'] y usa break para detenerte al encontrar ERROR."),
("Omitir temporales", "Recorre una lista de archivos y utiliza continue para no mostrar los que terminan en .tmp."),
("Buscar puerto con else", "Recorre [22, 53, 80, 443] buscando 3306 y usa for con else para indicar que no se encontró."),
("Tabla de multiplicar", "Pide un número y muestra su tabla del 1 al 10 con for y range()."),
("Suma de rango", "Suma con un for los números del 1 al 100 y muestra el resultado."),
("Contar vocales", "Pide una palabra y cuenta sus vocales recorriéndola con for."),
("Posiciones de caracteres", "Pide una palabra y muestra índice y carácter usando enumerate()."),
("Múltiplos de tres", "Muestra los múltiplos de 3 entre 3 y 60 usando range()."),
("Primer negativo", "Recorre una lista de enteros y termina con break al encontrar el primer negativo."),
("Filtrar logs", "Recorre una lista de nombres y muestra únicamente los que terminan en .log."),
("Racks y posiciones", "Usa dos for anidados para mostrar racks 1–3 y posiciones 1–4."),
("Tabla cuadrada", "Usa dos bucles for anidados para mostrar los productos de 1 a 5 por 1 a 5."),
("Buscar letra con else", "Pide una palabra y una letra, recorre la palabra y utiliza for con else para avisar si la letra no aparece."),
]

DEPURACION = [
("ValueError básico", "Intenta convertir 'abc' con int(), identifica el error y corrige el dato para que el programa funcione."),
("DEBUG de edad", "Pide una edad como texto y muestra print(f'DEBUG: {edad=}') antes de convertirla a int()."),
("Capturar entero", "Pide un número y captura únicamente ValueError con try/except."),
("Assert de edad", "Crea una edad negativa y usa assert para comprobar que sea mayor o igual que cero; después corrige el valor."),
("División segura", "Pide dos números y captura ZeroDivisionError si el divisor es cero."),
("Conversión decimal", "Pide un precio y captura ValueError si no puede convertirse a float."),
("Índice inexistente", "Crea una lista de tres elementos, intenta acceder a una posición inexistente, identifica IndexError y corrige el acceso."),
("Clave inexistente", "Crea un diccionario sencillo, intenta consultar una clave que no existe, identifica KeyError y corrige la consulta."),
("Nombre mal escrito", "Escribe un ejemplo que provoque NameError por usar una variable con un nombre incorrecto y después arréglalo."),
("Traza de contador", "Crea un bucle corto y añade un print DEBUG que muestre el valor del contador en cada vuelta."),
("Traza de acumulador", "Suma varios números con un bucle y muestra el acumulador después de cada operación para seguir su evolución."),
("Comprobar porcentaje", "Pide un porcentaje, conviértelo a entero y usa assert para comprobar que esté entre 0 y 100."),
("Comprobar puerto", "Pide un puerto y usa assert para comprobar que esté entre 1 y 65535."),
("Dos conversiones", "Pide dos enteros dentro de un mismo try y muestra un mensaje claro si cualquiera produce ValueError."),
("Conversión repetida", "Usa while y try/except para repetir la petición hasta que el usuario introduzca un entero válido."),
("División y conversión", "Pide dividendo y divisor como texto y trata por separado ValueError y ZeroDivisionError."),
("Depurar condición", "Crea una condición que use por error = en lugar de ==, observa SyntaxError y corrígela."),
("Depurar indentación", "Escribe un if con una línea mal indentada, observa IndentationError y corrige la estructura."),
("Mensaje de excepción", "Captura ValueError como error y muestra el texto de la excepción junto con un mensaje propio."),
("Validación completa", "Pide una edad, captura ValueError y, si la conversión funciona, usa assert para comprobar que no sea negativa."),
]

BIBLIOTECAS = [
("Versión de Python", "Importa sys y muestra sys.version y sys.platform."),
("Argumento de usuario", "Importa sys y usa sys.argv para mostrar un nombre recibido como argumento o un mensaje de uso si falta."),
("Variable PATH", "Importa os y muestra la variable de entorno PATH con os.getenv()."),
("Directorio con os", "Importa os y muestra el directorio de trabajo actual."),
("Fecha actual", "Importa datetime y muestra fecha y hora actuales con datetime.datetime.now()."),
("Fecha de hoy", "Importa datetime y muestra únicamente la fecha actual."),
("Backup de ayer", "Importa datetime y genera un nombre backup_YYYY_MM_DD.zip correspondiente a ayer usando datetime.timedelta()."),
("Dentro de una semana", "Importa datetime y calcula qué fecha será dentro de siete días."),
("Sistema operativo", "Importa platform y muestra el sistema operativo y su versión."),
("Información de máquina", "Importa platform y muestra machine() y processor()."),
("Directorio actual", "Importa pathlib y muestra el directorio actual con pathlib.Path.cwd()."),
("Crear carpeta logs", "Importa pathlib, comprueba si existe logs y créala si no existe."),
("Existe un archivo", "Importa pathlib y comprueba con exists() si existe config.ini."),
("Listar Python", "Importa pathlib, recorre la carpeta actual con iterdir() y muestra solo los archivos .py."),
("Tamaño de archivo", "Importa pathlib y, si existe informe.log, muestra su tamaño con stat().st_size."),
("Buscar logs", "Importa pathlib y utiliza glob('*.log') para mostrar los .log de la carpeta actual."),
("Buscar logs recursivos", "Importa pathlib y utiliza rglob('*.log') para buscar también en subcarpetas."),
("Uso de disco", "Importa shutil, consulta disk_usage('/') y muestra espacio total, usado y libre."),
("Copiar archivo", "Importa pathlib y shutil. Si existe backup.zip, crea copias si hace falta y copia allí el archivo."),
("Mover archivo", "Importa pathlib y shutil. Si existe temporal.log, crea archivo si hace falta y mueve allí temporal.log."),
]

MIXTOS = [
("Inventario Python", "Combina pathlib, datetime, for e if para mostrar la fecha actual y contar cuántos archivos .py hay en la carpeta actual."),
("Alerta de disco", "Usa shutil.disk_usage(), calcula el porcentaje usado y clasifícalo con if como NORMAL, AVISO o CRÍTICO."),
("Listado numerado de logs", "Usa pathlib para obtener archivos .log y enumerate() para mostrarlos numerados."),
("Buscar configuración", "Usa pathlib.rglob() y un for para buscar archivos .conf; usa for...else para avisar si no aparece ninguno."),
("Backup con fecha", "Usa pathlib, shutil y datetime para copiar config.ini a una carpeta backup con la fecha actual en el nombre del archivo."),
("Limpiar temporales", "Usa pathlib para recorrer archivos .tmp y un if para mostrar cuáles eliminarías; no los borres."),
("Menú del sistema", "Crea un menú con while que permita mostrar platform.system(), pathlib.Path.cwd() o salir."),
("Validador de puerto", "Usa while y try/except para pedir un puerto entero hasta que sea válido; después clasifícalo como privilegiado o no privilegiado."),
("Argumentos y archivo", "Lee una ruta desde sys.argv, conviértela en pathlib.Path y muestra con if si existe y si es archivo o directorio."),
("Logs grandes", "Usa pathlib.rglob('*.log'), un for y stat().st_size para mostrar solo los logs mayores de un tamaño indicado por el usuario."),
("Resumen de extensiones", "Recorre con pathlib los archivos de una carpeta y cuenta con condicionales cuántos son .py, .txt y .log."),
("Comprobar espacio para copia", "Pide el tamaño de una copia, consulta shutil.disk_usage() y usa if para indicar si cabe en el espacio libre."),
("Fecha límite", "Pide un número de días, captura ValueError y usa datetime.timedelta() para mostrar la fecha límite resultante."),
("Servidores numerados", "Recorre una lista de hostnames con enumerate() y clasifica cada uno con if según empiece por PROD-, TEST- u otro prefijo."),
("Búsqueda con intentos", "Usa while para pedir una extensión válida y después pathlib.rglob() para buscarla recursivamente y contar resultados."),
("Informe del equipo", "Combina platform, datetime y shutil para mostrar sistema, fecha y porcentaje de disco utilizado."),
("Procesar argumentos", "Recorre sys.argv[1:] con for y muestra para cada argumento si representa una ruta existente usando pathlib."),
("Copia condicionada", "Pide confirmación con while; si la respuesta es s y existe origen.txt, usa shutil.copy() para copiarlo a copia.txt."),
("Auditoría sencilla", "Recorre archivos con pathlib, omite con continue los ocultos y muestra nombre, extensión y tamaño de los demás."),
("Mini diagnóstico", "Crea un programa que combine sys, platform, pathlib y shutil para mostrar versión de Python, sistema, directorio actual, número de archivos y espacio libre."),
]

BLOQUES = [
    ("Condicionales", CONDICIONALES),
    ("while", WHILE),
    ("for y range()", FOR),
    ("Depuración y errores", DEPURACION),
    ("Librerías sysadmin", BIBLIOTECAS),
    ("Ejercicios mixtos", MIXTOS),
]

BASE = pathlib.Path("docs/ejercicios/python")
DIR = BASE / "ut3"
DIR.mkdir(parents=True, exist_ok=True)

for antiguo in DIR.glob("ejercicio_*.py"):
    antiguo.unlink()

lineas = [
    "# UT3 · Ejercicios adicionales",
    "",
    "120 ejercicios ajustados a los temas 3.1–3.5. Primero se practica cada bloque por separado y al final se combinan los contenidos.",
    "",
    "!!! note \"Organización\"",
    "    **1–20:** condicionales · **21–40:** `while` · **41–60:** `for` y `range()` · **61–80:** depuración y errores · **81–100:** librerías sysadmin · **101–120:** ejercicios mixtos.",
    "",
]

numero = 1
for nombre_bloque, ejercicios in BLOQUES:
    lineas.extend([f"## {nombre_bloque}", ""])
    for titulo, enunciado in ejercicios:
        nombre = f"ejercicio_{numero:03d}.py"
        lineas.extend([
            f"### Ejercicio {numero:03d} · {titulo}",
            enunciado,
            "",
            f"[:material-language-python: Abrir {nombre}](ut3/{nombre}){{ .md-button }}",
            "",
        ])
        (DIR / nombre).write_text(
            f'# Ejercicio {numero:03d} · {titulo}\n# {enunciado}\n\n# Escribe aquí tu solución.\n',
            encoding="utf-8",
        )
        numero += 1

(BASE / "ut3.md").write_text("\n".join(lineas), encoding="utf-8")
print(f"Generados {numero - 1} ejercicios de UT3")
