# 2. El llenguatge

Si ja coneixes [Python](../python/index.md) o [Bash](../bash/index.md), PHP és molt semblant. Ací hi ha el que cal per a entendre i modificar una aplicació web.

## Un exemple complet

```php title="notes.php"
<?php
// Un array associatiu: clau => valor
$notes = [
    "ISO" => 8.5,
    "PAR" => 4,
    "GBD" => 9,
    "LMSGI" => 6.25,
];

function qualificacio(float $nota): string
{
    return match (true) {
        $nota < 5 => "Suspés",
        $nota < 7 => "Aprovat",
        $nota < 9 => "Notable",
        default   => "Excel·lent",
    };
}

foreach ($notes as $modul => $nota) {
    printf("%-6s %5.2f  %s\n", $modul, $nota, qualificacio($nota));
}

$mitjana = array_sum($notes) / count($notes);
echo "Mitjana: " . round($mitjana, 2) . "\n";

$aprovats = array_filter($notes, fn($n) => $n >= 5);
echo "Aprovats: " . implode(", ", array_keys($aprovats)) . "\n";

if ($mitjana >= 5 && count($aprovats) === count($notes)) {
    echo "Curs aprovat\n";
} else {
    echo "Mòduls suspesos: " . (count($notes) - count($aprovats)) . "\n";
}
```

```console
$ php notes.php
ISO     8.50  Notable
PAR     4.00  Suspés
GBD     9.00  Excel·lent
LMSGI   6.25  Aprovat
Mitjana: 6.94
Aprovats: ISO, GBD, LMSGI
Mòduls suspesos: 1
```

## Operadors

| Tipus | Operadors | Exemple → resultat |
| ----- | --------- | ------------------ |
| Aritmètics | `+ - * / % **` | `5 / 2` → `2.5` · `7 % 3` → `1` · `2 ** 3` → `8` · `intdiv(5, 2)` → `2` |
| Text | `.` (unir) · `.=` (afegir) | `$s .= "!"` |
| Comparació | `== != < > <= >=` | `"5" == "5.0"` → `true` (compara el **valor**) |
| Comparació estricta | **`===`** · `!==` | `"5" === 5` → `false` (compara valor **i tipus**) |
| Lògics | `&&` (i) · `||` (o) · `!` (no) | |
| Valor per defecte | `??` | `$_GET["p"] ?? 1` → 1 si no existix |
| Assignació | `= += -= *= /=` · `++` · `--` | |

!!! tip "Usa `===`"
    `==` fa conversions estranyes (`"abc" == 0` era `true` en PHP 7). `===` no en fa: és el segur.

## Condicionals

```php
if ($nota >= 9) {
    $text = "Excel·lent";
} elseif ($nota >= 5) {
    $text = "Aprovat";
} else {
    $text = "Suspés";
}

$text = $nota >= 5 ? "Aprovat" : "Suspés";       // ternari

$torn = match ($hora) {                          // match: compara amb ===
    8, 9, 10, 11, 12, 13 => "matí",
    15, 16, 17, 18, 19, 20 => "vesprada",
    default => "fora d'horari",
};

switch ($dia) {                                  // switch: la forma clàssica
    case "dissabte":
    case "diumenge":
        echo "Cap de setmana";
        break;
    default:
        echo "Laborable";
}
```

## Bucles

```php
for ($i = 1; $i <= 5; $i++) {
    echo "$i ";
}

$n = 10;
while ($n > 0) {
    $n -= 3;
}

foreach ($moduls as $modul) {               // recórrer un array ⭐
    echo "<li>$modul</li>";
}

foreach ($notes as $modul => $nota) {       // amb la clau
    echo "$modul: $nota";
}
```

`break` ix del bucle; `continue` passa a la següent volta.

## Arrays

```php
$moduls = ["ISO", "PAR", "GBD"];              // indexat: posicions 0, 1, 2
echo $moduls[0];                              // ISO
$moduls[] = "LMSGI";                          // afegir al final
echo count($moduls);                          // 4

$alumne = [                                   // associatiu
    "nom" => "Ana",
    "cognoms" => "Puig Vidal",
    "notes" => [8.5, 7, 9],                   // un array dins d'un altre
];
echo $alumne["nom"];
echo $alumne["notes"][1];                     // 7

$alumnes = [                                  // array d'arrays: com les files d'una taula
    ["nom" => "Ana", "cicle" => "ASIR"],
    ["nom" => "Pep", "cicle" => "DAW"],
];
foreach ($alumnes as $a) {
    echo "{$a['nom']} ({$a['cicle']})\n";
}
```

| Funció | Fa |
| ------ | -- |
| `count($a)` | quants elements |
| `in_array($x, $a)` | si hi és |
| `array_key_exists("k", $a)` / `isset($a["k"])` | si existix la clau |
| `array_keys($a)` / `array_values($a)` | les claus / els valors |
| `sort($a)` · `rsort` · `asort` · `ksort` | ordenar (per valor; al revés; mantenint claus; per clau) |
| `array_sum`, `max`, `min` | |
| `array_map(fn($x) => $x * 2, $a)` | aplicar una funció a cada element |
| `array_filter($a, fn($x) => $x > 5)` | quedar-se amb els que complixen |
| `implode(", ", $a)` / `explode(",", $text)` | array → text / text → array |
| `print_r($a)` / `var_dump($a)` | mostrar-lo (depurar) |

## Funcions de text

| Funció | Exemple → resultat |
| ------ | ------------------ |
| `strlen($s)` / **`mb_strlen($s)`** | `strlen("Món")` → 4 (bytes) · `mb_strlen("Món")` → 3 (caràcters) |
| `strtoupper`, `strtolower` / `mb_strtoupper` | `mb_strtoupper("àrea")` → `ÀREA` |
| `ucfirst($s)` | `"ana"` → `Ana` |
| `trim($s)` | lleva espais del principi i del final |
| `str_replace("a", "4", "casa")` | `c4s4` |
| `substr("PostgreSQL", 0, 4)` | `Post` |
| `str_contains($s, "x")` · `str_starts_with` · `str_ends_with` | `true` / `false` |
| `sprintf("%05.2f", 3.14159)` | `03.14` |
| `number_format(1234.5, 2, ",", ".")` | `1.234,50` |
| `htmlspecialchars($s)` | escapar per a HTML (tema 3) ⭐ |

!!! warning "Accents i `mb_`"
    Amb text en valencià, usa les funcions **`mb_`** (`mb_strlen`, `mb_substr`, `mb_strtoupper`): les normals compten **bytes**, i les lletres amb accent ocupen 2 bytes en UTF-8.

## Funcions

```php
function saluda(string $nom, string $salutacio = "Hola"): string    // amb valor per defecte
{
    return "$salutacio, $nom!";
}

echo saluda("Ana");                   // Hola, Ana!
echo saluda("Pep", "Bon dia");        // Bon dia, Pep!

$doble = fn($x) => $x * 2;            // funció fletxa (anònima, d'una línia)
echo $doble(4);                       // 8
```

- Els tipus (`string`, `int`, `float`, `bool`, `array`, `?string` = pot ser null) són opcionals però recomanats.
- Les variables de dins d'una funció **no** veuen les de fora (cal passar-les com a paràmetres).

## Incloure altres fitxers

Les aplicacions es dividixen en fitxers: la connexió a la base de dades, la capçalera i el peu de les pàgines, les funcions...

```php
require "db.php";              // si no existix: ERROR i s'atura
require_once "funcions.php";   // només una vegada encara que es demane més ⭐
include "capcalera.php";       // si no existix: només un avís, i continua
```

```php
<?php require __DIR__ . "/capcalera.php"; ?>
<main>
    <h1>Inici</h1>
</main>
<?php require __DIR__ . "/peu.php"; ?>
```

`__DIR__` és la carpeta del fitxer actual: així la ruta funciona des d'on siga.

## Dates

```php
echo date("d/m/Y H:i");                       // 12/10/2026 11:25
echo date("Y-m-d");                           // 2026-10-12 (el format de les bases de dades)
$d = new DateTime("2004-03-12");
echo $d->diff(new DateTime())->y;             // anys passats: l'edat
date_default_timezone_set("Europe/Madrid");
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `Undefined array key "x"` | La clau no existix (per exemple, un camp del formulari que no s'ha enviat) | `$a["x"] ?? valor` o `isset()` |
| `Undefined variable $x` dins d'una funció | Les funcions no veuen les variables de fora | Passa-la com a paràmetre |
| `Call to undefined function x()` | Mal escrita, o el fitxer on està no s'ha inclòs (o falta una extensió: `mb_strlen` → `php-mbstring`) | `require`; instal·la l'extensió |
| `Failed opening required 'x.php'` | Ruta incorrecta | `require __DIR__ . "/x.php"` |
| `Cannot redeclare function x()` | El fitxer s'ha inclòs dues vegades | `require_once` |
| Un `if ($a = 5)` sempre és cert | `=` assigna; per a comparar: `===` | `if ($a === 5)` |
| Comptar malament les lletres amb accent | `strlen` compta bytes | `mb_strlen` |

!!! success "Per a l'examen"
    ```php
    if (...) { } elseif (...) { } else { }        $x = $c ? "a" : "b";      $v = $_GET["p"] ?? 1;
    $r = match ($x) { 1, 2 => "a", default => "b" };
    for ($i = 0; $i < 5; $i++) { }     while (...) { }     foreach ($arr as $clau => $valor) { }
    $a = ["k" => "v"]; $a[] = "nou"; count($a); in_array(); implode(", ", $a); explode(",", $s);
    function nom(string $x, int $y = 0): string { return ...; }
    require_once __DIR__ . "/fitxer.php";
    ```
    - **`===`** (valor i tipus) · `.` concatena · `??` valor per defecte · funcions **`mb_`** per al text amb accents
