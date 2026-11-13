# Preguntas tipo examen · UT1 + UT2

Mismo formato que el examen: un caso y tres apartados (a, b, c). La solución está plegada debajo de cada pregunta.
Todas están basadas en lo que has hecho en las prácticas y ejercicios.

**Cómo usarlo:** intenta responder cada pregunta por escrito **antes** de abrir la solución. Después compara y apunta lo que te haya faltado. Volver a ver la [estructura para responder](index.md#como-responder-una-pregunta).

---

## UT1 · Entorno de implantación web

### Ejercicio 1 · El puerto equivocado

En `compose.yaml` el servicio web está así:

```yaml
nginx:
  image: nginx:stable
  ports:
    - "8080:80"
```

Un compañero quiere que la web se abra en `http://localhost:8081` y lo cambia por `"80:8081"`. Ahora la web no responde.

- **a)** Explica qué significa cada número en `"8080:80"`.
- **b)** ¿Por qué falla el cambio del compañero? Escribe la línea correcta.
- **c)** ¿Qué harías para que se aplique el cambio y cómo comprobarías que funciona?

??? success "Solución razonada"
    - **a)** El de la **izquierda** es el puerto del ordenador (host), el que se escribe en el navegador. El de la **derecha** es el puerto **dentro del contenedor**, donde escucha nginx (el 80, por `listen 80`).
    - **b)** El compañero los ha cambiado de lado: ahora el ordenador usa el 80 y lo manda al 8081 del contenedor, donde nginx no escucha. Lo correcto es cambiar solo el de la izquierda: `"8081:80"`.
    - **c)** `docker compose up -d` (Compose detecta el cambio y recrea nginx). Comprobación: `docker compose ps` debe mostrar `0.0.0.0:8081->80/tcp`, y abrir `http://localhost:8081`. Si no responde, `docker compose logs nginx`.

### Ejercicio 2 · El navegador descarga el PHP

Al abrir `http://localhost:8080/index.php`, el navegador descarga el fichero en lugar de mostrar la página. El `default.conf` de nginx tiene esto:

```nginx
server {
    listen 80;
    root /var/www/html;
    index index.php index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

- **a)** ¿Qué componente del stack está fallando y por qué el navegador descarga el fichero?
- **b)** ¿Qué bloque falta en `default.conf`? Indica las directivas importantes.
- **c)** Después de añadirlo, sigue igual. ¿Qué harías y qué evidencia revisarías?

??? success "Solución razonada"
    - **a)** Falla **nginx**: no sabe qué hacer con los `.php`, así que los trata como un fichero normal y lo envía tal cual. El código no llega a PHP-FPM.
    - **b)** Falta el bloque `location ~ \.php$` con `include fastcgi_params;`, `fastcgi_pass php:9000;` (nombre del servicio, no `localhost`) y `fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;`.
    - **c)** nginx solo lee `default.conf` al arrancar: hay que hacer `docker compose restart nginx`. Si sigue mal, revisar `docker compose logs nginx` y `docker compose ps` (que `php` esté en marcha). Recargar el navegador con Ctrl+Shift+R por la caché.

### Ejercicio 3 · El registro que no aparece

El servicio `db` monta `./sql/init.sql` en `/docker-entrypoint-initdb.d/` y usa el volumen `db_data` para `/var/lib/mysql`. Un alumno añade un segundo `INSERT` a `init.sql`, ejecuta `docker compose down` y `docker compose up -d`, pero la página sigue mostrando **1 registro**.

- **a)** Explica por qué no aparece el nuevo registro.
- **b)** ¿Qué tendría que hacer para que se ejecute el nuevo `init.sql`?
- **c)** ¿Qué consecuencia tiene ese comando? ¿Para qué sirve el volumen `db_data`?

---

## UT2 · Programación web en servidor con PHP

??? success "Solución razonada"
    - **a)** `init.sql` solo se ejecuta la **primera vez**, cuando el volumen `db_data` está vacío. `docker compose down` borra los contenedores, pero **no** el volumen, así que la base de datos ya existe y MariaDB no vuelve a ejecutar el script.
    - **b)** `docker compose down -v` (borra también el volumen) y `docker compose up -d`. Después, revisar `docker compose logs db` para ver `running /docker-entrypoint-initdb.d/init.sql`.
    - **c)** Se pierden **todos** los datos de la base de datos. El volumen `db_data` sirve para que los datos sobrevivan aunque se paren o se borren los contenedores (persistencia).

### Ejercicio 4 · Cambios en el presupuesto

En la práctica del presupuesto, la empresa pide dos cambios:

1. Que el mínimo de contratación sea **3 meses** (el máximo sigue siendo 24).
2. Añadir un plan nuevo, **Premium**, de **20 €/mes**.

- **a)** Indica qué bloques del programa habría que tocar para el cambio 1.
- **b)** Indica los **tres** sitios que habría que modificar para el cambio 2.
- **c)** ¿Qué valores probarías para comprobar el cambio 1? Justifícalo.

??? success "Solución razonada"
    - **a)** Solo la **validación de los meses**: cambiar la condición del mínimo (`$meses < 1` → `$meses < 3`) y su mensaje de error. Opcionalmente, el texto del formulario ("1 a 24" → "3 a 24").
    - **b)** 1) La **función** `obtenerPrecioPlan()`: añadir un `elseif ($plan === 'Premium') { return 20; }` (antes del `else`). 2) La **validación del plan**: añadir `'Premium'` a la lista del `in_array`. 3) El **formulario**: añadir un `<option value="Premium">` en el `select` (con su `if ... selected`).
    - **c)** Valores frontera: **2** (debe dar error), **3** (debe aceptarse), **24** (aceptado) y **25** (error). Los errores suelen estar justo en los límites.

### Ejercicio 5 · El checkbox que da error

Un alumno recoge los extras del formulario así:

```php
$backup = $_POST['backup'];
$soporte = $_POST['soporte'];
```

Cuando el usuario **no** marca alguna casilla, aparece el aviso `Undefined array key "backup"`.

- **a)** Explica por qué ocurre solo cuando la casilla no está marcada.
- **b)** Escribe cómo debería recogerse cada checkbox.
- **c)** Si hay un error en otro campo, ¿cómo conseguirías que la casilla siga marcada al volver a mostrar el formulario?

??? success "Solución razonada"
    - **a)** Un checkbox **no marcado no se envía**: la clave no existe en `$_POST`, y leerla directamente da error. Cuando está marcado sí se envía.
    - **b)** `$backup = isset($_POST['backup']);` y `$soporte = isset($_POST['soporte']);` → valen `true` si se ha marcado y `false` si no.
    - **c)** En el `input` del checkbox: `<?php if ($backup) { echo 'checked'; } ?>`. Así, si el formulario se vuelve a mostrar por un error, la casilla aparece como el usuario la dejó.

### Ejercicio 6 · El panel que no está protegido

En la práctica del login, un alumno ha escrito así `panel.php`:

```php
<?php
session_start();
?>
<h1>Bienvenido, <?php echo $_SESSION['nombre'] ?? ''; ?></h1>
<a href="logout.php">Cerrar sesión</a>
```

Y su `logout.php` solo tiene:

```php
<?php
header('Location: login.php');
exit;
```

- **a)** ¿Qué pasa si alguien escribe `panel.php` en la URL sin haber hecho login? ¿Y si cierra sesión y vuelve atrás?
- **b)** ¿Qué añadirías en `panel.php` para protegerlo y qué añadirías en `logout.php`?
- **c)** Explica cómo comprobarías que dos usuarios no comparten sus datos de sesión.

---

??? success "Solución razonada"
    - **a)** Cualquiera puede entrar escribiendo la URL, porque el panel no comprueba nada (solo mostraría el nombre vacío). Y al "cerrar sesión" la sesión sigue existiendo: si vuelve al panel, sigue dentro.
    - **b)** En `panel.php`, justo después de `session_start()`: `if (!isset($_SESSION['usuario'])) { header('Location: login.php'); exit; }`. En `logout.php`: `session_start(); $_SESSION = []; session_destroy();` antes de la redirección.
    - **c)** Entrar con un usuario en una ventana normal y con otro en una ventana de incógnito (o en otro navegador). Uno guarda una nota o sube su contador, y se comprueba que el otro no lo ve. Cada contexto de navegador tiene su propio identificador de sesión.
