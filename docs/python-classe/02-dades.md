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

## Ejemplo resuelto: empaquetar muestras de cerámica

**Problema propio:** tenemos 29 muestras y cada estuche admite 8. ¿Cuántos estuches llenos podemos preparar, cuántas muestras sobran y cuántos estuches necesitamos en total?

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

!!! success "Para repasar"
    Antes de una operación, identifica los tipos. El texto `"8"` y el entero `8` tienen significados diferentes aunque se parezcan en pantalla.

---

Fuentes del temario: [03-datos-variables](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/03-datos-variables/), [04-numeros-operadores](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/04-numeros-operadores/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
