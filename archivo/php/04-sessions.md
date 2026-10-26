# 4. Sessions i usuaris

HTTP **no té memòria**: cada petició és independent, i el servidor no sap si dues peticions venen de la mateixa persona. Per a recordar coses (qui ha entrat, el carret de la compra) s'usen **galetes** i **sessions**.

## Galetes (*cookies*)

Una **galeta** és una dada xicoteta que el servidor demana al navegador que guarde, i que el navegador **torna a enviar** en cada petició a eixe lloc.

```php
setcookie("idioma", "ca", [
    "expires"  => time() + 30 * 24 * 3600,     // 30 dies (sense: s'esborra en tancar el navegador)
    "path"     => "/",
    "httponly" => true,                        // JavaScript no la pot llegir
    "samesite" => "Lax",
]);

$idioma = $_COOKIE["idioma"] ?? "ca";           // llegir-la (en la petició SEGÜENT)
```

!!! warning "Les galetes les controla el client"
    L'usuari pot veure-les i **canviar-les** (++f12++ → Aplicació → Galetes). Mai guardes en una galeta coses com `admin=1` o el nom de l'usuari que ha entrat. Per a això hi ha les sessions.

## Sessions ⭐

Amb una **sessió**, les dades es guarden **en el servidor**, i el navegador només guarda una galeta amb un **identificador** aleatori (`PHPSESSID`).

```text
 Navegador                                     Servidor
    │  POST login.php (usuari, contrasenya)       │
    │ ──────────────────────────────────────────▶ │  session_start() → crea la sessió "eaecghgi..."
    │                                             │  $_SESSION["usuari"] = "ana"  (es guarda en el SERVIDOR)
    │ ◀── Set-Cookie: PHPSESSID=eaecghgi...  ──── │
    │                                             │
    │  GET privada.php                            │
    │  Cookie: PHPSESSID=eaecghgi...  ──────────▶ │  session_start() → recupera la sessió
    │                                             │  $_SESSION["usuari"] → "ana" ✅
```

```php
session_start();                      // AL PRINCIPI de cada pàgina que use la sessió (abans de cap eixida)
$_SESSION["usuari"] = "ana";          // guardar
echo $_SESSION["usuari"];             // llegir
unset($_SESSION["carret"]);           // esborrar una dada
session_destroy();                    // acabar la sessió
```

## Un *login* complet

Tres fitxers: entrar, una pàgina privada i eixir. [:material-download: login.zip](../assets/fitxers/php/login.zip)

### Les contrasenyes: mai en clar

Les contrasenyes **no** es guarden mai tal qual (si algú roba la base de dades, les tindria totes). Es guarda un **hash**: el resultat d'una funció d'una sola direcció. Per a comprovar-la, es calcula el hash del que escriu l'usuari i es compara.

```php
$hash = password_hash("Secret123", PASSWORD_DEFAULT);      // en crear l'usuari
// $2y$10$s4doXGBHudCgrUFdIaSUgOEI.h3euOBS0okhtU.iB/JE.hl.sBQxG

password_verify("Secret123", $hash);    // true
password_verify("dolenta", $hash);      // false
```

- `password_hash` usa **bcrypt** i afig una **sal** aleatòria: la mateixa contrasenya dona un hash **diferent** cada vegada (i, tot i això, `password_verify` funciona).
- **Mai** `md5()` ni `sha1()` per a contrasenyes: són massa ràpids i es poden trencar.
- El camp de la base de dades per al hash: `VARCHAR(255)`.

### `usuaris.php`

```php title="usuaris.php"
<?php
// En una aplicació real, açò estaria en la base de dades.
// Els hash s'han generat amb: php -r 'echo password_hash("Secret123", PASSWORD_DEFAULT);'
return [
    "ana" => '$2y$10$s4doXGBHudCgrUFdIaSUgOEI.h3euOBS0okhtU.iB/JE.hl.sBQxG',
];
```

### `login.php`

```php title="login.php"
<?php
session_start();
$usuaris = require "usuaris.php";
$error = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $usuari = $_POST["usuari"] ?? "";
    $clau   = $_POST["clau"] ?? "";

    if (isset($usuaris[$usuari]) && password_verify($clau, $usuaris[$usuari])) {
        session_regenerate_id(true);          // nou identificador de sessió (seguretat)
        $_SESSION["usuari"] = $usuari;
        header("Location: privada.php");
        exit;
    }
    $error = "Usuari o contrasenya incorrectes.";
}
?>
<!DOCTYPE html>
<html lang="ca"><head><meta charset="UTF-8"><title>Entrar</title></head>
<body>
    <h1>Entrar</h1>
    <?php if ($error): ?><p class="error"><?= htmlspecialchars($error) ?></p><?php endif; ?>
    <form method="post">
        <label>Usuari <input name="usuari" required></label>
        <label>Contrasenya <input type="password" name="clau" required></label>
        <button>Entrar</button>
    </form>
</body></html>
```

!!! info "Per què el mateix missatge"
    «Usuari o contrasenya incorrectes» i no «l'usuari no existix»: així un atacant no pot saber quins usuaris existixen.

### `privada.php`

```php title="privada.php"
<?php
session_start();
if (!isset($_SESSION["usuari"])) {          // no ha entrat: a la pàgina d'entrada
    header("Location: login.php");
    exit;
}
$_SESSION["visites"] = ($_SESSION["visites"] ?? 0) + 1;
?>
<!DOCTYPE html>
<html lang="ca"><head><meta charset="UTF-8"><title>Zona privada</title></head>
<body>
    <h1>Hola, <?= htmlspecialchars($_SESSION["usuari"]) ?></h1>
    <p>Has visitat esta pàgina <?= $_SESSION["visites"] ?> vegades en esta sessió.</p>
    <p><a href="logout.php">Eixir</a></p>
</body></html>
```

Les primeres línies (fins a l'`exit`) es posen al principi de **cada** pàgina privada. Millor en un fitxer `protegix.php` que s'inclou amb `require`.

### `logout.php`

```php title="logout.php"
<?php
session_start();
$_SESSION = [];
session_destroy();
setcookie(session_name(), "", time() - 3600, "/");   // esborrar la galeta de sessió
header("Location: login.php");
exit;
```

### Provat

```console
$ curl -s -o /dev/null -w "%{http_code} -> %{redirect_url}\n" http://localhost:8000/privada.php
302 -> http://localhost:8000/login.php                        ← sense entrar: fora

$ curl -s -d "usuari=ana&clau=dolenta" http://localhost:8000/login.php | grep error
    <p class="error">Usuari o contrasenya incorrectes.</p>

$ curl -s -c galetes.txt -b galetes.txt -o /dev/null -w "%{http_code} -> %{redirect_url}\n" \
       -d "usuari=ana&clau=Secret123" http://localhost:8000/login.php
302 -> http://localhost:8000/privada.php                      ← entra

$ curl -s -c galetes.txt -b galetes.txt http://localhost:8000/privada.php | grep vegades
    <p>Has visitat esta pàgina 1 vegades en esta sessió.</p>
$ curl -s -c galetes.txt -b galetes.txt http://localhost:8000/privada.php | grep vegades
    <p>Has visitat esta pàgina 2 vegades en esta sessió.</p>  ← la sessió recorda
```

(`-c` i `-b` fan que `curl` guarde i torne a enviar les galetes, com un navegador.)

## Usuaris en la base de dades

```sql
CREATE TABLE usuaris (
    id      SERIAL PRIMARY KEY,
    usuari  VARCHAR(50) UNIQUE NOT NULL,
    hash    VARCHAR(255) NOT NULL,
    rol     VARCHAR(20) NOT NULL DEFAULT 'usuari'
);
```

```php
$stmt = bd()->prepare("SELECT id, hash, rol FROM usuaris WHERE usuari = ?");
$stmt->execute([$usuari]);
$fila = $stmt->fetch();
if ($fila && password_verify($clau, $fila["hash"])) {
    session_regenerate_id(true);
    $_SESSION["id"]  = $fila["id"];
    $_SESSION["rol"] = $fila["rol"];
    // ...
}
```

I per a limitar pàgines a un **rol**: `if (($_SESSION["rol"] ?? "") !== "admin") { http_response_code(403); exit("Prohibit"); }`.

## Seguretat de les sessions

| Mesura | Per què |
| ------ | ------- |
| **HTTPS** | si no, l'identificador de sessió viatja en clar i es pot robar |
| `session_regenerate_id(true)` en entrar | evita la **fixació de sessió** (que un atacant et faça usar un identificador que ell ja coneix) |
| Galeta de sessió `HttpOnly`, `Secure`, `SameSite` | que JavaScript no la llija, que només vaja per HTTPS, que no s'envie des d'altres webs |
| Temps d'inactivitat | tancar la sessió després d'un temps sense ús |
| Escapar amb `htmlspecialchars` | un XSS permetria robar la galeta |

```php
// Abans de session_start(), o en php.ini (session.cookie_httponly = 1...)
session_set_cookie_params(["httponly" => true, "secure" => true, "samesite" => "Lax"]);
session_start();
```

## Errors típics

| Problema | Per què | Solució |
| -------- | ------- | ------- |
| `session_start(): Session cannot be started after headers have already been sent` | Hi ha eixida (HTML, `echo`, un espai) abans de `session_start()` | `session_start()` en la **primera** línia |
| La sessió «s'oblida» en cada pàgina | Falta `session_start()` en eixa pàgina | En **totes** |
| `password_verify` sempre torna `false` | El hash s'ha tallat en guardar-lo (camp massa curt) o s'ha posat entre cometes dobles (`"$2y$..."`: PHP interpreta `$2y` com a variable) | `VARCHAR(255)`; cometes **simples** |
| Després d'eixir, amb el botó «enrere» es veu la pàgina privada | És la memòria cau del navegador; si recarregues, et trau | Normal; afig capçaleres `Cache-Control: no-store` si cal |
| `$_COOKIE["x"]` no existix just després de `setcookie` | La galeta arriba en la **petició següent** | Llig-la en la pròxima pàgina |

!!! success "Per a l'examen"
    ```php
    session_start();                                   // primera línia, en TOTES les pàgines
    $_SESSION["usuari"] = $u;  isset($_SESSION["usuari"]);  session_destroy();
    $hash = password_hash($clau, PASSWORD_DEFAULT);    password_verify($clau, $hash);
    session_regenerate_id(true);                       // en entrar
    if (!isset($_SESSION["usuari"])) { header("Location: login.php"); exit; }
    setcookie("nom", "valor", ["expires" => time() + 3600, "httponly" => true]);  $_COOKIE["nom"];
    ```
    - **Galeta** = en el **client** (es pot manipular) · **Sessió** = dades en el **servidor**, en el client només l'identificador (`PHPSESSID`)
    - Contrasenyes: **`password_hash`** / **`password_verify`** (bcrypt + sal), mai en clar ni MD5
    - Missatge d'error genèric · HTTPS · `HttpOnly`
