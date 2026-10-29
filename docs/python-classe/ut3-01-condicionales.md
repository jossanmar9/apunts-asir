# UT3 · 3.1 Condicionales: tomar decisiones

## Tomar decisiones en un programa

Hasta ahora muchas instrucciones se ejecutaban de arriba abajo. Los condicionales permiten decidir qué bloque se ejecuta según una condición.

```python
edad = int(input("Edad: "))

if edad >= 18:
    print("Puedes acceder")
```

La expresión `edad >= 18` produce `True` o `False`. El bloque indentado solo se ejecuta cuando es verdadera.

## La indentación es obligatoria

Python no utiliza llaves para delimitar bloques. La indentación forma parte de la sintaxis. La convención habitual es utilizar cuatro espacios.

```python
if edad >= 18:
    print("Mayor de edad")
    print("Acceso permitido")
```

## `if`, `else` y `elif`

`else` se ejecuta cuando la condición del `if` no se cumple.

```python
if edad >= 18:
    print("Puedes acceder")
else:
    print("No puedes acceder")
```

Cuando hay varias posibilidades utilizamos `elif`:

```python
nota = float(input("Nota: "))

if nota < 5:
    print("Suspenso")
elif nota < 7:
    print("Aprobado")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
```

Python evalúa las condiciones en orden. Cuando una se cumple, ejecuta ese bloque y no evalúa los siguientes bloques de la cadena.

## Operadores lógicos

Podemos combinar condiciones con `and`, `or` y `not`.

| Operador | Significado |
| --- | --- |
| `and` | deben cumplirse ambas condiciones |
| `or` | basta con que se cumpla una |
| `not` | niega una condición |

```python
edad = 20
tiene_entrada = True

if edad >= 18 and tiene_entrada:
    print("Puede entrar")
```

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("Fin de semana")
```

```python
es_laboral = False

if not es_laboral:
    print("Fin de semana")
```

## Evaluación en cortocircuito

Con `and`, si la primera condición es `False`, Python no necesita evaluar la segunda. Con `or`, si la primera ya es `True`, tampoco necesita evaluar la segunda.

```python
x = 0

if x != 0 and 10 / x > 2:
    print("Se cumple")
```

La división no llega a evaluarse cuando `x` vale cero.

## Paréntesis

No son obligatorios alrededor de la condición:

```python
if edad >= 18:
    print("OK")
```

Pueden mejorar la claridad en condiciones largas:

```python
if (edad >= 18 and tiene_entrada) or es_admin:
    print("Acceso permitido")
```

## Asignación condicional

Python permite una asignación condicional sencilla:

```python
resultado = "apto" if nota >= 5 else "no apto"
```

Equivale a un `if`/`else` que asigna uno de los dos valores. No conviene utilizar esta forma si hace el código difícil de leer.

## Valores verdaderos y falsos

Algunos valores se comportan como falsos dentro de una condición, entre ellos:

```python
""
0
[]
None
```

Por ejemplo:

```python
nombre = input("Nombre: ").strip()

if nombre:
    print(f"Hola, {nombre}")
else:
    print("No has escrito nada")
```

## Ejemplo aplicado a sistemas

```python
espacio_libre_gb = 3

if espacio_libre_gb < 5:
    print("Aviso: queda poco espacio libre")
else:
    print("Espacio suficiente")
```

Más adelante podremos obtener datos reales del sistema mediante librerías; la estructura de decisión será la misma.

## Errores frecuentes

No confundas asignación y comparación:

```python
edad = 18     # asignación
edad == 18    # comparación
```

Un `if` necesita `:` al final:

```python
if edad >= 18:
    print("OK")
```

Y el bloque debe estar correctamente indentado.

## Comprueba que sabes...

- Utilizar `if`, `elif` y `else`.
- Entender que los bloques se definen por indentación.
- Utilizar `and`, `or` y `not`.
- Explicar la evaluación en cortocircuito.
- Diferenciar `=` de `==`.
- Escribir una asignación condicional sencilla.
- Saber que los paréntesis no son obligatorios en un `if`.
- Reconocer valores vacíos que se comportan como falsos.

!!! success "Para el examen"
    Lee una cadena de `if`/`elif` de arriba abajo: **se ejecuta el primer bloque cuya condición sea verdadera**.

---

Fuente principal: material de clase **Introducción a Python 3.1 · Condicionales**.