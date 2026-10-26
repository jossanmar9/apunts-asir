# UT2 · 3. Formularios: recibir, validar y conservar datos

## El recorrido completo

HTML presenta los controles; el navegador envía los que tienen `name`; PHP recibe los valores en `$_GET` o `$_POST`. El servidor debe validarlos aunque el formulario utilice `required`, `min` o un desplegable: una petición se puede enviar sin utilizar esa interfaz.

El orden que ayuda a pensar es **leer → validar → calcular → mostrar**. Escapar con `htmlspecialchars` es necesario al insertar texto en HTML, pero no comprueba que el contenido sea admisible para el problema.

## Ejemplo resuelto: solicitar tiempo de un telescopio

**Problema propio:** solicitar un turno de observación de 5 a 40 minutos. Hay que elegir telescopio y aceptar la norma de dejarlo recogido. El formulario conserva los datos si hay un error. No calcula presupuestos ni resuelve la práctica de contratación de clase.

Guarda este archivo como `turno.php` en el servidor PHP:

```php
<?php
function h(string $texto): string {
    return htmlspecialchars($texto, ENT_QUOTES, 'UTF-8');
}
function campo(string $nombre): string {
    $valor = $_POST[$nombre] ?? '';
    return is_string($valor) ? trim($valor) : '';
}
$errores = [];
$equipo = '';
$minutosTexto = '';
$aceptado = false;
$enviado = $_SERVER['REQUEST_METHOD'] === 'POST';
if ($enviado) {
    $equipo = campo('equipo');
    $minutosTexto = campo('minutos');
    $aceptado = campo('recoger') === 'si';
    $minutos = filter_var($minutosTexto, FILTER_VALIDATE_INT);
    if (!in_array($equipo, ['refractor', 'reflector'], true)) {
        $errores[] = 'Elige uno de los dos telescopios.';
    }
    if ($minutos === false || $minutos < 5 || $minutos > 40) {
        $errores[] = 'La duración debe ser un entero de 5 a 40.';
    }
    if (!$aceptado) {
        $errores[] = 'Debes aceptar dejar el material recogido.';
    }
}
?>
<!doctype html>
<html lang="es">
<meta charset="utf-8">
<title>Turno del telescopio</title>
<h1>Turno de observación</h1>
<?php foreach ($errores as $error): ?>
<p><?= h($error) ?></p>
<?php endforeach; ?>
<form action="turno.php" method="post">
    <label>Telescopio
        <select name="equipo">
            <option value="">Elige uno</option>
            <option value="refractor" <?= $equipo === 'refractor' ? 'selected' : '' ?>>Refractor</option>
            <option value="reflector" <?= $equipo === 'reflector' ? 'selected' : '' ?>>Reflector</option>
        </select>
    </label>
    <label>Minutos
        <input name="minutos" type="number" min="5" max="40"
               required value="<?= h($minutosTexto) ?>">
    </label>
    <label>
        <input type="checkbox" name="recoger" value="si"
               <?= $aceptado ? 'checked' : '' ?>>Dejaré el material recogido
    </label>
    <button>Comprobar turno</button>
</form>
<?php if ($enviado && !$errores): ?>
<p>Solicitud válida: <?= h($equipo) ?> durante <?= $minutos ?> minutos.</p>
<?php endif; ?>
</html>
```

## ¿Por qué está escrito así?

1. En GET se muestran campos vacíos y ningún error: todavía no se ha enviado nada.
2. En POST, `campo()` proporciona texto o una cadena vacía. También rechaza un array inesperado, porque los datos HTTP no son fiables.
3. El array de valores permitidos impide inventar otro telescopio modificando la petición.
4. `FILTER_VALIDATE_INT` devuelve `false` si no puede validar el entero. No uses `if (!$minutos)` como sustituto general: confunde cero con fallo.
5. Un checkbox desmarcado no envía el campo. Aquí se comprueba el valor admitido; `isset($_POST['recoger'])` serviría para comprobar solo su presencia.
6. La misma variable rellena el formulario y el mensaje: los datos no se pierden cuando falla otra condición.

## Comprueba los casos, no solo el camino correcto

| Entrada | Resultado esperado |
| --- | --- |
| Refractor, 15, aceptado | Solicitud válida durante 15 minutos |
| Reflector, 4, aceptado | Error de duración |
| Sin telescopio, 20, sin marcar | Dos errores; se conserva 20 |
| Minutos `muchos` en una petición manual | Error de duración |

Esta demostración valida una solicitud; no comprueba disponibilidad real ni la guarda. Si el formulario tiene correo, utiliza `filter_var($correo, FILTER_VALIDATE_EMAIL)` para validar su formato. Si más adelante modifica el estado de un usuario autenticado, añade protección CSRF.

| Síntoma | Revisión |
| --- | --- |
| `$_POST` vacío | `method`, atributos `name` y archivo `action`. |
| Resultado antes de enviar | Falta distinguir GET y POST. |
| Los valores se pierden | No los vuelves a escribir en `value`, `selected` o `checked`. |

!!! success "Para repasar"
    Antes de calcular nada, define qué entradas son válidas. Prepara un caso correcto, un límite y un caso incorrecto.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
