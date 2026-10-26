# UT3 · 2. Leer errores y depurar con método

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Excepción** | Evento que interrumpe el flujo normal de ejecución y puede ser tratado por un manejador. |
| **Traza de llamadas** | Secuencia de puntos de ejecución que ayuda a localizar dónde se produjo una excepción. |
| **Error lógico** | Resultado incorrecto aunque el programa no produzca ninguna excepción. |

## Tres problemas diferentes

Un error de **sintaxis** impide interpretar el programa. Una excepción **durante la ejecución** aparece cuando una operación no se puede completar. Un error **lógico** produce una respuesta equivocada sin que Python lo detecte.

| Ejemplo | Tipo de problema |
| --- | --- |
| `if pendiente > 0` sin `:` | Sintaxis |
| `int("cuatro")` | Excepción `ValueError` |
| Multiplicar por unidades equivocadas | Lógica |

## Caso resuelto: un recuento que parece funcionar

**Objetivo propio:** saber cuántos sobres hacen falta para 19 tarjetas, con 6 tarjetas por sobre. El código inicial utiliza `sobres = 19 // 6` y muestra 3.

1. Calcula manualmente: tres sobres guardan 18 tarjetas y queda una fuera.
2. Inspecciona `tarjetas`, `capacidad` y el resto con un breakpoint o impresiones.
3. El problema es el redondeo: la división entera cuenta solo sobres completos.
4. Para estos enteros positivos, utiliza `(tarjetas + capacidad - 1) // capacidad`.
5. Comprueba también 0, 6, 7 y 18 tarjetas.

```python
tarjetas = 19
capacidad = 6
sobres = (tarjetas + capacidad - 1) // capacidad
print(f"{tarjetas=}, {capacidad=}, {sobres=}")
```

**Resultado:** `tarjetas=19, capacidad=6, sobres=4`. No había un mensaje de error que leer: has necesitado contrastar la respuesta con el significado del problema.

## Leer una traza de llamadas

Mira la última línea para reconocer el tipo y el mensaje; después localiza la línea de tu archivo indicada justo antes. Si hay varias llamadas, sigue cómo se ha llegado a la operación que falla.

- `NameError`: nombre ausente o mal escrito.
- `TypeError`: operación incompatible con los tipos.
- `ValueError`: tipo de entrada esperado, pero contenido no convertible o inadmisible.
- `IndexError`: posición fuera de la secuencia.
- `FileNotFoundError`: ruta que no se puede encontrar.

## Excepciones: reconocer las herramientas

La teoría las presenta como ampliación; no son necesarias para resolver todos los ejercicios de iniciación. Ejemplo didáctico separado:

```python
texto = "muchas"
try:
    piezas = int(texto)
except ValueError:
    print("No se puede interpretar como un entero")
else:
    print(f"Piezas leídas: {piezas}")
```

**Resultado:** se ejecuta `except`, porque `int` falla. Captura el error concreto que esperas, no cualquier excepción para continuar sin saber qué ha ocurrido. El `else` se ejecutaría si la conversión terminara sin excepción.

`raise ValueError("capacidad incorrecta")` lanza una excepción. `assert condicion` comprueba una hipótesis interna durante el desarrollo; no debe ser la única validación de entrada de un programa, porque las aserciones se pueden desactivar.

## Guía mientras trabajas

Reproduce el caso pequeño que falla, anota qué esperabas y observa los valores antes de la línea. Cambia una causa concreta y repite el caso original y los límites. En VS Code, una variable que todavía no aparece puede simplemente no haberse asignado en el punto donde estás detenido.

## Capturar solo lo que sabes tratar

Una validación que repite la lectura puede separar conversión y regla del problema:

```python
while True:
    texto = input("Piezas de 1 a 9: ")
    try:
        piezas = int(texto)
    except ValueError:
        print("Escribe un entero")
        continue
    if 1 <= piezas <= 9:
        break
    print("El valor está fuera del rango")
print(f"Piezas aceptadas: {piezas}")
```

Con las entradas `muchas`, `0` y `4`, aparecen el aviso de conversión, el aviso de rango y finalmente `Piezas aceptadas: 4`. `continue` vuelve a pedir después de la conversión fallida. No captures cualquier error con `except:`: podrías esconder un fallo de programación o impedir una interrupción que el usuario pretendía realizar.

Este patrón amplía la explicación de excepciones de la teoría; si una actividad todavía no permite utilizarlas, sigue su método de validación indicado.

!!! success "Para repasar"
    Que el programa termine sin excepciones no demuestra que sea correcto. Necesitas datos de prueba con un resultado que puedas justificar.

---

Fuentes del temario: [04-depuracion-excepciones](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/04-depuracion-excepciones/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
