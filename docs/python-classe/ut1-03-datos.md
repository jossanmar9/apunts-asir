# UT1 · 1.3 Datos, variables, tipos y objetos

## Qué debes aprender

En Python trabajamos constantemente con datos. Cada dato tiene un **tipo**, y utilizamos **variables** para poder referirnos a esos datos durante el programa.

## Datos y tipos

Un dato es una pieza de información que el programa puede manejar:

```python
42
"Ana"
3.14
True
```

Podemos consultar el tipo con `type()`:

```python
print(type(42))      # <class 'int'>
print(type("Ana"))   # <class 'str'>
print(type(3.14))    # <class 'float'>
print(type(True))    # <class 'bool'>
```

Tipos básicos del tema:

| Tipo | Ejemplo | Uso |
| --- | --- | --- |
| `int` | `10` | Enteros |
| `float` | `3.5` | Decimales |
| `str` | `"hola"` | Texto |
| `bool` | `True` | Verdadero/falso |
| `complex` | `3+5j` | Números complejos |

## En Python todo son objetos

Una idea básica del temario es que en Python los datos son **objetos**. De momento basta con pensar que un objeto tiene:

- un tipo;
- un valor;
- una identidad.

```python
texto = "python"
print(type(texto))
print(texto.upper())
```

No necesitas dominar todavía la programación orientada a objetos para entender esta idea.

## Variables

Una variable es un **nombre que apunta a un dato**.

```python
nombre = "Ana"
edad = 20
```

En:

```python
num_items = 10
```

`num_items` es el nombre y `10` es el valor al que queda asociado.

### Lado izquierdo y lado derecho

```python
precio = 50 + 10
```

Primero se evalúa `50 + 10` y después el resultado se asigna a `precio`.

En algunos textos verás:

- **LHS** (*left-hand side*): lado izquierdo de la asignación;
- **RHS** (*right-hand side*): lado derecho que se evalúa.

## Nombres de variables

Un nombre puede contener letras, números y guiones bajos, pero no puede comenzar por un número.

Correcto:

```python
edad = 20
nombre_alumno = "Ana"
precio2 = 15.5
```

Incorrecto:

```python
2precio = 10
nombre-alumno = "Ana"
class = "ASIR"
```

Buenas prácticas:

- nombres claros;
- minúsculas y guiones bajos;
- evitar abreviaturas que no aporten claridad;
- no utilizar como variable nombres de funciones como `type`, `input`, `list` o `str`.

## Constantes

Python no impide modificar una constante, pero por convenio escribimos en mayúsculas los valores que no deberían cambiar:

```python
IVA = 0.21
MAX_INTENTOS = 3
```

Es una **convención**, no una protección del lenguaje.

## Asignación múltiple

Python permite asignar varios valores a la vez:

```python
nombre, edad = "Ana", 20
```

También el mismo objeto a varios nombres:

```python
a = b = c = 0
```

Con objetos mutables hay que tener cuidado porque varios nombres pueden apuntar al mismo objeto.

## Identidad: `id()`

`id()` devuelve un identificador asociado al objeto durante la ejecución:

```python
x = [1, 2, 3]
y = x

print(id(x))
print(id(y))
```

Si ambos nombres apuntan al mismo objeto, sus cambios se comparten:

```python
x = [1, 2, 3]
y = x
y.append(4)

print(x)  # [1, 2, 3, 4]
```

## Mutabilidad

Un objeto **mutable** puede cambiar después de crearse. Por ejemplo, una lista:

```python
numeros = [1, 2, 3]
numeros.append(4)
print(numeros)
```

Los enteros, flotantes, booleanos, cadenas y tuplas son **inmutables**.

```python
texto = "hola"
# texto[0] = "H"  # Error
```

Para obtener otro texto creamos una cadena nueva:

```python
texto = "hola"
texto = "H" + texto[1:]
print(texto)
```

## Ayuda integrada

Puedes consultar ayuda desde Python:

```python
help(print)
help(str)
```

Y comprobar tipos:

```python
valor = "10"
print(type(valor))
```

## Ejemplo explicado

```python
cantidad = 4
otra = cantidad
cantidad = cantidad + 2

print(cantidad)
print(otra)
```

Salida:

```text
6
4
```

`otra` quedó asociada al valor anterior. La instrucción `cantidad = cantidad + 2` calcula un resultado nuevo y vuelve a asociar el nombre `cantidad`.

## Comprueba que sabes...

- Reconocer `int`, `float`, `str`, `bool` y `complex`.
- Utilizar `type()`.
- Explicar qué es una variable.
- Distinguir nombre, valor y asignación.
- Crear nombres de variables válidos.
- Explicar la convención de las constantes.
- Utilizar una asignación múltiple sencilla.
- Entender la idea básica de objeto.
- Distinguir mutable e inmutable.
- Explicar para qué sirven `id()` y `help()`.

!!! success "Para el examen"
    No pienses en una variable únicamente como una «caja». En Python es más preciso pensar que es **un nombre asociado a un objeto**.

---

Fuente principal: material de clase **Introducción a Python 1.3 · Datos, variables, tipos y objetos**, consultado el 29/10/2026.