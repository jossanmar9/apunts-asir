# UT3 · Ejercicios adicionales

120 ejercicios ajustados a los temas 3.1–3.5. Primero se practica cada bloque por separado y al final se combinan los contenidos.

!!! note "Organización"
    **1–20:** condicionales · **21–40:** `while` · **41–60:** `for` y `range()` · **61–80:** depuración y errores · **81–100:** librerías sysadmin · **101–120:** ejercicios mixtos.

## Condicionales

### Ejercicio 001 · Mayor de edad
Pide una edad y muestra si la persona es mayor o menor de edad.

[:material-language-python: Abrir ejercicio_001.py](ut3/ejercicio_001.py){ .md-button }

### Ejercicio 002 · Positivo, negativo o cero
Pide un número y clasifícalo como positivo, negativo o cero.

[:material-language-python: Abrir ejercicio_002.py](ut3/ejercicio_002.py){ .md-button }

### Ejercicio 003 · Par o impar
Pide un entero e indica si es par o impar.

[:material-language-python: Abrir ejercicio_003.py](ut3/ejercicio_003.py){ .md-button }

### Ejercicio 004 · Múltiplo de cinco
Pide un entero e indica si es múltiplo de 5.

[:material-language-python: Abrir ejercicio_004.py](ut3/ejercicio_004.py){ .md-button }

### Ejercicio 005 · Intervalo permitido
Pide un número e indica si está entre 10 y 20, ambos incluidos.

[:material-language-python: Abrir ejercicio_005.py](ut3/ejercicio_005.py){ .md-button }

### Ejercicio 006 · Nota válida
Pide una nota e indica si está dentro del intervalo válido de 0 a 10.

[:material-language-python: Abrir ejercicio_006.py](ut3/ejercicio_006.py){ .md-button }

### Ejercicio 007 · Calificación
Pide una nota de 0 a 10 y clasifícala como insuficiente, suficiente, bien, notable o sobresaliente.

[:material-language-python: Abrir ejercicio_007.py](ut3/ejercicio_007.py){ .md-button }

### Ejercicio 008 · Puerto conocido
Pide un puerto y muestra SSH para 22, WEB para 80 o 443 y OTRO en cualquier otro caso.

[:material-language-python: Abrir ejercicio_008.py](ut3/ejercicio_008.py){ .md-button }

### Ejercicio 009 · Puerto válido
Pide un entero e indica si es un puerto válido entre 1 y 65535.

[:material-language-python: Abrir ejercicio_009.py](ut3/ejercicio_009.py){ .md-button }

### Ejercicio 010 · Puerto privilegiado
Pide un puerto válido e indica si es privilegiado, menor de 1024, o no privilegiado.

[:material-language-python: Abrir ejercicio_010.py](ut3/ejercicio_010.py){ .md-button }

### Ejercicio 011 · Uso de CPU
Pide el porcentaje de CPU y clasifícalo como NORMAL, ALTO o CRÍTICO usando dos umbrales.

[:material-language-python: Abrir ejercicio_011.py](ut3/ejercicio_011.py){ .md-button }

### Ejercicio 012 · Uso de memoria
Pide el porcentaje de RAM utilizada y clasifícalo en BAJO, MEDIO o ALTO.

[:material-language-python: Abrir ejercicio_012.py](ut3/ejercicio_012.py){ .md-button }

### Ejercicio 013 · Espacio libre
Pide los GB libres de un disco y muestra un aviso si quedan menos de 10 GB.

[:material-language-python: Abrir ejercicio_013.py](ut3/ejercicio_013.py){ .md-button }

### Ejercicio 014 · Temperatura de CPU
Pide una temperatura y clasifícala como NORMAL, CALIENTE o CRÍTICA.

[:material-language-python: Abrir ejercicio_014.py](ut3/ejercicio_014.py){ .md-button }

### Ejercicio 015 · Horario de soporte
Pide una hora de 0 a 23 e indica si está dentro del horario de soporte de 8 a 18 usando and.

[:material-language-python: Abrir ejercicio_015.py](ut3/ejercicio_015.py){ .md-button }

### Ejercicio 016 · Extensión permitida
Pide un nombre de archivo y acepta solo los que terminen en .txt, .log o .conf.

[:material-language-python: Abrir ejercicio_016.py](ut3/ejercicio_016.py){ .md-button }

### Ejercicio 017 · Entorno por hostname
Pide un hostname y muestra PRODUCCIÓN si empieza por PROD-, PRUEBAS si empieza por TEST- y DESCONOCIDO en otro caso.

[:material-language-python: Abrir ejercicio_017.py](ut3/ejercicio_017.py){ .md-button }

### Ejercicio 018 · Usuario especial
Pide un usuario y muestra PRIVILEGIADO si es root o administrator; en otro caso, ESTÁNDAR.

[:material-language-python: Abrir ejercicio_018.py](ut3/ejercicio_018.py){ .md-button }

### Ejercicio 019 · Asignación condicional
Pide una nota y guarda APTO o NO APTO en una variable mediante una asignación condicional.

[:material-language-python: Abrir ejercicio_019.py](ut3/ejercicio_019.py){ .md-button }

### Ejercicio 020 · Acceso con requisitos
Pide edad y autorización (s/n). Permite el acceso únicamente si es mayor de edad y tiene autorización.

[:material-language-python: Abrir ejercicio_020.py](ut3/ejercicio_020.py){ .md-button }

## while

### Ejercicio 021 · Contador ascendente
Muestra los números del 1 al 10 utilizando while.

[:material-language-python: Abrir ejercicio_021.py](ut3/ejercicio_021.py){ .md-button }

### Ejercicio 022 · Cuenta atrás
Pide un entero positivo y muestra una cuenta atrás hasta 0 utilizando while.

[:material-language-python: Abrir ejercicio_022.py](ut3/ejercicio_022.py){ .md-button }

### Ejercicio 023 · Pares con while
Muestra los números pares del 2 al 20 utilizando while.

[:material-language-python: Abrir ejercicio_023.py](ut3/ejercicio_023.py){ .md-button }

### Ejercicio 024 · Contraseña repetida
Pide una contraseña hasta que el usuario escriba 'python'.

[:material-language-python: Abrir ejercicio_024.py](ut3/ejercicio_024.py){ .md-button }

### Ejercicio 025 · Validar positivo
Pide un número como texto y repite la entrada mientras no sea un entero positivo usando isdigit().

[:material-language-python: Abrir ejercicio_025.py](ut3/ejercicio_025.py){ .md-button }

### Ejercicio 026 · Comando salir
Crea un while True que pida comandos y termine con break cuando se escriba salir.

[:material-language-python: Abrir ejercicio_026.py](ut3/ejercicio_026.py){ .md-button }

### Ejercicio 027 · Saltar el cinco
Muestra del 1 al 10 con while y utiliza continue para no mostrar el número 5.

[:material-language-python: Abrir ejercicio_027.py](ut3/ejercicio_027.py){ .md-button }

### Ejercicio 028 · Suma hasta cero
Pide enteros y acumula su suma hasta que se introduzca 0.

[:material-language-python: Abrir ejercicio_028.py](ut3/ejercicio_028.py){ .md-button }

### Ejercicio 029 · Tres intentos
Permite introducir una clave como máximo tres veces y termina antes con break si es correcta.

[:material-language-python: Abrir ejercicio_029.py](ut3/ejercicio_029.py){ .md-button }

### Ejercicio 030 · Menú sencillo
Muestra un menú con opciones 1, 2 y 0 dentro de un while y repite hasta elegir 0.

[:material-language-python: Abrir ejercicio_030.py](ut3/ejercicio_030.py){ .md-button }

### Ejercicio 031 · Acumular hasta cien
Pide números y súmalos hasta que el total sea igual o superior a 100.

[:material-language-python: Abrir ejercicio_031.py](ut3/ejercicio_031.py){ .md-button }

### Ejercicio 032 · Primer múltiplo
Pide enteros hasta introducir uno que sea múltiplo de 7.

[:material-language-python: Abrir ejercicio_032.py](ut3/ejercicio_032.py){ .md-button }

### Ejercicio 033 · Confirmación
Pregunta '¿Continuar? (s/n)' hasta recibir una respuesta válida.

[:material-language-python: Abrir ejercicio_033.py](ut3/ejercicio_033.py){ .md-button }

### Ejercicio 034 · PIN limitado
Permite tres intentos para introducir un PIN correcto y muestra si se agotaron los intentos.

[:material-language-python: Abrir ejercicio_034.py](ut3/ejercicio_034.py){ .md-button }

### Ejercicio 035 · Contar entradas
Pide palabras hasta escribir fin y muestra cuántas palabras se introdujeron antes.

[:material-language-python: Abrir ejercicio_035.py](ut3/ejercicio_035.py){ .md-button }

### Ejercicio 036 · Media hasta cero
Pide números hasta introducir 0 y calcula la media de los anteriores.

[:material-language-python: Abrir ejercicio_036.py](ut3/ejercicio_036.py){ .md-button }

### Ejercicio 037 · Solo impares
Recorre con while los números del 1 al 20 y usa continue para mostrar solo los impares.

[:material-language-python: Abrir ejercicio_037.py](ut3/ejercicio_037.py){ .md-button }

### Ejercicio 038 · Buscar mayor que cien
Pide números hasta introducir uno mayor que 100 y utiliza while con else al finalizar normalmente.

[:material-language-python: Abrir ejercicio_038.py](ut3/ejercicio_038.py){ .md-button }

### Ejercicio 039 · Repetir ruta
Pide una ruta hasta que el usuario introduzca una cadena que empiece por '/'.

[:material-language-python: Abrir ejercicio_039.py](ut3/ejercicio_039.py){ .md-button }

### Ejercicio 040 · Descenso configurable
Pide un número inicial positivo y un paso positivo y haz una cuenta atrás con while hasta llegar a 0 o menos.

[:material-language-python: Abrir ejercicio_040.py](ut3/ejercicio_040.py){ .md-button }

## for y range()

### Ejercicio 041 · Recorrer palabra
Pide una palabra y muestra cada carácter en una línea utilizando for.

[:material-language-python: Abrir ejercicio_041.py](ut3/ejercicio_041.py){ .md-button }

### Ejercicio 042 · Cero a nueve
Muestra los números del 0 al 9 utilizando for y range().

[:material-language-python: Abrir ejercicio_042.py](ut3/ejercicio_042.py){ .md-button }

### Ejercicio 043 · Uno a veinte
Muestra los números del 1 al 20 utilizando range(inicio, fin).

[:material-language-python: Abrir ejercicio_043.py](ut3/ejercicio_043.py){ .md-button }

### Ejercicio 044 · Pares hasta treinta
Muestra los pares del 2 al 30 usando el paso de range().

[:material-language-python: Abrir ejercicio_044.py](ut3/ejercicio_044.py){ .md-button }

### Ejercicio 045 · Cuenta atrás con range
Muestra del 10 al 0 utilizando range() con paso negativo.

[:material-language-python: Abrir ejercicio_045.py](ut3/ejercicio_045.py){ .md-button }

### Ejercicio 046 · Repetir mensaje
Pide un mensaje y muéstralo cinco veces usando for y _ como variable no utilizada.

[:material-language-python: Abrir ejercicio_046.py](ut3/ejercicio_046.py){ .md-button }

### Ejercicio 047 · Enumerar servidores
Recorre ['web', 'db', 'dns'] con enumerate(..., 1) y muestra número y nombre.

[:material-language-python: Abrir ejercicio_047.py](ut3/ejercicio_047.py){ .md-button }

### Ejercicio 048 · Buscar error
Recorre ['OK', 'OK', 'ERROR', 'OK'] y usa break para detenerte al encontrar ERROR.

[:material-language-python: Abrir ejercicio_048.py](ut3/ejercicio_048.py){ .md-button }

### Ejercicio 049 · Omitir temporales
Recorre una lista de archivos y utiliza continue para no mostrar los que terminan en .tmp.

[:material-language-python: Abrir ejercicio_049.py](ut3/ejercicio_049.py){ .md-button }

### Ejercicio 050 · Buscar puerto con else
Recorre [22, 53, 80, 443] buscando 3306 y usa for con else para indicar que no se encontró.

[:material-language-python: Abrir ejercicio_050.py](ut3/ejercicio_050.py){ .md-button }

### Ejercicio 051 · Tabla de multiplicar
Pide un número y muestra su tabla del 1 al 10 con for y range().

[:material-language-python: Abrir ejercicio_051.py](ut3/ejercicio_051.py){ .md-button }

### Ejercicio 052 · Suma de rango
Suma con un for los números del 1 al 100 y muestra el resultado.

[:material-language-python: Abrir ejercicio_052.py](ut3/ejercicio_052.py){ .md-button }

### Ejercicio 053 · Contar vocales
Pide una palabra y cuenta sus vocales recorriéndola con for.

[:material-language-python: Abrir ejercicio_053.py](ut3/ejercicio_053.py){ .md-button }

### Ejercicio 054 · Posiciones de caracteres
Pide una palabra y muestra índice y carácter usando enumerate().

[:material-language-python: Abrir ejercicio_054.py](ut3/ejercicio_054.py){ .md-button }

### Ejercicio 055 · Múltiplos de tres
Muestra los múltiplos de 3 entre 3 y 60 usando range().

[:material-language-python: Abrir ejercicio_055.py](ut3/ejercicio_055.py){ .md-button }

### Ejercicio 056 · Primer negativo
Recorre una lista de enteros y termina con break al encontrar el primer negativo.

[:material-language-python: Abrir ejercicio_056.py](ut3/ejercicio_056.py){ .md-button }

### Ejercicio 057 · Filtrar logs
Recorre una lista de nombres y muestra únicamente los que terminan en .log.

[:material-language-python: Abrir ejercicio_057.py](ut3/ejercicio_057.py){ .md-button }

### Ejercicio 058 · Racks y posiciones
Usa dos for anidados para mostrar racks 1–3 y posiciones 1–4.

[:material-language-python: Abrir ejercicio_058.py](ut3/ejercicio_058.py){ .md-button }

### Ejercicio 059 · Tabla cuadrada
Usa dos bucles for anidados para mostrar los productos de 1 a 5 por 1 a 5.

[:material-language-python: Abrir ejercicio_059.py](ut3/ejercicio_059.py){ .md-button }

### Ejercicio 060 · Buscar letra con else
Pide una palabra y una letra, recorre la palabra y utiliza for con else para avisar si la letra no aparece.

[:material-language-python: Abrir ejercicio_060.py](ut3/ejercicio_060.py){ .md-button }

## Depuración y errores

### Ejercicio 061 · ValueError básico
Intenta convertir 'abc' con int(), identifica el error y corrige el dato para que el programa funcione.

[:material-language-python: Abrir ejercicio_061.py](ut3/ejercicio_061.py){ .md-button }

### Ejercicio 062 · DEBUG de edad
Pide una edad como texto y muestra print(f'DEBUG: {edad=}') antes de convertirla a int().

[:material-language-python: Abrir ejercicio_062.py](ut3/ejercicio_062.py){ .md-button }

### Ejercicio 063 · Capturar entero
Pide un número y captura únicamente ValueError con try/except.

[:material-language-python: Abrir ejercicio_063.py](ut3/ejercicio_063.py){ .md-button }

### Ejercicio 064 · Assert de edad
Crea una edad negativa y usa assert para comprobar que sea mayor o igual que cero; después corrige el valor.

[:material-language-python: Abrir ejercicio_064.py](ut3/ejercicio_064.py){ .md-button }

### Ejercicio 065 · División segura
Pide dos números y captura ZeroDivisionError si el divisor es cero.

[:material-language-python: Abrir ejercicio_065.py](ut3/ejercicio_065.py){ .md-button }

### Ejercicio 066 · Conversión decimal
Pide un precio y captura ValueError si no puede convertirse a float.

[:material-language-python: Abrir ejercicio_066.py](ut3/ejercicio_066.py){ .md-button }

### Ejercicio 067 · Índice inexistente
Crea una lista de tres elementos, intenta acceder a una posición inexistente, identifica IndexError y corrige el acceso.

[:material-language-python: Abrir ejercicio_067.py](ut3/ejercicio_067.py){ .md-button }

### Ejercicio 068 · Clave inexistente
Crea un diccionario sencillo, intenta consultar una clave que no existe, identifica KeyError y corrige la consulta.

[:material-language-python: Abrir ejercicio_068.py](ut3/ejercicio_068.py){ .md-button }

### Ejercicio 069 · Nombre mal escrito
Escribe un ejemplo que provoque NameError por usar una variable con un nombre incorrecto y después arréglalo.

[:material-language-python: Abrir ejercicio_069.py](ut3/ejercicio_069.py){ .md-button }

### Ejercicio 070 · Traza de contador
Crea un bucle corto y añade un print DEBUG que muestre el valor del contador en cada vuelta.

[:material-language-python: Abrir ejercicio_070.py](ut3/ejercicio_070.py){ .md-button }

### Ejercicio 071 · Traza de acumulador
Suma varios números con un bucle y muestra el acumulador después de cada operación para seguir su evolución.

[:material-language-python: Abrir ejercicio_071.py](ut3/ejercicio_071.py){ .md-button }

### Ejercicio 072 · Comprobar porcentaje
Pide un porcentaje, conviértelo a entero y usa assert para comprobar que esté entre 0 y 100.

[:material-language-python: Abrir ejercicio_072.py](ut3/ejercicio_072.py){ .md-button }

### Ejercicio 073 · Comprobar puerto
Pide un puerto y usa assert para comprobar que esté entre 1 y 65535.

[:material-language-python: Abrir ejercicio_073.py](ut3/ejercicio_073.py){ .md-button }

### Ejercicio 074 · Dos conversiones
Pide dos enteros dentro de un mismo try y muestra un mensaje claro si cualquiera produce ValueError.

[:material-language-python: Abrir ejercicio_074.py](ut3/ejercicio_074.py){ .md-button }

### Ejercicio 075 · Conversión repetida
Usa while y try/except para repetir la petición hasta que el usuario introduzca un entero válido.

[:material-language-python: Abrir ejercicio_075.py](ut3/ejercicio_075.py){ .md-button }

### Ejercicio 076 · División y conversión
Pide dividendo y divisor como texto y trata por separado ValueError y ZeroDivisionError.

[:material-language-python: Abrir ejercicio_076.py](ut3/ejercicio_076.py){ .md-button }

### Ejercicio 077 · Depurar condición
Crea una condición que use por error = en lugar de ==, observa SyntaxError y corrígela.

[:material-language-python: Abrir ejercicio_077.py](ut3/ejercicio_077.py){ .md-button }

### Ejercicio 078 · Depurar indentación
Escribe un if con una línea mal indentada, observa IndentationError y corrige la estructura.

[:material-language-python: Abrir ejercicio_078.py](ut3/ejercicio_078.py){ .md-button }

### Ejercicio 079 · Mensaje de excepción
Captura ValueError como error y muestra el texto de la excepción junto con un mensaje propio.

[:material-language-python: Abrir ejercicio_079.py](ut3/ejercicio_079.py){ .md-button }

### Ejercicio 080 · Validación completa
Pide una edad, captura ValueError y, si la conversión funciona, usa assert para comprobar que no sea negativa.

[:material-language-python: Abrir ejercicio_080.py](ut3/ejercicio_080.py){ .md-button }

## Librerías sysadmin

### Ejercicio 081 · Versión de Python
Importa sys y muestra sys.version y sys.platform.

[:material-language-python: Abrir ejercicio_081.py](ut3/ejercicio_081.py){ .md-button }

### Ejercicio 082 · Argumento de usuario
Importa sys y usa sys.argv para mostrar un nombre recibido como argumento o un mensaje de uso si falta.

[:material-language-python: Abrir ejercicio_082.py](ut3/ejercicio_082.py){ .md-button }

### Ejercicio 083 · Variable PATH
Importa os y muestra la variable de entorno PATH con os.getenv().

[:material-language-python: Abrir ejercicio_083.py](ut3/ejercicio_083.py){ .md-button }

### Ejercicio 084 · Directorio con os
Importa os y muestra el directorio de trabajo actual.

[:material-language-python: Abrir ejercicio_084.py](ut3/ejercicio_084.py){ .md-button }

### Ejercicio 085 · Fecha actual
Importa datetime y muestra fecha y hora actuales con datetime.datetime.now().

[:material-language-python: Abrir ejercicio_085.py](ut3/ejercicio_085.py){ .md-button }

### Ejercicio 086 · Fecha de hoy
Importa datetime y muestra únicamente la fecha actual.

[:material-language-python: Abrir ejercicio_086.py](ut3/ejercicio_086.py){ .md-button }

### Ejercicio 087 · Backup de ayer
Importa datetime y genera un nombre backup_YYYY_MM_DD.zip correspondiente a ayer usando datetime.timedelta().

[:material-language-python: Abrir ejercicio_087.py](ut3/ejercicio_087.py){ .md-button }

### Ejercicio 088 · Dentro de una semana
Importa datetime y calcula qué fecha será dentro de siete días.

[:material-language-python: Abrir ejercicio_088.py](ut3/ejercicio_088.py){ .md-button }

### Ejercicio 089 · Sistema operativo
Importa platform y muestra el sistema operativo y su versión.

[:material-language-python: Abrir ejercicio_089.py](ut3/ejercicio_089.py){ .md-button }

### Ejercicio 090 · Información de máquina
Importa platform y muestra machine() y processor().

[:material-language-python: Abrir ejercicio_090.py](ut3/ejercicio_090.py){ .md-button }

### Ejercicio 091 · Directorio actual
Importa pathlib y muestra el directorio actual con pathlib.Path.cwd().

[:material-language-python: Abrir ejercicio_091.py](ut3/ejercicio_091.py){ .md-button }

### Ejercicio 092 · Crear carpeta logs
Importa pathlib, comprueba si existe logs y créala si no existe.

[:material-language-python: Abrir ejercicio_092.py](ut3/ejercicio_092.py){ .md-button }

### Ejercicio 093 · Existe un archivo
Importa pathlib y comprueba con exists() si existe config.ini.

[:material-language-python: Abrir ejercicio_093.py](ut3/ejercicio_093.py){ .md-button }

### Ejercicio 094 · Listar Python
Importa pathlib, recorre la carpeta actual con iterdir() y muestra solo los archivos .py.

[:material-language-python: Abrir ejercicio_094.py](ut3/ejercicio_094.py){ .md-button }

### Ejercicio 095 · Tamaño de archivo
Importa pathlib y, si existe informe.log, muestra su tamaño con stat().st_size.

[:material-language-python: Abrir ejercicio_095.py](ut3/ejercicio_095.py){ .md-button }

### Ejercicio 096 · Buscar logs
Importa pathlib y utiliza glob('*.log') para mostrar los .log de la carpeta actual.

[:material-language-python: Abrir ejercicio_096.py](ut3/ejercicio_096.py){ .md-button }

### Ejercicio 097 · Buscar logs recursivos
Importa pathlib y utiliza rglob('*.log') para buscar también en subcarpetas.

[:material-language-python: Abrir ejercicio_097.py](ut3/ejercicio_097.py){ .md-button }

### Ejercicio 098 · Uso de disco
Importa shutil, consulta disk_usage('/') y muestra espacio total, usado y libre.

[:material-language-python: Abrir ejercicio_098.py](ut3/ejercicio_098.py){ .md-button }

### Ejercicio 099 · Copiar archivo
Importa pathlib y shutil. Si existe backup.zip, crea copias si hace falta y copia allí el archivo.

[:material-language-python: Abrir ejercicio_099.py](ut3/ejercicio_099.py){ .md-button }

### Ejercicio 100 · Mover archivo
Importa pathlib y shutil. Si existe temporal.log, crea archivo si hace falta y mueve allí temporal.log.

[:material-language-python: Abrir ejercicio_100.py](ut3/ejercicio_100.py){ .md-button }

## Ejercicios mixtos

### Ejercicio 101 · Inventario Python
Combina pathlib, datetime, for e if para mostrar la fecha actual y contar cuántos archivos .py hay en la carpeta actual.

[:material-language-python: Abrir ejercicio_101.py](ut3/ejercicio_101.py){ .md-button }

### Ejercicio 102 · Alerta de disco
Usa shutil.disk_usage(), calcula el porcentaje usado y clasifícalo con if como NORMAL, AVISO o CRÍTICO.

[:material-language-python: Abrir ejercicio_102.py](ut3/ejercicio_102.py){ .md-button }

### Ejercicio 103 · Listado numerado de logs
Usa pathlib para obtener archivos .log y enumerate() para mostrarlos numerados.

[:material-language-python: Abrir ejercicio_103.py](ut3/ejercicio_103.py){ .md-button }

### Ejercicio 104 · Buscar configuración
Usa pathlib.rglob() y un for para buscar archivos .conf; usa for...else para avisar si no aparece ninguno.

[:material-language-python: Abrir ejercicio_104.py](ut3/ejercicio_104.py){ .md-button }

### Ejercicio 105 · Backup con fecha
Usa pathlib, shutil y datetime para copiar config.ini a una carpeta backup con la fecha actual en el nombre del archivo.

[:material-language-python: Abrir ejercicio_105.py](ut3/ejercicio_105.py){ .md-button }

### Ejercicio 106 · Limpiar temporales
Usa pathlib para recorrer archivos .tmp y un if para mostrar cuáles eliminarías; no los borres.

[:material-language-python: Abrir ejercicio_106.py](ut3/ejercicio_106.py){ .md-button }

### Ejercicio 107 · Menú del sistema
Crea un menú con while que permita mostrar platform.system(), pathlib.Path.cwd() o salir.

[:material-language-python: Abrir ejercicio_107.py](ut3/ejercicio_107.py){ .md-button }

### Ejercicio 108 · Validador de puerto
Usa while y try/except para pedir un puerto entero hasta que sea válido; después clasifícalo como privilegiado o no privilegiado.

[:material-language-python: Abrir ejercicio_108.py](ut3/ejercicio_108.py){ .md-button }

### Ejercicio 109 · Argumentos y archivo
Lee una ruta desde sys.argv, conviértela en pathlib.Path y muestra con if si existe y si es archivo o directorio.

[:material-language-python: Abrir ejercicio_109.py](ut3/ejercicio_109.py){ .md-button }

### Ejercicio 110 · Logs grandes
Usa pathlib.rglob('*.log'), un for y stat().st_size para mostrar solo los logs mayores de un tamaño indicado por el usuario.

[:material-language-python: Abrir ejercicio_110.py](ut3/ejercicio_110.py){ .md-button }

### Ejercicio 111 · Resumen de extensiones
Recorre con pathlib los archivos de una carpeta y cuenta con condicionales cuántos son .py, .txt y .log.

[:material-language-python: Abrir ejercicio_111.py](ut3/ejercicio_111.py){ .md-button }

### Ejercicio 112 · Comprobar espacio para copia
Pide el tamaño de una copia, consulta shutil.disk_usage() y usa if para indicar si cabe en el espacio libre.

[:material-language-python: Abrir ejercicio_112.py](ut3/ejercicio_112.py){ .md-button }

### Ejercicio 113 · Fecha límite
Pide un número de días, captura ValueError y usa datetime.timedelta() para mostrar la fecha límite resultante.

[:material-language-python: Abrir ejercicio_113.py](ut3/ejercicio_113.py){ .md-button }

### Ejercicio 114 · Servidores numerados
Recorre una lista de hostnames con enumerate() y clasifica cada uno con if según empiece por PROD-, TEST- u otro prefijo.

[:material-language-python: Abrir ejercicio_114.py](ut3/ejercicio_114.py){ .md-button }

### Ejercicio 115 · Búsqueda con intentos
Usa while para pedir una extensión válida y después pathlib.rglob() para buscarla recursivamente y contar resultados.

[:material-language-python: Abrir ejercicio_115.py](ut3/ejercicio_115.py){ .md-button }

### Ejercicio 116 · Informe del equipo
Combina platform, datetime y shutil para mostrar sistema, fecha y porcentaje de disco utilizado.

[:material-language-python: Abrir ejercicio_116.py](ut3/ejercicio_116.py){ .md-button }

### Ejercicio 117 · Procesar argumentos
Recorre sys.argv[1:] con for y muestra para cada argumento si representa una ruta existente usando pathlib.

[:material-language-python: Abrir ejercicio_117.py](ut3/ejercicio_117.py){ .md-button }

### Ejercicio 118 · Copia condicionada
Pide confirmación con while; si la respuesta es s y existe origen.txt, usa shutil.copy() para copiarlo a copia.txt.

[:material-language-python: Abrir ejercicio_118.py](ut3/ejercicio_118.py){ .md-button }

### Ejercicio 119 · Auditoría sencilla
Recorre archivos con pathlib, omite con continue los ocultos y muestra nombre, extensión y tamaño de los demás.

[:material-language-python: Abrir ejercicio_119.py](ut3/ejercicio_119.py){ .md-button }

### Ejercicio 120 · Mini diagnóstico
Crea un programa que combine sys, platform, pathlib y shutil para mostrar versión de Python, sistema, directorio actual, número de archivos y espacio libre.

[:material-language-python: Abrir ejercicio_120.py](ut3/ejercicio_120.py){ .md-button }
