# UT2 · 2. F-strings, formatos y Unicode

## El valor y su presentación son cosas diferentes

Una f-string transforma expresiones en texto. El formato `:.2f` muestra dos cifras decimales; `:03d` muestra un entero con al menos tres cifras y ceros a la izquierda. El valor numérico original no cambia porque lo muestres con un formato.

## Ejemplo resuelto: tarjeta de una muestra mineral

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

## Caso resuelto: ¿por qué falla un filtro?

**Situación:** esperas `"cuarzo"`, pero recibes `" Cuarzo "`. La igualdad directa es falsa. Primero limpia los extremos con `strip()` y después convierte el caso con `lower()`; el resultado es `"cuarzo"`. Si recibes `"cuarzo azul"`, seguirá siendo un texto diferente: normalizar no significa ignorar cualquier diferencia.

| Error | Comprobación |
| --- | --- |
| Llaves sin sustituir | Falta `f` al principio. |
| `ValueError` con formato `d` | El valor no es un entero compatible con el formato. |
| Comparación sorprendente | Mira mayúsculas, espacios y representación con `repr`. |

!!! success "Para repasar"
    Separa el cálculo del formato. Para comprobar texto, define primero qué diferencias quieres aceptar.

---

Fuentes del temario: [03-formateo-fstrings-unicode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/03-formateo-fstrings-unicode/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
