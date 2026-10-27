# UT2 · 2. F-strings, formatos y Unicode

## El valor y su presentación son cosas diferentes

Una f-string transforma expresiones en texto. El formato `:.2f` muestra dos cifras decimales; `:03d` muestra un entero con al menos tres cifras y ceros a la izquierda. El valor numérico original no cambia porque lo muestres con un formato.

## Construir una frase sin perder los valores originales

Una f-string es texto en el que puedes insertar el resultado de expresiones. La `f` delante de la comilla activa ese comportamiento y las llaves delimitan dónde evaluar. No cambia el significado de la variable fuera de la cadena.

```python
cantidad = 3
nombre = "láminas"
mensaje = f"Hay {cantidad} {nombre}"
print(mensaje)
print(cantidad + 1)
```

La salida es `Hay 3 láminas` y después 4. Aunque `mensaje` sea texto, `cantidad` sigue siendo un entero. Puedes seguir calculando sin intentar recuperar el número desde la frase.

Si olvidas la `f`, las llaves y el nombre aparecen literalmente. Si escribes un nombre que no existe dentro de una f-string, Python intentará evaluarlo y puede producir `NameError`. Estos dos errores tienen causas distintas.

## El formato aparece después de los dos puntos

En `{masa:.2f}`, la parte anterior a `:` es la expresión y la posterior describe su presentación. `.2f` pide dos decimales. `03d` pide un entero con anchura mínima tres, completando con ceros cuando haga falta.

No conviertas todos los números en cadenas formateadas al comenzar. Calcula con sus tipos numéricos y aplica el formato al presentar. Si formateas demasiado pronto, ya no tendrás el mismo tipo para realizar las operaciones siguientes.

Un porcentaje también puede representarse con formato. Si la fracción es 0.25, `{fraccion:.0%}` muestra `25%`: el formato ya multiplica por cien para la presentación. Si antes multiplicas tú por cien y después vuelves a usar `%`, puedes mostrar un resultado cien veces mayor del esperado.

## Alinear no es recortar

Una anchura mínima reserva espacio si el contenido es corto. Si es más largo, el formato puede ocupar más. Por eso una tabla que parece alineada con palabras pequeñas puede desplazarse cuando aparece un nombre largo.

La alineación a izquierda `<`, derecha `>` o centro `^` decide dónde se colocan los espacios. Para cantidades suele resultar más legible alinear a la derecha y usar un número consistente de decimales. Para textos, la izquierda permite localizar rápidamente el principio.

Estas reglas mejoran un informe que lee una persona. Para entregar información a otra aplicación, utiliza un formato de datos adecuado en lugar de asumir que podrá interpretar cualquier tabla visual.

## Qué explica Unicode y qué no resuelve automáticamente

Unicode permite representar caracteres de muchas lenguas mediante puntos de código. `ord` obtiene el correspondiente a un carácter y `chr` construye el carácter a partir de un código válido. No es un mecanismo para traducir textos ni aplicar las reglas alfabéticas de cada idioma.

Al comparar cadenas, Python sigue un orden definido por sus caracteres. Una mayúscula y una minúscula pueden tener posiciones distintas de las que esperas al ordenar palabras mentalmente. Para respuestas que no deben distinguir caso, normaliza antes de comparar según la regla de tu programa.

No necesitas memorizar códigos numéricos de letras para esta unidad. Lo que necesitas entender es por qué una comparación textual puede sorprender y por qué normalizar debe ser una decisión explícita, no una corrección arbitraria después de ver un resultado.

## Problema explicado paso a paso: tarjeta de una muestra mineral

```python
codigo = 7
masa = 12.375
mineral = "cuarzo"
print(f"M-{codigo:03d} | {mineral.upper()} | {masa:.2f} g")
print(f"{masa=}")
print(f"Etiqueta literal: {{M-{codigo:03d}}}")
```

**Salida esperada:**

```text
M-007 | CUARZO | 12.38 g
masa=12.375
Etiqueta literal: {M-007}
```

1. `:03d` no altera el código 7; crea la representación `007`.
2. `:.2f` redondea la representación para mostrarla. No convierte `masa` en 12.38.
3. `{masa=}` muestra el nombre de la expresión y su valor; resulta útil al depurar.
4. `{{` y `}}` permiten escribir llaves literales dentro de una f-string.

También puedes utilizar `:d` para enteros, `:f` para decimales y `:s` para cadenas. Un formato incompatible con el tipo produce un error. `str(codigo).zfill(3)` es una alternativa para obtener `007` como texto.

## Unicode y comparación

Python representa texto con Unicode. `ord(caracter)` obtiene el punto de código y `chr(numero)` hace el recorrido inverso:

```python
print(ord("Ω"))           # 937
print(chr(937))           # Ω
print("Z" < "a")          # True
print("Cuarzo" == "cuarzo")  # False
```

La comparación de cadenas es lexicográfica por puntos de código, no una ordenación alfabética adaptada a la lengua. Si el usuario debe escribir una orden independientemente de las mayúsculas, normaliza con `strip().lower()` o `casefold()` según el caso. Pasar a minúsculas no elimina acentos ni convierte automáticamente dos textos Unicode visualmente iguales en la misma secuencia de caracteres.

## Problema explicado paso a paso: ¿por qué falla un filtro?

**Situación:** esperas `"cuarzo"`, pero recibes `" Cuarzo "`. La igualdad directa es falsa. Primero limpia los extremos con `strip()` y después convierte el caso con `lower()`; el resultado es `"cuarzo"`. Si recibes `"cuarzo azul"`, seguirá siendo un texto diferente: normalizar no significa ignorar cualquier diferencia.

| Error | Comprobación |
| --- | --- |
| Llaves sin sustituir | Falta `f` al principio. |
| `ValueError` con formato `d` | El valor no es un entero compatible con el formato. |
| Comparación sorprendente | Mira mayúsculas, espacios y representación con `repr`. |

## Alinear una tabla sin cambiar los valores

```python
for nombre, cantidad in [("Cuarzo", 7), ("Mica", 12)]:
    print(f"{nombre:<10}{cantidad:>4d}")
```

`<10` reserva al menos diez posiciones y alinea el nombre a la izquierda; `>4d` alinea el entero a la derecha en al menos cuatro posiciones. Verás dos filas con las cantidades alineadas. El ancho mínimo no recorta textos más largos.

Esto ayuda a construir informes de terminal. Para intercambiar datos con otro programa, elige un formato estructurado como JSON o CSV en lugar de obligarlo a reconstruir columnas visuales.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Muestra el avance de una revisión

Se han revisado 3 de 8 páginas. Calcula la fracción revisada y muéstrala como porcentaje con un decimal usando el formato de una f-string. No multipliques por cien antes de utilizar el formato `%`.

??? tip "Pista"
    El formato de porcentaje ya transforma una fracción en su representación porcentual.

??? success "Solución paso a paso"
    ```python
    revisadas = 3
    total = 8
    fraccion = revisadas / total
    print(f"Avance: {fraccion:.1%}")
    ```

    La salida es `Avance: 37.5%`. La variable conserva 0.375; solo cambia la presentación. Multiplicar antes por cien haría que el formato lo volviera a multiplicar.

### 2. Comprueba si el formato modifica el valor

Guarda `distancia=2.71828`. Muéstrala con dos decimales y después vuelve a mostrar la variable sin ese formato. Escribe las dos salidas y explica si el primer `print` redondea permanentemente la variable.

??? tip "Pista"
    Una representación de salida no es una nueva asignación a la variable.

??? success "Solución paso a paso"
    ```python
    distancia = 2.71828
    print(f"{distancia:.2f}")
    print(distancia)
    ```

    Las líneas son `2.72` y `2.71828`. El primer formato redondea el texto presentado; no cambia el valor que se utiliza en la segunda impresión.

### 3. Alinea dos columnas sencillas

Presenta `Caja` con cantidad 4 y `Sobre` con cantidad 15. Reserva ocho posiciones para el nombre alineado a la izquierda y tres para el entero alineado a la derecha. Escribe dos `print`; aquí no necesitas un bucle.

??? tip "Pista"
    Los formatos se aplican a cada campo: `<8` para el nombre y `>3d` para el entero.

??? success "Solución paso a paso"
    ```python
    print(f"{'Caja':<8}{4:>3d}")
    print(f"{'Sobre':<8}{15:>3d}")
    ```

    Las cantidades quedan alineadas a la derecha. Los espacios completan el ancho mínimo, pero no recortan un nombre largo. Cada fila tiene once posiciones con estos datos.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Unicode** | Estándar de representación de caracteres mediante puntos de código. |
| **Formato de presentación** | Regla que decide cómo se muestra un valor sin cambiar necesariamente ese valor. |
| **Comparación lexicográfica** | Orden que compara secuencias elemento a elemento; no equivale automáticamente al orden alfabético de una lengua. |

!!! success "Para repasar"
    Separa el cálculo del formato. Para comprobar texto, define primero qué diferencias quieres aceptar.

---

Fuentes del temario: [03-formateo-fstrings-unicode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/03-formateo-fstrings-unicode/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
