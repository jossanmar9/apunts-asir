# UT2 · 4. Cookies, sesiones y acceso privado

## ¿Por qué una variable no recuerda la visita anterior?

Cada petición ejecuta de nuevo el programa. Una variable como `$seccion = 'mapas';` no recuerda una selección hecha en una petición anterior. HTTP no incorpora por sí mismo una memoria de usuario: la aplicación debe construirla.

| Mecanismo | Dónde queda la información | Ejemplo |
| --- | --- | --- |
| Variable normal | Durante la ejecución de la petición | Resultado de un cálculo |
| Cookie | En el navegador, que la envía en peticiones posteriores | Preferencia de vista |
| Sesión | Habitualmente en el servidor; el navegador conserva el identificador | Usuario autenticado |

El cliente puede modificar las cookies. No las uses como prueba de permisos. Una sesión también necesita controles de acceso en el servidor.

## Qué se pierde al terminar una petición

Una variable normal existe durante la ejecución que la crea. Al pedir otra página, el servidor inicia otro procesamiento. Si necesitas recordar una preferencia o quién ha iniciado sesión, debes guardar ese estado mediante algún mecanismo apropiado.

Esto no significa que el navegador olvide todo visualmente ni que se borren las tablas de una base de datos en cada visita. Significa que HTTP no relaciona por sí solo dos peticiones con un estado de aplicación que tú hayas definido.

Una cookie permite al navegador conservar un dato y devolverlo en peticiones posteriores dentro de su ámbito. Una sesión utiliza normalmente una cookie identificadora para localizar información guardada en el servidor. Son mecanismos relacionados, no dos nombres para lo mismo.

## Qué ocurre al guardar una cookie

`setcookie` añade una cabecera a la respuesta. Esa cabecera solicita al navegador guardar el dato. El navegador lo enviará después si la ruta, dominio y demás condiciones corresponden.

Por eso `$_COOKIE` no contiene automáticamente el valor que acabas de enviar: representa lo recibido al comenzar esta petición. La nueva cookie todavía está viajando en sentido contrario. El ejemplo redirige para provocar un GET posterior y leer en él el dato actualizado.

Al definir caducidad, piensa qué quieres recordar y durante cuánto tiempo. Al definir ruta, piensa qué páginas necesitan recibirla. Para una preferencia de vista basta un valor permitido, como `lista` o `cuadricula`; no necesitas guardar en la cookie todo el contenido del catálogo.

## Qué hace `session_start`

Esta llamada crea o recupera la sesión correspondiente al identificador del cliente. Debe ejecutarse en cada página que vaya a utilizar ese estado y antes de enviar una salida que impida preparar las cabeceras necesarias.

Después puedes escribir en `$_SESSION` y recuperar el valor en otra petición de la misma sesión. No basta con escribir una variable `$usuario` en una página y esperar que exista en las demás. Tampoco basta con mostrar un botón de entrada: la ruta privada necesita una comprobación en el servidor.

Distingue el nombre de usuario del identificador de sesión. El navegador suele conservar el segundo; el servidor asocia con él la información necesaria. Compartir ordenador no obliga a compartir sesión, pero dos pestañas del mismo perfil normalmente comparten sus cookies.

## Entender el acceso por contraseña sin aprenderlo de memoria

El formulario entrega un usuario y una clave. El servidor busca si conoce ese usuario y verifica la clave con el hash guardado. Si la comprobación funciona, renueva el identificador y conserva la identidad en la sesión. Después redirige a la zona privada.

Un hash no es una clave cifrada que puedas recuperar con una operación inversa. `password_verify` utiliza la información del hash para comprobar una candidata. No compares el texto de dos llamadas nuevas a `password_hash`: pueden producir representaciones diferentes para la misma contraseña debido al uso de una sal aleatoria.

Si la comprobación falla, el programa no debe crear una sesión autenticada por el simple hecho de que el campo usuario no esté vacío. Haber recibido un nombre no demuestra la identidad. El mensaje al usuario puede ser genérico para no revelar qué parte de las credenciales coincidió.

## Cómo comprobar entrada y salida

Prueba primero abrir directamente la página privada sin entrar. Debe rechazarte o redirigirte. Prueba después una clave incorrecta y confirma que sigues sin acceso. Con la clave del laboratorio, entra y solicita de nuevo la página privada.

Por último, sal y vuelve a pedir esa ruta. Destruir la sesión y eliminar su cookie no son exactamente la misma operación: el ejemplo contempla ambas. No te limites a pulsar «atrás», porque el navegador podría mostrar una representación ya almacenada sin que el servidor acabe de autorizarla otra vez.

## Problema explicado paso a paso: recordar la vista de un catálogo

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

### Problema explicado paso a paso: entrar no significa tener cualquier permiso

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

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Elige dónde recordar cada dato

Para un visor de partituras debes guardar una preferencia de tamaño de letra y, por separado, la identidad del usuario que ha entrado. Explica qué dato podrías guardar como cookie de preferencia y cuál mantendrías en la sesión del servidor.

??? tip "Pista"
    Una preferencia modificable no cumple el mismo papel que una identidad verificada.

??? success "Solución paso a paso"
    El tamaño puede guardarse como cookie, validando sus opciones al leerlo. La identidad verificada debe mantenerse como estado de sesión en el servidor.

    El navegador puede conservar un identificador de sesión. No utilizaría una cookie con el nombre escrito por el usuario como prueba de que ha iniciado sesión.

### 2. Revisa dos navegadores

Has iniciado sesión en un perfil y la zona privada funciona. En otro perfil limpio, la misma URL solicita acceso. ¿Es necesariamente un fallo? Explica la diferencia entre este caso y dos pestañas del primer perfil.

??? tip "Pista"
    Los perfiles tienen almacenes de cookies independientes.

??? success "Solución paso a paso"
    No es necesariamente un fallo: el perfil limpio no dispone de la cookie identificadora de la primera sesión.

    Dos pestañas del mismo perfil normalmente comparten cookies. Por eso no equivalen a dos usuarios independientes. Para comprobar aislamiento, los perfiles separados son una prueba más apropiada.

### 3. Distingue entrar de tener permiso

Un usuario ha iniciado sesión, pero solo el rol `editor` puede modificar una ficha. Escribe el control PHP de esa operación suponiendo que `$_SESSION['rol']` se asignó desde datos fiables durante el acceso. Devuelve 403 si no corresponde.

??? tip "Pista"
    Una identidad válida no concede todos los permisos.

??? success "Solución paso a paso"
    ```php
    <?php
    session_start();
    if (($_SESSION['rol'] ?? '') !== 'editor') {
        http_response_code(403);
        exit('No puedes modificar esta ficha');
    }
    echo 'Puedes continuar con la modificación';
    ```

    La comparación se hace antes de modificar nada. Un rol ausente también se rechaza. No se toma el permiso de un campo editable del formulario.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Cookie** | Dato que guarda el navegador y envía en las peticiones que corresponden a su ámbito. |
| **Sesión** | Estado que el servidor asocia con un identificador del cliente entre varias peticiones. |
| **Hash de contraseña** | Representación calculada para verificar una contraseña sin guardarla en claro; no se descifra. |
| **Autenticación y autorización** | Comprobar la identidad y decidir los permisos de esa identidad. |

!!! success "Para repasar"
    Ocultar un enlace no protege una ruta. La comprobación debe ejecutarse en el servidor antes de cualquier contenido privado.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
