# UT2 · 5. Depurar una aplicación sin probar al azar

## Sigue el recorrido de la petición

Cuando una página no hace lo que esperas, separa tres preguntas: **¿ha llegado la petición?**, **¿qué ha recibido PHP?** y **¿qué respuesta ha generado?**. Un formulario que no conserva un valor no se diagnostica igual que un contenedor que no arranca.

## Caso resuelto: no aparece la duración del turno

**Situación propia:** en un formulario de visita guiada el control dice `name="duracion"`, pero el receptor lee `$_POST['tiempo']`. Al enviar 25, el resumen aparece vacío.

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

!!! success "Para repasar"
    Reproduce, observa, explica una causa, corrige y repite el caso que fallaba. Cambiar muchas cosas a la vez dificulta saber cuál resolvía el problema.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
