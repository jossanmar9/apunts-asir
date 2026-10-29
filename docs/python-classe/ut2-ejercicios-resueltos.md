## Ejercicios resueltos paso a paso · UT2

### 2.1 · Objetos predefinidos

#### Ejercicio 1 · Operaciones con texto
```python
nombre = "Servidor Web"
print(len(nombre))
print(nombre[0])
```
`len()` cuenta todos los caracteres, incluido el espacio. `[0]` obtiene el primer carácter porque los índices comienzan en cero.

#### Ejercicio 2 · Cortar una cadena
```python
ip = "192.168.1.50"
print(ip[0:7])
```
El *slice* `[0:7]` toma caracteres desde la posición 0 hasta antes de la 7. El límite final nunca se incluye.

#### Ejercicio 3 · Pertenencia
```python
archivo = "backup.sql"
print(".sql" in archivo)
```
`in` pregunta si una cadena aparece dentro de otra y devuelve un booleano. Aquí el resultado es `True`.

### 2.2 · Métodos de cadenas

#### Ejercicio 1 · Limpiar entrada
```python
usuario = "  ADMIN  "
usuario = usuario.strip().lower()
print(usuario)
```
`strip()` elimina espacios exteriores. Sobre el resultado, `lower()` convierte a minúsculas. La salida es `admin`.

#### Ejercicio 2 · Sustituir texto
```python
ruta = "datos\\usuarios\\lista.txt"
ruta = ruta.replace("\\", "/")
print(ruta)
```
`replace()` crea una nueva cadena sustituyendo cada barra invertida por `/`. Las cadenas son inmutables: por eso reasignamos el resultado.

#### Ejercicio 3 · Separar datos
```python
linea = "web01;192.168.1.10;activo"
datos = linea.split(";")
print(datos[0])
print(datos[1])
```
`split(";")` divide el texto usando `;` como separador y devuelve una lista. `[0]` y `[1]` acceden a sus dos primeros elementos.

### 2.3 · f-strings y Unicode

#### Ejercicio 1 · Informe con f-string
```python
host = "web01"
cpu = 37.456
print(f"{host}: CPU {cpu:.1f}%")
```
La `f` permite insertar expresiones entre llaves. `{cpu:.1f}` muestra el número con un decimal: `web01: CPU 37.5%`.

#### Ejercicio 2 · Alinear una tabla
```python
servicio = "nginx"
estado = "activo"
print(f"{servicio:<12}{estado:>10}")
```
`<12` reserva 12 posiciones y alinea a la izquierda; `>10` reserva 10 y alinea a la derecha. Es útil para informes de terminal.

#### Ejercicio 3 · Unicode
```python
mensaje = "Servidor ✓"
print(mensaje)
print(len(mensaje))
```
Python 3 trabaja con Unicode. El símbolo `✓` forma parte de la cadena y `len()` cuenta caracteres, no los bytes usados para almacenarlos.

!!! tip "Comprueba que lo entiendes"
    Modifica las cadenas, índices, separadores y formatos. Si puedes anticipar el nuevo resultado antes de ejecutar, estás entendiendo la operación.