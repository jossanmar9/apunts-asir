# UT2 · 2. Decisiones, bucles, arrays y funciones

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Condición y condicional** | Expresión que se evalúa y estructura que decide qué bloque ejecutar. |
| **Bucle e iteración** | Estructura que repite y cada una de sus vueltas. |
| **Función y llamada** | Bloque reutilizable con nombre y acción de ejecutarlo con unos argumentos. |
| **Retorno y variable local** | Resultado entregado a quien llama y dato cuyo ámbito está dentro de la función. |
| **Array indexado y asociativo** | Colección consultada por posición o por claves con significado. |

## Elige la estructura según el problema

Utiliza `if/elseif/else` cuando importen condiciones o intervalos; `switch` cuando compares opciones concretas. Un `for` sirve para una repetición con contador; `while`, para repetir mientras se cumple una condición; `foreach`, para recorrer los elementos de un array.

No escribas un bucle por costumbre. Pregúntate qué cambia en cada vuelta, cuándo termina y qué resultado debes acumular.

## Ejemplo resuelto: preparar cajas de libros

**Problema propio:** hay tres lotes de libros. Cada caja admite seis ejemplares. Queremos mostrar cuántas cajas necesita cada lote y el total de cajas; los lotes no se mezclan.

```php
<?php
function cajasNecesarias(int $libros, int $capacidad): int
{
    return (int) ceil($libros / $capacidad);
}

$lotes = ['Poesía' => 13, 'Teatro' => 6, 'Ensayo' => 2];
$total = 0;
foreach ($lotes as $categoria => $cantidad) {
    $cajas = cajasNecesarias($cantidad, 6);
    $total += $cajas;
    echo htmlspecialchars($categoria, ENT_QUOTES, 'UTF-8')
        . ': ' . $cajas . " cajas\n";
}
echo 'Total: ' . $total . " cajas\n";
```

Puedes ejecutarlo como script con `php lotes.php`. En una página HTML, utiliza `<pre>` o elementos HTML para ver los saltos de línea.

### Sigue los valores

| Vuelta | Libros | División | Redondeo hacia arriba | Total acumulado |
| --- | --- | --- | --- | --- |
| Poesía | 13 | 13 / 6 ≈ 2,17 | 3 | 3 |
| Teatro | 6 | 6 / 6 = 1 | 1 | 4 |
| Ensayo | 2 | 2 / 6 ≈ 0,33 | 1 | 5 |

`ceil` redondea hacia arriba: una caja medio llena sigue siendo una caja. El casting `(int)` convierte el resultado a entero. `return` devuelve el valor a la llamada; no lo imprime. La función presupone cantidades no negativas y una capacidad positiva: valida esas condiciones si pasan a ser datos introducidos por el usuario.

## Decisiones con ejemplos pequeños

```php
<?php
$pendiente = 4;
if ($pendiente === 0) {
    $mensaje = 'Preparación terminada';
} elseif ($pendiente <= 3) {
    $mensaje = 'Queda poco';
} else {
    $mensaje = 'Hay que continuar';
}
echo $mensaje; // Hay que continuar

$formato = 'audio';
switch ($formato) {
    case 'audio':
        echo 'Escuchar';
        break;
    case 'papel':
        echo 'Leer';
        break;
    default:
        echo 'Formato desconocido';
}
```

`break` evita continuar con el siguiente caso. El `switch` tradicional hace comparaciones flexibles; con entradas mixtas conviene validar el tipo o utilizar comparaciones estrictas con `if`.

## Repetir con contador o condición

```php
<?php
for ($turno = 1; $turno <= 3; $turno++) {
    echo "Turno $turno\n";
}
$paquetes = 2;
while ($paquetes > 0) {
    echo "Quedan $paquetes\n";
    $paquetes--;
}
```

El `for` muestra los turnos 1, 2 y 3. El `while` muestra 2 y 1, y termina cuando el contador llega a cero. Si olvidas decrementarlo, nunca llega a la condición de parada.

## Reutilizar sin perder el hilo

Una función recibe parámetros, calcula y devuelve un resultado. Las variables locales no son automáticamente las del programa principal. Para separar archivos, `require_once __DIR__ . '/funciones.php';` carga un archivo necesario una vez; `include` genera un aviso si no puede cargarlo y puede continuar. Utiliza rutas propias del proyecto, no una ruta recibida directamente del usuario.

| Error | Cómo detectarlo |
| --- | --- |
| Reiniciar `$total` dentro del bucle | Solo queda el resultado de la última vuelta. Inicializa antes. |
| `echo` en lugar de `return` | La pantalla muestra algo, pero la llamada no recibe el valor calculado. |
| Condición que no cambia | El bucle no termina. Anota la variable que avanza. |

## Recorrer claves y valores sin perder la relación

`foreach ($datos as $clave => $valor)` conserva la asociación. Es útil para generar una lista de cantidades o un resumen de formulario. En un array indexado la clave suele ser una posición; en uno asociativo expresa el significado del dato.

Una función con parámetros explícitos es más fácil de probar que otra que lee directamente `$_POST`. Por ejemplo, `cajasNecesarias(13, 6)` puede probarse sin navegador. El receptor del formulario debe leer y validar; la función debe recibir los datos ya preparados para su tarea.

## Parámetros opcionales y responsabilidad local

```php
<?php
function etiqueta(string $nombre, string $prefijo = 'Sala'): string
{
    return $prefijo . ': ' . $nombre;
}
echo etiqueta('Azul') . "\n";
echo etiqueta('Azul', 'Zona') . "\n";
```

Resultado esperado: `Sala: Azul` y `Zona: Azul`. El segundo parámetro tiene un valor predeterminado, pero puede sustituirse. `$nombre` y `$prefijo` son locales a la llamada; `return` entrega el texto a quien la llamó.

Para archivos que solo contienen funciones PHP, suele ser práctico omitir la etiqueta de cierre `?>`: reduces el riesgo de introducir espacios que se envíen accidentalmente antes de una cabecera HTTP.

!!! success "Para repasar"
    Haz una tabla de seguimiento: entrada de cada vuelta, cálculo y acumulador. Si puedes explicarla, entiendes el bucle.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
