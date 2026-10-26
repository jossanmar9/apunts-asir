# UT1 · 3. Leer datos y mostrar resultados

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Conversión de tipo** | Construcción de un valor de otro tipo, como `int("12")`. |
| **Entrada y salida** | Datos que recibe el programa y resultados que presenta. |
| **F-string** | Cadena que incorpora expresiones entre llaves para construir una representación textual. |

## `input()` siempre devuelve texto

Si el usuario escribe `12`, `input()` devuelve `"12"`. Para calcular debes convertirlo con `int()` o `float()`. Convertir no es lo mismo que validar todas las reglas del problema: un entero negativo sigue siendo un entero, pero puede ser inadmisible como cantidad de muestras.

`print()` puede separar argumentos con `sep` y elegir el final con `end`. Las f-strings insertan expresiones entre llaves. Un `\n` representa un salto de línea y `\t` una tabulación. Las comillas triples permiten escribir texto de varias líneas.

## Ejemplo resuelto: consumo de una impresora 3D

**Problema propio:** estimar cuántos metros de filamento consume una sesión según las horas y los metros por hora. Suponemos entradas positivas y decimales con punto; la validación se introduce en UT3.

```python
horas = float(input("Horas de trabajo: "))
metros_hora = float(input("Metros de filamento por hora: "))
consumo = horas * metros_hora
print(f"Filamento estimado: {consumo:.2f} m")
print("Unidad", "metros", sep=": ")
```

### Prueba con datos conocidos

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

!!! success "Para repasar"
    Lee texto, convierte cuando haga falta y muestra un formato comprensible. Identifica en qué paso puede fallar cada entrada.

---

Fuentes del temario: [05-cadenas-entrada-salida](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/05-cadenas-entrada-salida/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
