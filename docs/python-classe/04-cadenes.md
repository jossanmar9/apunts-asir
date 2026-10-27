# UT2 · 1. Objetos, métodos y tratamiento de cadenas

## Función y método

Una función se llama como `len(texto)`. Un método se llama sobre el objeto: `texto.upper()`. Los paréntesis ejecutan la operación; `texto.upper` solo obtiene una referencia al método. Las cadenas son inmutables: debes conservar el valor devuelto si quieres seguir utilizando la transformación.

## Un texto es una secuencia de caracteres

Una cadena permite acceder a sus caracteres por posición. El primer índice es 0 porque se cuenta desde el principio sin avanzar ninguna posición; el segundo está a un paso, en el índice 1. Un índice negativo cuenta desde el final, de modo que `-1` identifica el último carácter.

Es útil escribir los índices debajo de la palabra antes de hacer cortes:

```text
Texto:   m  a  p  a
Índice:  0  1  2  3
Final:  -4 -3 -2 -1
```

`"mapa"[0]` obtiene `m` y `"mapa"[-1]` obtiene `a`. Pedir una posición inexistente es distinto de pedir un tramo que llega más allá del final: un acceso individual puede producir `IndexError`, mientras un corte se ajusta a los límites disponibles.

## Leer un corte como dos fronteras

En `texto[inicio:fin]`, se incluye `inicio` y se excluye `fin`. Con paso 1 y límites válidos dentro de la cadena, la longitud es `fin - inicio`. Si el límite queda fuera de la cadena, Python lo ajusta y esa resta por sí sola ya no describe el resultado. En `"mapa"[1:3]` se toman los índices 1 y 2: el resultado es `ap`, no `apa`.

Si omites el inicio, partes del principio. Si omites el final, llegas hasta el final. Un tercer valor indica el paso. `texto[::-1]` recorre en orden inverso; no modifica por sí mismo la variable original.

```python
texto = "laminas"
print(texto[:3])
print(texto[3:])
print(texto[::2])
```

La salida es `lam`, `inas` y `lmns`. Antes de ejecutar, escribe los índices y marca cuáles selecciona cada expresión. Así puedes explicar un corte en un examen sin depender de recordarlo como un truco.

## Los métodos devuelven resultados

`strip` produce una cadena sin espacios de los extremos. `upper` produce una representación en mayúsculas. `replace` produce un resultado con sustituciones. Ninguno convierte una cadena inmutable en una caja de caracteres que se altere en el mismo lugar.

```python
texto = "  mapa  "
limpio = texto.strip()
print(repr(texto))
print(repr(limpio))
```

Se muestra `'  mapa  '` y después `'mapa'`. Si quieres seguir trabajando con la versión limpia bajo el mismo nombre, escribe `texto = texto.strip()`. Si necesitas conservar ambas versiones, utiliza dos nombres como en el ejemplo.

## Elegir entre buscar una posición y comprobar una presencia

Si solo necesitas saber si aparece un texto, `in` expresa la pregunta directamente. Si necesitas cortar antes o después de un separador, puede interesarte su posición con `find`. Si necesitas contar cuántas veces aparece, utiliza `count`.

No uses el resultado de `find` como booleano sin interpretarlo: una coincidencia en la posición cero no es lo mismo que ausencia, que se representa mediante -1. Compara explícitamente cuando corresponda. La diferencia entre `find` e `index` se vuelve importante cuando el separador puede faltar.

## Separar campos no es adivinar su significado

`split(';')` divide por el separador y devuelve una lista. A continuación debes comprobar cuántas partes hay y qué representa cada una. Una columna que contiene `18` sigue siendo texto hasta que la conviertes; una línea incompleta puede no tener la posición que intentas consultar.

`join` hace la operación de presentación contraria: une cadenas con un separador. La llamada se escribe sobre el separador, como `' / '.join(partes)`. No convierte automáticamente elementos numéricos de una lista en textos si necesitas unirlos.

## Problema explicado paso a paso: interpretar una etiqueta de archivo sonoro

De la etiqueta `"  jazz:directo:flac  "`, obtener el estilo, el tipo de grabación y el formato. Los dos separadores están garantizados en este primer ejemplo.

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

## Separar y reunir texto

Los apuntes anteriores incluían `split` y `join`, útiles cuando el separador expresa la estructura de los datos:

```python
registro = "azul;18;abierta"
partes = registro.split(";")
print(partes)
print(" | ".join(partes))
```

La salida es `['azul', '18', 'abierta']` y `azul | 18 | abierta`. Separar no convierte `18` a entero ni valida que existan exactamente tres campos. Antes de extraer posiciones o convertir, comprueba la estructura que espera el problema.

`split()` sin argumentos agrupa espacios en blanco y descarta los de los extremos. `split(' ')` utiliza exactamente un espacio y puede crear elementos vacíos. Elige según lo que significa el formato, no solo por cuál parece funcionar con un ejemplo.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Limpia una línea de opciones

A partir de `"  sonido=SI  "`, obtiene la cadena `"sonido=si"` y comprueba si termina en `"=si"`. Muestra tanto el resultado como el booleano. No uses bucles ni condicionales.

??? tip "Pista"
    Puedes encadenar métodos, guardando el resultado de la transformación.

??? success "Solución paso a paso"
    ```python
    linea = "  sonido=SI  "
    limpia = linea.strip().lower()
    print(limpia)
    print(limpia.endswith("=si"))
    ```

    La salida es `sonido=si` y `True`. Primero se limpian los extremos y después el caso de las letras. La comprobación no modifica la cadena.

### 2. Reconstruye una lista con otro separador

Recibes `"rojo,verde,azul"`. Conviértelo en una lista con `split` y produce una sola línea `"rojo / verde / azul"` con `join`. No escribas los colores otra vez en el resultado.

??? tip "Pista"
    El separador con el que unes puede ser distinto del que se utilizó al recibir los datos.

??? success "Solución paso a paso"
    ```python
    colores = "rojo,verde,azul"
    partes = colores.split(",")
    resultado = " / ".join(partes)
    print(resultado)
    ```

    `split` obtiene tres cadenas. `join` las reúne con el nuevo separador y la salida es `rojo / verde / azul`. No se calcula ninguna posición manualmente.

### 3. Cambia solo la primera coincidencia

En `"borrador - borrador - final"`, sustituye solo el primer `borrador` por `revisado`. Conserva la cadena original y muestra ambas. No utilices una sustitución global.

??? tip "Pista"
    `replace` admite un tercer argumento que limita el número de cambios.

??? success "Solución paso a paso"
    ```python
    original = "borrador - borrador - final"
    revisado = original.replace("borrador", "revisado", 1)
    print(original)
    print(revisado)
    ```

    La segunda línea es `revisado - borrador - final`. La primera conserva el texto inicial porque la transformación devuelve otra cadena.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Método** | Operación que se llama sobre un objeto, como `texto.strip()`. |
| **Propiedad o atributo** | Dato accesible en un objeto; en `ruta.name`, `name` es un atributo, no una llamada. |
| **Slicing** | Extracción de una parte de una secuencia con inicio, fin y paso. |
| **Cadena inmutable** | Texto cuyos caracteres no se cambian en el mismo objeto; los métodos devuelven nuevos resultados. |

!!! success "Para repasar"
    Escribe los índices bajo la cadena antes de cortarla. Comprueba siempre qué ocurre si falta el separador que esperas.

---

Fuentes del temario: [01-objetos-predefinidos](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/01-objetos-predefinidos/), [02-metodos-cadenas](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/02-metodos-cadenas/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
