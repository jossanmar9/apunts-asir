## Ejercicios resueltos paso a paso · UT1

### Arquitectura web

#### Ejercicio 1 · Seguir una petición
**Enunciado.** Explica qué ocurre al abrir una página servida por Nginx. **Paso a paso:** 1) el navegador crea una petición HTTP; 2) llega al servidor y puerto correspondiente; 3) Nginx recibe la petición; 4) localiza el recurso o la deriva a otro componente; 5) genera una respuesta HTTP; 6) el navegador interpreta la respuesta. **Entrada:** petición. **Proceso:** servidor web. **Salida:** respuesta.

#### Ejercicio 2 · Estático frente a dinámico
Si se solicita `logo.png`, Nginx puede leer y devolver el archivo directamente. Si se solicita un `.php`, la configuración puede pasar la ejecución a PHP-FPM. Nginx gestiona HTTP; PHP-FPM ejecuta PHP. Son responsabilidades distintas.

#### Ejercicio 3 · Identificar componentes
En una pila Nginx + PHP-FPM + MariaDB: Nginx atiende HTTP, PHP-FPM ejecuta la lógica PHP y MariaDB almacena datos persistentes. El ejercicio consiste en dibujar `navegador → Nginx → PHP-FPM → MariaDB` y explicar qué información circula en cada salto.

### HTTP

#### Ejercicio 1 · Leer una petición
```http
GET /index.html HTTP/1.1
Host: ejemplo.local
```
`GET` es el método; `/index.html` es el recurso; `HTTP/1.1` es la versión y `Host` indica el sitio solicitado. No hay que interpretar toda la línea como una URL.

#### Ejercicio 2 · Interpretar un estado
```http
HTTP/1.1 404 Not Found
```
`404` pertenece a los códigos 4xx: la petición llegó al servidor, pero el recurso solicitado no se encontró. No significa necesariamente que el servidor esté apagado.

#### Ejercicio 3 · GET frente a POST
Un formulario de búsqueda suele poder usar `GET`: los parámetros aparecen en la URL y la operación consulta información. Un formulario que envía datos para crear o modificar algo suele usar `POST`: los datos viajan en el cuerpo. El método no sustituye a la validación ni aporta seguridad por sí solo.

### Entorno de implantación

#### Ejercicio 1 · Contenedor Nginx
```bash
docker run --rm -p 8080:80 nginx:stable
```
`docker run` crea y ejecuta el contenedor; `--rm` lo elimina al terminar; `-p 8080:80` publica el puerto 80 del contenedor como 8080 del host; `nginx:stable` es la imagen.

#### Ejercicio 2 · Volumen enlazado
```bash
docker run --rm -p 8080:80 -v "$PWD/web:/usr/share/nginx/html:ro" nginx:stable
```
`-v` enlaza la carpeta local `web` con el directorio servido por Nginx. `:ro` la monta como solo lectura dentro del contenedor.

#### Ejercicio 3 · Compose
```yaml
services:
  web:
    image: nginx:stable
    ports:
      - "8080:80"
```
`services` agrupa servicios; `web` es el nombre lógico; `image` selecciona la imagen y `ports` define el mapeo host:contenedor. `docker compose up` crea lo descrito en el archivo.

!!! tip "Pregunta clave"
    En cada práctica pregúntate: ¿qué proceso escucha?, ¿en qué puerto?, ¿qué componente ejecuta el código? y ¿dónde están los datos?