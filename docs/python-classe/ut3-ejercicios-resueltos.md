## Ejercicios resueltos paso a paso · UT3

### 3.1 · Condicionales

#### Ejercicio 1 · Espacio en disco
```python
libre = 8
if libre < 10:
    print("Aviso: poco espacio")
else:
    print("Espacio suficiente")
```
`libre < 10` produce `True`; por eso se ejecuta el bloque indentado del `if`. `else` solo se ejecutaría si la condición fuera falsa.

#### Ejercicio 2 · Clasificar carga
```python
carga = 72
if carga >= 90:
    print("Crítica")
elif carga >= 60:
    print("Alta")
else:
    print("Normal")
```
Python comprueba las condiciones de arriba abajo y se queda con la primera verdadera. Con 72 imprime `Alta`.

#### Ejercicio 3 · Dos condiciones
```python
usuario = "admin"
activo = True
if usuario == "admin" and activo:
    print("Acceso permitido")
```
`==` compara; `and` exige que ambas condiciones sean verdaderas. No debe confundirse `==` con `=`.

### 3.2 · while

#### Ejercicio 1 · Contador
```python
n = 1
while n <= 5:
    print(n)
    n += 1
```
`while` repite mientras `n <= 5`. `n += 1` actualiza el contador; sin esa línea tendríamos un bucle infinito.

#### Ejercicio 2 · Reintentos
```python
intentos = 0
while intentos < 3:
    print("Intento", intentos + 1)
    intentos += 1
```
El contador empieza en 0, la condición limita a tres vueltas y `intentos + 1` permite mostrar 1, 2 y 3 al usuario.

#### Ejercicio 3 · Salir con break
```python
while True:
    orden = input("Orden (salir para terminar): ")
    if orden == "salir":
        break
```
`while True` sería infinito. `break` rompe el bucle cuando se cumple la condición.

### 3.3 · for y range

#### Ejercicio 1 · Recorrer números
```python
for numero in range(1, 6):
    print(numero)
```
`range(1, 6)` genera 1, 2, 3, 4 y 5: el límite final no se incluye. `for` asigna cada valor a `numero`.

#### Ejercicio 2 · Recorrer servicios
```python
servicios = ["nginx", "ssh", "mariadb"]
for servicio in servicios:
    print("Revisando", servicio)
```
En cada vuelta `servicio` toma un elemento de la lista. No necesitamos gestionar un índice manual.

#### Ejercicio 3 · Acumulador
```python
total = 0
for n in range(1, 5):
    total += n
print(total)
```
`total` empieza en cero y acumula 1 + 2 + 3 + 4. La salida es `10`.

### 3.4 · Depuración y errores

#### Ejercicio 1 · TypeError
```python
edad = "36"
# print(edad + 1)  # Error
print(int(edad) + 1)
```
No se puede sumar directamente `str` e `int`. `int(edad)` convierte el texto antes de sumar.

#### Ejercicio 2 · ValueError controlado
```python
texto = "abc"
try:
    numero = int(texto)
except ValueError:
    print("No es un entero válido")
```
`int("abc")` lanza `ValueError`. `try` contiene la operación que puede fallar y `except ValueError` trata ese error concreto.

#### Ejercicio 3 · Seguir valores
```python
x = 2
print("x inicial:", x)
x = x * 3
print("x final:", x)
```
Los `print()` temporales ayudan a observar el estado del programa. Primero vale 2 y después 6; esta técnica sencilla permite localizar muchos errores lógicos.

### 3.5 · Bibliotecas para administración

#### Ejercicio 1 · Fecha actual
```python
import datetime
ahora = datetime.datetime.now()
print(ahora)
```
`import datetime` carga el módulo. `datetime.datetime.now()` obtiene fecha y hora actuales y devuelve un objeto que guardamos en `ahora`.

#### Ejercicio 2 · Rutas con pathlib
```python
import pathlib
ruta = pathlib.Path("datos")
print(ruta.exists())
```
`Path()` representa una ruta como objeto. `exists()` consulta al sistema de archivos y devuelve `True` o `False`.

#### Ejercicio 3 · Información del sistema
```python
import platform
print(platform.system())
print(platform.python_version())
```
`platform.system()` informa del sistema operativo y `platform.python_version()` de la versión de Python. El punto accede a funciones definidas dentro del módulo.

!!! success "Objetivo"
    No memorices las soluciones. Explica en voz alta qué valor tiene cada variable, qué condición se comprueba y por qué se ejecuta cada línea.