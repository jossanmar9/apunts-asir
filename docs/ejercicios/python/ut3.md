# UT3 · Ejercicios adicionales revisados

50 ejercicios ajustados a los contenidos de los temas 3.1–3.5: condicionales, `while`, `for`, depuración y librerías de administración.

!!! note "Organización"
    **1–10:** condicionales · **11–20:** `while` · **21–32:** `for` y `range()` · **33–36:** depuración · **37–50:** librerías sysadmin.

## Ejercicio 01 · Control de acceso por edad
Pide una edad y muestra ACCESO si es mayor o igual que 18; en caso contrario, DENEGADO.

[:material-language-python: Abrir ejercicio_01.py](ut3/ejercicio_01.py){ .md-button }

## Ejercicio 02 · Estado de temperatura
Pide una temperatura y clasifícala como BAJO CERO, CERO o SOBRE CERO.

[:material-language-python: Abrir ejercicio_02.py](ut3/ejercicio_02.py){ .md-button }

## Ejercicio 03 · Puerto web
Pide un puerto y muestra WEB si es 80 o 443, SSH si es 22 y OTRO en cualquier otro caso.

[:material-language-python: Abrir ejercicio_03.py](ut3/ejercicio_03.py){ .md-button }

## Ejercicio 04 · Espacio de disco
Pide los GB libres. Muestra CRÍTICO si son menos de 5, AVISO si son menos de 15 y CORRECTO en otro caso.

[:material-language-python: Abrir ejercicio_04.py](ut3/ejercicio_04.py){ .md-button }

## Ejercicio 05 · Horario permitido
Pide una hora de 0 a 23 y muestra si está dentro del horario de soporte de 8 a 18 usando and.

[:material-language-python: Abrir ejercicio_05.py](ut3/ejercicio_05.py){ .md-button }

## Ejercicio 06 · Archivo de configuración
Pide un nombre de archivo y muestra ACEPTADO si termina en .conf o .ini; en otro caso, RECHAZADO.

[:material-language-python: Abrir ejercicio_06.py](ut3/ejercicio_06.py){ .md-button }

## Ejercicio 07 · Usuario especial
Pide un usuario y muestra PRIVILEGIADO si es root o administrator; en otro caso, ESTÁNDAR.

[:material-language-python: Abrir ejercicio_07.py](ut3/ejercicio_07.py){ .md-button }

## Ejercicio 08 · Asignación condicional
Pide una nota y guarda en una variable el texto APTO o NO APTO mediante una asignación condicional. Después muéstrala.

[:material-language-python: Abrir ejercicio_08.py](ut3/ejercicio_08.py){ .md-button }

## Ejercicio 09 · Nombre no vacío
Pide un nombre, aplica strip() y utiliza directamente su valor verdadero o falso para indicar si se ha escrito algo.

[:material-language-python: Abrir ejercicio_09.py](ut3/ejercicio_09.py){ .md-button }

## Ejercicio 10 · Acceso con dos requisitos
Pide edad y si tiene autorización (s/n). Permite el acceso únicamente si es mayor de edad y tiene autorización.

[:material-language-python: Abrir ejercicio_10.py](ut3/ejercicio_10.py){ .md-button }

## Ejercicio 11 · Contador del 1 al 10
Muestra los números del 1 al 10 utilizando while.

[:material-language-python: Abrir ejercicio_11.py](ut3/ejercicio_11.py){ .md-button }

## Ejercicio 12 · Cuenta atrás
Pide un entero positivo y muestra una cuenta atrás hasta 0 utilizando while.

[:material-language-python: Abrir ejercicio_12.py](ut3/ejercicio_12.py){ .md-button }

## Ejercicio 13 · Contraseña repetida
Pide una contraseña hasta que el usuario escriba 'python'. Después muestra ACCESO CONCEDIDO.

[:material-language-python: Abrir ejercicio_13.py](ut3/ejercicio_13.py){ .md-button }

## Ejercicio 14 · Validar entero positivo
Pide un número como texto y repite la entrada mientras no sea un número positivo usando isdigit() y while.

[:material-language-python: Abrir ejercicio_14.py](ut3/ejercicio_14.py){ .md-button }

## Ejercicio 15 · Salir con break
Crea un while True que pida comandos. Termina con break cuando el usuario escriba salir.

[:material-language-python: Abrir ejercicio_15.py](ut3/ejercicio_15.py){ .md-button }

## Ejercicio 16 · Saltar el cinco
Muestra del 1 al 10 con while, pero utiliza continue para no mostrar el número 5.

[:material-language-python: Abrir ejercicio_16.py](ut3/ejercicio_16.py){ .md-button }

## Ejercicio 17 · Suma hasta cero
Pide números enteros y acumula su suma. El programa termina cuando se introduce 0.

[:material-language-python: Abrir ejercicio_17.py](ut3/ejercicio_17.py){ .md-button }

## Ejercicio 18 · Tres intentos
Permite introducir una clave como máximo tres veces usando while. Termina antes con break si la clave es correcta.

[:material-language-python: Abrir ejercicio_18.py](ut3/ejercicio_18.py){ .md-button }

## Ejercicio 19 · Buscar sin break
Pide números hasta introducir uno mayor que 100. Usa while con else para mostrar que el bucle terminó de forma normal.

[:material-language-python: Abrir ejercicio_19.py](ut3/ejercicio_19.py){ .md-button }

## Ejercicio 20 · Menú sencillo
Muestra un menú con opciones 1, 2 y 0 dentro de un while. Repite hasta elegir 0 y usa if/elif para responder a cada opción.

[:material-language-python: Abrir ejercicio_20.py](ut3/ejercicio_20.py){ .md-button }

## Ejercicio 21 · Recorrer palabra
Pide una palabra y muestra cada carácter en una línea utilizando for.

[:material-language-python: Abrir ejercicio_21.py](ut3/ejercicio_21.py){ .md-button }

## Ejercicio 22 · Números del 0 al 9
Muestra los números del 0 al 9 utilizando for y range().

[:material-language-python: Abrir ejercicio_22.py](ut3/ejercicio_22.py){ .md-button }

## Ejercicio 23 · Números del 1 al 20
Muestra los números del 1 al 20 utilizando range(inicio, fin).

[:material-language-python: Abrir ejercicio_23.py](ut3/ejercicio_23.py){ .md-button }

## Ejercicio 24 · Pares hasta 30
Muestra los números pares del 2 al 30 usando el paso de range().

[:material-language-python: Abrir ejercicio_24.py](ut3/ejercicio_24.py){ .md-button }

## Ejercicio 25 · Cuenta atrás con range
Muestra del 10 al 0 utilizando range() con paso negativo.

[:material-language-python: Abrir ejercicio_25.py](ut3/ejercicio_25.py){ .md-button }

## Ejercicio 26 · Repetir mensaje
Pide un mensaje y muéstralo cinco veces usando for y _ como variable no utilizada.

[:material-language-python: Abrir ejercicio_26.py](ut3/ejercicio_26.py){ .md-button }

## Ejercicio 27 · Enumerar servidores
Recorre la lista ['web', 'db', 'dns'] con enumerate(..., 1) y muestra número y nombre.

[:material-language-python: Abrir ejercicio_27.py](ut3/ejercicio_27.py){ .md-button }

## Ejercicio 28 · Buscar error
Recorre ['OK', 'OK', 'ERROR', 'OK'] y usa break para detenerte al encontrar ERROR.

[:material-language-python: Abrir ejercicio_28.py](ut3/ejercicio_28.py){ .md-button }

## Ejercicio 29 · Omitir temporal
Recorre una lista de nombres de archivo y utiliza continue para no mostrar los que terminan en .tmp.

[:material-language-python: Abrir ejercicio_29.py](ut3/ejercicio_29.py){ .md-button }

## Ejercicio 30 · Buscar puerto con else
Recorre [22, 53, 80, 443] buscando el puerto 3306. Usa for con else para indicar que no se encontró.

[:material-language-python: Abrir ejercicio_30.py](ut3/ejercicio_30.py){ .md-button }

## Ejercicio 31 · Tabla de multiplicar
Pide un número y muestra su tabla del 1 al 10 con for y range().

[:material-language-python: Abrir ejercicio_31.py](ut3/ejercicio_31.py){ .md-button }

## Ejercicio 32 · Coordenadas de rack
Usa dos bucles for anidados para mostrar combinaciones de rack 1–3 y posición 1–4.

[:material-language-python: Abrir ejercicio_32.py](ut3/ejercicio_32.py){ .md-button }

## Ejercicio 33 · Localizar un ValueError
Escribe un pequeño programa que intente convertir 'abc' con int(). Ejecútalo, identifica el tipo de error y corrige el dato para que funcione.

[:material-language-python: Abrir ejercicio_33.py](ut3/ejercicio_33.py){ .md-button }

## Ejercicio 34 · Depurar con f-string
Pide una edad como texto, muestra print(f'DEBUG: {edad=}') antes de convertirla a int() y comprueba qué ocurre con una entrada no numérica.

[:material-language-python: Abrir ejercicio_34.py](ut3/ejercicio_34.py){ .md-button }

## Ejercicio 35 · Capturar conversión
Pide un número y captura únicamente ValueError con try/except para mostrar un mensaje claro si la conversión falla.

[:material-language-python: Abrir ejercicio_35.py](ut3/ejercicio_35.py){ .md-button }

## Ejercicio 36 · Comprobar con assert
Crea una variable edad con un valor negativo y usa assert para comprobar que sea mayor o igual que cero. Observa el error y después corrige el valor.

[:material-language-python: Abrir ejercicio_36.py](ut3/ejercicio_36.py){ .md-button }

## Ejercicio 37 · Versión de Python
Importa sys y muestra sys.version y sys.platform.

[:material-language-python: Abrir ejercicio_37.py](ut3/ejercicio_37.py){ .md-button }

## Ejercicio 38 · Argumento de usuario
Importa sys. Si no existe sys.argv[1], muestra el uso del programa; si existe, saluda al nombre recibido.

[:material-language-python: Abrir ejercicio_38.py](ut3/ejercicio_38.py){ .md-button }

## Ejercicio 39 · Variable PATH
Importa os y muestra el valor de la variable de entorno PATH con os.getenv().

[:material-language-python: Abrir ejercicio_39.py](ut3/ejercicio_39.py){ .md-button }

## Ejercicio 40 · Fecha actual
Importa datetime y muestra la fecha y hora actuales usando datetime.datetime.now().

[:material-language-python: Abrir ejercicio_40.py](ut3/ejercicio_40.py){ .md-button }

## Ejercicio 41 · Backup de ayer
Importa datetime y genera un nombre backup_YYYY_MM_DD.zip correspondiente a ayer usando datetime.timedelta().

[:material-language-python: Abrir ejercicio_41.py](ut3/ejercicio_41.py){ .md-button }

## Ejercicio 42 · Información del sistema
Importa platform y muestra sistema operativo, versión y procesador.

[:material-language-python: Abrir ejercicio_42.py](ut3/ejercicio_42.py){ .md-button }

## Ejercicio 43 · Directorio actual
Importa pathlib y muestra el directorio actual con pathlib.Path.cwd().

[:material-language-python: Abrir ejercicio_43.py](ut3/ejercicio_43.py){ .md-button }

## Ejercicio 44 · Crear carpeta logs
Importa pathlib. Comprueba si existe la carpeta logs y créala si no existe.

[:material-language-python: Abrir ejercicio_44.py](ut3/ejercicio_44.py){ .md-button }

## Ejercicio 45 · Listar archivos Python
Importa pathlib y recorre la carpeta actual con iterdir(). Muestra solo los archivos cuya extensión sea .py.

[:material-language-python: Abrir ejercicio_45.py](ut3/ejercicio_45.py){ .md-button }

## Ejercicio 46 · Tamaño de un archivo
Importa pathlib, comprueba si existe informe.log y, si existe, muestra su tamaño con stat().st_size.

[:material-language-python: Abrir ejercicio_46.py](ut3/ejercicio_46.py){ .md-button }

## Ejercicio 47 · Buscar logs recursivamente
Importa pathlib y utiliza rglob('*.log') para mostrar archivos .log de la carpeta actual y sus subcarpetas.

[:material-language-python: Abrir ejercicio_47.py](ut3/ejercicio_47.py){ .md-button }

## Ejercicio 48 · Uso de disco
Importa shutil, consulta disk_usage('/') y muestra el porcentaje de espacio utilizado.

[:material-language-python: Abrir ejercicio_48.py](ut3/ejercicio_48.py){ .md-button }

## Ejercicio 49 · Copiar backup
Importa pathlib y shutil. Si existe backup.zip, crea la carpeta copias si hace falta y copia allí el archivo.

[:material-language-python: Abrir ejercicio_49.py](ut3/ejercicio_49.py){ .md-button }

## Ejercicio 50 · Inventario Python
Importa datetime, pathlib y platform. Muestra sistema, fecha actual y cuántos archivos .py hay en la carpeta actual combinando for e if.

[:material-language-python: Abrir ejercicio_50.py](ut3/ejercicio_50.py){ .md-button }
