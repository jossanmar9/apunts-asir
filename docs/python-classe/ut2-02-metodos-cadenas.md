# UT2 · 2.2 Métodos y operaciones con cadenas

## Las cadenas son secuencias

Una cadena (`str`) es una secuencia de caracteres. Podemos consultar su longitud, acceder a posiciones y extraer fragmentos.

```python
texto = "Python"

print(len(texto))  # 6
print(texto[0])    # P
print(texto[-1])   # n
```

Los índices empiezan en `0`. Los índices negativos cuentan desde el final.

```text
Texto:   P  y  t  h  o  n
Índice:  0  1  2  3  4  5
Final:  -6 -5 -4 -3 -2 -1
```

## Slicing: extraer fragmentos

La forma general es:

```python
texto[inicio:fin:paso]
```

El carácter situado en `inicio` se incluye y el situado en `fin` no.

```python
texto = "Python"

print(texto[0:2])  # Py
print(texto[2:])   # thon
print(texto[:4])   # Pyth
print(texto[::2])  # Pto
print(texto[::-1]) # nohtyP
```

!!! tip "Truco para el examen"
    Si un slicing te cuesta, escribe debajo de la palabra los índices `0, 1, 2...` y marca qué posiciones entran. Recuerda: **el final queda fuera**.

Acceder a una posición que no existe produce `IndexError`:

```python
texto = "Python"
# print(texto[20])
```

Un slicing, en cambio, puede superar el final sin producir ese error:

```python
print(texto[:20])  # Python
```

## Operadores con cadenas

### Concatenar

```python
nombre = "Ana"
saludo = "Hola " + nombre
print(saludo)
```

### Repetir

```python
print("-" * 10)
```

### Comprobar pertenencia

```python
frase = "servidor web"

print("web" in frase)      # True
print("linux" in frase)    # False
print("linux" not in frase) # True
```

Si solo necesitas saber si aparece una subcadena, `in` suele ser más claro que buscar manualmente su posición.

## Eliminar espacios de los extremos

```python
texto = "  hola  "

print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())
```

- `strip()` limpia ambos extremos.
- `lstrip()` limpia el izquierdo.
- `rstrip()` limpia el derecho.

No eliminan automáticamente los espacios interiores.

## Mayúsculas y minúsculas

```python
texto = "python para ASIR"

print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
```

Estos métodos son especialmente útiles para normalizar una entrada:

```python
respuesta = input("¿Continuar? ").strip().lower()
```

Así `" SI "` se transforma en `"si"`.

## Buscar texto

### `find()`

Devuelve la posición de la primera coincidencia o `-1` si no encuentra el texto.

```python
texto = "servidor-web"

print(texto.find("web"))
print(texto.find("php"))  # -1
```

!!! warning "No confundas posición 0 con ausencia"
    Si el texto aparece al principio, `find()` devuelve `0`. Si no aparece, devuelve `-1`.

### `index()`

También busca una posición, pero si no encuentra el texto produce `ValueError`.

```python
texto = "servidor-web"
print(texto.index("web"))
```

### `rfind()`

Busca desde la derecha y devuelve la posición de la última coincidencia.

```python
ruta = "docs/python/tema.md"
print(ruta.rfind("/"))
```

## Comprobar el principio o el final

```python
archivo = "informe.pdf"

print(archivo.startswith("informe"))  # True
print(archivo.endswith(".pdf"))       # True
```

Son más claros que construir manualmente un slicing cuando la intención es precisamente comprobar el principio o el final.

## Contar coincidencias

```python
texto = "uno,dos,tres,cuatro"
print(texto.count(","))  # 3
```

`count()` cuenta cuántas veces aparece una subcadena.

## Sustituir texto

```python
texto = "servidor viejo"
nuevo = texto.replace("viejo", "nuevo")
print(nuevo)
```

Podemos limitar el número de sustituciones:

```python
texto = "error error error"
print(texto.replace("error", "aviso", 1))
```

Resultado:

```text
aviso error error
```

La cadena original no se modifica.

## Separar una cadena: `split()`

```python
registro = "ana;20;asir"
partes = registro.split(";")
print(partes)
```

Resultado:

```text
['ana', '20', 'asir']
```

`split()` devuelve una lista de cadenas. El `20` sigue siendo texto.

```python
edad = int(partes[1])
```

Sin argumento, `split()` separa por espacios en blanco:

```python
frase = "uno   dos  tres"
print(frase.split())
```

Resultado:

```text
['uno', 'dos', 'tres']
```

## Unir cadenas: `join()`

`join()` realiza la operación contraria: reúne cadenas utilizando un separador.

```python
partes = ["ana", "20", "asir"]
resultado = " | ".join(partes)
print(resultado)
```

Resultado:

```text
ana | 20 | asir
```

La sintaxis puede parecer extraña al principio: el método se llama sobre el **separador**.

```python
" - ".join(partes)
```

Los elementos que se unen deben ser cadenas.

## Métodos de comprobación

```python
print("Python".isalpha())
print("Python3".isalnum())
print("123".isdigit())
print("PYTHON".isupper())
print("python".islower())
```

| Método | Comprueba |
| --- | --- |
| `isalpha()` | caracteres alfabéticos |
| `isalnum()` | letras o números |
| `isdigit()` | caracteres considerados dígitos |
| `isupper()` | letras en mayúsculas |
| `islower()` | letras en minúsculas |

!!! warning "`isdigit()` no valida cualquier número"
    Por ejemplo, `"-12".isdigit()` y `"3.5".isdigit()` son `False`. Utilízalo solo cuando encaje con la regla que quieres comprobar.

## Ejemplo explicado: procesar un registro

Tenemos:

```text
  jose;asir;activo  
```

Queremos limpiar los extremos, separar los tres campos y mostrar el nombre en mayúsculas.

```python
registro = "  jose;asir;activo  "
registro = registro.strip()
partes = registro.split(";")

nombre = partes[0]
ciclo = partes[1]
estado = partes[2]

print(nombre.upper())
print(ciclo)
print(estado)
```

Resultado:

```text
JOSE
asir
activo
```

Antes de acceder a posiciones de una lista obtenida con `split()`, en un programa real conviene comprobar que la estructura recibida tiene los campos esperados. Aquí suponemos que el formato es correcto para centrarnos en las cadenas.

## Ejemplo explicado: extraer una extensión

```python
archivo = "copia.seguridad.tar.gz"
posicion = archivo.rfind(".")
extension = archivo[posicion + 1:]
print(extension)
```

Resultado:

```text
gz
```

`rfind()` localiza el último punto. Sumamos uno para que el punto no forme parte del slicing.

## Errores frecuentes

| Problema | Causa probable |
| --- | --- |
| `IndexError` | Se ha accedido a una posición inexistente. |
| `ValueError` con `index()` | No existe la subcadena buscada. |
| `find()` devuelve `-1` | La subcadena no aparece. |
| `strip()` no elimina un espacio interior | Solo actúa sobre los extremos. |
| `join()` falla | Algún elemento no es una cadena. |
| El método parece no haber hecho nada | No se guardó el nuevo resultado. |

## Comprueba que sabes...

- Utilizar índices positivos y negativos.
- Explicar por qué el final de un slicing no se incluye.
- Utilizar `inicio:fin:paso`.
- Invertir una cadena con slicing.
- Utilizar `in` y `not in`.
- Utilizar `strip()`, `lower()` y `upper()`.
- Diferenciar `find()` e `index()`.
- Utilizar `startswith()` y `endswith()`.
- Utilizar `count()` y `replace()`.
- Separar texto con `split()`.
- Unir cadenas con `join()`.
- Reconocer qué comprueban `isalpha()`, `isalnum()` e `isdigit()`.
- Recordar que los métodos de cadenas devuelven nuevos resultados.

!!! success "Para el examen"
    Los puntos que más conviene practicar son **índices y slicing**, `find()`, `split()`, `join()`, `strip()` y la diferencia entre modificar una variable y obtener una nueva cadena.

---

Fuente principal: material de clase **Introducción a Python 2.2**, consultado el 29/10/2026.