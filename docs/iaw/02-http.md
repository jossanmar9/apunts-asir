# UT1 · 2. HTTP: peticiones, respuestas y diagnóstico

## Qué viaja por la red

HTTP define cómo un cliente solicita una acción y cómo contesta un servidor. HTTPS protege esa comunicación mediante TLS. Una petición incluye un método, una ruta, cabeceras y, a veces, un cuerpo. La respuesta incluye un estado, cabeceras y, habitualmente, un cuerpo.

Ejemplo didáctico de una API de préstamo de material audiovisual:

```http
GET /api/prestamos/73 HTTP/1.1
Host: material.example
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"codigo":73,"material":"Proyector","estado":"reservado"}
```

`GET` es la acción, `/api/prestamos/73` es el recurso y `Accept` indica qué acepta el cliente. `Content-Type` describe el contenido que realmente devuelve el servidor. La línea en blanco separa cabeceras y cuerpo. `.example` se utiliza como dominio ficticio; esta respuesta es ilustrativa.

## ¿Qué método elijo?

| Método | Intención habitual | Ejemplo del almacén |
| --- | --- | --- |
| GET | Consultar sin modificar el estado del servidor | Ver un préstamo |
| POST | Enviar datos para procesarlos o crear un recurso | Solicitar un préstamo |
| PUT | Sustituir la representación de un recurso | Cambiar una ficha completa |
| PATCH | Modificar algunos campos | Cambiar solo la fecha de devolución |
| DELETE | Eliminar un recurso | Eliminar una reserva |

POST no cifra los datos: la protección en tránsito depende de HTTPS. GET coloca los parámetros de un formulario en la URL; POST los envía habitualmente en el cuerpo. Las cabeceras `Cookie`, `Authorization` y `Content-Type` tienen funciones diferentes: estado del navegador, autenticación y formato de los datos, respectivamente.

## Leer una petición como una ficha de trabajo

Una petición HTTP expresa «quiero hacer esta operación sobre este recurso». El método indica la intención y la ruta identifica el recurso. Las cabeceras añaden información sobre la petición. El cuerpo permite transportar datos cuando el tipo de operación lo necesita.

No confundas la URL completa con la ruta. En `http://localhost:8092/ayuda.php?seccion=horario`, el navegador conecta al equipo local en el puerto 8092, solicita `/ayuda.php` y adjunta la consulta `seccion=horario`. PHP puede leer ese parámetro; no es una carpeta llamada `ayuda.php?seccion=horario`.

La respuesta no es solo «la página». Primero informa de su estado y formato; después entrega el contenido. Un navegador puede mostrar HTML, descargar un archivo o representar una imagen según el recurso y las cabeceras. Una API puede devolver JSON sin ninguna página HTML.

## GET y POST con una decisión sencilla

Si buscas piezas por sala, quieres consultar un resultado. GET permite poner el filtro en la URL, compartirla y repetir la consulta. Si envías una solicitud para reservar una visita, estás entregando datos para procesarlos; normalmente se utiliza POST.

La diferencia no es «GET es inseguro y POST seguro». Los datos de ambos pueden viajar sin protección si usas HTTP sin TLS. Además, cambiar de método no valida los campos ni comprueba permisos: esas tareas siguen en el servidor.

Un formulario GET con un campo `name="sala"` puede producir una consulta `?sala=azul`. En POST, ese dato se transporta habitualmente en el cuerpo. El receptor debe leer el lugar correspondiente. Si el formulario manda POST y el programa solo consulta `$_GET`, parece que los datos han desaparecido, aunque hayan llegado correctamente.

## Interpretar un estado sin sacar conclusiones demasiado rápidas

Un 200 indica que la petición se atendió correctamente según el servidor, pero no garantiza que tu cálculo sea el correcto. Una página puede responder 200 y mostrar un número mal calculado. Un 404 indica que no se encontró el recurso solicitado; no significa que no exista ningún servidor.

Un 500 señala una incidencia interna que requiere revisar el código o los registros. Un 502 puede aparecer cuando Nginx no obtiene una respuesta adecuada del servicio al que deriva el trabajo. Cada estado orienta hacia una parte del recorrido, no cuenta por sí solo toda la causa.

Por eso conviene separar tres pruebas: ¿puedo conectar?, ¿qué respuesta HTTP recibo? y ¿el contenido tiene sentido? Resolver la primera no demuestra las otras dos.

## Inspección guiada con el navegador

Abre las herramientas de desarrollo, entra en Red y recarga la página. Selecciona primero la petición del documento principal. Mira la URL, el método, el estado y `Content-Type`. Después revisa si hay peticiones adicionales a imágenes, CSS o datos.

Una sola página visible puede producir varias peticiones. Que el documento principal tenga estado 200 no impide que una imagen devuelva 404. Esto explica por qué una web puede cargar a medias: no siempre falla el mismo recurso que ves en la barra de direcciones.

Al enviar un formulario, localiza su petición y comprueba los nombres y valores enviados. Esta observación es más útil que añadir impresiones al azar: permite verificar si el problema está antes o después de que los datos lleguen a PHP.

## Problema explicado paso a paso: la petición llega, pero ¿qué falla?

**Situación:** una consulta al servicio de préstamos devuelve `404`; otra petición a PHP devuelve `502`.

1. Un `404` es una respuesta HTTP: has contactado con un servidor. Revisa la ruta, el archivo, el identificador y la configuración que resuelve las rutas.
2. Un `502` de Nginx apunta a un problema de comunicación con el servicio que tiene detrás. Revisa si PHP-FPM está activo y si `fastcgi_pass` utiliza el nombre y el puerto correctos. No demuestra por sí solo que el código PHP sea incorrecto.
3. Si `curl` indica que no se puede conectar, todavía no hay respuesta HTTP: revisa servicio, puerto publicado y dirección.

En el laboratorio del siguiente tema puedes observar las respuestas con:

```bash
curl -i http://localhost:8092/
curl -I http://localhost:8092/
```

`-i` muestra cabeceras y cuerpo. `-I` solicita solo cabeceras mediante HEAD; una aplicación puede tratar HEAD de forma distinta. Con F12 → Red → recargar, el navegador también permite inspeccionar métodos, redirecciones y recursos secundarios.

## Los estados que necesitas reconocer

| Estado | Lectura útil |
| --- | --- |
| 200 / 201 | Operación correcta / recurso creado |
| 301 / 302 / 303 | Redirección; consulta `Location` |
| 400 | Petición que la aplicación considera incorrecta |
| 401 | Hay que autenticarse correctamente |
| 403 | Acceso rechazado |
| 404 | Recurso no encontrado |
| 500 | Fallo interno; revisa los logs |
| 502 / 503 | Problema con el servicio posterior / servicio no disponible |

## HTTPS, certificados y lectura de una URL

En `https://museo.example:8443/piezas?zona=azul`, `https` es el esquema, `museo.example` el host, `8443` el puerto explícito, `/piezas` la ruta y `zona=azul` la consulta. El fragmento de una URL, como `#horario`, lo interpreta normalmente el cliente y no se envía como parte de la petición HTTP al servidor.

TLS protege la conexión y el certificado permite verificar la identidad del servidor para el dominio solicitado. HTTPS no decide si un usuario tiene permiso para entrar: esa autorización sigue siendo responsabilidad de la aplicación.

### Problema explicado paso a paso: seguir una redirección

Cuando el ejemplo de cookies guarda una preferencia, responde con 303 y `Location: vista.php`. La primera respuesta no contiene necesariamente la vista final. El navegador solicita después esa dirección con GET.

Para verlo con `curl`, usa `-i` para inspeccionar la respuesta original y `-L` para seguir la redirección. Si hay cookies, `-c cookies.txt -b cookies.txt` permite conservarlas entre peticiones. Sin un almacén de cookies, dos llamadas separadas no simulan necesariamente una misma sesión de navegador.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **HTTP y HTTPS** | Protocolo de petición/respuesta y su uso sobre una conexión protegida con TLS. |
| **TLS y certificado** | TLS protege la conexión; el certificado vincula una identidad con una clave pública verificable. |
| **Cabecera y cuerpo** | Metadatos de una petición o respuesta y su contenido. |
| **JSON / XML** | Formatos de texto para representar e intercambiar datos; no implican por sí mismos una base de datos. |

!!! success "Para repasar"
    Separa método, ruta, cabeceras, cuerpo y estado. Un código HTTP orienta el diagnóstico, pero debes contrastarlo con la petición y los logs.

---

Fuente del temario: [apuntes originales de UT1](https://victoria-nr.github.io/iaw-alumnos/UT1/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
