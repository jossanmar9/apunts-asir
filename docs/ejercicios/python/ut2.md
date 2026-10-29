# UT2 · Ejercicios adicionales

50 ejercicios distintos de los ejercicios originales de practicar y entregar.

!!! note "Organización"
    **1–20:** básicos · **21–40:** intermedios · **41–50:** repaso.

## Ejercicio 01 · Código de inventario
Dado el texto '  srv-042  ', elimina espacios de los extremos y muéstralo en mayúsculas.

## Ejercicio 02 · Etiqueta de rack
Pide rack y posición y construye con f-string una etiqueta como 'RACK-03-POS-12'.

## Ejercicio 03 · Banner repetido
Pide una palabra y muestra esa palabra repetida cinco veces.

## Ejercicio 04 · Extremos de una palabra
Pide una palabra y muestra sus dos primeros y sus dos últimos caracteres.

## Ejercicio 05 · Centro de una etiqueta
Dada la cadena 'SERVIDOR-DB-01', extrae mediante slicing la parte 'DB'.

## Ejercicio 06 · Invertir identificador
Pide un identificador y muéstralo al revés usando slicing.

## Ejercicio 07 · Caracteres alternos
Pide una cadena y muestra los caracteres situados cada tres posiciones usando slicing.

## Ejercicio 08 · Quitar prefijo
Dada 'USR-jvicente', muestra solo 'jvicente' mediante slicing.

## Ejercicio 09 · Longitud sin bordes
Pide un texto con espacios al principio o final y muestra la longitud después de strip().

## Ejercicio 10 · Ciudad normalizada
Pide una ciudad y muestra el texto con strip() y title().

## Ejercicio 11 · Código en minúsculas
Pide un código y muéstralo completamente en minúsculas.

## Ejercicio 12 · Contar guiones
Dada una etiqueta de red, muestra cuántos guiones contiene usando count().

## Ejercicio 13 · Contar barras
Dada una ruta Linux, cuenta cuántos caracteres '/' contiene.

## Ejercicio 14 · Posición de dos puntos
Dada 'usuario:grupo', localiza la posición de ':' con find().

## Ejercicio 15 · Separar usuario y grupo
Dada 'operador:admins', usa find() y slicing para obtener las dos partes.

## Ejercicio 16 · Extraer protocolo
Dada 'https://servidor.local', extrae 'https' localizando '://'.

## Ejercicio 17 · Extraer host de URL
Dada 'https://intranet.local/panel', obtén 'intranet.local' con find() y slicing.

## Ejercicio 18 · Extraer recurso de URL
Dada 'https://intranet.local/panel', extrae '/panel' mediante slicing.

## Ejercicio 19 · Nombre sin extensión
Dado 'informe_final.txt', muestra el nombre sin '.txt' usando slicing.

## Ejercicio 20 · Cambiar extensión
Dado 'datos.csv', genera el nombre 'datos.bak' usando slicing y concatenación.

## Ejercicio 21 · Comprobar sufijo log
Pide un nombre de fichero y muestra True o False según termine en '.log' usando endswith().

## Ejercicio 22 · Comprobar prefijo SRV
Pide una etiqueta y muestra True o False según empiece por 'SRV-' usando startswith().

## Ejercicio 23 · Buscar dominio local
Pide una dirección y muestra si contiene '.local' usando in.

## Ejercicio 24 · Buscar arroba
Pide una cadena y muestra si contiene '@' usando in.

## Ejercicio 25 · Solo letras
Pide un alias y muestra el resultado de isalpha().

## Ejercicio 26 · Alias alfanumérico
Pide un alias y muestra el resultado de isalnum().

## Ejercicio 27 · Código en minúsculas válido
Pide una cadena y muestra el resultado de islower().

## Ejercicio 28 · Código en mayúsculas válido
Pide una cadena y muestra el resultado de isupper().

## Ejercicio 29 · Número de serie
Pide un número de serie como texto y muestra el resultado de isdigit().

## Ejercicio 30 · Limpiar separadores
Dado 'AA__BB__CC', sustituye '__' por '-' usando replace().

## Ejercicio 31 · Cambiar separador de fecha
Dada '2026/10/29', conviértela a '2026-10-29' usando replace().

## Ejercicio 32 · Eliminar espacios internos
Dado 'A B C 1 2 3', elimina todos los espacios con replace().

## Ejercicio 33 · Ocultar palabra
Pide una frase y una palabra; sustituye esa palabra por '***' con replace(), sin condicionales.

## Ejercicio 34 · Siguiente Unicode
Pide un carácter, muestra su código Unicode y el carácter correspondiente al código siguiente.

## Ejercicio 35 · Desplazar carácter
Pide una letra, obtén su código con ord(), suma 1 y muestra el carácter con chr().

## Ejercicio 36 · Ficha de servidor
Pide nombre, IP y sistema y crea con f-string: 'Servidor X | IP Y | SO Z'.

## Ejercicio 37 · Mensaje tabulado
Crea una cadena que muestre tres campos en líneas distintas usando saltos de línea y tabulaciones.

## Ejercicio 38 · Comillas en mensaje
Pide una palabra y muéstrala entre comillas dobles dentro de una frase.

## Ejercicio 39 · Tres líneas
Pide tres textos cortos y construye una única cadena multilínea con ellos.

## Ejercicio 40 · Primer bloque
Pide una cadena de al menos 9 caracteres y muestra sus primeros 3 caracteres.

## Ejercicio 41 · Último bloque
Pide una cadena de al menos 9 caracteres y muestra sus últimos 3 caracteres.

## Ejercicio 42 · Segmento interior
Dada 'ABC-123-XYZ', extrae '123' usando find() y slicing.

## Ejercicio 43 · Nombre y versión
Dada 'app:2.7.4', extrae por slicing el nombre 'app' y la versión '2.7.4'.

## Ejercicio 44 · Usuario de cuenta
Dada una cuenta con formato 'DOMINIO\alumno', extrae solo 'alumno'.

## Ejercicio 45 · Dominio de cuenta
Dada una cuenta con formato 'DOMINIO\alumno', extrae solo 'DOMINIO'.

## Ejercicio 46 · Puerto en dirección
Dada 'servidor.local:8080', extrae host y puerto usando find() y slicing.

## Ejercicio 47 · Generar PIN textual
Usa random y string.digits para construir un PIN de 4 dígitos sin bucles.

## Ejercicio 48 · Código de soporte
Usa random y string.ascii_uppercase para generar 3 letras y después 3 dígitos, sin bucles.

## Ejercicio 49 · Token corto
Genera un token de 8 caracteres alternando letra y dígito cuatro veces, usando random y string sin bucles.

## Ejercicio 50 · Normalizar alias
Dado '  José.Pérez  ', limpia bordes, pasa a minúsculas y sustituye vocales acentuadas con replace().
