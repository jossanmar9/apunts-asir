# UT1 · 2. HTTP: peticiones, respuestas y diagnóstico

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **HTTP y HTTPS** | Protocolo de petición/respuesta y su uso sobre una conexión protegida con TLS. |
| **TLS y certificado** | TLS protege la conexión; el certificado vincula una identidad con una clave pública verificable. |
| **Cabecera y cuerpo** | Metadatos de una petición o respuesta y su contenido. |
| **JSON / XML** | Formatos de texto para representar e intercambiar datos; no implican por sí mismos una base de datos. |

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

## Caso resuelto: la petición llega, pero ¿qué falla?

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

### Caso resuelto: seguir una redirección

Cuando el ejemplo de cookies guarda una preferencia, responde con 303 y `Location: vista.php`. La primera respuesta no contiene necesariamente la vista final. El navegador solicita después esa dirección con GET.

Para verlo con `curl`, usa `-i` para inspeccionar la respuesta original y `-L` para seguir la redirección. Si hay cookies, `-c cookies.txt -b cookies.txt` permite conservarlas entre peticiones. Sin un almacén de cookies, dos llamadas separadas no simulan necesariamente una misma sesión de navegador.

!!! success "Para repasar"
    Separa método, ruta, cabeceras, cuerpo y estado. Un código HTTP orienta el diagnóstico, pero debes contrastarlo con la petición y los logs.

---

Fuente del temario: [apuntes originales de UT1](https://victoria-nr.github.io/iaw-alumnos/UT1/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
