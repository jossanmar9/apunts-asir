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

## Ejemplo resuelto: plazas de un taller de cerámica

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

!!! success "Para repasar"
    Primero se calculan los datos; después se genera la respuesta. Validar datos y escapar HTML son operaciones diferentes.

---

Fuente del temario: [apuntes originales de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
