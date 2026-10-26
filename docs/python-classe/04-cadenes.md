# UT2 · 1. Objetos, métodos y tratamiento de cadenas

## Función y método

Una función se llama como `len(texto)`. Un método se llama sobre el objeto: `texto.upper()`. Los paréntesis ejecutan la operación; `texto.upper` solo obtiene una referencia al método. Las cadenas son inmutables: debes conservar el valor devuelto si quieres seguir utilizando la transformación.

## Ejemplo resuelto: interpretar una etiqueta de archivo sonoro

**Problema propio:** de la etiqueta `"  jazz:directo:flac  "`, obtener el estilo, el tipo de grabación y el formato. Los dos separadores están garantizados en este primer ejemplo.

```python
original = "  jazz:directo:flac  "
etiqueta = original.strip()
primero = etiqueta.find(":")
ultimo = etiqueta.rfind(":")
estilo = etiqueta[:primero]
grabacion = etiqueta[primero + 1:ultimo]
formato_audio = etiqueta[ultimo + 1:]
print(estilo.title(), grabacion, formato_audio.upper(), sep=" | ")
print(etiqueta.count(":"))
print(etiqueta.startswith("jazz:"), etiqueta.endswith(":flac"))
```

**Resultado esperado:** `Jazz | directo | FLAC`, después `2` y `True True`.

### Sigue los índices

La cadena limpia es `jazz:directo:flac`. El primer `:` está en la posición 4 y el último en la 12. `[:4]` toma las posiciones 0 a 3. `[5:12]` toma `directo`. `[13:]` toma hasta el final. El límite derecho del corte queda excluido.

`find()` devuelve -1 cuando no encuentra la subcadena; `index()` lanza `ValueError`. Si los separadores no están garantizados, compruébalos antes de extraer: un corte con -1 podría dar un resultado aparentemente correcto, pero equivocado.

## Operaciones que conviene tener a mano

| Operación | Ejemplo y lectura |
| --- | --- |
| `strip`, `lstrip`, `rstrip` | Quitar espacios de ambos extremos, izquierda o derecha |
| `lower`, `upper` | Pasar a minúsculas o mayúsculas |
| `capitalize`, `title` | Primera letra de la frase o inicios de palabra |
| `replace('a', 'b', 1)` | Sustituir solo la primera coincidencia |
| `count(':')` | Contar apariciones |
| `isalpha`, `isalnum` | Solo letras / letras o números |
| `isdigit`, `isupper`, `islower` | Comprobar el contenido o las letras con distinción de caso |

`isdigit()` incluye determinados caracteres Unicode que no admite `int()`; no es un validador universal de números. Tampoco acepta signo negativo o punto decimal. Para una entrada ASCII restringida puedes comprobar explícitamente los caracteres admitidos.

```python
sonido = "violin"
print(sonido[0], sonido[-1])  # v n
print(sonido[::2])           # voi
print(sonido[::-1])          # niloiv
print("ol" in sonido)        # True
print("-" * 4)              # ----
```

Acceder a `sonido[99]` produce `IndexError`, pero un corte como `sonido[:99]` se ajusta al final disponible. `strip()` no quita espacios internos. `replace()` no valida si el significado del resultado es correcto.

## Funciones de biblioteca y aleatoriedad

`string.ascii_letters` y `string.digits` proporcionan alfabetos útiles. `random.choice(secuencia)` selecciona un elemento y `random.randint(a, b)` incluye ambos extremos. Para demostrar una selección de muestra puedes hacer `random.choice("ABC")`; el resultado varía. Las contraseñas o tokens reales necesitan una fuente adecuada como `secrets`, no la aleatoriedad de simulación de `random`.

!!! success "Para repasar"
    Escribe los índices bajo la cadena antes de cortarla. Comprueba siempre qué ocurre si falta el separador que esperas.

---

Fuentes del temario: [01-objetos-predefinidos](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/01-objetos-predefinidos/), [02-metodos-cadenas](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/02-metodos-cadenas/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
