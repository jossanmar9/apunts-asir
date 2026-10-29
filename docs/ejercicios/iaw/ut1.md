# UT1 · Entorno de implantación web

Banco de **60 ejercicios adicionales** para practicar. No incluyen solución y están pensados para complementar, no copiar, las actividades de clase.

[:material-download: Descargar los 60 ejercicios de UT1](../descargas/iaw-ut1.zip){ .md-button .md-button--primary }

## Ejercicio 001 · Estático o dinámico

Clasifica varios recursos web como estáticos, dinámicos o mixtos y justifica cada decisión.

[:material-code-tags: Abrir ejercicio_001.txt](ut1/ejercicio_001.txt){ .md-button }

## Ejercicio 002 · Ruta de una petición

Explica paso a paso qué ocurre desde que el navegador solicita index.php hasta que recibe HTML.

[:material-code-tags: Abrir ejercicio_002.txt](ut1/ejercicio_002.txt){ .md-button }

## Ejercicio 003 · Papel de Nginx

Describe qué peticiones puede resolver Nginx directamente y cuáles debe reenviar a PHP-FPM.

[:material-code-tags: Abrir ejercicio_003.txt](ut1/ejercicio_003.txt){ .md-button }

## Ejercicio 004 · Papel de PHP-FPM

Explica por qué PHP-FPM no sustituye a Nginx y qué devuelve después de ejecutar un script.

[:material-code-tags: Abrir ejercicio_004.txt](ut1/ejercicio_004.txt){ .md-button }

## Ejercicio 005 · Papel de MariaDB

Indica qué información tendría sentido guardar de forma persistente en una aplicación web sencilla.

[:material-code-tags: Abrir ejercicio_005.txt](ut1/ejercicio_005.txt){ .md-button }

## Ejercicio 006 · Código HTTP

Relaciona situaciones habituales con 200, 301/302, 403, 404 y 500.

[:material-code-tags: Abrir ejercicio_006.txt](ut1/ejercicio_006.txt){ .md-button }

## Ejercicio 007 · Petición HTTP

Identifica método, ruta y cabeceras en una petición HTTP de ejemplo.

[:material-code-tags: Abrir ejercicio_007.txt](ut1/ejercicio_007.txt){ .md-button }

## Ejercicio 008 · Respuesta HTTP

Identifica estado, cabeceras y cuerpo en una respuesta HTTP de ejemplo.

[:material-code-tags: Abrir ejercicio_008.txt](ut1/ejercicio_008.txt){ .md-button }

## Ejercicio 009 · GET y POST

Elige GET o POST para cinco situaciones web y justifica la elección.

[:material-code-tags: Abrir ejercicio_009.txt](ut1/ejercicio_009.txt){ .md-button }

## Ejercicio 010 · Diagnóstico 404

Propón una secuencia de comprobaciones cuando Nginx devuelve 404.

[:material-code-tags: Abrir ejercicio_010.txt](ut1/ejercicio_010.txt){ .md-button }

## Ejercicio 011 · Diagnóstico 500

Propón una secuencia de comprobaciones ante un error 500 en una página PHP.

[:material-code-tags: Abrir ejercicio_011.txt](ut1/ejercicio_011.txt){ .md-button }

## Ejercicio 012 · Puerto publicado

Explica qué significa 8080:80 y desde qué URL accederías al servicio.

[:material-code-tags: Abrir ejercicio_012.txt](ut1/ejercicio_012.txt){ .md-button }

## Ejercicio 013 · Conflicto de puerto

Un contenedor no arranca porque 8080 está ocupado. Indica cómo diagnosticarlo y una solución.

[:material-code-tags: Abrir ejercicio_013.txt](ut1/ejercicio_013.txt){ .md-button }

## Ejercicio 014 · Primer contenedor Nginx

Escribe y explica un docker run que publique Nginx en un puerto no estándar.

[:material-code-tags: Abrir ejercicio_014.txt](ut1/ejercicio_014.txt){ .md-button }

## Ejercicio 015 · Ciclo de un contenedor

Practica docker ps, logs, stop, start y rm sobre un contenedor de prueba.

[:material-code-tags: Abrir ejercicio_015.txt](ut1/ejercicio_015.txt){ .md-button }

## Ejercicio 016 · Bind mount

Monta una carpeta local con un index.html dentro de Nginx y comprueba que los cambios se reflejan.

[:material-code-tags: Abrir ejercicio_016.txt](ut1/ejercicio_016.txt){ .md-button }

## Ejercicio 017 · Montaje de solo lectura

Explica y prueba el efecto de :ro en un volumen de Nginx.

[:material-code-tags: Abrir ejercicio_017.txt](ut1/ejercicio_017.txt){ .md-button }

## Ejercicio 018 · Imagen frente a contenedor

Explica con un ejemplo práctico la diferencia entre una imagen y un contenedor.

[:material-code-tags: Abrir ejercicio_018.txt](ut1/ejercicio_018.txt){ .md-button }

## Ejercicio 019 · Dockerfile PHP

Diseña un Dockerfile mínimo basado en PHP-FPM y explica cada instrucción.

[:material-code-tags: Abrir ejercicio_019.txt](ut1/ejercicio_019.txt){ .md-button }

## Ejercicio 020 · Extensión PDO MySQL

Investiga qué necesita una imagen PHP para conectar mediante PDO con MariaDB y documenta la decisión.

[:material-code-tags: Abrir ejercicio_020.txt](ut1/ejercicio_020.txt){ .md-button }

## Ejercicio 021 · Tres servicios

Escribe el esqueleto de un compose.yaml con nginx, php y db.

[:material-code-tags: Abrir ejercicio_021.txt](ut1/ejercicio_021.txt){ .md-button }

## Ejercicio 022 · Dependencias

Añade depends_on donde tenga sentido y explica qué garantiza y qué no garantiza.

[:material-code-tags: Abrir ejercicio_022.txt](ut1/ejercicio_022.txt){ .md-button }

## Ejercicio 023 · Volúmenes Compose

Monta app/ en Nginx y PHP indicando por qué ambos necesitan acceder al código.

[:material-code-tags: Abrir ejercicio_023.txt](ut1/ejercicio_023.txt){ .md-button }

## Ejercicio 024 · Configuración Nginx

Monta default.conf desde el host y explica por qué es útil mantenerlo en el proyecto.

[:material-code-tags: Abrir ejercicio_024.txt](ut1/ejercicio_024.txt){ .md-button }

## Ejercicio 025 · FastCGI

Identifica la directiva de Nginx que permite enviar PHP al servicio PHP-FPM y explica el flujo.

[:material-code-tags: Abrir ejercicio_025.txt](ut1/ejercicio_025.txt){ .md-button }

## Ejercicio 026 · Nombre de servicio

Explica por qué PHP puede usar db como host de MariaDB dentro de Compose.

[:material-code-tags: Abrir ejercicio_026.txt](ut1/ejercicio_026.txt){ .md-button }

## Ejercicio 027 · No usar localhost

Razona por qué localhost desde el contenedor PHP no apunta al contenedor de base de datos.

[:material-code-tags: Abrir ejercicio_027.txt](ut1/ejercicio_027.txt){ .md-button }

## Ejercicio 028 · Variables de entorno

Pasa DB_HOST, DB_NAME, DB_USER y DB_PASSWORD al servicio PHP.

[:material-code-tags: Abrir ejercicio_028.txt](ut1/ejercicio_028.txt){ .md-button }

## Ejercicio 029 · .env.example

Crea una plantilla .env.example sin secretos reales y explica para qué sirve.

[:material-code-tags: Abrir ejercicio_029.txt](ut1/ejercicio_029.txt){ .md-button }

## Ejercicio 030 · .env y Git

Prepara .gitignore para evitar publicar el .env real.

[:material-code-tags: Abrir ejercicio_030.txt](ut1/ejercicio_030.txt){ .md-button }

## Ejercicio 031 · environment y env_file

Compara las dos formas de proporcionar variables a un servicio Compose.

[:material-code-tags: Abrir ejercicio_031.txt](ut1/ejercicio_031.txt){ .md-button }

## Ejercicio 032 · Inicialización SQL

Crea un init.sql que genere una tabla sencilla e inserte un registro inicial.

[:material-code-tags: Abrir ejercicio_032.txt](ut1/ejercicio_032.txt){ .md-button }

## Ejercicio 033 · Volumen de MariaDB

Añade persistencia para la base de datos y comprueba qué ocurre al recrear el contenedor.

[:material-code-tags: Abrir ejercicio_033.txt](ut1/ejercicio_033.txt){ .md-button }

## Ejercicio 034 · Reinicializar base

Explica por qué un init.sql puede no volver a ejecutarse si ya existe el volumen de datos.

[:material-code-tags: Abrir ejercicio_034.txt](ut1/ejercicio_034.txt){ .md-button }

## Ejercicio 035 · Construir y levantar

Practica docker compose up -d --build y explica cuándo necesitas --build.

[:material-code-tags: Abrir ejercicio_035.txt](ut1/ejercicio_035.txt){ .md-button }

## Ejercicio 036 · Estado del stack

Usa docker compose ps para comprobar el estado de los tres servicios.

[:material-code-tags: Abrir ejercicio_036.txt](ut1/ejercicio_036.txt){ .md-button }

## Ejercicio 037 · Logs completos

Obtén los logs del stack e identifica qué líneas pertenecen a cada servicio.

[:material-code-tags: Abrir ejercicio_037.txt](ut1/ejercicio_037.txt){ .md-button }

## Ejercicio 038 · Logs de un servicio

Sigue en tiempo real únicamente los logs de PHP o Nginx.

[:material-code-tags: Abrir ejercicio_038.txt](ut1/ejercicio_038.txt){ .md-button }

## Ejercicio 039 · Entrar en un contenedor

Usa docker compose exec para inspeccionar rutas y archivos dentro de un servicio.

[:material-code-tags: Abrir ejercicio_039.txt](ut1/ejercicio_039.txt){ .md-button }

## Ejercicio 040 · Comprobar variables

Comprueba desde el contenedor PHP que las variables de entorno esperadas existen.

[:material-code-tags: Abrir ejercicio_040.txt](ut1/ejercicio_040.txt){ .md-button }

## Ejercicio 041 · Conexión PHP-MariaDB

Crea una prueba mínima que confirme que PHP puede abrir una conexión PDO con db.

[:material-code-tags: Abrir ejercicio_041.txt](ut1/ejercicio_041.txt){ .md-button }

## Ejercicio 042 · Error de credenciales

Provoca una contraseña incorrecta y utiliza los logs para localizar el problema.

[:material-code-tags: Abrir ejercicio_042.txt](ut1/ejercicio_042.txt){ .md-button }

## Ejercicio 043 · Error de host

Cambia temporalmente DB_HOST por un nombre incorrecto y compara el error con el de credenciales.

[:material-code-tags: Abrir ejercicio_043.txt](ut1/ejercicio_043.txt){ .md-button }

## Ejercicio 044 · Error de Nginx-PHP

Rompe temporalmente el destino FastCGI y determina qué evidencia aparece en los logs.

[:material-code-tags: Abrir ejercicio_044.txt](ut1/ejercicio_044.txt){ .md-button }

## Ejercicio 045 · Servicio no disponible

Detén db y observa cómo se comporta la aplicación; documenta el diagnóstico.

[:material-code-tags: Abrir ejercicio_045.txt](ut1/ejercicio_045.txt){ .md-button }

## Ejercicio 046 · Reproducibilidad

Explica qué archivos necesitaría otra persona para levantar el mismo entorno desde cero.

[:material-code-tags: Abrir ejercicio_046.txt](ut1/ejercicio_046.txt){ .md-button }

## Ejercicio 047 · Seguridad de puertos

Decide qué servicios necesitan publicar puertos al host y cuáles pueden quedar solo en la red interna.

[:material-code-tags: Abrir ejercicio_047.txt](ut1/ejercicio_047.txt){ .md-button }

## Ejercicio 048 · Usuario de base de datos

Explica por qué la aplicación no debería conectarse habitualmente como root.

[:material-code-tags: Abrir ejercicio_048.txt](ut1/ejercicio_048.txt){ .md-button }

## Ejercicio 049 · Secretos

Localiza posibles secretos en una configuración de ejemplo y propón dónde deberían guardarse.

[:material-code-tags: Abrir ejercicio_049.txt](ut1/ejercicio_049.txt){ .md-button }

## Ejercicio 050 · Documentar el stack

Escribe una sección README con requisitos, arranque, comprobación, parada y solución de problemas.

[:material-code-tags: Abrir ejercicio_050.txt](ut1/ejercicio_050.txt){ .md-button }

## Ejercicio 051 · Mapa del stack

Dibuja en texto el recorrido navegador → Nginx → PHP-FPM → MariaDB y anota el protocolo o función de cada salto.

[:material-code-tags: Abrir ejercicio_051.txt](ut1/ejercicio_051.txt){ .md-button }

## Ejercicio 052 · Prueba de estáticos

Añade un archivo CSS y comprueba que Nginx puede servirlo sin ejecutar PHP.

[:material-code-tags: Abrir ejercicio_052.txt](ut1/ejercicio_052.txt){ .md-button }

## Ejercicio 053 · Prueba de PHP

Crea un script PHP mínimo y demuestra que el navegador recibe el resultado, no el código fuente.

[:material-code-tags: Abrir ejercicio_053.txt](ut1/ejercicio_053.txt){ .md-button }

## Ejercicio 054 · Página de estado

Crea una página de diagnóstico que indique si PHP funciona y si puede conectar con la base de datos.

[:material-code-tags: Abrir ejercicio_054.txt](ut1/ejercicio_054.txt){ .md-button }

## Ejercicio 055 · Cambio de puerto

Cambia solo el puerto del host sin modificar el puerto interno de Nginx y comprueba el resultado.

[:material-code-tags: Abrir ejercicio_055.txt](ut1/ejercicio_055.txt){ .md-button }

## Ejercicio 056 · Dos stacks

Plantea cómo ejecutar dos copias del proyecto simultáneamente evitando conflictos de puertos y nombres.

[:material-code-tags: Abrir ejercicio_056.txt](ut1/ejercicio_056.txt){ .md-button }

## Ejercicio 057 · Compose config

Usa docker compose config para revisar la configuración resultante y detectar variables ausentes.

[:material-code-tags: Abrir ejercicio_057.txt](ut1/ejercicio_057.txt){ .md-button }

## Ejercicio 058 · Recrear servicios

Compara restart con down/up y explica en qué situaciones no producen el mismo efecto.

[:material-code-tags: Abrir ejercicio_058.txt](ut1/ejercicio_058.txt){ .md-button }

## Ejercicio 059 · Evidencia técnica

Prepara una lista de comandos y capturas/resultados que demostrarían que el stack funciona correctamente.

[:material-code-tags: Abrir ejercicio_059.txt](ut1/ejercicio_059.txt){ .md-button }

## Ejercicio 060 · Caso final UT1

Monta desde una carpeta vacía un stack Nginx + PHP-FPM + MariaDB que muestre un registro inicial y documenta el diagnóstico de al menos un fallo provocado.

[:material-code-tags: Abrir ejercicio_060.txt](ut1/ejercicio_060.txt){ .md-button }
