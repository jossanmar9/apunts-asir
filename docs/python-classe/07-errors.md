# UT3 · 2. Leer errores y depurar con método

## Tres problemas diferentes

Un error de **sintaxis** impide interpretar el programa. Una excepción **durante la ejecución** aparece cuando una operación no se puede completar. Un error **lógico** produce una respuesta equivocada sin que Python lo detecte.

| Ejemplo | Tipo de problema |
| --- | --- |
| `if pendiente > 0` sin `:` | Sintaxis |
| `int("cuatro")` | Excepción `ValueError` |
| Multiplicar por unidades equivocadas | Lógica |

## Leer lo ocurrido sin empezar cambiando código

Cuando aparece una excepción, la última línea permite identificar su tipo y mensaje. Las líneas anteriores muestran el recorrido de llamadas y dónde falló. Busca la primera operación de tu programa que no pudo completar lo que esperaba hacer.

`ValueError` en una conversión indica que el texto no representaba el valor esperado. `TypeError` apunta a una operación incompatible con los tipos. `NameError` puede ser simplemente un nombre mal escrito. No uses la misma corrección para errores que responden a preguntas diferentes.

Si el programa termina sin excepciones, todavía puede calcular mal. En ese caso compara con un resultado sencillo que puedas obtener a mano y localiza el primer valor que se desvía de tu previsión.

## Cómo recorre Python un `try/except`

El bloque `try` contiene la operación que puede fallar. Si termina correctamente, se omiten los manejadores `except`. Si aparece una excepción reconocida por uno de ellos, se abandona el resto del `try` y se ejecuta ese manejador.

No vuelve automáticamente a la línea que falló ni completa las asignaciones pendientes. Si una conversión no ha creado una variable, no puedes usarla después como si contuviera un número válido. Para volver a preguntar necesitas una repetición explícita o terminar ese camino.

```python
texto = "cuatro"
try:
    cantidad = int(texto)
except ValueError:
    print("No se ha obtenido una cantidad")
else:
    print(f"Cantidad válida: {cantidad}")
print("Comprobación terminada")
```

La salida es `No se ha obtenido una cantidad` y `Comprobación terminada`. No se muestra `Cantidad válida`, porque la conversión falló. El `else` se utiliza aquí para el código que solo debe ejecutarse después de un `try` correcto.

## Elegir qué errores tiene sentido tratar

Captura una excepción cuando sabes qué alternativa ofrecer: pedir de nuevo un número, avisar de un archivo ausente o terminar con un mensaje concreto. Capturar cualquier cosa y seguir como si nada puede esconder un error de programación.

Un error que esperas no significa que el dato sea válido después de capturarlo. La alternativa debe mantener un estado coherente: o consigues otro dato, o no realizas la operación. Esto es especialmente importante en cálculos donde una variable sin preparar acabaría produciendo otra excepción más confusa.

`finally` permite ejecutar una acción al salir del bloque, haya o no error, dentro del flujo normal del lenguaje. Para archivos, `with` suele expresar con más claridad la necesidad de cerrarlos. No necesitas añadir `finally` a todos los ejemplos solo porque exista.

## Puntos de interrupción y seguimiento de valores

Pon una pausa antes de la línea que sospechas y observa sus entradas. Si el resultado de una resta es incorrecto, comprueba los operandos antes de cambiar la resta. Si el problema está en la lectura, corregir el cálculo no recuperará el dato original.

Al avanzar, identifica qué línea se ha ejecutado y cuál está pendiente. Un nombre ausente antes de su asignación no es una prueba de que el depurador funcione mal. La observación debe relacionarse con el orden real del programa.

## Comprobar la corrección, no solo que desaparezca el mensaje

Después de corregir, repite el caso original y otro que antes funcionaba. Añade los límites si has tocado condiciones. Una corrección que evita una excepción devolviendo siempre cero puede ocultar el fallo y producir resultados incorrectos.

Guarda el motivo de la corrección en tus notas: qué entrada causaba el problema, qué regla faltaba y qué comportamiento tiene ahora. Esa explicación te servirá al enfrentarte a un ejercicio parecido sin repetir el mismo error.

## Problema explicado paso a paso: un recuento que parece funcionar

Saber cuántos sobres hacen falta para 19 tarjetas, con 6 tarjetas por sobre. El código inicial utiliza `sobres = 19 // 6` y muestra 3.

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

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Corrige un nombre incoherente

El programa asigna `paginas = 8` y después intenta `print(pagina + 1)`. Identifica el tipo de error que cabe esperar, corrige la línea y explica por qué no hace falta envolverla en un `try/except`.

??? tip "Pista"
    Comprueba qué nombres existen realmente antes de la impresión.

??? success "Solución paso a paso"
    ```python
    paginas = 8
    print(paginas + 1)
    ```

    La salida correcta es 9. El nombre `pagina` no se había definido y provocaría `NameError`. Es un error de escritura del programa: corregirlo es mejor que ocultarlo capturando una excepción.

### 2. Separa un error de conversión de uno de rango

Lee un entero para un turno de 1 a 4. Si no puede convertirse, muestra `Escribe un entero`. Si se convierte pero queda fuera del rango, muestra `Turno fuera de rango`. Para uno válido, muestra `Turno aceptado`. Basta una lectura, sin repetir.

??? tip "Pista"
    Captura `ValueError` de la conversión y utiliza `else` para las comprobaciones posteriores.

??? success "Solución paso a paso"
    ```python
    texto = input("Turno: ")
    try:
        turno = int(texto)
    except ValueError:
        print("Escribe un entero")
    else:
        if 1 <= turno <= 4:
            print("Turno aceptado")
        else:
            print("Turno fuera de rango")
    ```

    `dos` toma el camino de conversión fallida; `5` se convierte y falla el rango; `3` se acepta. El rango no se evalúa con una variable que no haya podido obtenerse.

### 3. Repara un acumulador que se reinicia

Quieres sumar `[2, 4, 3]`, pero tu programa pone `total = 0` dentro del `for`, justo antes de añadir cada elemento. Predice qué obtiene al final y corrígelo. Explica por qué no aparece necesariamente una excepción.

??? tip "Pista"
    El total debe conservar lo anterior entre vueltas, no volver a cero cada vez.

??? success "Solución paso a paso"
    ```python
    cantidades = [2, 4, 3]
    total = 0
    for cantidad in cantidades:
        total += cantidad
    print(total)
    ```

    El programa defectuoso termina con 3, porque borra el progreso en cada vuelta. El corregido muestra 9. Es un error lógico: las instrucciones son válidas, pero la inicialización estaba en un lugar que no respondía al objetivo.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Excepción** | Evento que interrumpe el flujo normal de ejecución y puede ser tratado por un manejador. |
| **Traza de llamadas** | Secuencia de puntos de ejecución que ayuda a localizar dónde se produjo una excepción. |
| **Error lógico** | Resultado incorrecto aunque el programa no produzca ninguna excepción. |

!!! success "Para repasar"
    Que el programa termine sin excepciones no demuestra que sea correcto. Necesitas datos de prueba con un resultado que puedas justificar.

---

Fuentes del temario: [04-depuracion-excepciones](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/04-depuracion-excepciones/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
