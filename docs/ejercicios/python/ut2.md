# UT2 · Objetos predefinidos y cadenas

50 ejercicios para practicar esta unidad.

!!! note "Organización"
    **1–20:** básicos · **21–40:** intermedios · **41–50:** repaso tipo examen.

## Ejercicio 01 · Tres tipos de cadenas
Crea una cadena con comillas simples, otra con dobles y otra multilínea. Imprime las tres.

## Ejercicio 02 · Nombre completo
Pide nombre y apellidos y construye una frase usando un f-string.

## Ejercicio 03 · Repetir palabra
Pide una palabra y un número y repítela ese número de veces.

## Ejercicio 04 · Primer y último carácter
Pide una palabra y muestra su primer y último carácter.

## Ejercicio 05 · Cinco primeros
Pide una frase y muestra sus cinco primeros caracteres.

## Ejercicio 06 · Cinco últimos
Pide una frase y muestra sus cinco últimos caracteres.

## Ejercicio 07 · Cadena invertida
Pide una palabra y muéstrala al revés usando slicing.

## Ejercicio 08 · Posiciones pares
Pide una frase y muestra los caracteres en posiciones pares usando slicing.

## Ejercicio 09 · Longitud de frase
Pide una frase y muestra cuántos caracteres contiene.

## Ejercicio 10 · Mayúsculas
Pide una frase y muéstrala en mayúsculas.

## Ejercicio 11 · Minúsculas
Pide una frase y muéstrala en minúsculas.

## Ejercicio 12 · Formato título
Pide un nombre completo en minúsculas y muéstralo con formato de título.

## Ejercicio 13 · Eliminar bordes
Pide un texto con posibles espacios exteriores y aplica strip().

## Ejercicio 14 · Cambiar separadores
Pide una fecha AAAA_MM_DD y cambia los guiones bajos por guiones.

## Ejercicio 15 · Contar letras
Pide una frase y una letra y cuenta sus apariciones con count().

## Ejercicio 16 · Buscar arroba
Pide un email y muestra la posición de @ usando find().

## Ejercicio 17 · Extraer usuario de email
Pide un email y extrae la parte anterior a @ usando find() y slicing.

## Ejercicio 18 · Extraer dominio de email
Pide un email y extrae todo lo posterior a @.

## Ejercicio 19 · Comprobar prefijo PC
Pide un hostname y muestra True o False según empiece por 'PC-' usando startswith().

## Ejercicio 20 · Comprobar extensión
Pide un archivo y muestra True o False según termine en '.txt' usando endswith().

## Ejercicio 21 · Pertenencia simple
Pide una palabra y muestra si contiene 'a' usando in.

## Ejercicio 22 · Palabra dentro de frase
Pide una frase y una palabra y muestra si aparece dentro.

## Ejercicio 23 · Solo números
Pide un texto y comprueba con isdigit() si todos sus caracteres son numéricos.

## Ejercicio 24 · Solo letras
Pide un texto y comprueba con isalpha() si contiene solo letras.

## Ejercicio 25 · Alfanumérico
Pide un texto y comprueba con isalnum() si es alfanumérico.

## Ejercicio 26 · Todo mayúsculas
Pide una cadena y comprueba si está completamente en mayúsculas.

## Ejercicio 27 · Todo minúsculas
Pide una cadena y comprueba si está completamente en minúsculas.

## Ejercicio 28 · Normalizar hostname
Convierte '  pc -- laboratorio -  12  ' en 'PC-LABORATORIO-12' sin condicionales ni bucles.

## Ejercicio 29 · Normalizar código
Convierte '  srv -- web -  03  ' en 'SRV-WEB-03' usando strip(), replace() y upper().

## Ejercicio 30 · Extraer aula
De 'PC-AULA-27', extrae 'AULA' con find() y slicing.

## Ejercicio 31 · Extraer número de equipo
De 'PC-AULA-27', extrae '27'.

## Ejercicio 32 · Unidad de Windows
De la ruta 'D:\\Usuarios\\ana\\Documentos', extrae la letra de unidad.

## Ejercicio 33 · Usuario de ruta Windows
De 'C:\\Users\\maria\\Desktop\\proyecto', extrae 'maria' con find()/index() y slicing.

## Ejercicio 34 · Carpeta de ruta Windows
De esa misma ruta, extrae 'Desktop'.

## Ejercicio 35 · Primer octeto IPv4
De '  10.20.30.40  ', elimina espacios y extrae el primer octeto.

## Ejercicio 36 · Último octeto IPv4
De '172.16.5.200', extrae el último octeto con rfind() o métodos y slicing.

## Ejercicio 37 · Contar puntos IPv4
Pide una IPv4 y muestra cuántos puntos contiene.

## Ejercicio 38 · Fecha de backup
De 'backup_2026_10_29.tar.gz', muestra la fecha como '29-10-2026'.

## Ejercicio 39 · Cambiar extensión backup
Cambia 'backup_2026_10_29.tar.gz' para obtener un nombre terminado en '.zip' usando replace().

## Ejercicio 40 · Nombre de log
De 'servidor_web_2026.log', extrae 'servidor_web'.

## Ejercicio 41 · Iniciales
Pide nombre y dos apellidos y muestra sus tres iniciales en mayúsculas.

## Ejercicio 42 · Nombre sin espacios
Pide un nombre completo y cuenta sus caracteres sin espacios usando replace() y len().

## Ejercicio 43 · Mensaje con escapes
Pide un mensaje y muéstralo entre comillas dobles, con una tabulación y un salto de línea.

## Ejercicio 44 · Código Unicode
Pide un carácter y muestra su código Unicode usando ord().

## Ejercicio 45 · Carácter desde código
Pide un número entre 32 y 126 y muestra el carácter usando chr().

## Ejercicio 46 · Comparar palabras
Pide dos palabras y muestra True o False según sean iguales.

## Ejercicio 47 · Orden lexicográfico
Pide dos palabras y muestra si la primera es mayor lexicográficamente.

## Ejercicio 48 · Contraseña simple aleatoria
Genera una contraseña de 8 caracteres: 4 letras y 4 dígitos usando string y random, sin bucles.

## Ejercicio 49 · Código de inventario aleatorio
Genera un código de 3 letras mayúsculas y 3 dígitos usando string y random, sin bucles.

## Ejercicio 50 · Username normalizado
Con nombre='  José  ' y apellido='  Martínez  ', crea un username con 3 letras de cada uno, en minúsculas y sin tildes, más dos dígitos aleatorios. Sin condicionales ni bucles.