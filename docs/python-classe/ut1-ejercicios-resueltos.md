## Ejercicios resueltos paso a paso · UT1

Estos ejercicios complementan la teoría. En cada caso se separa **entrada → proceso → salida** y se explica qué hace cada parte del código.

### 1.1 · Introducción a Python

#### Ejercicio 1 · Calcular un precio con IVA
**Enunciado.** Calcula el precio final de un producto de 80 € aplicando un 21 % de IVA.

```python
precio = 80
iva = precio * 0.21
total = precio + iva
print(total)
```

**Paso a paso:** `precio = 80` guarda el dato inicial; `precio * 0.21` calcula el 21 %; `total` suma precio e impuesto; `print()` muestra `96.8`. **Entrada:** 80. **Proceso:** multiplicar y sumar. **Salida:** 96.8.

#### Ejercicio 2 · Minutos de lectura
```python
palabras = 1200
ritmo = 150
minutos = palabras / ritmo
print(minutos)
```
`palabras` y `ritmo` son los datos. `/` realiza una división real. El resultado `8.0` se guarda en `minutos` y después se muestra.

#### Ejercicio 3 · Datos de un servidor
```python
servidor = "web01"
puerto = 8080
print("Servidor:", servidor)
print("Puerto:", puerto)
```
Las comillas crean cadenas; `puerto` es un entero; la coma de `print()` permite mostrar texto y variables sin convertirlas manualmente.

### 1.2 · Entorno de trabajo y ejecución

#### Ejercicio 1 · Crear y ejecutar un script
Guarda `print("Python funciona")` en `prueba.py` y ejecuta `python3 prueba.py`. El archivo `.py` contiene el código fuente; `python3` inicia el intérprete; `prueba.py` es el argumento que indica qué programa ejecutar.

#### Ejercicio 2 · Comprobar la versión
Ejecuta `python3 --version`. `python3` selecciona el intérprete y `--version` pide información en vez de ejecutar un programa. Sirve para comprobar que el entorno está preparado.

#### Ejercicio 3 · Interpretar un error de nombre
```python
nombre = "Ana"
print(nomre)
```
Python produce `NameError` porque `nomre` no existe. La solución es escribir `print(nombre)`. El mensaje de error indica **tipo de error + línea + nombre problemático**.

### 1.3 · Variables y tipos de datos

#### Ejercicio 1 · Identificar tipos
```python
usuario = "jose"
intentos = 3
espacio = 18.5
activo = True
print(type(usuario), type(intentos), type(espacio), type(activo))
```
`str` representa texto, `int` enteros, `float` números con decimales y `bool` valores lógicos. `type()` permite comprobar el tipo real de cada objeto.

#### Ejercicio 2 · Conversión de texto a número
```python
edad_texto = "36"
edad = int(edad_texto)
print(edad + 1)
```
`"36"` es texto y no debe sumarse directamente a `1`. `int()` crea el entero `36`; después la suma produce `37`.

#### Ejercicio 3 · Intercambiar valores
```python
a = 10
b = 20
a, b = b, a
print(a, b)
```
Python evalúa primero los valores de la derecha y después los asigna a la izquierda. El resultado es `20 10`.

### 1.4 · Números y operadores

#### Ejercicio 1 · Cociente y resto
```python
segundos = 367
minutos = segundos // 60
resto = segundos % 60
print(minutos, resto)
```
`//` obtiene el cociente entero (`6`) y `%` el resto (`7`). Por tanto, 367 segundos son 6 minutos y 7 segundos.

#### Ejercicio 2 · Potencia
```python
lado = 5
area = lado ** 2
print(area)
```
`**` es el operador de potencia. `5 ** 2` equivale a 5 × 5 y produce `25`.

#### Ejercicio 3 · Prioridad de operadores
```python
resultado = (10 + 2) * 3
print(resultado)
```
Los paréntesis obligan a calcular primero `10 + 2`; después se multiplica por 3. El resultado es `36`. Sin paréntesis sería `16`.

### 1.5 · Cadenas, entrada y salida

#### Ejercicio 1 · Pedir el nombre
```python
nombre = input("Nombre: ")
print("Hola", nombre)
```
`input()` muestra el mensaje y espera teclado. Lo escrito se devuelve siempre como `str`; la variable `nombre` conserva ese texto y `print()` lo muestra.

#### Ejercicio 2 · Pedir dos números
```python
a = int(input("Primer número: "))
b = int(input("Segundo número: "))
print("Suma:", a + b)
```
Cada `input()` devuelve texto; `int()` lo convierte a entero. Solo después `a + b` realiza una suma numérica.

#### Ejercicio 3 · Longitud y acceso a una cadena
```python
usuario = "admin"
print(len(usuario))
print(usuario[0])
print(usuario[-1])
```
`len()` devuelve 5 caracteres; `[0]` accede al primero (`a`) y `[-1]` al último (`n`). Los índices empiezan en cero.

!!! tip "Método de estudio"
    Antes de ejecutar cada solución, intenta predecir el resultado. Después cambia un dato y explica por qué cambia la salida.