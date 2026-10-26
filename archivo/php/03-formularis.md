# 3. Formularis

Els formularis HTML (`<form>`, `<input>`, `<button>`) envien les dades al servidor. PHP les rep en dos arrays:

| Mètode del formulari | PHP les té en | Es veuen en la URL | Per a |
| -------------------- | ------------- | ------------------ | ----- |
| `method="get"` | **`$_GET`** | sí: `cerca.php?q=linux&pagina=2` | **cercar**, filtrar, paginar (es pot guardar com a marcador) |
| `method="post"` | **`$_POST`** | no (van en el cos de la petició) | **enviar dades**: altes, modificacions, *login*, fitxers |

La clau de cada dada és l'atribut **`name`** del camp: `<input name="correu">` → `$_POST["correu"]`.

## Un formulari que es processa a si mateix

El patró més comú: el mateix fitxer mostra el formulari i el processa.

```php title="contacte.php"
<?php
$errors = [];
$nom = $correu = $missatge = "";

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // 1. Llegir les dades (?? "" per si no arriben)
    $nom      = trim($_POST["nom"] ?? "");
    $correu   = trim($_POST["correu"] ?? "");
    $missatge = trim($_POST["missatge"] ?? "");

    // 2. Validar-les EN EL SERVIDOR
    if ($nom === "") {
        $errors[] = "El nom és obligatori.";
    }
    if (!filter_var($correu, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "El correu no és vàlid.";
    }
    if (mb_strlen($missatge) < 10) {
        $errors[] = "El missatge ha de tindre almenys 10 caràcters.";
    }

    // 3. Si tot està bé, fer la feina (guardar, enviar...) i acabar
    if (!$errors) {
        echo "<p>Gràcies, " . htmlspecialchars($nom) . ". Hem rebut el teu missatge.</p>";
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="ca">
<head><meta charset="UTF-8"><title>Contacte</title></head>
<body>
    <h1>Contacte</h1>

    <?php if ($errors): ?>
        <ul class="errors">
            <?php foreach ($errors as $e): ?>
                <li><?= htmlspecialchars($e) ?></li>
            <?php endforeach; ?>
        </ul>
    <?php endif; ?>

    <form method="post" action="">
        <label>Nom <input name="nom" value="<?= htmlspecialchars($nom) ?>"></label>
        <label>Correu <input type="email" name="correu" value="<?= htmlspecialchars($correu) ?>"></label>
        <label>Missatge <textarea name="missatge"><?= htmlspecialchars($missatge) ?></textarea></label>
        <button>Enviar</button>
    </form>
</body>
</html>
```

**Com funciona:**

1. La primera vegada s'entra amb **GET** (escrivint la URL): no s'executa el bloc del `POST` i es mostra el formulari buit.
2. En prémer *Enviar*, el navegador fa un **POST** al mateix fitxer.
3. Si hi ha errors, es tornen a mostrar **amb les dades que havia escrit** (el `value=`), per a no haver de tornar-ho a escriure tot.

**Provat amb `curl`** (les eixides són reals):

```console
$ curl -s -d "nom=&correu=noesvalid&missatge=hola" http://localhost:8000/contacte.php | grep -E "<li>|value="
    <li>El nom és obligatori.</li>
    <li>El correu no és vàlid.</li>
    <li>El missatge ha de tindre almenys 10 caràcters.</li>
    <label>Nom <input name="nom" value=""></label>
    <label>Correu <input type="email" name="correu" value="noesvalid"></label>
```

!!! danger "Valida sempre en el servidor"
    `required`, `type="email"` o `maxlength` en l'HTML ajuden l'usuari, però **no** protegixen: qualsevol pot enviar el que vulga amb `curl` o modificant la pàgina amb les eines del navegador. La validació de veritat és la de PHP.

### Validar

| Comprovació | Codi |
| ----------- | ---- |
| obligatori | `trim($x) === ""` |
| correu | `filter_var($x, FILTER_VALIDATE_EMAIL)` |
| enter (i en un rang) | `filter_var($x, FILTER_VALIDATE_INT, ["options" => ["min_range" => 1, "max_range" => 10]])` |
| decimal | `filter_var($x, FILTER_VALIDATE_FLOAT)` |
| URL | `filter_var($x, FILTER_VALIDATE_URL)` |
| llargària | `mb_strlen($x) <= 50` |
| patró | `preg_match('/^[0-9]{5}$/', $cp)` |
| d'una llista | `in_array($x, ["ASIR", "DAW", "SMX"], true)` |

`filter_input(INPUT_GET, "id", FILTER_VALIDATE_INT)` llig i valida alhora (torna `false` si no és vàlid, `null` si no hi és).

## XSS: no mostres mai les dades sense escapar ⭐

Si es mostra en la pàgina el que ha escrit l'usuari **tal qual**, pot escriure codi HTML o JavaScript i s'executarà en el navegador dels altres. És l'atac **XSS** (*Cross-Site Scripting*): robar galetes de sessió, redirigir a una web falsa...

```php
echo "Hola, " . $_GET["nom"];                      // ❌ si nom = <script>...</script>, s'executa
echo "Hola, " . htmlspecialchars($_GET["nom"]);    // ✅
```

`htmlspecialchars` canvia els caràcters especials per entitats:

| Caràcter | Es convertix en |
| -------- | --------------- |
| `<` | `&lt;` |
| `>` | `&gt;` |
| `"` | `&quot;` |
| `'` | `&#039;` (amb `ENT_QUOTES`, per defecte en PHP 8.1+) |
| `&` | `&amp;` |

```console
$ curl -s --data-urlencode "nom=<script>alert(1)</script>" \
       -d "correu=ana@exemple.com&missatge=Vull informació del cicle" http://localhost:8000/contacte.php
<p>Gràcies, &lt;script&gt;alert(1)&lt;/script&gt;. Hem rebut el teu missatge.</p>
```

El navegador **mostra** el text `<script>alert(1)</script>`, però no l'executa.

!!! tip "Una funció curta"
    ```php
    function e(?string $text): string {
        return htmlspecialchars($text ?? "", ENT_QUOTES, "UTF-8");
    }
    ```
    I escriure sempre `<?= e($variable) ?>`.

**Regla**: escapa en el moment de **mostrar** (amb `htmlspecialchars`), no en el moment de guardar. Per a la base de dades, la protecció és una altra: les [consultes preparades](05-pdo.md#injeccio-sql).

## Els camps especials

```php
// Caselles (checkbox): només s'envien si estan marcades
$accepta = isset($_POST["accepta"]);

// Diverses caselles amb el mateix nom: name="moduls[]"
$moduls = $_POST["moduls"] ?? [];          // un array

// Llista desplegable (select)
$cicle = $_POST["cicle"] ?? "";
if (!in_array($cicle, ["ASIR", "DAW", "SMX"], true)) { $errors[] = "Cicle no vàlid"; }
```

```html
<input type="checkbox" name="accepta" value="si"> Accepte les condicions
<input type="checkbox" name="moduls[]" value="ISO"> ISO
<input type="checkbox" name="moduls[]" value="PAR"> PAR
```

## Pujar fitxers

```html
<form method="post" enctype="multipart/form-data">
    <input type="file" name="foto" accept="image/png, image/jpeg">
    <button>Pujar</button>
</form>
```

```php
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_FILES["foto"])) {
    $f = $_FILES["foto"];
    $tipus = mime_content_type($f["tmp_name"]);            // el tipus REAL, no el que diu el navegador

    if ($f["error"] !== UPLOAD_ERR_OK) {
        $errors[] = "Error en pujar el fitxer.";
    } elseif (!in_array($tipus, ["image/png", "image/jpeg"], true)) {
        $errors[] = "Només imatges PNG o JPEG.";
    } elseif ($f["size"] > 2 * 1024 * 1024) {
        $errors[] = "Màxim 2 MB.";
    } else {
        $nom = bin2hex(random_bytes(8)) . ($tipus === "image/png" ? ".png" : ".jpg");   // nom nou: mai el de l'usuari
        move_uploaded_file($f["tmp_name"], __DIR__ . "/pujades/$nom");
    }
}
```

| `$_FILES["foto"][...]` | |
| ---------------------- | - |
| `name` | el nom original (no te'n fies) |
| `tmp_name` | on l'ha deixat PHP temporalment |
| `size` | mida en bytes |
| `error` | `0` (`UPLOAD_ERR_OK`) si tot ha anat bé |

!!! danger "Un fitxer pujat pot ser un programa"
    Si algú puja `virus.php` i la carpeta de pujades s'executa com a PHP, pot controlar el servidor. Comprova el **tipus real**, canvia-li el **nom**, i que la carpeta de pujades **no execute PHP** (o que estiga fora del `DocumentRoot`). Els límits de mida estan també en `php.ini`: `upload_max_filesize` i `post_max_size`.

## Redirigir després d'un POST (PRG)

Si després de guardar es mostra directament una pàgina, en recarregar-la el navegador **torna a enviar** el formulari (i es duplica l'alta). La solució és el patró **Post → Redirect → Get**:

```php
// ... guardar ...
header("Location: llista.php");     // redirigir
exit;                               // i acabar ⭐
```

!!! warning "`header()` abans de res"
    Les capçaleres s'han d'enviar **abans** de qualsevol eixida (un `echo`, HTML, o fins i tot un espai abans de `<?php`). Si no: `Cannot modify header information - headers already sent`.

## Errors típics

| Problema | Per què | Solució |
| -------- | ------- | ------- |
| `Undefined array key "nom"` | S'ha llegit `$_POST["nom"]` en entrar per GET, o el camp no té `name` | `$_POST["nom"] ?? ""`; comprova el `name` |
| No arriba cap dada | El camp no té atribut `name`, o el formulari usa GET i llegixes `$_POST` | `name=`; el mateix mètode |
| `Cannot modify header information - headers already sent` | Alguna eixida abans del `header()` (també un espai o una línia en blanc fora de `<?php`) | El `header()` al principi; sense res abans de `<?php` |
| En recarregar es duplica l'alta | Falta la redirecció després del POST | PRG: `header("Location: ...")` + `exit` |
| La caixa de text mostra `&amp;` duplicats | S'ha escapat dues vegades (en guardar i en mostrar) | Escapa només en mostrar |
| `$_FILES` buit | Falta `enctype="multipart/form-data"`, o el fitxer passa del límit de `php.ini` | Revisa el formulari i `upload_max_filesize` |

!!! success "Per a l'examen"
    ```php
    if ($_SERVER["REQUEST_METHOD"] === "POST") {
        $x = trim($_POST["x"] ?? "");
        if ($x === "") $errors[] = "...";
        if (!filter_var($correu, FILTER_VALIDATE_EMAIL)) $errors[] = "...";
        if (!$errors) { /* guardar */ header("Location: ok.php"); exit; }
    }
    <input name="x" value="<?= htmlspecialchars($x) ?>">
    ```
    - **GET** (URL, cercar) / **POST** (enviar dades) · `$_GET`, `$_POST`, `$_FILES` · la clau és el **`name`**
    - **Valida en el servidor** sempre · **`htmlspecialchars`** en mostrar (contra **XSS**)
    - Fitxers: `enctype="multipart/form-data"` · tipus real · nom nou · `move_uploaded_file`
    - **PRG**: després d'un POST, `header("Location: ...")` + `exit`
