# UT3 · 1. Condicionales y bucles con seguimiento de valores

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Indentación** | Espacios iniciales que delimitan los bloques de Python. |
| **Iterable** | Objeto del que un recorrido puede obtener elementos uno a uno. |
| **Contador y acumulador** | Variable que cuenta coincidencias y variable que suma cantidades. |
| **Bucle anidado** | Bucle dentro de otro; sus recorridos pueden multiplicar el trabajo total. |

## Decidir con `if`

Un bloque comienza con `:` y se delimita con una indentación coherente. `if/elif/else` prueba las condiciones en orden y ejecuta el primer bloque que corresponde. No es lo mismo que varios `if` independientes, que pueden ejecutar más de un bloque.

## Ejemplo resuelto: estado de una cola de impresión

**Problema propio:** con 0 documentos la cola está vacía; de 1 a 4, es corta; a partir de 5, es larga. Una cantidad negativa es incoherente.

```python
documentos = 4
if documentos < 0:
    estado = "Dato incorrecto"
elif documentos == 0:
    estado = "Vacía"
elif documentos <= 4:
    estado = "Corta"
else:
    estado = "Larga"
print(estado)
```

**Resultado:** `Corta`. Prueba -1, 0, 1, 4 y 5 para cubrir errores y límites. Al llegar a `documentos <= 4`, ya sabes que no es negativo ni cero: las condiciones anteriores también aportan información.

## Repetir con `while`: ejemplo resuelto de cortar una cinta

Tenemos 17 cm y queremos fragmentos completos de 5 cm:

```python
restante = 17
fragmentos = 0
while restante >= 5:
    restante -= 5
    fragmentos += 1
print(f"Fragmentos: {fragmentos}; restante: {restante} cm")
```

| Vuelta | Restante antes | Restante después | Fragmentos |
| --- | --- | --- | --- |
| 1 | 17 | 12 | 1 |
| 2 | 12 | 7 | 2 |
| 3 | 7 | 2 | 3 |

La cuarta comprobación es falsa; la salida es `Fragmentos: 3; restante: 2 cm`. La variable que controla la parada cambia en cada vuelta.

Un `while` también puede repetir una entrada hasta que sea válida. Para un catálogo de dos opciones:

```python
opcion = input("¿Material: papel o tela? ").strip().lower()
while opcion not in ("papel", "tela"):
    opcion = input("Escribe papel o tela: ").strip().lower()
print(f"Material elegido: {opcion}")
```

## Repetir con `for` y `range`

`for` recorre un iterable. `range(inicio, fin, paso)` excluye `fin`; el paso no puede ser cero. `range` no crea una lista entera: puedes convertirlo con `list()` si la necesitas.

```python
for pagina in range(2, 9, 3):
    print(pagina)  # 2, 5, 8 en líneas separadas
for cuenta in range(3, 0, -1):
    print(cuenta)  # 3, 2, 1
```

Para numerar elementos, `enumerate` evita gestionar un índice manual:

```python
for posicion, color in enumerate(["ocre", "azul", "gris"], start=1):
    print(posicion, color)
```

Muestra `1 ocre`, `2 azul` y `3 gris`. Utiliza `_` como nombre de variable por convenio cuando solo quieres repetir y no necesitas el valor, como en `for _ in range(2): print("marca")`.

## `break`, `continue` y `else` de un bucle

Ejemplo propio: buscar una etiqueta urgente entre notas:

```python
notas = ["pendiente", "urgente", "resuelto"]
for nota in notas:
    if nota == "resuelto":
        continue
    if nota == "urgente":
        print("Hay una nota urgente")
        break
else:
    print("No hay notas urgentes")
```

`break` termina el bucle y evita su `else`. Si eliminas `urgente` de los datos, el recorrido termina normalmente y ejecuta el `else`. En un `while`, la regla es la misma: `else` se ejecuta cuando termina sin `break`, incluso si nunca ha entrado en el cuerpo.

Los bucles anidados multiplican recorridos: dos colores por tres tamaños producen seis combinaciones. Antes de anidar, calcula cuántas vueltas darás.

## Separar búsqueda, contador y acumulador

Una búsqueda intenta encontrar un caso; un contador suma una unidad por coincidencia; un acumulador suma una cantidad. Identifica cuál necesitas antes de escribir el bucle.

```python
duraciones = [4, 9, 6]
contador = 0
total = 0
for duracion in duraciones:
    if duracion >= 6:
        contador += 1
        total += duracion
print(f"Sesiones seleccionadas: {contador}; minutos: {total}")
```

Resultado: `Sesiones seleccionadas: 2; minutos: 15`. El contador no debe sumar la duración; el acumulador sí. Ambos se inicializan antes del recorrido, no en cada vuelta.

Como ampliación de los apuntes propios, Python también dispone de `match` para seleccionar casos desde Python 3.10. No necesitas introducirlo en un ejercicio que pide `if`: dominar el razonamiento y respetar las herramientas del enunciado es más importante que usar una sintaxis distinta.

!!! success "Para repasar"
    Escribe la condición, qué cambia y cuándo termina. En un recorrido, separa «omitir este elemento» de «dejar de buscar».

---

Fuentes del temario: [01-condicionales](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/01-condicionales/), [02-while](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/02-while/), [03-for-range](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/03-for-range/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
