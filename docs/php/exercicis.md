# Exercicis resolts d'IAW

Totes les solucions s'han provat amb el servidor de PHP (`php -S`) i `curl`, sobre la [base de dades `institut`](index.md#la-base-de-dades-dexemple). Les que usen la base de dades fan servir el `db.php` de l'[aplicació CRUD](06-crud.md).

## PHP bàsic

### 1. Taula de multiplicar

Fes `taula.php` que mostre la taula de multiplicar del número que arriba per la URL (`taula.php?n=7`). Si no arriba o no és un enter entre 1 i 10, la del 5.

??? success "Solució"
    ```php title="taula.php"
    <?php
    $n = filter_input(INPUT_GET, "n", FILTER_VALIDATE_INT, ["options" => ["min_range" => 1, "max_range" => 10]]) ?: 5;
    ?>
    <!DOCTYPE html>
    <html lang="ca"><head><meta charset="UTF-8"><title>Taula del <?= $n ?></title></head>
    <body>
        <h1>Taula del <?= $n ?></h1>
        <table>
            <?php for ($i = 1; $i <= 10; $i++): ?>
                <tr><td><?= $n ?> × <?= $i ?></td><td><?= $n * $i ?></td></tr>
            <?php endfor; ?>
        </table>
    </body></html>
    ```
    ```console
    $ curl -s "http://localhost:8000/taula.php?n=7" | grep -E "<h1>|7 × 3"
        <h1>Taula del 7</h1>
                <tr><td>7 × 3</td><td>21</td></tr>
    $ curl -s "http://localhost:8000/taula.php?n=99" | grep "<h1>"
        <h1>Taula del 5</h1>
    ```
    `filter_input` amb `min_range` i `max_range` torna `false` si no és vàlid; `?: 5` posa el valor per defecte.

### 2. Calculadora d'IVA

Un formulari amb un preu i el tipus d'IVA (21, 10 o 4 %) que mostre el preu amb IVA. Ha d'acceptar decimals amb coma, validar el preu i el tipus, i conservar el que s'havia escrit.

??? success "Solució"
    ```php title="iva.php"
    <?php
    $preu = $_POST["preu"] ?? "";
    $tipus = $_POST["tipus"] ?? "21";
    $tipusPermesos = ["21" => 21, "10" => 10, "4" => 4];
    $resultat = null;
    $error = "";

    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        $valor = filter_var(str_replace(",", ".", $preu), FILTER_VALIDATE_FLOAT);
        if ($valor === false || $valor < 0) {
            $error = "El preu ha de ser un número positiu.";
        } elseif (!isset($tipusPermesos[$tipus])) {
            $error = "Tipus d'IVA no vàlid.";
        } else {
            $iva = $valor * $tipusPermesos[$tipus] / 100;
            $resultat = sprintf("%s € + %s € d'IVA = %s €",
                number_format($valor, 2, ",", "."),
                number_format($iva, 2, ",", "."),
                number_format($valor + $iva, 2, ",", "."));
        }
    }
    ?>
    <form method="post">
        <input name="preu" value="<?= htmlspecialchars($preu) ?>">
        <select name="tipus">
            <?php foreach ($tipusPermesos as $clau => $pct): ?>
                <option value="<?= $clau ?>" <?= $clau == $tipus ? "selected" : "" ?>><?= $pct ?> %</option>
            <?php endforeach; ?>
        </select>
        <button>Calcular</button>
    </form>
    <?php if ($error): ?><p class="error"><?= htmlspecialchars($error) ?></p><?php endif; ?>
    <?php if ($resultat): ?><p><?= $resultat ?></p><?php endif; ?>
    ```
    ```console
    $ curl -s -d "preu=100&tipus=21" http://localhost:8000/iva.php | grep "<p>"
    <p>100,00 € + 21,00 € d'IVA = 121,00 €</p>
    $ curl -s -d "preu=19,99&tipus=10" http://localhost:8000/iva.php | grep "<p>"
    <p>19,99 € + 2,00 € d'IVA = 21,99 €</p>
    $ curl -s -d "preu=abc&tipus=21" http://localhost:8000/iva.php | grep error
    <p class="error">El preu ha de ser un número positiu.</p>
    $ curl -s -d "preu=10&tipus=50" http://localhost:8000/iva.php | grep error
    <p class="error">Tipus d&#039;IVA no vàlid.</p>
    ```
    El tipus es comprova contra una llista: encara que el `<select>` només tinga tres opcions, es pot enviar qualsevol cosa.

## Seguretat

### 3. Troba els problemes

```php
<?php
$pdo = new PDO("pgsql:host=localhost;dbname=institut", "postgres", "postgres");
$usuari = $_POST["usuari"];
$fila = $pdo->query("SELECT * FROM usuaris WHERE usuari = '$usuari' AND clau = '" . md5($_POST["clau"]) . "'")->fetch();
if ($fila) {
    setcookie("usuari", $usuari);
    echo "Benvingut, " . $_POST["usuari"];
}
```

??? success "Solució"
    1. Es connecta com a **`postgres`** (superusuari) amb una contrasenya trivial: cal un usuari propi amb el mínim de permisos.
    2. **Injecció SQL**: `$usuari` es concatena en el SQL. Amb `' OR '1'='1' --` s'entra sense contrasenya. → consulta **preparada**.
    3. **MD5** per a contrasenyes: és insegur. → `password_hash` / `password_verify`.
    4. Qui ha entrat es guarda en una **galeta**: l'usuari la pot canviar i fer-se passar per un altre. → **`$_SESSION`**.
    5. **XSS**: `$_POST["usuari"]` es mostra sense escapar. → `htmlspecialchars`.
    6. `$_POST["usuari"]` sense `?? ""`: avís si no arriba.

    ```php
    <?php
    session_start();
    $stmt = bd()->prepare("SELECT id, hash FROM usuaris WHERE usuari = ?");
    $stmt->execute([$_POST["usuari"] ?? ""]);
    $fila = $stmt->fetch();
    if ($fila && password_verify($_POST["clau"] ?? "", $fila["hash"])) {
        session_regenerate_id(true);
        $_SESSION["id"] = $fila["id"];
        echo "Benvingut, " . htmlspecialchars($_POST["usuari"]);
    }
    ```

### 4. Protegir l'aplicació CRUD

Fes que només es puga usar l'aplicació CRUD després d'entrar amb el [login del tema 4](04-sessions.md).

??? success "Solució"
    Un fitxer que s'inclou al principi de **cada** pàgina de l'aplicació (`index.php`, `form.php`, `esborra.php`):

    ```php title="protegix.php"
    <?php
    session_start();
    if (!isset($_SESSION["usuari"])) {
        header("Location: login.php");
        exit;
    }
    ```
    ```php
    <?php
    require __DIR__ . "/protegix.php";
    require __DIR__ . "/db.php";
    // ...
    ```

## Bases de dades

### 5. Cercador

Una pàgina amb un camp per a buscar alumnes per **població** (que trobe també trossos: «cast» → Castelló) i que mostre quants n'ha trobat.

??? success "Solució"
    ```php title="cerca.php"
    <?php
    require __DIR__ . "/db.php";      // el de l'aplicació CRUD

    $poblacio = trim($_GET["poblacio"] ?? "");
    $alumnes = [];
    if ($poblacio !== "") {
        $stmt = bd()->prepare("SELECT nom, cognoms FROM alumnes WHERE poblacio ILIKE ? ORDER BY cognoms");
        $stmt->execute(["%$poblacio%"]);
        $alumnes = $stmt->fetchAll();
    }
    ?>
    <form method="get">
        <input name="poblacio" value="<?= e($poblacio) ?>" placeholder="Població">
        <button>Buscar</button>
    </form>
    <?php if ($poblacio !== ""): ?>
        <p><?= count($alumnes) ?> resultats per a «<?= e($poblacio) ?>»</p>
        <ul>
            <?php foreach ($alumnes as $a): ?>
                <li><?= e($a["cognoms"]) ?>, <?= e($a["nom"]) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>
    ```
    ```console
    $ curl -s "http://localhost:8000/cerca.php?poblacio=cast" | grep -E "resultats|<li>"
        <p>3 resultats per a «cast»</p>
                <li>Beltran Ros, Sara</li>
                <li>Pons Ferrer, Laura</li>
                <li>Puig Vidal, Ana</li>
    $ curl -s "http://localhost:8000/cerca.php" --get --data-urlencode "poblacio=x' OR '1'='1" | grep resultats
        <p>0 resultats per a «x&#039; OR &#039;1&#039;=&#039;1»</p>
    ```
    - **GET** perquè és una cerca (es pot guardar l'enllaç).
    - Els `%` del `ILIKE` van **en el valor** del paràmetre, no en el SQL.
    - L'intent d'injecció no fa res: es busca literalment eixe text.

### 6. Paginació

Mostra els alumnes de 3 en 3, amb enllaços a les pàgines (`pagina.php?p=2`).

??? success "Solució"
    ```php title="pagina.php"
    <?php
    require __DIR__ . "/db.php";      // el de l'aplicació CRUD
    $perPagina = 3;
    $total = (int) bd()->query("SELECT COUNT(*) FROM alumnes")->fetchColumn();
    $pagines = max(1, (int) ceil($total / $perPagina));
    $pagina = filter_input(INPUT_GET, "p", FILTER_VALIDATE_INT, ["options" => ["min_range" => 1, "max_range" => $pagines]]) ?: 1;

    $stmt = bd()->prepare("SELECT nom, cognoms FROM alumnes ORDER BY cognoms LIMIT ? OFFSET ?");
    $stmt->execute([$perPagina, ($pagina - 1) * $perPagina]);
    foreach ($stmt->fetchAll() as $a) {
        echo "<li>" . e($a["cognoms"]) . ", " . e($a["nom"]) . "</li>\n";
    }
    echo "<p>Pàgina $pagina de $pagines</p>\n";
    for ($i = 1; $i <= $pagines; $i++) {
        echo $i === $pagina ? "<strong>$i</strong> " : "<a href=\"?p=$i\">$i</a> ";
    }
    ```
    ```console
    $ curl -s "http://localhost:8000/pagina.php?p=2"
    <li>Pons Ferrer, Laura</li>
    <li>Puig Vidal, Ana</li>
    <li>Roig Serra, Pep</li>
    <p>Pàgina 2 de 3</p>
    <a href="?p=1">1</a> <strong>2</strong> <a href="?p=3">3</a>
    $ curl -s "http://localhost:8000/pagina.php?p=9" | grep Pàgina
    <p>Pàgina 1 de 3</p>
    ```
    `OFFSET = (pàgina − 1) × per pàgina`. La pàgina es valida amb el rang de pàgines que existixen.

## Desplegament

### 7. Permisos

Has copiat una aplicació en `/var/www/app`. Té una carpeta `pujades/` on els usuaris pengen imatges. Quins propietaris i permisos poses? Com evites que s'execute PHP en `pujades/`?

??? success "Solució"
    ```bash
    sudo chown -R root:www-data /var/www/app
    sudo find /var/www/app -type d -exec chmod 750 {} +
    sudo find /var/www/app -type f -exec chmod 640 {} +
    sudo chown www-data:www-data /var/www/app/pujades
    sudo chmod 750 /var/www/app/pujades
    ```
    En Apache:
    ```text
    <Directory /var/www/app/pujades>
        php_admin_flag engine off
        <FilesMatch "\.php$">
            Require all denied
        </FilesMatch>
    </Directory>
    ```
    En Nginx: `location ^~ /pujades/ { location ~ \.php$ { deny all; } }`.

### 8. Per què falla?

Després de desplegar, la web dona error 500. En `error.log` hi ha: `PHP Fatal error: Uncaught PDOException: could not find driver`. Però `php -m` en el terminal mostra `pdo_pgsql`. Què passa?

??? success "Solució"
    El PHP del terminal (CLI) i el d'Apache (o PHP-FPM) tenen **configuracions separades** (`/etc/php/8.3/cli/` contra `/etc/php/8.3/apache2/` o `fpm/`), i potser fins i tot versions diferents. Cal que l'extensió estiga en la del servidor web: `sudo apt install php8.3-pgsql` (la mateixa versió que usa Apache) i **reiniciar** Apache o PHP-FPM. Per a veure les extensions del servidor web: una pàgina amb `phpinfo()` (i esborrar-la després).

!!! success "Per a l'examen"
    Les tres regles de seguretat: **valida** en el servidor, **escapa** en mostrar (`htmlspecialchars`), **prepara** les consultes (PDO). I les contrasenyes amb `password_hash`.
