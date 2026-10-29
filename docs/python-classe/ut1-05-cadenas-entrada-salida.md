# UT1 · 1.5 Cadenas, entrada/salida y f-strings

## Cadenas de texto

Las cadenas (`str`) permiten trabajar con nombres, mensajes, rutas, líneas de archivos, comandos y textos introducidos por el usuario.

Podemos utilizar comillas simples o dobles:

```python
nombre = 'Ana'
mensaje = "Hola"
```

Ambas formas son válidas. Conviene ser consistente.

### Cadenas multilínea

```python
texto = """Primera línea
Segunda línea
Tercera línea"""
```

Las triples comillas también se utilizan en *docstrings* para documentar funciones y otros elementos de Python.

### Cadena vacía

```python
vacia = ""
```

Es una cadena válida con longitud 0.

## Unicode

Python 3 utiliza Unicode para representar texto:

```python
texto = "áéíóú ñ 中文"
print(texto)
```

Cada carácter tiene un código numérico. Podemos consultar y convertir códigos con:

```python
print(ord("A"))  # 65
print(chr(65))   # A
```

## Conversión de tipos

```python
numero = 10
texto = str(numero)
```

Y de texto a número:

```python
edad = int("20")
precio = float("3.50")
```

La cadena debe representar un valor válido:

```python
float("3.1a")  # ValueError
```

`int()` también permite indicar la base:

```python
print(int("1010", 2))  # 10
```

## Caracteres de escape

| Secuencia | Significado |
| --- | --- |
| `\n` | salto de línea |
| `\t` | tabulación |
| `\\` | barra invertida |
| `\"` | comilla doble |

Ejemplo:

```python
print("abc\ndef")
```

Salida:

```text
abc
def
```

## Mostrar información con `print()`

```python
nombre = "Ana"
edad = 20
print(nombre, edad)
```

Por defecto, `print()` separa los argumentos con espacios.

### `sep`

```python
print("Ana", "20", "ASIR", sep=";")
```

Salida:

```text
Ana;20;ASIR
```

### `end`

```python
print("Hola", end=" ")
print("Ana")
```

Salida:

```text
Hola Ana
```

## Pedir información con `input()`

`input()` **siempre devuelve una cadena de texto**.

```python
nombre = input("Nombre: ")
print("Hola", nombre)
```

Aunque el usuario escriba un número:

```python
edad = input("Edad: ")
print(type(edad))  # <class 'str'>
```

Para calcular con ese dato debemos convertirlo:

```python
edad = int(input("Edad: "))
print(edad + 1)
```

No utilices `input` como nombre de variable:

```python
input = "Ana"  # Mala práctica
```

Estarías ocultando la función `input()`.

## Operaciones con cadenas

### Concatenar

```python
saludo = "Hola" + " " + "Ana"
print(saludo)
```

### Repetir

```python
print("Wow" * 3)  # WowWowWow
```

### Longitud

```python
print(len("Hola"))  # 4
```

### Pertenencia con `in`

```python
frase = "Hola, Ana"
print("Ana" in frase)   # True
print("Luis" in frase)  # False
```

## Índices

Las posiciones comienzan en 0:

```python
texto = "Python"
print(texto[0])   # P
print(texto[1])   # y
print(texto[-1])  # n
```

Los índices negativos cuentan desde el final.

## Slicing o troceado

La forma básica es `[inicio:fin]`. El índice final **no se incluye**.

```python
texto = "Python"
print(texto[0:2])  # Py
print(texto[2:])   # thon
print(texto[:4])   # Pyth
```

## Las cadenas son inmutables

No podemos modificar directamente un carácter:

```python
texto = "python"
# texto[0] = "P"  # Error
```

Creamos una cadena nueva:

```python
texto = "python"
texto = "P" + texto[1:]
print(texto)  # Python
```

## F-strings

Las f-strings permiten combinar texto, variables y expresiones de forma legible.

```python
nombre = "Ana"
edad = 20
print(f"{nombre} tiene {edad} años")
```

Salida:

```text
Ana tiene 20 años
```

Si olvidamos la `f`:

```python
print("{nombre} tiene {edad} años")
```

Python mostrará las llaves literalmente.

### Expresiones dentro de una f-string

```python
a = 5
b = 3
print(f"La suma es {a + b}")
```

### Mostrar llaves literales

```python
valor = 10
print(f"El diccionario es {{'valor': {valor}}}")
```

### Formatear decimales

```python
precio = 19.995
print(f"Precio final: {precio:.2f} €")
```

`.2f` muestra el valor con dos decimales.

```python
numero = 3.14159265
print(f"{numero:.3f}")  # 3.142
```

El formato cambia **cómo se muestra** el valor, no el valor original de la variable.

## Ejemplo explicado

```python
nombre = input("Nombre: ")
edad = int(input("Edad: "))

print(f"Hola, {nombre}")
print(f"El año que viene tendrás {edad + 1} años")
```

Si introducimos `Jose` y `36`:

1. `input()` devuelve `"Jose"`.
2. El segundo `input()` devuelve inicialmente `"36"`.
3. `int()` lo convierte en el entero `36`.
4. La f-string calcula `edad + 1`.
5. Se muestra `37` dentro del mensaje.

## Comprueba que sabes...

- Crear cadenas con comillas simples, dobles y triples.
- Reconocer una cadena vacía.
- Entender que Python 3 utiliza Unicode.
- Utilizar `ord()` y `chr()`.
- Convertir con `str()`, `int()` y `float()`.
- Reconocer un `ValueError` por conversión inválida.
- Utilizar `\n`, `\t`, `\\` y `\"`.
- Utilizar `print()` con `sep` y `end`.
- Explicar que `input()` siempre devuelve `str`.
- Concatenar y repetir cadenas.
- Utilizar `len()` e `in`.
- Acceder mediante índices positivos y negativos.
- Utilizar slicing básico.
- Explicar por qué una cadena es inmutable.
- Crear f-strings con variables y expresiones.
- Formatear decimales con `.2f`.

!!! success "Para el examen"
    Recuerda la cadena completa: **`input()` → texto → conversión si hace falta → cálculo → `print()`/f-string**.

---

Fuente principal: material de clase **Introducción a Python 1.5 · Cadenas de texto, entrada y salida, f-strings**, consultado el 29/10/2026.