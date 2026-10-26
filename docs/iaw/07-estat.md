# UT2 · 4. Cookies, sessions i accés privat

## Per què una variable no recorda la visita anterior?

Cada petició executa de nou el programa. Una variable com `$seccio = 'mapes';` no recorda una selecció feta en una petició anterior. HTTP no incorpora per si mateix una memòria d'usuari: l'aplicació ha de construir-la.

| Mecanisme | On queda la informació | Exemple |
| --- | --- | --- |
| Variable normal | Durant l'execució de la petició | Resultat d'un càlcul |
| Cookie | Al navegador, que l'envia en peticions posteriors | Preferència de vista |
| Sessió | Habitualment al servidor; el navegador conserva l'identificador | Usuari autenticat |

Les cookies poden ser modificades pel client. No les uses com a prova de permisos. Una sessió també necessita controls d'accés al servidor.

## Exemple resolt: recordar la vista d'un catàleg

Desa `vista.php`:

```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $vista = $_POST['vista'] ?? '';
    if (is_string($vista) && in_array($vista, ['graella', 'llista'], true)) {
        setcookie('vista_catalog', $vista, [
            'expires' => time() + 86400 * 7,
            'path' => '/',
            'httponly' => true,
            'samesite' => 'Lax',
        ]);
        header('Location: vista.php', true, 303);
        exit;
    }
}
$vista = $_COOKIE['vista_catalog'] ?? 'graella';
if (!is_string($vista) || !in_array($vista, ['graella', 'llista'], true)) {
    $vista = 'graella';
}
?>
<p>Vista: <?= htmlspecialchars($vista, ENT_QUOTES, 'UTF-8') ?></p>
<form method="post" action="vista.php">
    <button name="vista" value="graella">Graella</button>
    <button name="vista" value="llista">Llista</button>
</form>
```

**Seguiment:** la primera visita mostra graella. El botó envia POST; PHP envia `Set-Cookie` i una redirecció 303; el navegador fa un nou GET amb la cookie i mostra llista. `$_COOKIE` no s'actualitza automàticament amb el valor que acabes d'enviar: es llig de la petició rebuda. En HTTPS afegeix `'secure' => true` a les opcions de la cookie.

`setcookie`, `session_start` i `header` han d'anar abans de qualsevol eixida. Després d'una redirecció, `exit` atura el programa. És el patró POST–Redirect–GET: recarregar la pàgina final repeteix el GET.

## Autenticació: comprovar qui entra

La idea és **formulari → verificar credencials → renovar identificador → guardar identitat → comprovar identitat en cada ruta privada**. Autoritzar és decidir què pot fer eixa identitat; autenticar i autoritzar són decisions diferents.

Mini laboratori independent d'una biblioteca de partitures. Genera un hash amb `php -r 'echo password_hash("Partitura!47", PASSWORD_DEFAULT), PHP_EOL;'`. Copia el resultat en un fitxer local `usuaris.php`:

```php
<?php
return ['arxiver' => 'ENGANXA_ACI_EL_HASH_GENERAT'];
```

`acces.php` conté el formulari i el processament:

```php
<?php
session_start();
$usuaris = require __DIR__ . '/usuaris.php';
$error = '';
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $usuari = $_POST['usuari'] ?? '';
    $clau = $_POST['clau'] ?? '';
    if (is_string($usuari) && is_string($clau)
        && isset($usuaris[$usuari])
        && password_verify($clau, $usuaris[$usuari])) {
        session_regenerate_id(true);
        $_SESSION['identitat'] = $usuari;
        header('Location: arxiu.php', true, 303);
        exit;
    }
    $error = 'No s’ha pogut validar l’accés.';
}
?>
<p><?= htmlspecialchars($error, ENT_QUOTES, 'UTF-8') ?></p>
<form action="acces.php" method="post">
    <label>Usuari <input name="usuari" required></label>
    <label>Clau <input name="clau" type="password" required></label>
    <button>Entrar</button>
</form>
```

`arxiu.php` comprova l'accés abans d'enviar HTML:

```php
<?php
session_start();
if (!isset($_SESSION['identitat'])) {
    header('Location: acces.php');
    exit;
}
?>
<h1>Arxiu de partitures</h1>
<p>Identitat: <?= htmlspecialchars($_SESSION['identitat'], ENT_QUOTES, 'UTF-8') ?></p>
<form action="eixir.php" method="post"><button>Eixir</button></form>
```

`eixir.php` tanca la sessió:

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
header('Location: acces.php', true, 303);
exit;
```

**Resultat esperat:** l'accés directe a `arxiu.php` redirigeix; les credencials del laboratori permeten entrar; després d'eixir, l'accés directe torna a redirigir. El hash és una representació per a verificar la clau, no una clau xifrada que es desxifra. Les credencials mostrades són només de prova.

Aquest exemple explica el mecanisme. Una aplicació publicada també necessita HTTPS, configuració segura de sessió, protecció CSRF i controls contra intents repetits.

## Comprovar l'aïllament

Entra en una finestra normal i obri `arxiu.php` en una finestra privada: la segona ha de demanar accés. Dues pestanyes del mateix perfil solen compartir cookies i sessió; no serveixen per a simular dos usuaris independents.

!!! success "Per a repassar"
    Amagar un enllaç no protegeix una ruta. La comprovació ha d'executar-se al servidor abans de qualsevol contingut privat.

---

Font del temari: [apunts originals de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
