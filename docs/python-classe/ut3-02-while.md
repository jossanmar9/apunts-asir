# UT3 · 3.2 Bucles `while`

## Repetir mientras se cumpla una condición

Un bucle permite repetir instrucciones. `while` repite un bloque mientras su condición sea verdadera y resulta útil cuando no sabemos de antemano cuántas repeticiones serán necesarias.

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

Cada repetición se denomina **iteración**.

## Cómo funciona

En cada vuelta Python evalúa la condición:

1. Si es `True`, ejecuta el bloque.
2. Al terminar, vuelve a comprobar la condición.
3. Cuando es `False`, sale del bucle.

Por eso debemos asegurarnos de que algo pueda hacer que la condición deje de cumplirse.

## Repetir una entrada de usuario

```python
clave = ""

while clave != "python":
    clave = input("Contraseña: ")

print("Acceso concedido")
```

Este patrón permite repetir una pregunta hasta recibir el dato esperado.

## Bucles infinitos

Este bucle nunca termina:

```python
contador = 1

while contador <= 5:
    print(contador)
```

Falta modificar `contador`, así que siempre vale 1.

También podemos utilizar voluntariamente `while True`, pero debe existir una forma de salir:

```python
while True:
    comando = input("Comando: ")

    if comando == "salir":
        break

    print(f"Ejecutando {comando}")
```

## `break`

`break` termina inmediatamente el bucle.

```python
while True:
    texto = input("Escribe algo: ")

    if texto == "fin":
        break

    print(texto)
```

Cuando el usuario escribe `fin`, la ejecución continúa después del bucle.

## `continue`

`continue` salta directamente a la siguiente iteración.

```python
numero = 0

while numero < 5:
    numero += 1

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

Cuando `numero` vale 3 no se llega al `print()` de esa iteración.

!!! warning "Cuidado con `continue`"
    Antes de ejecutar `continue`, asegúrate de que las variables que controlan el bucle se actualizan. De lo contrario puedes crear un bucle infinito.

## `while` con `else`

Python permite asociar un `else` a un `while`.

```python
contador = 1

while contador <= 3:
    print(contador)
    contador += 1
else:
    print("Bucle terminado sin break")
```

El `else` se ejecuta cuando el bucle termina de forma normal porque la condición pasa a ser falsa. Si termina mediante `break`, el `else` no se ejecuta.

```python
contador = 1

while contador <= 3:
    if contador == 2:
        break

    print(contador)
    contador += 1
else:
    print("No se ejecuta")
```

## Validar una entrada

Podemos combinar `while` con métodos de cadenas:

```python
edad = input("Edad: ")

while not edad.isdigit():
    print("Debes escribir un número")
    edad = input("Edad: ")

edad = int(edad)
print(f"Edad registrada: {edad}")
```

Primero mantenemos el dato como cadena para comprobarlo. Cuando cumple la condición esperada, lo convertimos a entero.

## Ejemplo paso a paso

Queremos pedir un número positivo hasta que el usuario escriba uno válido.

```python
numero = int(input("Número positivo: "))

while numero <= 0:
    print("El número debe ser mayor que cero")
    numero = int(input("Número positivo: "))

print(f"Número aceptado: {numero}")
```

La variable se vuelve a actualizar dentro del bucle. Si olvidáramos la segunda lectura, una entrada negativa produciría un bucle infinito.

## Cuándo pensar en `while`

Utiliza `while` cuando la repetición depende principalmente de una **condición** y no conoces necesariamente de antemano el número de iteraciones. Ejemplos del temario son repetir una contraseña o validar una entrada.

## Comprueba que sabes...

- Explicar qué es una iteración.
- Utilizar `while` con una condición.
- Actualizar correctamente la variable que controla el bucle.
- Detectar un posible bucle infinito.
- Utilizar `break`.
- Utilizar `continue`.
- Entender cuándo se ejecuta el `else` de un `while`.
- Validar una entrada de usuario mediante `while`.

!!! success "Para el examen"
    Antes de ejecutar mentalmente un `while`, localiza tres cosas: **valor inicial**, **condición** y **actualización**.

---

Fuente principal: material de clase **Introducción a Python 3.2 · Bucles while**.