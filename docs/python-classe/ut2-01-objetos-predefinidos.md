# UT2 · 2.1 Objetos predefinidos, funciones y métodos

## Qué debes entender

En Python trabajamos con **objetos**. Un entero, una cadena o una lista son objetos y cada objeto tiene un tipo que determina qué operaciones podemos realizar con él.

```python
nombre = "Ana"
edad = 20

print(type(nombre))  # <class 'str'>
print(type(edad))    # <class 'int'>
```

Esta unidad no pretende que estudies todavía programación orientada a objetos. Lo importante es reconocer qué objeto tienes y distinguir entre **funciones**, **métodos** y **atributos**.

## Funciones predefinidas

Python incluye funciones que podemos utilizar directamente.

```python
texto = "Python"

print(len(texto))
print(type(texto))
print(id(texto))
```

- `len()` devuelve la longitud.
- `type()` indica el tipo del objeto.
- `id()` devuelve un identificador asociado al objeto durante la ejecución.

Una función recibe el objeto como argumento:

```python
len(texto)
```

## Métodos

Un método es una operación asociada a un objeto. Se escribe después del objeto y de un punto:

```python
texto = "python"
print(texto.upper())
```

Aquí `upper()` es un método del objeto `texto`.

La diferencia visual es importante:

```python
len(texto)       # función
texto.upper()    # método
```

!!! warning "No olvides los paréntesis"
    `texto.upper` hace referencia al método, pero `texto.upper()` lo ejecuta.

## Atributos

Un atributo representa información asociada a un objeto. A diferencia de un método, normalmente no lleva paréntesis.

Más adelante encontrarás ejemplos como:

```python
ruta.name
```

`name` es un atributo. En cambio:

```python
texto.upper()
```

`upper()` es un método.

## Los tipos determinan las operaciones posibles

No todos los objetos admiten las mismas operaciones.

```python
texto = "hola"
numero = 10

print(texto.upper())
print(numero + 5)
```

No tendría sentido utilizar `upper()` sobre un entero.

```python
numero = 10
# numero.upper()  # AttributeError
```

Cuando Python indica que un objeto no tiene determinado atributo o método, comprueba primero su tipo.

## Mutabilidad e inmutabilidad

Ya vimos en UT1 que algunos objetos pueden modificarse y otros no.

Las cadenas son **inmutables**. Sus métodos no cambian la cadena original: producen otra cadena.

```python
texto = "python"
mayusculas = texto.upper()

print(texto)       # python
print(mayusculas)  # PYTHON
```

También puedes reasignar el resultado:

```python
texto = texto.upper()
```

Ahora el nombre `texto` queda asociado al nuevo valor.

## Encadenar métodos

Cuando un método devuelve un objeto que admite otro método, podemos encadenarlos.

```python
entrada = "  Python  "
resultado = entrada.strip().lower()
print(resultado)
```

Salida:

```text
python
```

Se ejecuta primero `strip()` y sobre el resultado se ejecuta `lower()`.

Para estudiar, si una expresión encadenada te confunde, sepárala:

```python
entrada = "  Python  "
limpia = entrada.strip()
resultado = limpia.lower()
```

## Consultar ayuda

Python permite consultar documentación desde el propio intérprete:

```python
help(str)
help(len)
help(str.upper)
```

También puedes utilizar `dir()` para observar los nombres disponibles en un objeto:

```python
texto = "hola"
print(dir(texto))
```

No necesitas memorizar la salida de `dir()`. Sirve para explorar qué operaciones ofrece un objeto.

## Ejemplo explicado

Queremos limpiar una respuesta introducida por un usuario y comprobar su longitud.

```python
respuesta = "  SI  "
limpia = respuesta.strip().lower()
longitud = len(limpia)

print(limpia)
print(longitud)
print(type(limpia))
```

Resultado:

```text
si
2
<class 'str'>
```

Paso a paso:

1. `respuesta` es una cadena.
2. `strip()` devuelve otra cadena sin los espacios exteriores.
3. `lower()` devuelve otra cadena en minúsculas.
4. `len()` recibe esa cadena y devuelve un entero.
5. `type()` permite comprobar el tipo del resultado.

## Errores frecuentes

### Confundir método y función

Incorrecto:

```python
# texto.len()
```

Correcto:

```python
len(texto)
```

### Olvidar guardar el resultado

```python
texto = "  hola  "
texto.strip()
print(texto)
```

`texto` sigue conteniendo los espacios. Si quieres conservar el resultado:

```python
texto = texto.strip()
```

### Utilizar un método que el tipo no tiene

Si no sabes qué tipo contiene una variable:

```python
print(type(valor))
```

Comprueba el tipo antes de intentar corregir el resto del programa.

## Comprueba que sabes...

- Explicar de forma sencilla qué es un objeto en Python.
- Utilizar `type()`, `len()` e `id()`.
- Diferenciar una función de un método.
- Reconocer un atributo por su forma de acceso.
- Entender que una cadena es inmutable.
- Explicar por qué `texto.upper()` no modifica automáticamente `texto`.
- Encadenar métodos sencillos.
- Utilizar `help()` para consultar ayuda.
- Reconocer un `AttributeError` causado por utilizar una operación que el objeto no ofrece.

!!! success "Para el examen"
    Si ves `funcion(objeto)`, piensa en una **función**. Si ves `objeto.metodo()`, piensa en un **método**. Antes de utilizar cualquiera de los dos, identifica qué tipo de objeto estás manejando.

---

Fuente principal: material de clase **Introducción a Python 2.1**, consultado el 29/10/2026.