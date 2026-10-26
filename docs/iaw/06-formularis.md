# UT2 · 3. Formularios: recibir, validar y conservar datos

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Validación** | Comprobación de que los datos cumplen la estructura y las reglas del problema. |
| **XSS** | Interpretación de contenido no fiable como código o marcado ejecutable en una página; exige una salida adecuada a cada contexto. |
| **Inyección SQL** | Alteración de una consulta al mezclar datos con instrucciones SQL; se previene separando consulta y parámetros. |
| **POST–Redirect–GET** | Procesar el envío, redirigir y mostrar el resultado mediante una nueva consulta GET. |

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

## Tabla de consulta: controles y datos que recibe PHP

| Control | Lo que llega al servidor |
| --- | --- |
| `input name="titulo"` | Un campo `titulo` si se envía el control |
| `textarea name="nota"` | Texto, incluidos posibles saltos de línea |
| Checkbox sin marcar | Normalmente no envía ese campo |
| Varios campos `name="colores[]"` | Un array en `$_POST['colores']` |
| Archivo adjunto | Información en `$_FILES`, no el contenido en `$_POST` |

Valida también la estructura: si esperas texto, comprueba `is_string`; si esperas una colección, comprueba `is_array` y después cada valor permitido.

## XSS: validar no sustituye escapar

```php
<?php
$nota = '<b>Revisar vitrina</b>';
echo htmlspecialchars($nota, ENT_QUOTES, 'UTF-8');
```

La respuesta contiene `&lt;b&gt;Revisar vitrina&lt;/b&gt;`; el navegador muestra las etiquetas como texto. Así no interpretas la nota como marcado HTML. Este escape sirve para texto en HTML y atributos entrecomillados; otros contextos, como JavaScript o una URL, requieren su tratamiento correspondiente.

Guarda el dato con su significado original y escápalo al presentarlo. Escapar al guardar y volver a escapar al mostrar puede producir entidades duplicadas. La inyección SQL es un problema distinto: se evita separando parámetros de la consulta mediante consultas preparadas cuando trabajes con bases de datos.

## Adjuntos: entender el recorrido antes de implementarlos

Un formulario con archivos necesita `enctype="multipart/form-data"`. PHP deja un temporal y describe nombre, tamaño, ruta temporal y error en `$_FILES`. Comprueba primero `UPLOAD_ERR_OK`, después los límites y el tipo real; `accept` en HTML solo ayuda a elegir, no valida en el servidor.

La carpeta de destino y la política de ejecución son parte del diseño: un archivo recibido no debe convertirse accidentalmente en código ejecutable. El nombre del usuario no es un destino fiable. En este tema se explica el mecanismo; el laboratorio del telescopio no necesita adjuntos.

!!! success "Para repasar"
    Antes de calcular nada, define qué entradas son válidas. Prepara un caso correcto, un límite y un caso incorrecto.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
