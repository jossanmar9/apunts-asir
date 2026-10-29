# UT1 · 1.4 Números, booleanos y operadores

## Booleanos

Un booleano solo puede tener dos valores:

```python
True
False
```

Se escriben con la primera letra en mayúscula.

```python
activo = True
```

Esto es incorrecto:

```python
activo = true
```

Los booleanos representan condiciones: activo/inactivo, existe/no existe, aprobado/no aprobado.

En operaciones numéricas Python trata `True` como 1 y `False` como 0:

```python
print(True + 3)   # 4
print(False + 3)  # 3
```

No es una técnica que necesitemos utilizar habitualmente, pero ayuda a entender el tipo `bool`.

## Enteros: `int`

```python
edad = 20
saldo = -50
```

Los guiones bajos pueden mejorar la lectura de números grandes:

```python
poblacion = 47_000_000
```

No se puede escribir un entero decimal con un cero inicial:

```python
numero = 08  # Error de sintaxis
```

## Bases numéricas

```python
binario = 0b1010   # 10
octal = 0o12       # 10
hexadecimal = 0xA  # 10
```

Los prefijos indican cómo está escrito el número; el valor sigue siendo numérico.

## Flotantes: `float`

```python
precio = 19.99
temperatura = -3.5
```

También existe notación científica:

```python
valor = 0.4e1
print(valor)  # 4.0
```

Si mezclamos un entero y un flotante, el resultado suele ser flotante:

```python
resultado = 3 + 2.5
print(resultado)       # 5.5
print(type(resultado)) # <class 'float'>
```

## Operadores aritméticos

| Operador | Significado | Ejemplo | Resultado |
| --- | --- | --- | --- |
| `+` | suma | `3 + 2` | `5` |
| `-` | resta | `3 - 2` | `1` |
| `*` | multiplicación | `3 * 2` | `6` |
| `/` | división real | `9 / 2` | `4.5` |
| `//` | división entera | `9 // 2` | `4` |
| `%` | resto | `9 % 4` | `1` |
| `**` | potencia | `2 ** 3` | `8` |

### Cociente y resto

```python
minutos_totales = 1000
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(horas, minutos)  # 16 40
```

`//` obtiene grupos completos y `%` lo que sobra.

### Potencias y raíces

```python
cateto1 = 3
cateto2 = 4
hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
print(hipotenusa)  # 5.0
```

También podemos utilizar exponentes fraccionarios:

```python
numero = 27
raiz_cubica = numero ** (1 / 3)
print(raiz_cubica)  # 3.0
```

## División por cero

```python
print(10 / 0)
```

Produce `ZeroDivisionError`.

## Prioridad de operadores

Los paréntesis permiten indicar claramente qué debe calcularse primero.

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

De forma simplificada para este nivel:

1. paréntesis;
2. potencia `**`;
3. multiplicación, divisiones y resto;
4. suma y resta.

Si tienes dudas, utiliza paréntesis para hacer explícita tu intención.

## Asignación aumentada

```python
x = x + 3
```

Puede escribirse:

```python
x += 3
```

También existen:

```python
x -= 1
x *= 2
x /= 4
x //= 2
x %= 3
```

## Funciones numéricas útiles

```python
print(abs(-7))          # 7
print(round(3.1416, 2)) # 3.14
print(int(3.9))         # 3
print(float("3.5"))     # 3.5
```

!!! warning "`int()` no redondea"
    `int(3.9)` devuelve `3`. Para redondear utilizamos `round()`.

## Comparaciones

Las comparaciones producen booleanos:

```python
edad = 18
print(edad >= 18)  # True
print(edad < 18)   # False
```

| Operador | Significado |
| --- | --- |
| `==` | igual |
| `!=` | distinto |
| `<` | menor |
| `<=` | menor o igual |
| `>` | mayor |
| `>=` | mayor o igual |

No confundas asignación y comparación:

```python
edad = 18   # asigna
edad == 18  # compara
```

## Ejemplo explicado

Queremos saber cuántas cajas completas podemos llenar con 29 piezas si caben 8 por caja y cuántas sobran.

```python
piezas = 29
capacidad = 8

cajas_completas = piezas // capacidad
sobrantes = piezas % capacidad

print(cajas_completas)
print(sobrantes)
```

Resultado:

```text
3
5
```

## Comprueba que sabes...

- Utilizar `True` y `False` correctamente.
- Reconocer `int` y `float`.
- Leer números binarios, octales y hexadecimales sencillos.
- Utilizar `+`, `-`, `*`, `/`, `//`, `%` y `**`.
- Explicar la diferencia entre `/` y `//`.
- Utilizar cociente y resto en un problema.
- Entender la prioridad de operadores.
- Entender `x += 3`.
- Utilizar `abs()`, `round()`, `int()` y `float()`.
- Reconocer una división por cero.
- Diferenciar `=` de `==`.
- Utilizar operadores de comparación.

!!! success "Para el examen"
    `//` y `%` aparecen mucho en ejercicios: piensa en **grupos completos** y **lo que sobra**.

---

Fuente principal: material de clase **Introducción a Python 1.4 · Números, booleanos y operadores**, consultado el 29/10/2026.