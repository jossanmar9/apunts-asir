# UT3 · 3.3 Bucles `for`, `range()` y recorridos

## Recorrer elementos

El bucle `for` sirve para recorrer los elementos de un iterable: por ejemplo, cadenas, listas, rangos o líneas de un archivo.

A diferencia de `while`, normalmente utilizamos `for` cuando conocemos el conjunto de elementos que queremos recorrer.

## Recorrer una cadena

```python
for letra in "Python":
    print(letra)
```

Salida:

```text
P
y
t
h
o
n
```

Una cadena es una secuencia y puede recorrerse carácter a carácter.

## Recorrer una lista

```python
alumnos = ["Ana", "Luis", "Marta"]

for alumno in alumnos:
    print(alumno)
```

En este punto basta entender una lista como una colección ordenada de elementos dentro de una variable.

## `range()`

`range()` genera un rango de números que se utiliza muy a menudo con `for`.

```python
for numero in range(5):
    print(numero)
```

Salida:

```text
0
1
2
3
4
```

El límite final no se incluye.

### Inicio y fin

```python
for numero in range(1, 6):
    print(numero)
```

Recorre `1, 2, 3, 4, 5`.

### Inicio, fin y paso

```python
for numero in range(1, 6, 2):
    print(numero)
```

Salida:

```text
1
3
5
```

La forma general es:

```python
range(inicio, fin, paso)
```

## Contar hacia atrás

El paso puede ser negativo:

```python
for numero in range(2, -1, -1):
    print(numero)
```

Salida:

```text
2
1
0
```

Empieza en 2, resta 1 en cada iteración y se detiene antes de -1.

## `range()` no es una lista

En Python 3, `range()` devuelve un objeto `range`.

```python
valores = range(5)
print(valores)
print(list(valores))
```

Salida:

```text
range(0, 5)
[0, 1, 2, 3, 4]
```

No necesitas convertir un `range` a lista para recorrerlo con `for`.

## Índice y valor con `enumerate()`

Cuando necesitamos tanto el índice como el elemento, podemos utilizar `enumerate()`:

```python
alumnos = ["Ana", "Luis", "Marta"]

for indice, alumno in enumerate(alumnos):
    print(indice, alumno)
```

Salida:

```text
0 Ana
1 Luis
2 Marta
```

Podemos indicar otro valor inicial:

```python
for indice, alumno in enumerate(alumnos, 1):
    print(indice, alumno)
```

Ahora la numeración empieza en 1.

## `_` cuando no necesitamos la variable

Si queremos repetir una acción pero no utilizamos el valor del rango, es habitual escribir `_`:

```python
for _ in range(3):
    print("Repetir")
```

El guion bajo es una convención que indica que ese valor no nos interesa.

## `break` en un `for`

```python
for numero in range(1, 10):
    if numero == 5:
        break

    print(numero)
```

Salida:

```text
1
2
3
4
```

`break` termina completamente el bucle.

## `continue` en un `for`

```python
for numero in range(1, 6):
    if numero == 3:
        continue

    print(numero)
```

Salida:

```text
1
2
4
5
```

`continue` solo salta el resto de la iteración actual.

## `for` con `else`

Un `for` también puede tener `else`. El bloque `else` se ejecuta cuando el bucle termina normalmente, sin pasar por un `break`.

El ejemplo del temario busca divisores:

```python
numero = 7

for divisor in range(2, numero):
    if numero % divisor == 0:
        print("No es primo")
        break
else:
    print("Es primo")
```

Si se encuentra un divisor, `break` evita el `else`. Si se recorre todo el rango sin encontrarlo, se ejecuta `else`.

## Bucles anidados

Un bucle puede estar dentro de otro:

```python
for fila in range(1, 4):
    for columna in range(1, 4):
        print(f"Fila {fila}, columna {columna}")
```

El bucle interior se ejecuta completo por cada iteración del exterior. Hay que utilizarlos con cuidado porque el número de iteraciones se multiplica.

## Ejemplo aplicado a administración

```python
archivos = ["log1.txt", "foto.png", "log2.txt", "datos.csv"]

for archivo in archivos:
    if archivo.endswith(".txt"):
        print(f"Procesar {archivo}")
```

Este patrón será habitual: **recorrer elementos, comprobar una condición y actuar**.

## `for` o `while`

Como regla práctica basada en estos temas:

- `for`: quieres recorrer un conjunto de elementos o un rango.
- `while`: quieres repetir mientras se cumpla una condición y no necesariamente sabes cuántas iteraciones habrá.

## Comprueba que sabes...

- Recorrer cadenas y listas con `for`.
- Utilizar `range(fin)`.
- Utilizar `range(inicio, fin)`.
- Utilizar `range(inicio, fin, paso)`.
- Contar hacia atrás con un paso negativo.
- Saber que `range()` no devuelve directamente una lista.
- Utilizar `enumerate()` para obtener índice y valor.
- Reconocer el uso convencional de `_`.
- Utilizar `break` y `continue`.
- Entender el `else` asociado a un `for`.
- Leer bucles anidados.
- Aplicar un `for` para recorrer nombres de archivos.

!!! success "Para el examen"
    En `range(inicio, fin, paso)`, **fin nunca se incluye**. Antes de responder, escribe a mano los primeros valores que produciría el rango.

---

Fuente principal: material de clase **Introducción a Python 3.3 · Bucles for, range() y recorridos**.