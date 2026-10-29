# UT3 · 3.4 Depuración, errores y excepciones

Programar implica equivocarse. Lo importante es aprender a localizar, entender y corregir los errores.

## Tipos de errores

### Errores de sintaxis

El código no respeta las reglas del lenguaje y Python no puede ejecutarlo.

```python
if edad >= 18
    print("OK")
```

Faltan los dos puntos.

### Errores en tiempo de ejecución

El programa comienza, pero falla mientras se ejecuta.

```python
numero = int("abc")
```

Produce `ValueError` porque `"abc"` no puede convertirse a entero.

### Errores lógicos

El programa se ejecuta, pero el resultado es incorrecto.

```python
precio = 100
iva = 21
precio_final = precio + iva
```

Python no puede saber si nuestra fórmula era la que realmente queríamos. Por eso los errores lógicos suelen ser más difíciles de detectar.

## Leer una traza de error

Cuando Python falla, debemos fijarnos especialmente en:

- el tipo de error;
- la línea indicada;
- la última llamada de la traza;
- el mensaje final.

Ejemplo:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

La pista principal es que se ha intentado convertir `abc` a entero.

## Probar con casos pequeños

Es mejor ejecutar y comprobar el programa poco a poco que escribir muchas líneas antes de hacer la primera prueba.

```python
edad = input("Edad: ")
print(f"DEBUG: {edad=}")
```

El modo `variable=` de las f-strings permite inspeccionar rápidamente un valor.

## Excepciones

Una excepción es un evento anómalo durante la ejecución que interrumpe el flujo normal, por ejemplo una conversión inválida, una división por cero o un acceso fuera de rango.

El material presenta `try`, `except`, `raise` y `assert` para que sepamos para qué sirven, aunque indica que el manejo de excepciones no se utilizará en este módulo por considerarse contenido avanzado.

## `try` y `except`

Permiten capturar determinados errores previsibles:

```python
texto = input("Número: ")

try:
    numero = int(texto)
    print(numero * 2)
except ValueError:
    print("Debes escribir un número entero")
```

!!! warning "No ocultes errores"
    No utilices `try/except` para tapar un error que no entiendes. Primero identifica qué puede fallar.

## `raise`

Permite lanzar una excepción de forma explícita:

```python
edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

## `assert`

Sirve para comprobar condiciones durante el desarrollo:

```python
edad = 20
assert edad >= 0
```

Podemos añadir un mensaje:

```python
edad = -1
assert edad >= 0, "La edad no puede ser negativa"
```

Si la condición es falsa, Python lanza `AssertionError`.

Las aserciones sirven para detectar errores internos durante el desarrollo, no como mecanismo general para validar datos de usuario en producción.

## Depuración paso a paso

En VS Code podemos utilizar puntos de interrupción para detener temporalmente el programa e inspeccionar su estado. Para programas pequeños también podemos mostrar valores de forma temporal:

```python
print(f"DEBUG: {variable=}")
```

## Estrategia de depuración

El material propone este proceso:

1. Reproduce el error.
2. Lee la traza.
3. Localiza la línea.
4. Imprime o inspecciona variables.
5. Prueba con un caso pequeño.
6. Corrige y vuelve a probar.

## Ejemplo explicado

```python
edad = input("Edad: ")
print(f"DEBUG: {edad=}")
numero = int(edad)
print(numero + 1)
```

Si escribimos `abc`, el programa llega a ejecutarse pero falla en `int(edad)`. La traza indicará un `ValueError`. El mensaje de depuración permite comprobar qué contenía realmente `edad` antes de la conversión.

## Comprueba que sabes...

- Diferenciar errores de sintaxis, ejecución y lógica.
- Localizar el tipo de error al final de una traza.
- Utilizar mensajes de depuración sencillos.
- Probar el programa con casos pequeños.
- Explicar para qué sirven `try` y `except` con `ValueError`.
- Explicar para qué sirve `raise`.
- Explicar para qué sirve `assert`.
- Seguir una estrategia ordenada para depurar.

!!! success "Para el examen"
    No empieces cambiando código al azar. **Lee primero el tipo de error, el mensaje y la línea indicada**.

---

Fuente principal: material de clase **Introducción a Python 3.4 · Depuración, errores y excepciones**.