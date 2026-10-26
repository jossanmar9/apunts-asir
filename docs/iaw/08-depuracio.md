# UT2 · 5. Depurar una aplicación sin probar al azar

## Sigue el recorrido de la petición

Cuando una página no hace lo que esperas, separa tres preguntas: **¿ha llegado la petición?**, **¿qué ha recibido PHP?** y **¿qué respuesta ha generado?**. Un formulario que no conserva un valor no se diagnostica igual que un contenedor que no arranca.

## Empezar por una pregunta concreta

«La web no funciona» incluye demasiados problemas posibles. Convierte esa frase en una observación: no conecta, recibe un estado inesperado, falta un campo, aparece una excepción o el cálculo es incorrecto. Cada observación orienta hacia una comprobación distinta.

Anota también lo que esperabas. Si el formulario debía aceptar 15 minutos y muestra un error de rango, tienes una condición concreta que investigar. Si no sabes qué resultado esperabas, todavía no puedes decidir si el programa falla.

## Comprobar una capa cada vez

Empieza por el acceso al servidor: URL y puerto correctos, servicio levantado y respuesta recibida. Después mira el procesamiento PHP: archivo ejecutado, método y campos. Finalmente comprueba el significado del resultado: reglas y cálculo.

Esto evita cambiar la lógica de un formulario cuando todavía estás conectando al puerto equivocado. También evita reinstalar contenedores cuando el dato llega bien y el único fallo es leer una clave con otro nombre.

El navegador permite observar la petición y la respuesta. Los logs permiten observar lo que ocurrió en el servicio. Una impresión temporal como `var_dump` permite observar una variable en un punto. Cada herramienta responde a una pregunta distinta; elige la que te permita comprobar tu hipótesis.

## Una hipótesis debe poder ponerse a prueba

Si piensas «el campo no llega», abre el cuerpo del POST y búscalo. Si aparece, esa hipótesis ya no explica el problema. Mira después cómo lo lee el receptor. Si piensas «la sesión cambia en cada visita», observa la cookie y revisa si estás alternando perfiles.

Cambiar muchas cosas antes de comprobar impide saber cuál influía. Haz una corrección pequeña, repite la entrada que fallaba y comprueba después que el caso que antes funcionaba sigue funcionando.

No elimines una validación solo para obtener una pantalla de éxito. Puede que el dato enviado sea incorrecto y la validación esté haciendo bien su trabajo. La corrección debe respetar la regla que hayas definido para el problema.

## Leer un error de sintaxis con calma

Un mensaje puede señalar la línea donde el intérprete ya no pudo continuar, no necesariamente la primera línea que contiene la causa. Si falta una comilla o un punto y coma antes, el problema puede hacerse visible al llegar a la siguiente instrucción.

`php -l archivo.php` comprueba sintaxis sin atender una petición web completa. Que esa comprobación pase no demuestra que el formulario reciba sus datos ni que la sesión esté bien configurada. Después necesitas probar el comportamiento real.

## Guardar lo aprendido para la siguiente vez

Anota síntoma, causa y corrección. «POST vacío → el control no tenía `name` → añadir el nombre y leer esa clave» es una referencia útil. «Reinicié y funcionó» no permite explicar la causa ni repetir con seguridad la solución.

Este registro convierte los errores en material de estudio. Durante un ejercicio puedes reconocer un patrón sin repetir pruebas a ciegas, y en el examen puedes justificar qué comprobación harías primero y por qué.

## Problema explicado paso a paso: no aparece la duración del turno

En un formulario de visita guiada el control dice `name="duracion"`, pero el receptor lee `$_POST['tiempo']`. Al enviar 25, el resumen aparece vacío.

1. En Red del navegador, abre la petición POST. El cuerpo contiene `duracion=25`: el navegador envía bien el dato.
2. En desarrollo local, inspecciona el receptor con `var_dump($_POST);`. La clave es `duracion`, no `tiempo`.
3. Corrige la lectura a `$_POST['duracion'] ?? ''` y valida el resultado antes de calcular.
4. Vuelve a probar 25, un campo ausente y un texto no numérico.
5. Retira la impresión de depuración. Si la dejas antes de un `header()`, puede impedir la redirección.

**Conclusión del caso:** el problema era el acuerdo entre el nombre del campo y la clave que esperaba PHP. Añadir CSS, reiniciar MariaDB o cambiar de navegador no corrige ese desacuerdo.

## Dónde mirar según el síntoma

| Síntoma | Comprobación concreta |
| --- | --- |
| No conecta | `docker compose ps`, puerto y URL |
| Nginx devuelve 502 | `docker compose logs --tail=40 motor cartelera` en el laboratorio de UT1 |
| Error de sintaxis PHP | `php -l public/turno.php` si tienes PHP local |
| Campo ausente | `action`, `method`, `name` y cuerpo del POST |
| `Undefined array key` | Clave real y lectura con valor alternativo |
| `headers already sent` | HTML, espacios o `echo` anteriores a la cabecera |
| Sesión vacía | `session_start()`, cookie y perfil del navegador |
| Resultado numérico incorrecto | Valores de entrada, tipos y fórmula |

Para ver errores solo en un entorno local de desarrollo:

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
```

En un servidor publicado, los detalles deben ir a los logs y la respuesta al usuario debe ser adecuada. No muestres credenciales, tokens ni datos personales en las capturas de diagnóstico.

## Una comprobación útil antes de dar por terminado un tema

Prepara una tabla con caso normal, límite inferior, límite superior, dato ausente y dato incorrecto. Para el telescopio, por ejemplo, 5 y 40 son válidos, pero 4 y 41 no. Si solo pruebas 15, no has comprobado los límites.

En Git, registra una corrección coherente con `git add archivo.php`, `git diff --cached` y `git commit -m "Valida la duración del turno"`. El commit documenta el cambio; no sustituye la prueba de funcionamiento.

## Preparar una prueba que otra persona pueda repetir

Anota el archivo que se ejecuta, el comando o URL, los datos exactos y el resultado esperado. Una captura sin esos datos puede mostrar un resultado, pero no explicar cómo reproducirlo.

Para una validación de duraciones, separa los casos de **forma** (`muchos`), **rango** (4 o 41) y **estructura** (un array cuando esperabas texto). Si solo pruebas números dentro del rango, no detectas los otros problemas.

En la salida de `docker compose logs`, identifica qué servicio escribe el mensaje. Un fallo DNS al conectar con MariaDB, una credencial rechazada y una tabla ausente requieren correcciones diferentes, aunque todos puedan terminar en una página de error.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Depurar** | Localizar y corregir la causa de un comportamiento incorrecto. |
| **Log** | Registro de eventos o errores que ayuda a reconstruir lo ocurrido. |
| **Caso de prueba** | Entradas y condiciones concretas con un resultado esperado que puedes justificar. |

!!! success "Para repasar"
    Reproduce, observa, explica una causa, corrige y repite el caso que fallaba. Cambiar muchas cosas a la vez dificulta saber cuál resolvía el problema.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
