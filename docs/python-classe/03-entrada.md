# UT1 · 3. Leer datos y mostrar resultados

## `input()` siempre devuelve texto

Si el usuario escribe `12`, `input()` devuelve `"12"`. Para calcular debes convertirlo con `int()` o `float()`. Convertir no es lo mismo que validar todas las reglas del problema: un entero negativo sigue siendo un entero, pero puede ser inadmisible como cantidad de muestras.

`print()` puede separar argumentos con `sep` y elegir el final con `end`. Las f-strings insertan expresiones entre llaves. Un `\n` representa un salto de línea y `\t` una tabulación. Las comillas triples permiten escribir texto de varias líneas.

## Separar la pregunta, la respuesta y el cálculo

`input("Horas: ")` muestra una indicación, espera una línea y devuelve lo escrito como texto. El mensaje entre comillas no se incorpora al dato. Si escribes 2.5, la variable recibe una cadena con esos caracteres, no una operación ni una medida con unidad.

Después debes decidir qué representación necesita el programa. Si vas a multiplicar horas por consumo por hora, conviertes a `float`. Si necesitas contar unidades completas, puede corresponder `int`. La conversión debe depender de la pregunta del problema, no de usar siempre la misma función.

Leer y convertir en una sola línea es cómodo, pero al estudiar puedes separarlo para ver qué ocurre:

```python
texto = input("Longitud en metros: ")
longitud = float(texto)
centimetros = longitud * 100
print(f"Longitud: {centimetros:.1f} cm")
```

Si escribes `1.5`, la salida es `Longitud: 150.0 cm`. Primero existe el texto `"1.5"`; después el número 1.5; finalmente se calcula 150.0. No hay que aplicar la fórmula al texto inicial.

## Convertir no significa que el problema esté resuelto

`int("-3")` puede convertir una cadena a entero, pero tres unidades negativas no tienen por qué ser una cantidad admisible. Hay dos preguntas: «¿puedo interpretarlo como el tipo esperado?» y «¿cumple la regla del problema?».

En esta unidad se aprende el recorrido de los datos; en control de flujo se explica cómo repetir una pregunta o rechazar un valor. Mientras una demostración suponga entradas válidas, debe decirlo. No confundas una entrada de ejemplo con una garantía que el programa todavía no implementa.

Los decimales se escriben con punto en `float`. Sustituir una coma por un punto puede ser una decisión de interfaz para un formato sencillo, pero no valida cualquier formato numérico. No transformes a ciegas separadores de miles y decimales si no has definido qué acepta tu aplicación.

## Mostrar un resultado que puedas interpretar

Una salida debe identificar qué has calculado y en qué unidad. El número 150 sin explicación obliga al lector a adivinar si son metros, centímetros o una cantidad de objetos. Una f-string permite reunir nombre, valor y unidad sin convertir la variable de cálculo en texto permanentemente.

`:.1f` controla la presentación con un decimal. No modifica la cantidad guardada ni corrige un error de fórmula. Si la operación produjo metros y etiquetas el resultado como centímetros sin multiplicar por 100, el formato puede quedar bonito y el resultado seguir siendo incorrecto.

## Seguir la entrada a mano antes de ejecutar

Escribe una fila con lo que teclea el usuario y otra con el valor tras la conversión. Añade la operación y la salida esperada. Para el ejemplo de longitud, con entrada `2` esperas 200.0 cm; con `0.5`, 50.0 cm.

Escoge cantidades fáciles de calcular mentalmente. Después compara lo que esperabas con lo que muestra el programa. Esta costumbre permite distinguir un error de entrada, uno de conversión y uno de cálculo, en lugar de cambiar todas las líneas a la vez.

## Problema explicado paso a paso: consumo de una impresora 3D

Estimar cuántos metros de filamento consume una sesión según las horas y los metros por hora. Suponemos entradas positivas y decimales con punto; la validación se introduce en UT3.

```python
horas = float(input("Horas de trabajo: "))
metros_hora = float(input("Metros de filamento por hora: "))
consumo = horas * metros_hora
print(f"Filamento estimado: {consumo:.2f} m")
print("Unidad", "metros", sep=": ")
```

### Sigue la ejecución paso a paso

Escribe `2.5` y `1.2`.

1. Las dos entradas son inicialmente texto.
2. `float` las convierte a valores decimales.
3. `2.5 * 1.2` son 3.0 metros.
4. `:.2f` muestra dos cifras decimales: `Filamento estimado: 3.00 m`.
5. El segundo `print` muestra `Unidad: metros`.

Si escribes `dos`, la conversión produce `ValueError`. Si escribes `2,5`, también falla con este programa: el separador decimal que espera `float` es el punto. No anuncies que el programa acepta cualquier entrada si todavía no la validas.

## Otra prueba de tipos

```python
texto = "6"
print(texto * 3)       # 666
print(int(texto) * 3)  # 18
print(str(18) + " m")  # 18 m
```

La misma sintaxis `*` tiene significados diferentes según los tipos. `"6" + 3` falla porque no hay una concatenación automática de cadena y entero. Una f-string como `f"{3} m"` resuelve la presentación sin alterar el tipo de la variable original.

## Cómo estudiar un programa de entrada y salida

Haz una tabla con el texto introducido, el tipo después de la conversión, la fórmula y la salida. Después prueba un valor sencillo que puedas calcular mentalmente. Si un cálculo de consumo con cero horas devuelve una cantidad positiva, hay un error de lógica aunque Python no muestre ninguna excepción.

| Síntoma | Causa habitual |
| --- | --- |
| `TypeError` al sumar | Se están mezclando texto y números. |
| Se ve `{consumo}` literalmente | Falta la `f` antes de las comillas. |
| Aparecen demasiados decimales | Aplica un formato de presentación; no es una validación. |

## Separadores, final de línea y observación de valores

```python
print("azul", "gris", sep=" / ", end=" -> ")
print("fin")
texto = "  12  "
print(repr(texto))
```

Las dos primeras instrucciones producen una sola línea: `azul / gris -> fin`. `end` cambia el final de la primera impresión. `repr` muestra una representación que conserva visibles las comillas y los espacios: `'  12  '`. Es útil al comprobar por qué dos entradas no son iguales.

Distingue los datos del mensaje que pide esos datos. En `float(input('Horas: '))`, `Horas: ` es la indicación al usuario; el texto que escribe se convierte después. Si falla, inspecciona primero el texto recibido antes de cambiar la fórmula.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Conversión de tipo** | Construcción de un valor de otro tipo, como `int("12")`. |
| **Entrada y salida** | Datos que recibe el programa y resultados que presenta. |
| **F-string** | Cadena que incorpora expresiones entre llaves para construir una representación textual. |

!!! success "Para repasar"
    Lee texto, convierte cuando haga falta y muestra un formato comprensible. Identifica en qué paso puede fallar cada entrada.

---

Fuentes del temario: [05-cadenas-entrada-salida](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/05-cadenas-entrada-salida/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
