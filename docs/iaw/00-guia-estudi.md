# IAW · Guía de estudio de UT1 y UT2

Esta guía resume **qué debes entender de verdad** antes de entrar en el detalle de cada tema. Está alineada con la teoría y las prácticas de clase: primero el entorno web reproducible de UT1 y después la programación PHP de servidor de UT2.

## UT1 · La idea que une toda la unidad

Piensa siempre en este recorrido:

```text
Navegador → Nginx → PHP-FPM → MariaDB
              ↑          ↑
           HTTP      ejecuta PHP
```

- **Navegador**: hace la petición y muestra la respuesta.
- **Nginx**: recibe HTTP, sirve recursos estáticos y reenvía los `.php`.
- **PHP-FPM**: ejecuta PHP y devuelve el resultado a Nginx.
- **MariaDB**: guarda información persistente.

### Ejemplo fácil

Si visitas `http://localhost:8080/index.php`:

1. el navegador conecta con el puerto `8080` del equipo;
2. Docker lo dirige al puerto `80` de Nginx;
3. Nginx detecta que se solicita PHP;
4. reenvía la ejecución a PHP-FPM;
5. PHP puede consultar `db` (MariaDB);
6. PHP genera una respuesta;
7. Nginx la devuelve al navegador.

El navegador **no ejecuta PHP** y PHP no debería buscar MariaDB en `localhost` si la base de datos está en otro contenedor. Dentro de Compose se utiliza el nombre del servicio, por ejemplo `db`.

## Estático frente a dinámico

Un `logo.png` o un `estilos.css` puede servirse tal como está. Una página PHP puede generar un resultado diferente según datos, formularios, sesiones o la base de datos.

Regla mental: **estático = enviar un recurso; dinámico = generar una respuesta**.

## HTTP que conviene dominar

Una petición tiene, como mínimo, método, ruta, cabeceras y a veces cuerpo. Una respuesta contiene un código de estado, cabeceras y normalmente un cuerpo.

| Código | Idea |
| --- | --- |
| 200 | correcto |
| 301/302 | redirección |
| 403 | acceso prohibido |
| 404 | recurso no encontrado |
| 500 | error interno del servidor |

No memorices solo el número: pregúntate **en qué punto del recorrido puede haberse producido el fallo**.

## Docker: imagen, contenedor, puerto y volumen

- **Imagen**: plantilla con la que se crea un contenedor.
- **Contenedor**: instancia en ejecución.
- **Puerto**: permite acceder desde fuera al servicio cuando se publica.
- **Volumen/bind mount**: hace accesibles datos o archivos fuera de la capa efímera del contenedor.

```text
8080:80
│    └─ puerto dentro del contenedor
└────── puerto de tu equipo
```

Un montaje como `./app:/var/www/html` permite que el código de `app/` del equipo esté disponible dentro del contenedor.

## Docker Compose

Compose describe varios servicios juntos. En esta UT debes poder leer una configuración y localizar:

```yaml
services:
  nginx:
  php:
  db:
```

También debes reconocer `ports`, `volumes`, `environment` y `depends_on`.

La práctica de clase exige coordinar **nginx + php + db**, montar `app/`, proporcionar la configuración de Nginx, pasar datos de conexión mediante variables y cargar un SQL inicial.

## `.env` y `.env.example`

- `.env.example`: plantilla que documenta las variables necesarias.
- `.env`: valores reales de tu entorno.

```dotenv
DB_HOST=db
DB_NAME=ut1db
DB_USER=ut1user
DB_PASSWORD=una_clave_local
```

La contraseña real no debería quedar publicada en Git. La aplicación debe recibir configuración desde fuera en vez de repetir credenciales dentro del código.

## Diagnóstico en UT1

No cambies cosas al azar. Sigue evidencias:

```bash
docker compose ps
docker compose logs
docker compose logs -f nginx
docker compose logs -f php
docker compose exec php sh
docker compose config
```

Ejemplo: si Nginx funciona pero PHP no conecta con MariaDB, primero comprueba si `db` está levantado, después las variables de entorno, el host, el usuario y la contraseña y, finalmente, los logs.

---

# UT2 · PHP en servidor

La idea principal es:

```text
formulario/URL → petición HTTP → PHP → decisiones y validación → HTML → navegador
```

PHP se ejecuta **antes** de que el navegador reciba la página.

## Variables y salida

```php
<?php
$plan = 'Profesional';
$precio = 9;
echo "Plan: $plan - $precio €/mes";
```

Una variable empieza por `$`. `=` asigna. Para comparar de forma estricta puedes utilizar `===`.

## Decisiones

```php
if ($meses < 1) {
    echo 'Número de meses incorrecto';
} elseif ($meses > 24) {
    echo 'Máximo 24 meses';
} else {
    echo 'Dato correcto';
}
```

Lee `if` como una pregunta: **si esta condición es cierta, ¿qué hago?**

## Arrays y `foreach`

```php
$errores = ['Falta el nombre', 'Correo incorrecto'];

foreach ($errores as $error) {
    echo "<p>$error</p>";
}
```

Esto es especialmente importante porque la práctica de clase pide acumular errores en un array y mostrarlos con `foreach`.

## Funciones

```php
function calcularTotal(float $precio, int $meses): float
{
    return $precio * $meses;
}
```

Una función evita repetir una operación y le da un nombre claro.

## Formularios y POST

```html
<form method="post">
    <input name="nombre">
    <button>Enviar</button>
</form>
```

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = trim($_POST['nombre'] ?? '');
}
```

No des por hecho que un campo existe ni que su contenido es correcto.

## Validar no es lo mismo que recoger

```php
$correo = trim($_POST['correo'] ?? '');

if ($correo === '') {
    $errores[] = 'El correo es obligatorio';
} elseif (!filter_var($correo, FILTER_VALIDATE_EMAIL)) {
    $errores[] = 'El correo no tiene un formato válido';
}
```

Orden mental recomendado:

1. comprobar si se ha enviado el formulario;
2. recoger los datos;
3. normalizar (`trim`, etc.);
4. validar;
5. acumular errores;
6. si no hay errores, calcular o procesar;
7. generar la respuesta HTML.

## Salida segura

Si vuelves a mostrar texto introducido por el usuario:

```php
<?= htmlspecialchars($nombre, ENT_QUOTES, 'UTF-8') ?>
```

No confundas **validar** (decidir si un dato es aceptable) con **escapar** (evitar que un texto se interprete como HTML cuando lo muestras).

## Sesiones

```php
session_start();
$_SESSION['usuario'] = 'jose';
```

La sesión permite conservar estado entre peticiones. Para un cierre de sesión básico:

```php
session_start();
$_SESSION = [];
session_destroy();
header('Location: login.php');
exit;
```

`session_start()` y `header()` deben ejecutarse antes de haber enviado una salida que impida modificar las cabeceras.

## Depuración que debes saber hacer

```bash
php -l archivo.php
docker compose logs -f
docker compose exec php sh
```

Durante una prueba también puedes inspeccionar datos:

```php
var_dump($_POST);
var_dump($_SESSION);
```

`php -l` comprueba la sintaxis sin ejecutar el programa. Los `var_dump` de depuración deben retirarse cuando ya no hagan falta.

## Orden recomendado para estudiar

1. Entiende el recorrido navegador → Nginx → PHP-FPM → MariaDB.
2. Domina puertos, volúmenes, servicios y variables de Compose.
3. Practica el diagnóstico con `ps`, `logs`, `exec` y `config` de Compose.
4. Pasa a PHP: variables → condiciones → arrays → bucles → funciones.
5. Después, formularios: POST → recogida → validación → errores → respuesta.
6. Finalmente, practica sesiones, redirecciones y depuración.

Cuando puedas explicar **por qué** funciona cada paso sin mirar los apuntes, ya no estarás memorizando: estarás entendiendo el stack.
