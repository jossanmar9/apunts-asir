# UT1 · 2. Variables, tipos y operadores

## Un nombre apunta a un objeto

En `muestras = 12`, Python evalúa primero el lado derecho y asocia el nombre `muestras` con el resultado. El tipo pertenece al objeto: `type(muestras)` indica `int`. Un objeto tiene tipo, valor e identidad; `id()` permite consultar un identificador durante su vida, no un número estable que debas memorizar.

| Tipo | Ejemplo | Operaciones habituales |
| --- | --- | --- |
| int | `12` | Contar, dividir con cociente y resto |
| float | `1.75` | Cálculos aproximados con decimales |
| str | `"etiqueta"` | Concatenar, extraer, buscar |
| bool | `True` | Condiciones |
| complex | `2 + 3j` | Cálculos con parte real e imaginaria |

Utiliza nombres como `muestras_por_caja`, sin espacios ni guiones. No pueden comenzar por una cifra ni ser palabras reservadas. Evita ocultar funciones con nombres como `str` o `input`. Las constantes en mayúsculas, como `CAPACIDAD = 8`, son una convención, no una prohibición de cambiar el valor.

## Leer una asignación sin imaginar una caja mágica

En `cantidad = 4`, el lado derecho se evalúa y el nombre queda asociado al objeto resultante. En `otra = cantidad`, los dos nombres hacen referencia al objeto correspondiente en ese momento. No se crea una regla que mantenga las dos variables sincronizadas para siempre.

```python
cantidad = 4
otra = cantidad
cantidad = cantidad + 2
print(cantidad, otra)
```

La salida es `6 4`. Primero se guardó la referencia al valor 4 en `otra`; después `cantidad` se asoció con el resultado de otra operación. Entenderlo ayuda a distinguir una reasignación de una modificación de un objeto mutable.

No utilices el signo `=` como si fuera una comparación matemática. En un programa asigna una referencia a un nombre. Para preguntar si dos valores son iguales se utiliza `==`; la pregunta produce un booleano que luego puede dirigir una decisión.

## El tipo explica qué operación tiene sentido

`3 + 2` suma números y `"3" + "2"` une textos. El resultado es 5 en el primer caso y `"32"` en el segundo. Python no transforma automáticamente cualquier cadena en número porque parezca contener cifras.

Por eso conviene preguntar qué representa el dato. Un código postal puede contener cifras y aun así interesar como texto, porque no vas a sumarlo y puedes necesitar conservar ceros iniciales. Una cantidad de piezas que vas a contar suele necesitar un entero.

`type(valor)` permite comprobar el tipo. No lo memorices como una respuesta aislada: úsalo para explicar por qué falla una operación o por qué produce una repetición de texto en lugar de una multiplicación numérica.

## División, cociente y resto con significado

Si repartes 23 piezas en grupos de 5, caben cuatro grupos completos y sobran tres. `23 // 5` obtiene el cociente entero y `23 % 5` el resto. `23 / 5` obtiene 4.6, que es útil para una medida, pero no significa que hayas preparado físicamente 4.6 cajas.

La elección depende de la pregunta. Para grupos completos necesitas el cociente. Para saber lo que queda necesitas el resto. Para contar recipientes incluyendo el último incompleto necesitas decidir si ese resto obliga a sumar uno.

Con números negativos, `//` redondea hacia menos infinito; no lo describas como «borrar decimales» en todos los casos. Al empezar, utiliza cantidades no negativas y deja explícita esa condición. Esto facilita comprobar el razonamiento sin convertir la regla en algo falso.

## Booleanos y condiciones

Un booleano tiene valor `True` o `False`, sin comillas y con esa capitalización. Una comparación como `cantidad > 0` devuelve uno de ellos. Puedes guardar el resultado o utilizarlo directamente en un `if`.

`and` exige que se cumplan ambas condiciones, `or` admite que se cumpla una y `not` invierte el valor lógico. Al escribir rangos, explica los límites: `1 <= cantidad <= 9` incluye 1 y 9. Una condición clara se entiende mejor que varias negaciones que obligan a reconstruir su significado.

## Cuándo dos nombres comparten cambios

Las listas pueden modificarse sin cambiar de identidad. Si haces `segunda = primera` y añades un elemento a esa misma lista, ambos nombres permiten observar el cambio. En cambio, las cadenas y los enteros son inmutables: una transformación genera un resultado que puedes asociar de nuevo a un nombre.

No necesitas aprender todavía toda la programación orientada a objetos para usar esta distinción. Basta con preguntar «¿he modificado el objeto que compartían o he hecho que un nombre apunte a otro resultado?». Los ejemplos de copia que aparecen más abajo permiten observar ambos casos.

## Problema explicado paso a paso: empaquetar muestras de cerámica

Tenemos 29 muestras y cada estuche admite 8. ¿Cuántos estuches llenos podemos preparar, cuántas muestras sobran y cuántos estuches necesitamos en total?

```python
muestras = 29
capacidad = 8
llenos = muestras // capacidad
sobrantes = muestras % capacidad
necesarios = (muestras + capacidad - 1) // capacidad
print(f"Llenos: {llenos}; sobrantes: {sobrantes}; necesarios: {necesarios}")
```

**Resultado esperado:** `Llenos: 3; sobrantes: 5; necesarios: 4`.

1. `29 // 8` devuelve 3: tres estuches completos.
2. `29 % 8` devuelve 5: muestras que no caben en esos tres.
3. La fórmula `(n + capacidad - 1) // capacidad` redondea hacia arriba para enteros no negativos y capacidad positiva. El cuarto estuche contiene cinco muestras.

No utilices esta fórmula sin comprobar sus condiciones cuando la entrada proceda del usuario.

## Operadores y representación de números

`/` hace división y devuelve habitualmente `float`; `//` redondea el cociente hacia menos infinito; `%` devuelve el resto; `**` es la potencia. Los paréntesis hacen explícita la prioridad: `(2 + 3) * 4` devuelve 20, mientras que `2 + 3 * 4` devuelve 14.

`==`, `!=`, `<`, `<=`, `>` y `>=` comparan. `and`, `or` y `not` combinan condiciones. `=` asigna. En contexto numérico, los booleanos se comportan como 1 y 0, pero una condición clara es mejor que un truco difícil de leer.

```python
print(0b1100, 0o14, 0xC)  # 12 12 12
print(1.5e3)              # 1500.0
print(0.1 + 0.2 == 0.3)   # False
```

Las bases cambian la notación, no el valor. Muchos decimales no tienen representación binaria exacta; mostrar dos decimales no elimina la aproximación interna. Para dinero con requisitos exactos, utiliza céntimos enteros o herramientas decimales adecuadas.

## Mutabilidad: cambiar un objeto o cambiar de referencia

```python
etiquetas = ["rojo"]
otra_referencia = etiquetas
otra_referencia.append("azul")
print(etiquetas)  # ['rojo', 'azul']

texto = "rojo"
texto_nuevo = texto.upper()
print(texto, texto_nuevo)  # rojo ROJO
```

La lista es mutable y los dos nombres apuntan a la misma lista. La cadena es inmutable: `upper()` crea un resultado nuevo. `is` compara identidad y `==` compara igualdad de valores; para comparar textos utiliza `==`. Puedes explorar operaciones con `help(str)`.

## Referencia rápida de conversiones y valores lógicos

| Expresión | Resultado | Motivo |
| --- | --- | --- |
| `int('12')` | `12` | Texto decimal convertible a entero |
| `float('2.5')` | `2.5` | El punto es el separador que reconoce esta conversión |
| `str(12)` | `'12'` | Representación textual |
| `bool('False')` | `True` | Es una cadena no vacía, no el booleano `False` |
| `bool('')` | `False` | Cadena vacía |

La conversión no interpreta lo que una persona quería decir. Para una respuesta de sí/no, compara valores permitidos después de normalizar el texto, en lugar de utilizar `bool(input(...))`.

## Referencias compartidas y copia

```python
original = ["azul", "gris"]
copia = original.copy()
copia.append("ocre")
print(original)
print(copia)
```

La salida es `['azul', 'gris']` y `['azul', 'gris', 'ocre']`. `copy()` crea otra lista y añadir un elemento ya no modifica la primera. Es una copia superficial: si hubiera objetos mutables anidados, seguirían compartidos. El tema de estructuras de datos desarrollará esa diferencia; aquí sirve para entender nombres, identidad y mutabilidad.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Objeto y clase** | Valor concreto con tipo e identidad y tipo que define sus características; la creación de clases se desarrolla más adelante. |
| **Mutabilidad** | Capacidad de cambiar un objeto sin sustituirlo por otro. |
| **Lista y diccionario** | Colección ordenada consultable por índice y colección de pares clave–valor. |
| **Índice** | Posición utilizada para acceder a un elemento; las secuencias de Python empiezan en 0. |

!!! success "Para repasar"
    Antes de una operación, identifica los tipos. El texto `"8"` y el entero `8` tienen significados diferentes aunque se parezcan en pantalla.

---

Fuentes del temario: [03-datos-variables](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/03-datos-variables/), [04-numeros-operadores](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/04-numeros-operadores/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
