# 1. Què és PHP

**PHP** és un llenguatge de programació que s'executa **en el servidor** i genera pàgines web. Hi ha fet WordPress, Moodle, Nextcloud, Wikipedia (MediaWiki), Drupal, Laravel...

## Com funciona

```text
 Navegador                     Servidor web                         Base de dades
    │  GET /alumnes.php          │                                       │
    │ ─────────────────────────▶ │ 1. Apache/Nginx veu que és .php        │
    │                            │ 2. El passa a PHP                      │
    │                            │ 3. PHP executa el codi ──── SQL ─────▶ │
    │                            │                        ◀── files ───── │
    │                            │ 4. PHP genera HTML                     │
    │ ◀──────── HTML ─────────── │                                       │
    │  (el navegador NO veu el codi PHP, només l'HTML resultant)          │
```

| Codi que s'executa en... | Llenguatges | Qui el veu |
| ------------------------ | ----------- | ---------- |
| el **servidor** (*backend*) | PHP, Python, Java, Node.js | ningú: només s'envia el resultat |
| el **client** (*frontend*) | HTML, CSS, JavaScript | el navegador (qualsevol pot veure'l amb ++ctrl+u++) |

Per això en PHP es poden posar coses que l'usuari no ha de veure (la contrasenya de la base de dades, la lògica de validació).

## Instal·lar

```bash
sudo apt install php-cli               # per a executar PHP en el terminal
php -v
```

Per a la web, PHP s'integra amb Apache (`libapache2-mod-php`) o amb Nginx (`php-fpm`): es veu en [Desplegar aplicacions](07-desplegament.md). Per a programar i provar, PHP porta un **servidor web de proves**:

```bash
cd /ruta/del/projecte
php -S localhost:8000                  # i obrir http://localhost:8000
```

!!! warning "Només per a proves"
    `php -S` és per a desenvolupar en el teu equip. En producció, sempre Apache o Nginx.

## El primer script

```php title="hola.php"
<!DOCTYPE html>
<html lang="ca">
<head><meta charset="UTF-8"><title>Hola</title></head>
<body>
    <h1>Hola!</h1>
    <p>Hui és <?php echo date("d/m/Y"); ?> i són les <?= date("H:i") ?>.</p>
    <?php if (date("H") < 14): ?>
        <p>Bon dia.</p>
    <?php else: ?>
        <p>Bona vesprada.</p>
    <?php endif; ?>
</body>
</html>
```

- El codi PHP va entre **`<?php`** i **`?>`**. Tot el que hi ha fora es copia tal qual (l'HTML).
- **`<?= x ?>`** és una abreviatura de `<?php echo x; ?>`.
- Cada instrucció acaba en **`;`**.
- Comentaris: `// una línia`, `# una línia`, `/* diverses */`.
- Si el fitxer és només PHP (sense HTML), **no** es posa el `?>` final (evita que s'envien espais en blanc sense voler).

El navegador rep:

```html
<p>Hui és 12/10/2026 i són les 10:15.</p>
<p>Bon dia.</p>
```

## Variables i tipus

```php title="variables.php"
<?php
$nom = "Ana";                 // text (string)
$edat = 19;                   // enter (int)
$nota = 8.5;                  // decimal (float)
$aprovat = true;              // booleà (bool)
$res = null;                  // sense valor

echo "Hola, $nom!\n";                         // les cometes dobles substituïxen les variables
echo 'Hola, $nom!' . "\n";                    // les simples, no
echo "L'any que ve tindràs " . ($edat + 1) . " anys.\n";   // . uneix textos
echo "Nota: {$nota}\n";

var_dump($edat, $nota, $aprovat, $res);       // tipus i valor (per a depurar)
echo gettype($nom), "\n";
```

```console
$ php variables.php
Hola, Ana!
Hola, $nom!
L'any que ve tindràs 20 anys.
Nota: 8.5
int(19)
float(8.5)
bool(true)
NULL
string
```

| Regla | |
| ----- | - |
| Les variables comencen per **`$`** | `$nom`, `$total_alumnes` |
| Distingixen majúscules | `$Nom` ≠ `$nom` |
| No es declara el tipus | PHP el deduïx del valor |
| **`.`** uneix textos | `"Hola " . $nom` (no `+`) |
| `"..."` interpreta variables i `\n` | `'...'` és literal |
| `\n` | salt de línia (en el terminal; en HTML, `<br>`) |

## Mostrar els errors (mentre programes)

Per defecte, un error de PHP pot donar una **pàgina en blanc**. Per a veure'ls en desenvolupament:

```php
<?php
ini_set("display_errors", "1");
error_reporting(E_ALL);
```

O en `php.ini` (`/etc/php/8.3/apache2/php.ini`): `display_errors = On`. En **producció**, `Off` (no s'han de mostrar a l'usuari) i mirar el registre (`/var/log/apache2/error.log`).

```bash
php -l fitxer.php            # comprovar la sintaxi sense executar-lo ⭐
```

```text
PHP Parse error:  syntax error, unexpected token "echo" in hola.php on line 3
```

## Errors típics

| Problema | Per què | Solució |
| -------- | ------- | ------- |
| El navegador mostra el codi PHP o el descarrega | El servidor no té PHP, o el fitxer no acaba en `.php`, o l'has obert com a fitxer (`file://`) | Instal·la PHP en el servidor; obri'l per `http://` |
| Pàgina en blanc | Error de PHP amb `display_errors = Off` | Mira `error.log`; activa els errors en desenvolupament; `php -l` |
| `syntax error, unexpected token ...` | Falta un `;` (normalment en la línia **d'abans**), o una cometa o clau sense tancar | Mira la línia anterior |
| `Undefined variable $x` | Variable mal escrita o no inicialitzada | Revisa el nom (i les majúscules) |
| `Unsupported operand types: string + string` | En PHP els textos s'uneixen amb `.`, no amb `+` | `"Total: " . $n` |
| Ix `$nom` literalment | Cometes simples | Cometes dobles o concatenar |

!!! success "Per a l'examen"
    - PHP s'executa en el **servidor** i envia **HTML** · el client no veu el codi
    - `<?php ... ?>` · `<?= $x ?>` · `;` al final · `$variables` · `.` concatena · `"..."` interpreta variables
    - `php -S localhost:8000` (proves) · `php -l fitxer.php` (sintaxi) · `var_dump()` (depurar)
    - Errors: `display_errors` en desenvolupament, **Off** en producció → `error.log`
