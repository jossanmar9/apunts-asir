# UT2 · 2. Decisions, bucles, arrays i funcions

## Tria l'estructura segons el problema

Usa `if/elseif/else` quan importen condicions o intervals; `switch` quan compares opcions concretes. Un `for` serveix per a una repetició amb comptador; `while`, per a repetir mentre una condició es manté; `foreach`, per a recórrer els elements d'un array.

No escrigues un bucle per costum. Pregunta't què canvia en cada volta, quan s'atura i quin resultat has d'acumular.

## Exemple resolt: preparar caixes de llibres

**Problema nou:** hi ha tres lots de llibres. Cada caixa admet sis exemplars. Volem mostrar quantes caixes necessita cada lot i el total de caixes; els lots no es barregen.

```php
<?php
function caixesNecessaries(int $llibres, int $capacitat): int
{
    return (int) ceil($llibres / $capacitat);
}

$lots = ['Poesia' => 13, 'Teatre' => 6, 'Assaig' => 2];
$total = 0;
foreach ($lots as $categoria => $quantitat) {
    $caixes = caixesNecessaries($quantitat, 6);
    $total += $caixes;
    echo htmlspecialchars($categoria, ENT_QUOTES, 'UTF-8')
        . ': ' . $caixes . " caixes\n";
}
echo 'Total: ' . $total . " caixes\n";
```

Pots executar-lo com a script amb `php lots.php`. En una pàgina HTML, usa `<pre>` o elements HTML per a veure els salts de línia.

### Segueix els valors

| Volta | Llibres | Divisió | Arrodoniment cap amunt | Total acumulat |
| --- | --- | --- | --- | --- |
| Poesia | 13 | 13 / 6 ≈ 2,17 | 3 | 3 |
| Teatre | 6 | 6 / 6 = 1 | 1 | 4 |
| Assaig | 2 | 2 / 6 ≈ 0,33 | 1 | 5 |

`ceil` arrodoneix cap amunt: una caixa mig plena continua sent una caixa. El càsting `(int)` converteix el resultat a enter. `return` retorna el valor a la crida; no l'imprimeix. La funció pressuposa quantitats no negatives i una capacitat positiva: valida eixes condicions si passen a ser dades introduïdes per l'usuari.

## Decisions amb exemples menuts

```php
<?php
$pendent = 4;
if ($pendent === 0) {
    $missatge = 'Preparació acabada';
} elseif ($pendent <= 3) {
    $missatge = 'Queda poc';
} else {
    $missatge = 'Cal continuar';
}
echo $missatge; // Cal continuar

$format = 'audio';
switch ($format) {
    case 'audio':
        echo 'Escoltar';
        break;
    case 'paper':
        echo 'Llegir';
        break;
    default:
        echo 'Format desconegut';
}
```

`break` evita continuar amb el cas següent. El `switch` tradicional fa comparacions flexibles; amb entrades mixtes convé validar el tipus o usar comparacions estrictes amb `if`.

## Repetir amb comptador o condició

```php
<?php
for ($torn = 1; $torn <= 3; $torn++) {
    echo "Torn $torn\n";
}
$paquets = 2;
while ($paquets > 0) {
    echo "Queden $paquets\n";
    $paquets--;
}
```

El `for` mostra torns 1, 2 i 3. El `while` mostra 2 i 1, i para quan el comptador arriba a zero. Si oblides decrementar, no arriba mai a la condició de parada.

## Reutilitzar sense perdre el fil

Una funció rep paràmetres, calcula i retorna. Les variables locals no són automàticament les del programa principal. Per a separar fitxers, `require_once __DIR__ . '/funcions.php';` carrega un fitxer necessari una vegada; `include` genera un avís si no el pot carregar i pot continuar. Usa rutes pròpies del projecte, no una ruta rebuda directament de l'usuari.

| Error | Com detectar-lo |
| --- | --- |
| Reiniciar `$total` dins del bucle | Només queda el resultat de l'última volta. Inicialitza abans. |
| `echo` en lloc de `return` | La pantalla mostra alguna cosa, però la crida no rep el valor calculat. |
| Condició que no canvia | El bucle no acaba. Anota la variable que avança. |

!!! success "Per a repassar"
    Fes una taula de seguiment: entrada de cada volta, càlcul i acumulador. Si pots explicar-la, entens el bucle.

---

Font del temari: [apunts originals de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
