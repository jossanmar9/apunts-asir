# UT2 · 2. Decisiones, bucles, arrays y funciones

## Elige la estructura según el problema

Utiliza `if/elseif/else` cuando importen condiciones o intervalos; `switch` cuando compares opciones concretas. Un `for` sirve para una repetición con contador; `while`, para repetir mientras se cumple una condición; `foreach`, para recorrer los elementos de un array.

No escribas un bucle por costumbre. Pregúntate qué cambia en cada vuelta, cuándo termina y qué resultado debes acumular.

## Pensar una decisión antes de elegir la sintaxis

Un condicional responde a una pregunta. Antes de escribir `if`, exprésala con palabras: «si no quedan paquetes, termina» o «si la opción es audio, muestra escuchar». Después elige qué dato debe compararse y qué valores produce cada camino.

`if` sirve para una pregunta. `elseif` permite comprobar otra cuando la anterior fue falsa. `else` recoge los casos restantes. No se ejecutan todas las ramas de una cadena, sino la primera que corresponde. Si necesitas ejecutar varias comprobaciones independientes, utiliza varios `if` y explica por qué no se excluyen entre sí.

`switch` puede resultar más cómodo al comparar una misma opción con varios valores concretos. Cada `break` evita continuar dentro del siguiente caso. No lo introduzcas solo para hacer más corto el programa: primero debe estar claro qué caso representa cada valor.

## Un array reúne datos que vas a tratar de la misma manera

En lugar de crear `$sala1`, `$sala2` y `$sala3`, puedes reunir los nombres en un array y recorrerlo. En un array indexado accedes por posición; en uno asociativo, por una clave que expresa el significado del dato.

```php
<?php
$salas = ['Azul', 'Gris'];
$aforo = ['Azul' => 18, 'Gris' => 12];
foreach ($salas as $sala) {
    echo $sala . ': ' . $aforo[$sala] . " plazas\n";
}
```

La salida muestra `Azul: 18 plazas` y `Gris: 12 plazas`. La variable `$sala` toma un nombre en cada vuelta. Ese nombre permite consultar su cantidad en el segundo array. Este ejemplo presupone que ambas colecciones contienen las claves correspondientes; si los datos fueran externos habría que comprobarlo.

## Qué se repite en un bucle

Un bucle ejecuta un bloque varias veces. La parte que cambia puede ser el elemento que recorres, un contador o una cantidad pendiente. Lo que debe conservarse entre vueltas se inicializa antes; lo que representa un cálculo nuevo se obtiene dentro.

En el ejemplo de cajas, el total debe empezar en cero antes de `foreach`, porque reúne resultados de todos los lotes. El número de cajas del lote se calcula dentro, porque cambia con la cantidad de cada lote. Si inicializas ambos en el mismo lugar por costumbre, uno de ellos perderá su propósito.

Para depurar, escribe una fila por vuelta: valor actual, condición, resultado y acumulador. Esa tabla te permite comprobar el bucle sin ejecutarlo mentalmente de golpe.

## Crear una función significa poner nombre a una tarea

Una función tiene entradas, un trabajo y, si corresponde, una salida. Los parámetros son nombres que recibirán valores en cada llamada. `return` entrega el resultado y termina esa ejecución de la función; no imprime una respuesta para el usuario.

```php
<?php
function plazasLibres(int $capacidad, int $ocupadas): int
{
    return $capacidad - $ocupadas;
}
$primeraSala = plazasLibres(18, 11);
$segundaSala = plazasLibres(12, 4);
echo $primeraSala . ' / ' . $segundaSala . "\n";
```

La salida es `7 / 8`. No se ejecuta la resta al definir la función, sino en cada llamada. La primera utiliza 18 y 11; la segunda utiliza 12 y 4. Los nombres internos no obligan a que las variables del programa que llama tengan esos mismos nombres.

Esta separación facilita probar: puedes llamar a la función con cantidades pequeñas y saber qué esperas. Si dentro leyera directamente un formulario, necesitarías preparar además una petición HTTP para comprobar la misma resta.

## Evitar funciones que hacen demasiadas cosas

Una función que lee un formulario, valida, calcula, escribe HTML y redirige es difícil de reutilizar. Empieza por una separación sencilla: el receptor obtiene y valida; la función calcula; el HTML presenta. No hace falta convertir cada línea en otra función.

Utiliza nombres que expliquen el propósito. `plazasLibres` dice más que `hacerCosas`. Una función que devuelve una cantidad debería entregar esa cantidad, no una frase ya decorada que después tengas que volver a interpretar.

## Problema explicado paso a paso: preparar cajas de libros

Hay tres lotes de libros. Cada caja admite seis ejemplares. Queremos mostrar cuántas cajas necesita cada lote y el total de cajas; los lotes no se mezclan.

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
echo $mensaje . "\n"; // Hay que continuar

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

Ejecutado en el terminal, este bloque muestra primero `Hay que continuar` y después `Escuchar`, en líneas separadas.

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

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Muestra solo tareas pendientes

Crea el array `['pendiente', 'terminada', 'pendiente']`. Recórrelo y muestra únicamente los elementos iguales a `pendiente`. Deben aparecer dos líneas, sin escribir dos `echo` repetidos.

??? tip "Pista"
    Combina `foreach` con una comparación estricta dentro del recorrido.

??? success "Solución paso a paso"
    ```php
    <?php
    $tareas = ['pendiente', 'terminada', 'pendiente'];
    foreach ($tareas as $estado) {
        if ($estado === 'pendiente') {
            echo $estado . "\n";
        }
    }
    ```

    En cada vuelta se comprueba un estado. La segunda no imprime nada porque no cumple la condición. Las otras dos muestran `pendiente`.

### 2. Una función que responde una pregunta

Escribe `necesitaRevision($paginas)` para devolver `true` si la cantidad es mayor de 20 y `false` en otro caso. Supón enteros no negativos. Prueba con 20 y 21. La función no debe imprimir.

??? tip "Pista"
    Una comparación ya produce el booleano que necesitas devolver.

??? success "Solución paso a paso"
    ```php
    <?php
    function necesitaRevision(int $paginas): bool
    {
        return $paginas > 20;
    }
    var_dump(necesitaRevision(20));
    var_dump(necesitaRevision(21));
    ```

    Las salidas son `bool(false)` y `bool(true)`. El límite 20 no cumple «mayor de 20». `return` entrega el dato; las llamadas a `var_dump` permiten comprobarlo fuera de la función.

### 3. Suma solo las cantidades positivas

Con `[-2, 4, 0, 3]`, calcula mediante un bucle el total de las cantidades estrictamente positivas. No modifiques el array ni sumes los valores negativos.

??? tip "Pista"
    Inicializa el acumulador antes del bucle y actualízalo solo en el camino correcto.

??? success "Solución paso a paso"
    ```php
    <?php
    $cantidades = [-2, 4, 0, 3];
    $total = 0;
    foreach ($cantidades as $cantidad) {
        if ($cantidad > 0) {
            $total += $cantidad;
        }
    }
    echo $total . "\n";
    ```

    El total avanza de 0 a 4 y después a 7. El cero y -2 no lo cambian. El acumulador se prepara una vez, no en cada vuelta.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Condición y condicional** | Expresión que se evalúa y estructura que decide qué bloque ejecutar. |
| **Bucle e iteración** | Estructura que repite y cada una de sus vueltas. |
| **Función y llamada** | Bloque reutilizable con nombre y acción de ejecutarlo con unos argumentos. |
| **Retorno y variable local** | Resultado entregado a quien llama y dato cuyo ámbito está dentro de la función. |
| **Array indexado y asociativo** | Colección consultada por posición o por claves con significado. |

!!! success "Para repasar"
    Haz una tabla de seguimiento: entrada de cada vuelta, cálculo y acumulador. Si puedes explicarla, entiendes el bucle.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
