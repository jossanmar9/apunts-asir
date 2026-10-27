# UT2 · 1. PHP, variables y generación de HTML

## Dónde se ejecuta cada cosa

PHP se ejecuta en el servidor. El resultado puede ser HTML, JSON o texto. El navegador no ejecuta el PHP original. Abrir un `.php` como archivo local no equivale a solicitarlo a un servidor PHP.

Para estos ejemplos puedes utilizar la carpeta `public` del laboratorio de UT1. Si tienes instalado el intérprete PHP, también puedes probar solo PHP con `php -S 127.0.0.1:8093 -t public`. Ese servidor es para desarrollo local y no reproduce el stack completo de Nginx y MariaDB.

## Las reglas básicas

Las variables comienzan por `$` y distinguen mayúsculas. `=` asigna; `===` compara valor y tipo. Las instrucciones suelen acabar en `;`. El punto `.` concatena texto y `echo` escribe en la respuesta. `<?= expresion ?>` equivale a imprimir esa expresión.

| Tipo | Ejemplo | Para qué sirve |
| --- | --- | --- |
| int | `24` | Recuento entero |
| float | `2.75` | Cantidad decimal |
| string | `'Sala violeta'` | Texto |
| bool | `true` | Una condición |
| array | `['A', 'B']` | Una colección |
| null | `null` | Ausencia de valor |

Las comillas dobles pueden interpolar variables; las simples conservan el texto literal. `//` y `/* ... */` son comentarios PHP. Un comentario HTML puede llegar al navegador; un comentario PHP no forma parte de la respuesta.

## Qué hace PHP antes de que el navegador reciba la página

Un archivo PHP puede contener instrucciones del servidor y texto que formará parte de la respuesta. Cuando llega una petición, el intérprete ejecuta las instrucciones y produce una salida. El navegador recibe esa salida, no el programa que la generó.

Esto permite que dos visitas al mismo archivo reciban contenidos distintos: el programa puede utilizar datos enviados, resultados de una consulta o el estado de una sesión. Para empezar, usamos valores fijados dentro del código y así podemos seguir el cálculo sin añadir todavía formularios.

La apertura habitual es `<?php`. Dentro de ese bloque escribes instrucciones PHP, que suelen terminar con punto y coma. Al cerrar con `?>`, vuelves a texto de salida, normalmente HTML. La forma `<?= $valor ?>` imprime directamente una expresión dentro de esa salida.

## Leer una asignación de derecha a izquierda

En `$libres = $capacidad - $reservas;`, primero se leen los valores de la derecha, se calcula la resta y después se guarda el resultado bajo el nombre de la izquierda. El signo `=` no pregunta si ambos lados son iguales.

Si cambias `$reservas` más tarde, `$libres` no se recalcula por sí solo. Una variable que contiene el resultado no conserva una fórmula viva. Tendrás que ejecutar de nuevo la operación cuando corresponda. Esta idea ayuda a seguir programas donde las cantidades se actualizan por pasos.

```php
<?php
$capacidad = 10;
$reservas = 3;
$libres = $capacidad - $reservas;
$reservas = 5;
echo $libres . "\n";
$libres = $capacidad - $reservas;
echo $libres . "\n";
```

Primero aparece 7 y después 5. La segunda asignación a `$reservas` no modifica la resta anterior; la nueva resta sí obtiene el valor actualizado.

## Texto, números y booleanos tienen papeles distintos

`'18'` es texto y `18` es un entero. Pueden representar una información parecida para una persona, pero no son el mismo tipo. Una entrada HTTP llega normalmente como texto y debe validarse antes de usarse como cantidad.

Una comparación como `$libres === 0` produce `true` o `false`. Ese resultado puede utilizarse después en una decisión. No necesitas escribir el texto `'true'`: sería una cadena de cuatro letras, no el valor lógico.

Conocer el tipo evita interpretar una salida engañosa. `var_dump` resulta útil porque muestra valor y tipo; imprimir solo un booleano con `echo` puede ser poco claro, ya que su conversión a texto no presenta necesariamente las palabras que esperas.

## Concatenación e interpolación

La concatenación une textos con `.`. Las comillas dobles permiten interpolar una variable sencilla; las simples conservan el texto literal. Ambas formas son válidas si sabes qué resultado construyen.

```php
<?php
$sala = 'Azul';
echo 'Sala: ' . $sala . "\n";
echo "Sala: $sala\n";
echo 'Sala: $sala' . "\n";
```

Las dos primeras líneas muestran `Sala: Azul`; la tercera muestra literalmente `Sala: $sala`. El salto `\n` funciona aquí dentro de comillas dobles. En una página HTML normal, un salto del código fuente no obliga al navegador a dibujar otra línea: necesitas una estructura HTML adecuada.

## Separar el cálculo de la presentación

Organiza primero los datos y después el HTML que los muestra. De ese modo puedes comprobar una resta o una condición sin mezclarla con etiquetas y estilos. No hace falta crear una arquitectura complicada: basta con que el lector sepa dónde se preparan los valores y dónde se representan.

Cuando un valor contiene texto externo, escápalo al insertarlo en HTML. La razón no es que PHP no sepa imprimirlo, sino que el navegador podría interpretarlo como marcado. El ejemplo del taller muestra tanto el cálculo de plazas como la presentación segura del nombre.

## Problema explicado paso a paso: plazas de un taller de cerámica

**Objetivo:** mostrar las plazas disponibles. No hay formulario ni datos de clase: los valores están fijados para seguir el cálculo.

Guarda `taller.php`:

```php
<?php
$capacidad = 18;
$reservas = 11;
$libres = $capacidad - $reservas;
$nombre = 'Cerámica & color';
$completo = $libres === 0;
?>
<h1><?= htmlspecialchars($nombre, ENT_QUOTES, 'UTF-8') ?></h1>
<p>Plazas libres: <?= $libres ?></p>
<p><?= $completo ? 'Sin plazas' : 'Inscripción abierta' ?></p>
```

### Razonamiento paso a paso

1. PHP asocia 18 y 11 a dos variables enteras.
2. Resta las reservas de la capacidad: `18 - 11 = 7`.
3. La comparación `7 === 0` es falsa; `$completo` vale `false`.
4. El ternario `condicion ? valor_si : valor_no` elige el texto «Inscripción abierta».
5. `htmlspecialchars` transforma los caracteres especiales para insertar texto en HTML. El ampersand se codifica en el código fuente y el navegador muestra `&`.

**Resultado visible:** «Cerámica & color», «Plazas libres: 7» e «Inscripción abierta». Si reservas 18 plazas, verás 0 y «Sin plazas». Si pones 20 reservas, aparece un número negativo: el programa necesita una regla de validación; la resta, por sí sola, no garantiza datos coherentes.

## Operadores que utilizarás

`+`, `-`, `*`, `/` y `%` calculan. `&&`, `||` y `!` combinan o niegan condiciones. `??` aporta un valor alternativo cuando un dato no existe o es `null`, como en `$_GET['sala'] ?? ''`. No valida que el dato sea correcto.

Un array indexado utiliza posiciones: `$salas = ['Azul', 'Verde'];` y `$salas[0]` devuelve `Azul`. Un array asociativo utiliza claves: `$sala = ['nombre' => 'Azul', 'capacidad' => 18];`. Accedes con `$sala['capacidad']`. Si la clave no existe, compruébala o utiliza `??`.

| Error | Causa y solución |
| --- | --- |
| `Undefined variable` | Revisa el nombre y la asignación antes de usarla. |
| `Parse error` | Mira `;`, comillas y llaves, también en la línea anterior. |
| Se muestra código PHP | Abres el archivo directamente o el servidor no lo procesa. |
| El texto del usuario se convierte en HTML | Escápalo en el punto donde generas HTML. |

## Texto, tipos y operaciones que conviene distinguir

Los apuntes anteriores separaban bien la operación que calcula de la que presenta el resultado. En PHP, `.` concatena texto y `+` suma: no utilices uno esperando el comportamiento del otro. `strlen` cuenta bytes; para contar caracteres de texto multibyte puedes utilizar `mb_strlen`, si la extensión correspondiente está disponible.

```php
<?php
$texto = '  sala azul  ';
$limpio = trim($texto);
echo strtoupper($limpio) . "\n";
echo str_replace('azul', 'verde', $limpio) . "\n";
```

**Salida esperada:** `SALA AZUL` y `sala verde`. `trim` limpia los extremos, no los espacios interiores. `strtoupper` es suficiente para este texto ASCII; el tratamiento completo de mayúsculas Unicode requiere herramientas multibyte apropiadas.

### Diagnóstico de tipos

`var_dump($valor)` muestra tipo y contenido. Esto ayuda a explicar por qué `3 === '3'` es falso: uno es entero y otro es texto. No conviertas entradas a ciegas para hacer desaparecer el error; define primero qué representación admite el programa y valida antes del cálculo.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Calcula el material que falta

Guarda 30 como cantidad necesaria de hojas y 22 como cantidad disponible. Escribe un programa PHP que calcule lo que falta y muestre una frase. Calcula primero el número y construye después el mensaje.

??? tip "Pista"
    Utiliza una resta y concatena el resultado con texto.

??? success "Solución paso a paso"
    ```php
    <?php
    $necesarias = 30;
    $disponibles = 22;
    $faltan = $necesarias - $disponibles;
    echo 'Faltan ' . $faltan . " hojas\n";
    ```

    1. Restamos las disponibles a las necesarias.
    2. Guardamos 8 en `$faltan`.
    3. Mostramos `Faltan 8 hojas`. El texto no se suma: se concatena con `.`.

### 2. Comprueba cuándo se calcula un valor

Sin ejecutarlo primero, predice las dos líneas de este programa. Después compruébalo y explica por qué `$b` no cambia al asignar 10 a `$a`.

```php
<?php
$a = 6;
$b = $a + 1;
$a = 10;
echo $b . "\n";
$b = $a + 1;
echo $b . "\n";
```

??? tip "Pista"
    Una asignación guarda el resultado de ese momento, no una fórmula que se actualice sola.

??? success "Solución paso a paso"
    Las líneas son 7 y 11.

    1. La primera asignación a `$b` calcula `6 + 1`.
    2. Cambiar `$a` a 10 no vuelve a ejecutar esa suma.
    3. La segunda asignación a `$b` sí calcula con el nuevo valor: `10 + 1`.

    Para comprobarlo, guarda el programa en un archivo y ejecútalo con PHP.

### 3. Une texto sin ejecutar etiquetas

La variable `$titulo` contiene `<em>Rutas del barrio</em>`. Genera un párrafo HTML que muestre ese contenido como texto, sin que se convierta en cursiva. No sustituyas manualmente cada carácter.

??? tip "Pista"
    La transformación corresponde al momento de presentar el texto en HTML.

??? success "Solución paso a paso"
    ```php
    <?php
    $titulo = '<em>Rutas del barrio</em>';
    echo '<p>' . htmlspecialchars($titulo, ENT_QUOTES, 'UTF-8') . '</p>';
    ```

    1. Las etiquetas del párrafo son parte de nuestra presentación.
    2. El contenido de `$titulo` se escapa antes de insertarlo.
    3. El navegador muestra literalmente `<em>Rutas del barrio</em>` dentro del párrafo.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Variable y tipo de dato** | Nombre asociado a un valor y categoría que determina qué operaciones admite. |
| **Cadena y booleano** | Texto y valor lógico verdadero/falso, respectivamente. |
| **Sintaxis** | Reglas que permiten interpretar instrucciones de un lenguaje. |
| **Escape de HTML** | Transformación de texto para que no se interprete como marcado en el contexto de salida. |

!!! success "Para repasar"
    Primero se calculan los datos; después se genera la respuesta. Validar datos y escapar HTML son operaciones diferentes.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
