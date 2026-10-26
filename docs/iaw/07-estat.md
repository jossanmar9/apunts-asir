# UT2 · 4. Cookies, sesiones y acceso privado

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Cookie** | Dato que guarda el navegador y envía en las peticiones que corresponden a su ámbito. |
| **Sesión** | Estado que el servidor asocia con un identificador del cliente entre varias peticiones. |
| **Hash de contraseña** | Representación calculada para verificar una contraseña sin guardarla en claro; no se descifra. |
| **Autenticación y autorización** | Comprobar la identidad y decidir los permisos de esa identidad. |

## ¿Por qué una variable no recuerda la visita anterior?

Cada petición ejecuta de nuevo el programa. Una variable como `$seccion = 'mapas';` no recuerda una selección hecha en una petición anterior. HTTP no incorpora por sí mismo una memoria de usuario: la aplicación debe construirla.

| Mecanismo | Dónde queda la información | Ejemplo |
| --- | --- | --- |
| Variable normal | Durante la ejecución de la petición | Resultado de un cálculo |
| Cookie | En el navegador, que la envía en peticiones posteriores | Preferencia de vista |
| Sesión | Habitualmente en el servidor; el navegador conserva el identificador | Usuario autenticado |

El cliente puede modificar las cookies. No las uses como prueba de permisos. Una sesión también necesita controles de acceso en el servidor.

## Ejemplo resuelto: recordar la vista de un catálogo

Guarda `vista.php`:

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $vista = $_POST['vista'] ?? '';
    if (is_string($vista) && in_array($vista, ['cuadricula', 'lista'], true)) {
        setcookie('vista_catalogo', $vista, [
            'expires' => time() + 86400 * 7,
            'path' => '/',
            'httponly' => true,
            'samesite' => 'Lax',
        ]);
        header('Location: vista.php', true, 303);
        exit;
    }
}
$vista = $_COOKIE['vista_catalogo'] ?? 'cuadricula';
if (!is_string($vista) || !in_array($vista, ['cuadricula', 'lista'], true)) {
    $vista = 'cuadricula';
}
?>
<p>Vista: <?= htmlspecialchars($vista, ENT_QUOTES, 'UTF-8') ?></p>
<form method="post" action="vista.php">
    <button name="vista" value="cuadricula">Cuadrícula</button>
    <button name="vista" value="lista">Lista</button>
</form>
```

**Seguimiento:** la primera visita muestra cuadrícula. El botón envía POST; PHP envía `Set-Cookie` y una redirección 303; el navegador hace un nuevo GET con la cookie y muestra lista. `$_COOKIE` no se actualiza automáticamente con el valor que acabas de enviar: se lee de la petición recibida. En HTTPS añade `'secure' => true` a las opciones de la cookie.

`setcookie`, `session_start` y `header` deben ir antes de cualquier salida. Después de una redirección, `exit` detiene el programa. Es el patrón POST–Redirect–GET: recargar la página final repite el GET.

## Autenticación: comprobar quién entra

La idea es **formulario → verificar credenciales → renovar identificador → guardar identidad → comprobar identidad en cada ruta privada**. Autorizar es decidir qué puede hacer esa identidad; autenticar y autorizar son decisiones diferentes.

Minilaboratorio independiente de una biblioteca de partituras. Genera un hash con `php -r 'echo password_hash("Partitura!47", PASSWORD_DEFAULT), PHP_EOL;'`. Copia el resultado en un archivo local `usuarios.php`:

```php
<?php
return ['archivero' => 'PEGA_AQUI_EL_HASH_GENERADO'];
```

`acceso.php` contiene el formulario y el procesamiento:

```php
<?php
session_start();
$usuarios = require __DIR__ . '/usuarios.php';
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuario = $_POST['usuario'] ?? '';
    $clave = $_POST['clave'] ?? '';
    if (is_string($usuario) && is_string($clave)
        && isset($usuarios[$usuario])
        && password_verify($clave, $usuarios[$usuario])) {
        session_regenerate_id(true);
        $_SESSION['identidad'] = $usuario;
        header('Location: archivo.php', true, 303);
        exit;
    }
    $error = 'No se ha podido validar el acceso.';
}
?>
<p><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></p>
<form action="acceso.php" method="post">
    <label>Usuario <input name="usuario" required></label>
    <label>Clave <input name="clave" type="password" required></label>
    <button>Entrar</button>
</form>
```

`archivo.php` comprueba el acceso antes de enviar HTML:

```php
<?php
session_start();
if (!isset($_SESSION['identidad'])) {
    header('Location: acceso.php');
    exit;
}
?>
<h1>Archivo de partituras</h1>
<p>Identidad: <?= htmlspecialchars($_SESSION['identidad'], ENT_QUOTES, 'UTF-8') ?></p>
<form action="salir.php" method="post"><button>Salir</button></form>
```

`salir.php` cierra la sesión:

```php
<?php
session_start();
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    exit;
}
$_SESSION = [];
if (ini_get('session.use_cookies')) {
    $p = session_get_cookie_params();
    setcookie(session_name(), '', [
        'expires' => time() - 3600, 'path' => $p['path'],
        'domain' => $p['domain'], 'secure' => $p['secure'],
        'httponly' => $p['httponly'], 'samesite' => 'Lax',
    ]);
}
session_destroy();
header('Location: acceso.php', true, 303);
exit;
```

**Resultado esperado:** el acceso directo a `archivo.php` redirige; las credenciales del laboratorio permiten entrar; después de salir, el acceso directo vuelve a redirigir. El hash es una representación para verificar la clave, no una clave cifrada que se descifra. Las credenciales mostradas son solo de prueba.

Este ejemplo explica el mecanismo. Una aplicación publicada también necesita HTTPS, configuración segura de sesión, protección CSRF y controles contra intentos repetidos.

## Comprobar el aislamiento

Entra en una ventana normal y abre `archivo.php` en una ventana privada: la segunda debe pedir acceso. Dos pestañas del mismo perfil suelen compartir cookies y sesión; no sirven para simular dos usuarios independientes.

## Reglas de sesión recuperadas y puestas en contexto

| Medida | Qué aporta |
| --- | --- |
| `HttpOnly` | Impide leer la cookie mediante JavaScript; no elimina todos los efectos de XSS |
| `Secure` | Limita el envío de la cookie a conexiones HTTPS |
| `SameSite` | Restringe su envío en determinados contextos entre sitios |
| Renovar el identificador al entrar | Reduce el riesgo de fijación de sesión |
| Caducidad por inactividad | Limita cuánto dura un acceso abandonado |

Una política de inactividad se aplica comprobando la última actividad en el servidor, no solo ocultando una pantalla. Una cookie con `admin=1` no prueba autorización; el servidor debe recuperar los permisos desde una fuente en la que confíe.

### Caso resuelto: entrar no significa tener cualquier permiso

Imagina que el archivo de partituras distingue visitantes y personal de archivo. Después de verificar la identidad, la aplicación asigna un rol desde sus propios datos. Antes de una operación reservada, comprueba ese rol en el servidor.

```php
<?php
session_start();
if (($_SESSION['rol'] ?? '') !== 'archivo') {
    http_response_code(403);
    exit('Acceso no autorizado para esta operación');
}
echo 'Operación permitida al personal de archivo';
```

En este fragmento no se fija el rol desde un formulario: presupone que el proceso de acceso lo ha guardado desde datos fiables. Sin sesión o con otro rol devuelve 403; con rol `archivo`, permite continuar. Es una comprobación de autorización, distinta del acceso por contraseña.

El botón «atrás» puede mostrar una representación en caché después de salir. La prueba importante es solicitar de nuevo la ruta privada y comprobar que el servidor deniega el acceso. En contenido sensible puedes usar una política de caché como `Cache-Control: no-store`.

!!! success "Para repasar"
    Ocultar un enlace no protege una ruta. La comprobación debe ejecutarse en el servidor antes de cualquier contenido privado.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
