# Xuleta de PHP

> Consulta ràpida. La teoria completa està en la [secció de PHP](../php/index.md).

## Bàsic

```php
<?php                                  // fitxer només PHP: sense ?> al final
echo "Hola, $nom\n";                   // "..." interpreta variables · '...' no
$text = "Total: " . $n;                // . uneix textos
<?= htmlspecialchars($x) ?>            // dins d'HTML: mostrar (escapat)
var_dump($x); print_r($array);         // depurar
```

| | |
| - | - |
| Comparar | **`===`** `!==` `<` `>` · lògics `&&` `||` `!` |
| Per defecte | `$x = $_GET["x"] ?? "valor";` |
| Condició | `if (...) { } elseif (...) { } else { }` · `$a = $c ? "si" : "no";` |
| `match` | `$t = match ($x) { 1, 2 => "a", default => "b" };` |
| Bucles | `for ($i = 0; $i < 5; $i++) { }` · `while (...) { }` · `foreach ($arr as $clau => $valor) { }` |
| Funció | `function nom(string $x, int $y = 0): string { return ...; }` · `fn($x) => $x * 2` |
| Incloure | `require_once __DIR__ . "/db.php";` |

## Arrays i text

```php
$a = ["ISO", "PAR"];  $a[] = "GBD";        count($a);  in_array("PAR", $a, true);
$alumne = ["nom" => "Ana", "nota" => 8];    $alumne["nom"];  isset($alumne["x"]);
implode(", ", $a);  explode(",", $text);    sort($a);  array_sum($notes);
array_filter($a, fn($x) => $x > 5);         array_map(fn($x) => $x * 2, $a);
mb_strlen($s);  mb_strtoupper($s);  trim($s);  str_replace("a", "b", $s);  str_contains($s, "x");
sprintf("%.2f", $x);  number_format($x, 2, ",", ".");  date("d/m/Y H:i");
```

## Formularis

```php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $nom = trim($_POST["nom"] ?? "");
    if ($nom === "") $errors[] = "Falta el nom.";
    if (!filter_var($correu, FILTER_VALIDATE_EMAIL)) $errors[] = "Correu no vàlid.";
    if (!$errors) { /* guardar */ header("Location: llista.php"); exit; }   // PRG
}
$id = filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT);
```

- **GET** = URL (cercar) · **POST** = enviar dades · la clau és el `name` del camp
- **Valida en el servidor** · **`htmlspecialchars`** en mostrar (XSS)
- Fitxers: `enctype="multipart/form-data"` · `$_FILES` · `move_uploaded_file()`

## Sessions i contrasenyes

```php
session_start();                                     // primera línia de cada pàgina
$_SESSION["usuari"] = $u;    session_regenerate_id(true);    session_destroy();
if (!isset($_SESSION["usuari"])) { header("Location: login.php"); exit; }
$hash = password_hash($clau, PASSWORD_DEFAULT);      password_verify($clau, $hash);
setcookie("idioma", "ca", ["expires" => time() + 3600, "httponly" => true]);  $_COOKIE["idioma"];
```

## PDO (PostgreSQL)

```php
$pdo = new PDO("pgsql:host=127.0.0.1;port=5432;dbname=institut", "app", "clau", [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);
$files = $pdo->query("SELECT * FROM alumnes")->fetchAll();          // sense dades de l'usuari
$stmt = $pdo->prepare("SELECT * FROM alumnes WHERE id = ?");          // AMB dades: preparada
$stmt->execute([$id]);   $fila = $stmt->fetch();                      // false si no n'hi ha
$stmt = $pdo->prepare("INSERT INTO alumnes (nom, cicle) VALUES (:nom, :cicle)");
$stmt->execute(["nom" => $nom, "cicle" => $cicle]);   $stmt->rowCount();
$pdo->beginTransaction(); ... $pdo->commit(); / $pdo->rollBack();
```

MySQL: `mysql:host=...;dbname=...;charset=utf8mb4` · SQLite: `sqlite:/ruta/app.db`

## Terminal

```bash
php -S localhost:8000          # servidor de proves en la carpeta actual
php -l fitxer.php              # comprovar la sintaxi
php fitxer.php                 # executar en el terminal
php -m                         # extensions (php-pgsql, php-mbstring...)
```

## Desplegar

```bash
sudo apt install apache2 libapache2-mod-php php-pgsql
sudo chown -R root:www-data /var/www/app        # www-data LLIG, no escriu
sudo find /var/www/app -type d -exec chmod 750 {} +
sudo find /var/www/app -type f -exec chmod 640 {} +
sudo a2ensite app && sudo apache2ctl configtest && sudo systemctl reload apache2
tail -f /var/log/apache2/error.log              # si hi ha error 500
```

`php.ini` de producció: `display_errors = Off` · `log_errors = On` · `expose_php = Off`

Docker: `FROM php:8.3-apache` + `RUN docker-php-ext-install pdo_pgsql` · la BD es diu pel **nom del servei** (`host=bd`)

## Errors que més ixen

| Missatge | Solució |
| -------- | ------- |
| Pàgina en blanc / 500 | `error.log` · `php -l` |
| `syntax error, unexpected token` | falta `;` en la línia d'**abans** |
| `Undefined array key "x"` | `$_POST["x"] ?? ""` |
| `Cannot modify header information - headers already sent` | res (ni espais) abans de `<?php` i del `header()` |
| `could not find driver` | `apt install php-pgsql` i reiniciar Apache |
| `SQLSTATE[08006] ... Connection refused` | PostgreSQL parat o host/port malament |
| Es descarrega el `.php` | el servidor no té PHP |
