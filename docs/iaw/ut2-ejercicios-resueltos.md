## Ejercicios resueltos paso a paso · UT2

### PHP básico

#### Ejercicio 1 · Variables y salida
```php
<?php
$nombre = "Ana";
$edad = 20;
echo "$nombre tiene $edad años";
```
`$` identifica variables en PHP; `=` asigna; `;` termina instrucciones; `echo` envía contenido a la salida. Las comillas dobles permiten interpolar variables.

#### Ejercicio 2 · Operación numérica
```php
<?php
$precio = 80;
$iva = $precio * 0.21;
$total = $precio + $iva;
echo $total;
```
Primero se guarda el precio, después se calcula el impuesto y finalmente se suman ambos valores. La salida es `96.8`.

#### Ejercicio 3 · Concatenación
```php
<?php
$host = "web01";
$ip = "192.168.1.10";
echo $host . " - " . $ip;
```
`.` concatena cadenas en PHP. No debe confundirse con `+`, que se usa para operaciones numéricas.

### Control de flujo y funciones

#### Ejercicio 1 · if
```php
<?php
$uso = 85;
if ($uso >= 80) {
    echo "Aviso";
} else {
    echo "Correcto";
}
```
La comparación produce verdadero o falso. Las llaves delimitan cada bloque; con 85 se ejecuta el primero.

#### Ejercicio 2 · bucle
```php
<?php
for ($i = 1; $i <= 3; $i++) {
    echo $i . "<br>";
}
```
El `for` tiene inicialización, condición y actualización. `$i++` incrementa en uno tras cada vuelta.

#### Ejercicio 3 · función
```php
<?php
function saludar($nombre) {
    return "Hola, " . $nombre;
}
echo saludar("Ana");
```
`function` define código reutilizable; `$nombre` es el parámetro; `return` devuelve el resultado; la llamada pasa `"Ana"` como argumento.

### Formularios

#### Ejercicio 1 · Recibir GET
```php
<?php
$busqueda = $_GET['q'] ?? '';
echo htmlspecialchars($busqueda);
```
`$_GET` contiene parámetros de la URL; `?? ''` usa cadena vacía si `q` no existe; `htmlspecialchars()` escapa caracteres especiales antes de mostrarlos en HTML.

#### Ejercicio 2 · Recibir POST
```php
<?php
$nombre = trim($_POST['nombre'] ?? '');
if ($nombre === '') {
    echo "El nombre es obligatorio";
}
```
`$_POST` recibe datos enviados por POST; `trim()` elimina espacios exteriores; `===` compara valor y tipo; la validación evita aceptar una cadena vacía.

#### Ejercicio 3 · Validar entero
```php
<?php
$edad = filter_input(INPUT_POST, 'edad', FILTER_VALIDATE_INT);
if ($edad === false) {
    echo "Edad no válida";
}
```
`filter_input()` lee y valida. `FILTER_VALIDATE_INT` exige un entero; `false` indica que la validación no ha pasado.

### Estado: sesiones y cookies

#### Ejercicio 1 · Sesión
```php
<?php
session_start();
$_SESSION['usuario'] = 'ana';
echo $_SESSION['usuario'];
```
`session_start()` inicia o recupera la sesión antes de usar `$_SESSION`. El dato se asocia a la sesión del usuario entre peticiones.

#### Ejercicio 2 · Contador de sesión
```php
<?php
session_start();
$_SESSION['visitas'] = ($_SESSION['visitas'] ?? 0) + 1;
echo $_SESSION['visitas'];
```
Si no existe `visitas`, `?? 0` parte de cero. Después se suma uno y se guarda otra vez en la sesión.

#### Ejercicio 3 · Cookie
```php
<?php
setcookie('tema', 'oscuro', time() + 3600, '/');
```
`setcookie()` prepara una cabecera HTTP: nombre, valor, caducidad y ruta. Debe ejecutarse antes de enviar contenido de la respuesta.

### Depuración y errores

#### Ejercicio 1 · Inspeccionar una variable
```php
<?php
$datos = ['nginx', 'php', 'mariadb'];
var_dump($datos);
```
`var_dump()` muestra tipo, tamaño y contenido. Es útil durante la depuración, pero no debería dejarse como salida de una aplicación terminada.

#### Ejercicio 2 · Registrar información
```php
<?php
error_log('Inicio del procesamiento');
```
`error_log()` envía el mensaje al registro configurado en PHP. Permite investigar sin mostrar detalles internos al usuario final.

#### Ejercicio 3 · Comprobar un dato antes de usarlo
```php
<?php
$id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
if ($id === false || $id === null) {
    exit('ID no válido');
}
echo "ID: " . $id;
```
Primero se obtiene y valida la entrada; después se comprueban los casos inválidos; `exit()` detiene la ejecución y solo si todo es correcto se usa el dato.

!!! success "Método"
    En PHP sigue siempre el recorrido **entrada → validación → proceso → salida**. En formularios y estado, indica además de dónde procede cada dato (`$_GET`, `$_POST`, `$_SESSION` o cookie).