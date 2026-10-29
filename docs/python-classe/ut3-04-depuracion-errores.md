# UT3 · 3.4 Depuración, errores y excepciones

## Equivocarse forma parte de programar

Programar implica cometer errores. Lo importante es aprender a localizarlos, entender el mensaje que ofrece Python y corregirlos de forma ordenada.

## Tipos de errores

### Errores de sintaxis

El código no respeta las reglas del lenguaje.

```python
if edad >= 18
    print("OK")
```

Faltan los dos puntos y Python no puede ejecutar correctamente el programa.

### Errores en tiempo de ejecución

El programa comienza a ejecutarse, pero falla durante la ejecución.

```python
numero = int("abc")
```

Produce `ValueError` porque `"abc"` no puede convertirse a entero.

Otros errores que puedes encontrarte al practicar son `ZeroDivisionError`, `IndexError` o `NameError`.

### Errores lógicos

El programa se ejecuta sin lanzar una excepción, pero el resultado no es el esperado.

```python
precio = 100
iva = 21
precio_final = precio + iva
```

Python puede ejecutar esas instrucciones, pero la fórmula puede no representar el cálculo que pretendíamos realizar.

Los errores lógicos requieren revisar la lógica del programa porque Python no puede saber cuál era nuestra intención.

## Leer una traza

Cuando Python falla, la traza contiene pistas. Fíjate especialmente en:

- el tipo de error;
- la línea indicada;
- la última llamada de la traza;
- el mensaje final.

Ejemplo:

```text
ValueError: invalid literal for int() with base 10: 'abc'
```

La pista principal es que se ha intentado convertir `abc` a entero.

!!! tip "No empieces cambiando código al azar"
    Primero identifica el tipo de error y la línea. Después revisa los valores que llegan a esa instrucción.

## Probar poco a poco

El material recomienda no escribir muchas líneas antes de probar. Podemos inspeccionar valores temporalmente:

```python
edad = input("Edad: ")
print(f"DEBUG: {edad=}")
```

La sintaxis `{edad=}` permite ver el nombre de la variable y su valor.

## Excepciones

Una excepción es un evento anómalo durante la ejecución que interrumpe el flujo normal, por ejemplo una conversión inválida, una división por cero o un acceso incorrecto.

El temario presenta las herramientas de manejo de excepciones para que sepamos que existen, aunque indica que no se utilizarán en profundidad en este módulo por considerarlas programación más avanzada.

## `try` y `except`

Podemos capturar un error previsible:

```python
texto = input("Número: ")

try:
    numero = int(texto)
    print(numero * 2)
except ValueError:
    print("Debes escribir un número entero")
```

No debemos utilizar `try`/`except` simplemente para ocultar errores que no entendemos. Primero hay que comprender qué operación puede fallar.

## `raise`

`raise` permite lanzar explícitamente una excepción cuando detectamos una situación que consideramos inválida.

```python
edad = -5

if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

## `assert`

`assert` permite comprobar una condición durante el desarrollo.

```python
edad = 20
assert edad >= 0
```

Podemos añadir un mensaje:

```python
edad = -1
assert edad >= 0, "La edad no puede ser negativa"
```

Si la condición es falsa, se produce `AssertionError`.

Según el temario, las aserciones son útiles para detectar errores internos mientras desarrollamos; no deben entenderse como el mecanismo habitual para validar siempre los datos introducidos por un usuario.

## Depuración en VS Code

VS Code permite utilizar puntos de interrupción y ejecutar el programa paso a paso. También podemos utilizar temporalmente mensajes de depuración:

```python
print(f"DEBUG: {variable=}")
```

El objetivo es observar qué valores tiene el programa antes de la línea donde aparece el comportamiento inesperado.

## Estrategia de depuración

El procedimiento propuesto en el material es:

1. Reproduce el error.
2. Lee la traza.
3. Localiza la línea.
4. Imprime o inspecciona variables.
5. Prueba con un caso pequeño.
6. Corrige y vuelve a probar.

## Ejemplo explicado

```python
texto = input("Edad: ")
print(f"DEBUG: {texto=}")
edad = int(texto)
print(edad + 1)
```

Si escribimos `abc`, la conversión falla. En lugar de modificar varias líneas a la vez:

1. observamos que el error es `ValueError`;
2. localizamos `int(texto)`;
3. comprobamos con el mensaje `DEBUG` que `texto` contiene `"abc"`;
4. entendemos que el problema está en la conversión del dato recibido.

## Comprueba que sabes...

- Diferenciar un error de sintaxis, uno de ejecución y uno lógico.
- Localizar el tipo de error al final de una traza.
- Utilizar mensajes sencillos de depuración.
- Explicar para qué sirven `try` y `except`.
- Reconocer un `except ValueError`.
- Explicar para qué sirve `raise`.
- Explicar para qué sirve `assert`.
- Seguir un procedimiento ordenado de depuración.

!!! success "Para el examen"
    Ante una traza, empieza por **el tipo de error y el mensaje final**. Después localiza la línea y comprueba los valores que estaba utilizando.

---

Fuente principal: material de clase **Introducción a Python 3.4 · Depuración, errores y excepciones**.