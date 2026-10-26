# UT1 · 3. Docker Compose y un entorno que puedes reconstruir

## Conceptos antes de copiar configuraciones

Una **imagen** es la base con la que se crea un contenedor. Un **contenedor** es una instancia de esa imagen, que puede estar detenida o en ejecución. Un **servicio de Compose** describe cómo crearlo: imagen, configuración, red, montajes y puertos.

Un montaje de carpeta (*bind mount*) conecta una ruta de tu equipo con una del contenedor. Un volumen con nombre es almacenamiento gestionado por Docker; resulta apropiado para datos que deben sobrevivir a la sustitución del contenedor.

## Laboratorio resuelto: cartelera de un cineclub

Este ejemplo propio aísla la comunicación Nginx–PHP, sin reproducir la práctica de despliegue de clase. Necesitas Docker con Compose. Crea una carpeta de pruebas con esta estructura:

```text
cineclub/
├── compose.yaml
├── .env.example
├── .env
├── .gitignore
├── web.conf
└── public/
    └── index.php
```

`compose.yaml`:

```yaml
services:
  cartelera:
    image: nginx:stable-alpine
    ports:
      - "127.0.0.1:${WEB_PORT:-8092}:80"
    volumes:
      - ./public:/srv/cineclub:ro
      - ./web.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - motor
  motor:
    image: php:8.3-fpm-alpine
    volumes:
      - ./public:/srv/cineclub:ro
```

`web.conf`:

```nginx
server {
    listen 80;
    root /srv/cineclub;
    index index.php;
    location / {
        try_files $uri $uri/ =404;
    }
    location ~ \.php$ {
        try_files $uri =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass motor:9000;
    }
}
```

`public/index.php`:

```php
<?php
$titulo = 'Sesión de cortometrajes';
?>
<h1><?= htmlspecialchars($titulo, ENT_QUOTES, 'UTF-8') ?></h1>
<p>El motor PHP ha generado esta cartelera.</p>
```

`.env.example` y su copia local `.env`:

```dotenv
WEB_PORT=8092
```

`.gitignore`:

```gitignore
.env
```

### ¿Por qué funciona?

1. El navegador conecta al puerto **8092 del anfitrión**, publicado hacia el **80 de Nginx**. El prefijo `127.0.0.1` limita el acceso al propio equipo.
2. Nginx busca `index.php` en `/srv/cineclub`.
3. `motor` es el nombre DNS del servicio PHP dentro de la red de Compose. Desde Nginx, `localhost` sería el contenedor de Nginx, no PHP.
4. Los dos contenedores ven el mismo código en la misma ruta; PHP puede abrir el archivo que le indica Nginx.
5. `:ro` permite leer el montaje, pero impide escribir en él desde el contenedor.

### Comandos y comprobación

Desde la carpeta `cineclub`:

```bash
cp .env.example .env
docker compose config
docker compose up -d
docker compose ps
curl -i http://localhost:8092/
docker compose logs --tail=30 cartelera motor
docker compose down
```

**Resultado esperado:** estado HTTP 200 y una cartelera con «Sesión de cortometrajes». `config` comprueba y resuelve la configuración; `ps` muestra el estado; `logs` ayuda a investigar. `down` elimina los contenedores y la red del proyecto. `depends_on` ordena el arranque, pero con esta forma no garantiza que una aplicación esté preparada para atender peticiones.

## ¿Y si añadimos una base de datos?

MariaDB sería otro servicio, por ejemplo `archivo`. PHP conectaría a `archivo:3306`, no al puerto del anfitrión. Un volumen como `datos_archivo:/var/lib/mysql` conservaría la información. Los scripts de `/docker-entrypoint-initdb.d/` se aplican al inicializar un directorio de datos vacío; no vuelven a ejecutarse simplemente porque edites el SQL.

Un Dockerfile permite derivar una imagen, por ejemplo con `FROM php:8.3-fpm-alpine` y `RUN docker-php-ext-install pdo_mysql` para disponer del controlador PDO de MySQL/MariaDB. Después Compose utiliza `build:` y hay que reconstruir la imagen. La conexión y las consultas se trabajan en los [apuntes complementarios de PDO](../php/05-pdo.md).

## `.env`, `environment` y `env_file`

Compose puede leer `.env` para sustituir `${WEB_PORT}` en el YAML. Esto **no introduce automáticamente todas las variables dentro de PHP**. `environment:` pasa variables concretas al servicio; `env_file:` carga un archivo de variables dentro del contenedor. Un `.env.example` documenta los nombres con valores de prueba; las credenciales reales no deben ir al repositorio.

Las etiquetas de imagen de este ejemplo son móviles. Para repetir exactamente una versión debes registrar una versión inmutable o el digest, además del procedimiento.

| Síntoma | Qué revisas primero |
| --- | --- |
| Puerto ocupado | Cambia `WEB_PORT` y recrea el servicio. |
| 404 | Archivo, `root`, ruta del montaje y URL. |
| 502 | Estado de `motor`, nombre DNS y puerto FastCGI. |
| PHP no ve una variable | `environment` o `env_file`, no solo `.env`. |
| Los datos han desaparecido | Volumen utilizado y si se ha eliminado. `down -v` elimina volúmenes. |

!!! success "Para repasar"
    Explica cada lado de un puerto y de un montaje. Para reconstruir el proyecto necesitas código, configuración, variables documentadas y pasos de verificación.

---

Fuente del temario: [apuntes originales de UT1](https://victoria-nr.github.io/iaw-alumnos/UT1/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
