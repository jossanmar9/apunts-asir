# UT3 · 1. Condicionales y bucles con seguimiento de valores

## Decidir con `if`

Un bloque comienza con `:` y se delimita con una indentación coherente. `if/elif/else` prueba las condiciones en orden y ejecuta el primer bloque que corresponde. No es lo mismo que varios `if` independientes, que pueden ejecutar más de un bloque.

## Un programa toma un camino, no todos a la vez

Sin decisiones, las instrucciones se ejecutan según el orden establecido. Un `if` permite elegir si ejecutar un bloque. Su condición produce un resultado lógico y la indentación marca cuáles son las instrucciones que dependen de ella.

Dos `if` seguidos son dos decisiones independientes. Una cadena `if/elif/else` selecciona el primer camino que corresponde. Si necesitas clasificar un valor en una única categoría, esta diferencia importa: con varios `if` podrías imprimir más de una clasificación.

Al estudiar un condicional, toma un valor concreto y pregunta qué ocurre en cada línea. Si la primera condición es verdadera, las siguientes ramas de esa cadena no se ejecutan. Si es falsa, continúas a la siguiente. No intentes interpretar todas las condiciones como si se evaluaran simultáneamente.

## El orden de los límites forma parte de la solución

Antes de escribir código, define los intervalos con palabras. En la cola de impresión del ejemplo, cero tiene un significado distinto de uno y cuatro está dentro de la categoría corta. Cinco ya pertenece a otra categoría.

Una vez escritos los límites, prueba justo antes, en el límite y justo después. Esto revela diferencias entre `<` y `<=`. Un programa puede acertar con 2 y 8 y aun así fallar exactamente con 4 o 5.

No confundas validar con clasificar. Primero puede ser necesario rechazar una cantidad negativa; después clasificar los valores que tienen sentido. Si permites que una entrada incoherente llegue a un camino normal, el mensaje podría parecer correcto sin representar un estado posible.

## `while`: repetir a partir de un estado que cambia

La condición se comprueba antes de cada vuelta, incluida la primera. Si ya es falsa al principio, el cuerpo se ejecuta cero veces. Esto no es un error: puede ser precisamente el comportamiento deseado cuando no queda trabajo.

Identifica qué variable cambia y cómo se acerca a la parada. En el ejemplo de cinta se reduce la longitud restante. Si olvidas reducirla, la misma condición seguirá siendo verdadera. Si la reduces demasiado o en el lugar equivocado, puedes saltarte una vuelta necesaria.

Un bucle que pregunta al usuario también necesita avanzar: la nueva respuesta sustituye la anterior. Si solo imprimes «respuesta incorrecta» sin volver a leer, seguirá comprobando para siempre el mismo dato.

## `for`: recorrer una colección paso a paso

La variable del `for` toma cada elemento del iterable, no necesariamente su índice. En `for color in ['azul', 'gris']`, primero vale `azul` y luego `gris`. Si necesitas además una numeración, `enumerate` la proporciona de manera explícita.

`range(3)` representa 0, 1 y 2: son tres valores, aunque el último no sea 3. El límite excluido permite expresar un número de repeticiones sin añadir uno a la longitud. Con inicio y paso, escribe los primeros valores a mano para comprobar que interpretas correctamente el recorrido.

El cuerpo del bucle se ejecuta una vez por valor seleccionado. La instrucción situada después y al mismo nivel de indentación se ejecuta al terminar el recorrido. Una indentación incorrecta puede hacer que un resumen aparezca en cada vuelta en lugar de una sola vez.

## Acumular sin reiniciar el progreso

Un contador o acumulador que resume todo el recorrido se inicializa antes. Dentro se actualiza según la entrada de esa vuelta. Al terminar, se muestra el resultado final.

Si pones `total = 0` dentro del bucle, la siguiente vuelta olvida lo acumulado. Si imprimes el total dentro, obtienes resultados parciales. Ninguna de las dos cosas es incorrecta por sí misma, pero debe corresponder a lo que pide el problema. La posición de cada instrucción expresa esa decisión.

## Problema explicado paso a paso: estado de una cola de impresión

Con 0 documentos la cola está vacía; de 1 a 4, es corta; a partir de 5, es larga. Una cantidad negativa es incoherente.

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

Vamos a buscar una etiqueta urgente entre notas:

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

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Decide si se puede enviar un aviso

Con `contacto_disponible=True` y `aviso_enviado=False`, muestra `Enviar` solo si hay contacto y el aviso aún no se ha enviado. En los demás casos muestra `No enviar`. Utiliza `if/else` y comprueba las cuatro combinaciones de booleanos.

??? tip "Pista"
    La condición debe exigir un requisito y negar el otro.

??? success "Solución paso a paso"
    ```python
    contacto_disponible = True
    aviso_enviado = False
    if contacto_disponible and not aviso_enviado:
        print("Enviar")
    else:
        print("No enviar")
    ```

    Solo la combinación contacto verdadero y aviso falso muestra `Enviar`. Las otras tres muestran `No enviar`. Es una decisión, no una modificación real ni un envío de mensajes.

### 2. Cuenta letras sin contar espacios

Recorre `"sol y mar"` con un `for` y cuenta los caracteres diferentes del espacio. No utilices `replace` para eliminar espacios ni escribas el número final como respuesta del programa.

??? tip "Pista"
    Inicializa un contador y aumenta solo cuando el carácter no sea un espacio.

??? success "Solución paso a paso"
    ```python
    texto = "sol y mar"
    contador = 0
    for caracter in texto:
        if caracter != " ":
            contador += 1
    print(contador)
    ```

    La salida es 7: tres letras de `sol`, una de `y` y tres de `mar`. Los dos espacios se recorren, pero no aumentan el contador.

### 3. Cuenta hasta encontrar un bloqueo

Recorre los estados `["pendiente", "hecho", "pendiente", "bloqueado", "pendiente"]`. Cuenta los pendientes anteriores al primer bloqueo y termina al encontrarlo. No cuentes la tarea posterior al bloqueo ni escribas directamente el resultado.

??? tip "Pista"
    Combina un contador con una condición de parada; la parada debe comprobarse antes de seguir acumulando.

??? success "Solución paso a paso"
    ```python
    estados = ["pendiente", "hecho", "pendiente", "bloqueado", "pendiente"]
    contador = 0
    for estado in estados:
        if estado == "bloqueado":
            break
        if estado == "pendiente":
            contador += 1
    print(f"Pendientes antes del bloqueo: {contador}")
    ```

    El resultado es 2. La última tarea no se procesa porque `break` termina el recorrido. Contar todos los pendientes sin comprobar la parada daría 3 y respondería a otra pregunta.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Indentación** | Espacios iniciales que delimitan los bloques de Python. |
| **Iterable** | Objeto del que un recorrido puede obtener elementos uno a uno. |
| **Contador y acumulador** | Variable que cuenta coincidencias y variable que suma cantidades. |
| **Bucle anidado** | Bucle dentro de otro; sus recorridos pueden multiplicar el trabajo total. |

!!! success "Para repasar"
    Escribe la condición, qué cambia y cuándo termina. En un recorrido, separa «omitir este elemento» de «dejar de buscar».

---

Fuentes del temario: [01-condicionales](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/01-condicionales/), [02-while](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/02-while/), [03-for-range](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/03-for-range/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
