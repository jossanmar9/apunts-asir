# UT2 · 3. Formularios: recibir, validar y conservar datos

## El recorrido completo

HTML presenta los controles; el navegador envía los que tienen `name`; PHP recibe los valores en `$_GET` o `$_POST`. El servidor debe validarlos aunque el formulario utilice `required`, `min` o un desplegable: una petición se puede enviar sin utilizar esa interfaz.

El orden que ayuda a pensar es **leer → validar → calcular → mostrar**. Escapar con `htmlspecialchars` es necesario al insertar texto en HTML, pero no comprueba que el contenido sea admisible para el problema.

## Del control HTML a una variable PHP

Un formulario relaciona una interfaz con un receptor. `action` indica el destino y `method` el modo de envío. Cada control necesita un atributo `name` para identificar su dato; el texto de una etiqueta visible no sustituye a ese nombre.

Imagina un control `<input name="minutos">`. Cuando envías 15, el servidor recibe un campo llamado `minutos`. En un formulario POST, PHP lo sitúa en `$_POST['minutos']`. No lo buscará automáticamente en una variable `$minutos`: debes leerlo y decidir qué hacer con él.

`id` sirve para relaciones de la interfaz, como conectar un `<label>` con el control. `name` sirve para el envío. Puedes utilizar el mismo texto en ambos, pero cumplen funciones diferentes. Confundirlos hace que una entrada se vea bien y aun así no llegue con el nombre que espera el programa.

## La primera visita no es un envío vacío

Al abrir la página por su URL, normalmente haces GET. Todavía no has solicitado comprobar ninguna entrada. Si intentas validar todos los campos en ese momento, mostrarás errores antes de que el usuario haya tenido oportunidad de escribir.

Por eso el ejemplo distingue el método: primero inicializa valores para presentar el formulario y solo procesa cuando recibe POST. Después del envío puede representar errores o un resultado, conservando los datos cuando sea necesario.

No deduzcas que hay un envío solo porque exista alguna variable. Comprobar `REQUEST_METHOD` expresa la intención y permite entender el flujo de la página. Los campos individuales se comprueban después, porque pueden faltar aunque el método sea POST.

## Leer, limpiar, validar y escapar son pasos diferentes

Leer obtiene lo recibido. Limpiar puede quitar espacios de los extremos con `trim`. Validar comprueba reglas como «es un entero entre 5 y 40». Escapar prepara texto para representarlo en un contexto de salida, como HTML.

Si alguien envía ` 15 `, puede tener sentido quitar esos espacios antes de validar. Si envía `quince`, quitar espacios no lo convierte en el número 15. Si envía `<b>15</b>`, escapar permite mostrar ese texto, pero no lo convierte en una duración válida.

No uses una única operación para sustituir las otras. Este orden te permite explicar por qué un dato se acepta o se rechaza y evita que una presentación segura oculte una validación incompleta.

## Por qué se utiliza una lista de errores

El formulario puede tener más de un problema. Un array de errores permite comprobar cada campo y añadir un mensaje para cada incumplimiento. Solo cuando la lista está vacía continúas con el cálculo o la operación.

Los mensajes deben indicar qué corregir. «Duración fuera de rango: utiliza de 5 a 40 minutos» resulta más útil que «dato malo». Si hay dos errores, presentarlos juntos evita obligar al usuario a corregir uno y reenviar para descubrir el siguiente.

El ejemplo conserva las entradas aceptadas como texto para volver a rellenar los controles. Al escribirlas en `value`, se escapan. Para un desplegable se marca la opción con `selected`; para una casilla se utiliza `checked`. No son atributos que PHP añada automáticamente por haber leído el dato.

## Cómo leer el problema del telescopio

Primero sigue una visita GET: mira los valores iniciales y comprueba que todavía no hay un resultado. Después sigue un POST válido y anota qué devuelve cada llamada a `campo`. Finalmente, sigue un POST incorrecto y observa qué mensajes se acumulan.

No intentes entender todo el archivo como una sola operación. Separa su parte de procesamiento y su parte de presentación. Busca después dónde se conectan: las variables que prepara la primera aparecen en los controles y en los mensajes que construye la segunda.

Esta lectura sirve durante el examen y mientras haces otro formulario: identificas el mismo recorrido y adaptas sus reglas, en lugar de copiar campos que no pertenecen a tu enunciado.

## Problema explicado paso a paso: solicitar tiempo de un telescopio

Solicitar un turno de observación de 5 a 40 minutos. Hay que elegir telescopio y aceptar la norma de dejarlo recogido. El formulario conserva los datos si hay un error. No calcula presupuestos ni resuelve la práctica de contratación de clase.

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

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Encuentra por qué no llega el campo

El formulario usa `<input id="asunto">` y `method="post"`. PHP espera `$_POST['asunto']`. Explica qué falta y escribe el control corregido. Después indica cómo comprobarías el envío en el navegador.

??? tip "Pista"
    El nombre utilizado para enviar un campo no es su `id`.

??? success "Solución paso a paso"
    El control necesita `name`:

    ```html
    <input id="asunto" name="asunto">
    ```

    1. `id` identifica el elemento en la página.
    2. `name="asunto"` identifica el campo enviado.
    3. En Red del navegador, abriría la petición POST y buscaría `asunto` en sus datos.

### 2. Valida una opción de formato

En un receptor PHP debes aceptar solo `pdf` o `texto` en `$_POST['formato']`. Escribe la comprobación y un mensaje para cualquier otra entrada. Rechaza también un array inesperado. El código se ejecuta cuando ya has recibido un POST.

??? tip "Pista"
    Comprueba primero la estructura y después la lista de valores permitidos.

??? success "Solución paso a paso"
    ```php
    <?php
    $formato = $_POST['formato'] ?? '';
    if (!is_string($formato) || !in_array($formato, ['pdf', 'texto'], true)) {
        echo 'Elige pdf o texto';
    } else {
        echo 'Formato aceptado';
    }
    ```

    1. Un campo ausente toma `''` y se rechaza.
    2. `is_string` impide tratar un array como una opción de texto.
    3. `in_array` limita la respuesta a los dos valores admitidos. Prueba `pdf`, `imagen`, campo ausente y array.

### 3. Conserva una nota después de un error

Ya tienes en `$nota` el texto leído y validado como cadena. Escribe un `textarea` que conserve ese texto al volver a mostrar el formulario. Explica por qué no va en un atributo `value` y cómo evitas interpretarlo como HTML.

??? tip "Pista"
    El contenido de un textarea se coloca entre sus etiquetas.

??? success "Solución paso a paso"
    ```php
    <textarea name="nota"><?= htmlspecialchars($nota, ENT_QUOTES, 'UTF-8') ?></textarea>
    ```

    1. La cadena se coloca entre apertura y cierre de `textarea`.
    2. `name` permite enviarla de nuevo.
    3. El escape impide que el texto recibido cierre o altere el marcado de la página. Un `textarea` no se rellena como un `input value="..."`.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Validación** | Comprobación de que los datos cumplen la estructura y las reglas del problema. |
| **XSS** | Interpretación de contenido no fiable como código o marcado ejecutable en una página; exige una salida adecuada a cada contexto. |
| **Inyección SQL** | Alteración de una consulta al mezclar datos con instrucciones SQL; se previene separando consulta y parámetros. |
| **POST–Redirect–GET** | Procesar el envío, redirigir y mostrar el resultado mediante una nueva consulta GET. |

!!! success "Para repasar"
    Antes de calcular nada, define qué entradas son válidas. Prepara un caso correcto, un límite y un caso incorrecto.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
