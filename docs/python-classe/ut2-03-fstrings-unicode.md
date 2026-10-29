# UT2 · 2.3 F-strings, formato y Unicode

## F-strings

Las f-strings permiten construir cadenas introduciendo variables o expresiones directamente dentro del texto.

```python
nombre = "Ana"
edad = 20

print(f"{nombre} tiene {edad} años")
```

La `f` antes de las comillas activa el formato y las expresiones se escriben entre `{}`.

Si olvidas la `f`:

```python
print("{nombre} tiene {edad} años")
```

se mostrarán las llaves y los nombres literalmente.

## Podemos incluir expresiones

```python
a = 5
b = 3
print(f"La suma es {a + b}")
```

Resultado:

```text
La suma es 8
```

Conviene mantener los cálculos importantes en variables cuando eso hace el programa más fácil de leer.

```python
precio = 50
iva = precio * 0.21
precio_final = precio + iva

print(f"Precio final: {precio_final} €")
```

## Formatear decimales

```python
precio = 19.995
print(f"Precio final: {precio:.2f} €")
```

Resultado:

```text
Precio final: 20.00 €
```

`.2f` indica que queremos mostrar dos decimales.

!!! important "Formatear no modifica el valor"
    La variable `precio` sigue conteniendo su valor original. El formato afecta a cómo se representa dentro de esa cadena.

```python
numero = 3.14159265
print(f"{numero:.3f}")
print(numero)
```

La primera línea muestra `3.142`; la segunda sigue mostrando el valor original.

## Formatear enteros

Podemos reservar una anchura y completar con ceros.

```python
codigo = 7
print(f"{codigo:03d}")
```

Resultado:

```text
007
```

`03d` significa, para este ejemplo, entero decimal con una anchura mínima de tres posiciones y ceros de relleno.

## Porcentajes

```python
completado = 0.375
print(f"Progreso: {completado:.1%}")
```

Resultado:

```text
Progreso: 37.5%
```

El formato `%` ya transforma la fracción para mostrarla como porcentaje. No multipliques previamente por 100 si vas a utilizar este formato.

## Alineación

Las f-strings permiten alinear campos.

```python
print(f"{'Nombre':<10}{'Nota':>6}")
print(f"{'Ana':<10}{8:>6}")
print(f"{'Luis':<10}{10:>6}")
```

- `<` alinea a la izquierda.
- `>` alinea a la derecha.
- `^` centra.

El número indica una anchura mínima.

```python
print(f"{'ASIR':^10}")
```

La alineación sirve para presentar información. No cambia los datos originales.

## Mostrar el nombre de una variable al depurar

```python
usuarios = 12
print(f"{usuarios=}")
```

Resultado:

```text
usuarios=12
```

Puede ser útil mientras investigas el valor de una variable.

## Mostrar llaves literalmente

Dentro de una f-string, las llaves tienen un significado especial. Para mostrar una llave literal utilizamos dos:

```python
valor = 10
print(f"Valor: {{{valor}}}")
```

Resultado:

```text
Valor: {10}
```

## Unicode

Python 3 utiliza Unicode para representar texto. Esto permite trabajar directamente con caracteres de muchos idiomas.

```python
texto = "València · España · 中文 · Ω"
print(texto)
```

No necesitamos tratar las letras acentuadas como un tipo especial de cadena.

## `ord()` y `chr()`

`ord()` devuelve el punto de código de un carácter:

```python
print(ord("A"))
```

`chr()` realiza la operación inversa:

```python
print(chr(65))
```

Resultado:

```text
A
```

Otro ejemplo:

```python
print(ord("Ω"))
print(chr(937))
```

## Comparación de cadenas

Las cadenas distinguen mayúsculas y minúsculas.

```python
print("Python" == "python")  # False
```

Si la regla de nuestro programa permite ignorar mayúsculas y espacios exteriores, podemos normalizar antes de comparar:

```python
respuesta = "  SI  "
respuesta = respuesta.strip().lower()
print(respuesta == "si")
```

Resultado:

```text
True
```

Normalizar no significa eliminar cualquier diferencia. Solo debemos transformar aquello que la regla del problema permita ignorar.

## Unicode y orden de texto

Las comparaciones entre cadenas no equivalen necesariamente al orden alfabético que utilizaría una persona en un idioma concreto.

```python
print("Z" < "a")
```

Python compara las secuencias de caracteres según su representación. Para este nivel es suficiente entender que mayúsculas, minúsculas y otros caracteres pueden producir resultados que no coincidan con una ordenación lingüística intuitiva.

## Ejemplo explicado: ficha de producto

```python
codigo = 8
producto = "disco SSD"
precio = 59.9
stock = 0.75

print(f"Código: P-{codigo:03d}")
print(f"Producto: {producto}")
print(f"Precio: {precio:.2f} €")
print(f"Stock objetivo: {stock:.0%}")
```

Resultado:

```text
Código: P-008
Producto: disco SSD
Precio: 59.90 €
Stock objetivo: 75%
```

Cada variable conserva su tipo. La f-string solo construye la representación final.

## Ejemplo explicado: tabla sencilla

```python
nombre1 = "Nginx"
puerto1 = 80
nombre2 = "MariaDB"
puerto2 = 3306

print(f"{'Servicio':<12}{'Puerto':>8}")
print(f"{nombre1:<12}{puerto1:>8d}")
print(f"{nombre2:<12}{puerto2:>8d}")
```

El formato hace que las columnas sean más fáciles de leer. No es necesario convertir previamente los puertos a cadenas.

## Errores frecuentes

### Olvidar la `f`

```python
nombre = "Ana"
print("Hola {nombre}")
```

Muestra las llaves literalmente.

### Aplicar un formato incompatible

```python
numero = "12"
# print(f"{numero:03d}")
```

`numero` es una cadena, no un entero. Comprueba el tipo y convierte solo cuando tenga sentido.

### Confundir formato con cálculo

```python
precio = 3.14159
print(f"{precio:.2f}")
```

Esto no reasigna `precio` ni modifica permanentemente su precisión.

### Multiplicar dos veces un porcentaje

```python
fraccion = 0.25
print(f"{fraccion:.0%}")  # 25%
```

No necesitas hacer `fraccion * 100` antes.

## Comprueba que sabes...

- Crear una f-string.
- Introducir variables y expresiones entre llaves.
- Formatear un `float` con dos o tres decimales.
- Formatear un entero con ceros iniciales.
- Mostrar una fracción como porcentaje.
- Alinear texto e enteros.
- Explicar que el formato no cambia el valor original.
- Mostrar llaves literales.
- Entender que Python 3 trabaja con Unicode.
- Utilizar `ord()` y `chr()`.
- Reconocer que las comparaciones distinguen mayúsculas y minúsculas.
- Normalizar una entrada con `strip().lower()` cuando la regla del problema lo permita.

!!! success "Para el examen"
    Separa siempre **valor** y **presentación**: calcula con números y aplica el formato cuando vayas a mostrarlos. Recuerda especialmente `:.2f`, `:03d`, `:.1%` y las alineaciones `<`, `>` y `^`.

---

Fuente principal: material de clase **Introducción a Python 2.3**, consultado el 29/10/2026.