# UT2 · 3. Formularis: rebre, validar i conservar dades

## El recorregut complet

HTML presenta els controls; el navegador envia els que tenen `name`; PHP rep els valors en `$_GET` o `$_POST`. El servidor ha de validar-los encara que el formulari use `required`, `min` o un desplegable: una petició es pot enviar sense usar eixa interfície.

L'ordre que ajuda a pensar és **llegir → validar → calcular → mostrar**. Escapar amb `htmlspecialchars` és necessari quan insereixes text en HTML, però no comprova que el contingut siga admissible per al problema.

## Exemple resolt: sol·licitar temps d'un telescopi

**Problema nou:** demanar un torn d'observació de 5 a 40 minuts. S'ha de triar telescopi i acceptar la norma de deixar-lo recollit. El formulari conserva les dades si hi ha un error. No calcula pressupostos ni resol la pràctica de contractació de classe.

Desa aquest fitxer com a `torn.php` en el servidor PHP:

```php
<?php
function h(string $text): string {
    return htmlspecialchars($text, ENT_QUOTES, 'UTF-8');
}
function camp(string $nom): string {
    $valor = $_POST[$nom] ?? '';
    return is_string($valor) ? trim($valor) : '';
}
$errors = [];
$equip = '';
$minutsText = '';
$acceptat = false;
$enviat = $_SERVER['REQUEST_METHOD'] === 'POST';
if ($enviat) {
    $equip = camp('equip');
    $minutsText = camp('minuts');
    $acceptat = camp('recollir') === 'si';
    $minuts = filter_var($minutsText, FILTER_VALIDATE_INT);
    if (!in_array($equip, ['refractor', 'reflector'], true)) {
        $errors[] = 'Tria un dels dos telescopis.';
    }
    if ($minuts === false || $minuts < 5 || $minuts > 40) {
        $errors[] = 'La duració ha de ser un enter de 5 a 40.';
    }
    if (!$acceptat) {
        $errors[] = 'Cal acceptar deixar el material recollit.';
    }
}
?>
<!doctype html>
<html lang="ca">
<meta charset="utf-8">
<title>Torn del telescopi</title>
<h1>Torn d'observació</h1>
<?php foreach ($errors as $error): ?>
<p><?= h($error) ?></p>
<?php endforeach; ?>
<form action="torn.php" method="post">
    <label>Telescopi
        <select name="equip">
            <option value="">Tria'n un</option>
            <option value="refractor" <?= $equip === 'refractor' ? 'selected' : '' ?>>Refractor</option>
            <option value="reflector" <?= $equip === 'reflector' ? 'selected' : '' ?>>Reflector</option>
        </select>
    </label>
    <label>Minuts
        <input name="minuts" type="number" min="5" max="40"
               required value="<?= h($minutsText) ?>">
    </label>
    <label>
        <input type="checkbox" name="recollir" value="si"
               <?= $acceptat ? 'checked' : '' ?>>Deixaré el material recollit
    </label>
    <button>Comprovar torn</button>
</form>
<?php if ($enviat && !$errors): ?>
<p>Sol·licitud vàlida: <?= h($equip) ?> durant <?= $minuts ?> minuts.</p>
<?php endif; ?>
</html>
```

## Per què està escrit així?

1. En GET es mostren camps buits i cap error: encara no s'ha enviat res.
2. En POST, `camp()` proporciona text o una cadena buida. També rebutja un array inesperat, perquè les dades HTTP no són fiables.
3. L'array de valors permesos impedeix inventar un altre telescopi modificant la petició.
4. `FILTER_VALIDATE_INT` retorna `false` si no pot validar l'enter. No uses `if (!$minuts)` com a substitut general: confon zero amb fallada.
5. Un checkbox desmarcat no envia el camp. Ací es comprova el valor admés; `isset($_POST['recollir'])` serviria per a comprovar-ne només la presència.
6. La mateixa variable ompli el formulari i el missatge: no es perden les dades quan falla una altra condició.

## Comprova els casos, no només el camí correcte

| Entrada | Resultat esperat |
| --- | --- |
| Refractor, 15, acceptat | Sol·licitud vàlida durant 15 minuts |
| Reflector, 4, acceptat | Error de duració |
| Sense telescopi, 20, sense marcar | Dos errors; es conserva 20 |
| Minuts `molts` en una petició manual | Error de duració |

Aquesta demostració valida una sol·licitud; no comprova disponibilitat real ni la guarda. Si el formulari té correu, usa `filter_var($correu, FILTER_VALIDATE_EMAIL)` per a validar-ne el format. Si més endavant modifica estat d'un usuari autenticat, afegeix protecció CSRF.

| Símptoma | Revisió |
| --- | --- |
| `$_POST` buit | `method`, atributs `name` i fitxer `action`. |
| Resultat abans d'enviar | Falta distingir GET i POST. |
| Valors es perden | No els tornes a escriure en `value`, `selected` o `checked`. |

!!! success "Per a repassar"
    Abans de calcular res, defineix quines entrades són vàlides. Prepara un cas correcte, un límit i un cas incorrecte.

---

Font del temari: [apunts originals de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
