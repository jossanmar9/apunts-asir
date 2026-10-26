# UT1 · 2. Cálculos, comprobaciones y decisiones en Bash

## Tres tipos de comprobación

Para enteros, `(( expresion ))` permite calcular y comparar. Para texto y archivos, `[[ condicion ]]` resulta cómodo en Bash. La forma clásica `[ condicion ]` también existe y exige espacios alrededor de los corchetes y operandos bien separados.

| Necesidad | Expresión de Bash |
| --- | --- |
| Archivo ordinario | `[[ -f "$ruta" ]]` |
| Directorio | `[[ -d "$ruta" ]]` |
| Existe una entrada | `[[ -e "$ruta" ]]` |
| Enlace simbólico | `[[ -L "$ruta" ]]` |
| Texto vacío / no vacío | `[[ -z "$texto" ]]` / `[[ -n "$texto" ]]` |
| Texto igual | `[[ "$texto" == "abierto" ]]` |
| Entero de al menos 3 | `(( cantidad >= 3 ))` |

`-e` puede ser falso en un enlace roto: utiliza también `-L` si quieres detectar cualquier enlace. `&&` significa «y», `||` significa «o» y `!` niega una condición. Un comando con código 0 se considera correcto o verdadero en un `if`.

## Hacer cuentas: no todo texto parecido a una operación se calcula

Si escribes `printf '%s\n' '8 + 3'`, estás imprimiendo texto. La expansión aritmética `$((8 + 3))` pide a Bash que evalúe la operación y sustituya la expresión por su resultado.

```bash
piezas=23
capacidad=5
completos=$((piezas / capacidad))
sobrantes=$((piezas % capacidad))
printf 'Lotes completos: %s; piezas sueltas: %s\n' "$completos" "$sobrantes"
```

Resultado: `Lotes completos: 4; piezas sueltas: 3`. La división entera cuenta cuántos grupos completos caben; el resto cuenta lo que queda. No son resultados intercambiables. Si necesitas incluir un grupo incompleto, necesitas decidir qué hacer con el resto.

Las multiplicaciones y divisiones respetan la prioridad habitual; los paréntesis aclaran el orden. Al calcular un porcentaje entero, dividir demasiado pronto puede perder la fracción: con 3 de 8 piezas, `3 / 8 * 100` da 0, mientras `3 * 100 / 8` da 37. Este último valor sigue siendo una aproximación entera, no 37,5.

Dentro de `((...))` puedes utilizar el nombre de la variable sin `$`. Es un contexto aritmético, no una cadena normal. No introduzcas datos sin validar en él: la shell puede interpretarlos como expresiones y no como la cantidad literal que imaginabas.

## Cómo decide `if`: estado cero significa verdadero

La estructura se lee «ejecuta esta prueba; si termina con estado cero, ejecuta este bloque»:

```bash
if [[ 3 -gt 2 ]]; then
    printf 'La condición se cumple\n'
else
    printf 'La condición no se cumple\n'
fi
```

El ejemplo imprime «La condición se cumple» porque 3 es mayor que 2. `then` inicia el primer camino y `fi` cierra la estructura. `else` es opcional. El sangrado de los bloques facilita la lectura, pero Bash reconoce los límites por sus palabras de control, no por el número de espacios.

`[ ... ]` es una orden de prueba que exige argumentos separados: `[ "$a" -gt 3 ]` contiene espacios después de `[` y antes de `]`. `[[ ... ]]` es una construcción propia de Bash, con reglas más cómodas para patrones y condiciones compuestas. Para números, `((...))` admite comparaciones como `>=`.

No utilices un `>` suelto como si fuera una comparación numérica dentro de `[ ... ]`: la shell puede tratarlo como redirección. Los operadores numéricos clásicos son `-eq`, `-ne`, `-lt`, `-le`, `-gt` y `-ge`; los de texto son `=` y `!=`.

## Elegir el orden de varias condiciones

Un `if/elif/else` ejecuta el primer camino verdadero. Ese orden forma parte de la solución. Si primero preguntas «¿hay al menos una pieza?», una cantidad de veinte también cumple; nunca llegaría a un `elif` posterior pensado para cantidades grandes.

Define intervalos de manera que cubran los casos válidos sin dejar huecos. Prueba exactamente los valores de frontera, no solo valores intermedios. Un programa que distingue menos de 5, de 5 a 10 y más de 10 debe probar 4, 5, 10 y 11, además de una entrada inválida.

Al combinar condiciones, `A && B` exige ambas y `A || B` admite al menos una. El cortocircuito evita evaluar lo que ya no hace falta. Puedes aprovecharlo para validar antes de calcular: primero el texto debe tener la forma permitida y solo después haces la comparación numérica.

## Verificar una ruta es hacer una pregunta concreta

`-e` pregunta si existe, `-f` si es un archivo ordinario y `-d` si es un directorio. Una carpeta puede existir y aun así no ser un archivo de entrada válido. `-r`, `-w` y `-x` preguntan por accesos, mientras `-s` pregunta si tiene tamaño no nulo.

Si una operación falla, responde a la pregunta que realmente necesitabas comprobar. Por ejemplo, antes de leer un documento puedes exigir que sea archivo ordinario y legible; no necesitas hacerlo ejecutable. Sobre un directorio, `x` significa poder atravesarlo, no que sea un programa.

## Problema explicado paso a paso: comprobar una reserva de butacas

Una sala de prueba tiene 12 butacas libres. El script acepta una cantidad entre 1 y 12, escrita con una o dos cifras sin ceros iniciales.

```bash
#!/usr/bin/env bash
peticion=${1:-}
if [[ ! "$peticion" =~ ^[1-9][0-9]?$ ]]; then
    printf 'Escribe una cantidad de una o dos cifras, sin cero inicial.\n' >&2
    exit 1
fi
libres=12
if (( peticion > libres )); then
    printf 'No hay suficientes butacas.\n'
elif (( peticion == libres )); then
    printf 'La sala queda completa.\n'
else
    quedan=$((libres - peticion))
    printf 'Reserva aceptada. Quedan %s butacas.\n' "$quedan"
fi
```

### Sigue tres entradas

| Llamada | Condición | Salida esperada |
| --- | --- | --- |
| `bash butacas.sh 5` | 5 < 12 | Quedan 7 butacas |
| `bash butacas.sh 12` | 12 = 12 | Sala completa |
| `bash butacas.sh 13` | 13 > 12 | No hay suficientes butacas |
| `bash butacas.sh cinco` | No cumple el patrón | Mensaje de entrada incorrecta |

La validación se hace **antes** de la aritmética. `^` y `$` anclan todo el texto; `[1-9]` es la primera cifra y `[0-9]?` permite una segunda opcional. El patrón sin comillas a la derecha de `=~` es una expresión regular, no texto literal.

## Aritmética y opciones de menú

`$((7 / 2))` devuelve 3: la aritmética ordinaria de Bash es entera. `%` calcula el resto. Para decimales puedes utilizar `bc`, si está instalado:

```bash
printf 'scale=2; 7 / 2\n' | bc
```

Resultado: `3.50`. `scale` controla los decimales en la división; no es una regla universal de redondeo monetario. `expr` y `let` aparecen en scripts antiguos, pero `$((...))` suele ser más legible.

Para opciones concretas, `case` evita cadenas largas de igualdades:

```bash
accion=${1:-ayuda}
case "$accion" in
    resumen) printf 'Muestra el resumen de la sala\n' ;;
    ayuda) printf 'Opciones: resumen, ayuda\n' ;;
    *) printf 'Opción desconocida\n' >&2; exit 1 ;;
esac
```

## Usar directamente el resultado de un comando

Una condición de shell también puede ser un comando: no necesitas capturar su texto y compararlo si ya proporciona un estado útil.

```bash
#!/usr/bin/env bash
if command -v bash >/dev/null 2>&1; then
    printf 'Bash está disponible\n'
else
    printf 'No se ha localizado Bash en PATH\n' >&2
fi
```

`command -v` comprueba si puede localizar el comando. `>/dev/null 2>&1` descarta su salida y sus errores; el `if` sigue recibiendo el código de salida. En un sistema donde ejecutas este script con Bash, el resultado normal es el primer mensaje.

Las formas cortas `orden && siguiente` y `orden || alternativa` dependen del mismo mecanismo: la segunda orden se ejecuta si la primera termina bien o mal, respectivamente. No sustituyas automáticamente un `if/else` por `a && b || c`: si `b` falla, también se ejecuta `c`.

### Comparaciones que suelen confundirse

| Expresión | Qué pregunta |
| --- | --- |
| `[ "$a" = "$b" ]` | ¿Son iguales como texto? |
| `[ "$a" -eq "$b" ]` | ¿Son iguales como enteros? |
| `[[ -r "$ruta" ]]` | ¿Se puede leer la ruta? |
| `[[ -x "$ruta" ]]` | ¿Tiene acceso de ejecución o búsqueda para este usuario? |
| `[[ "$nombre" == *.txt ]]` | ¿Coincide con un patrón de nombre? |
| `[[ "$nombre" =~ ^[A-Z]+$ ]]` | ¿Coincide con esta expresión regular? |

En la prueba de patrón `*.txt`, dejar el patrón sin comillas permite interpretarlo como patrón; la variable sigue protegida. Diferencia este caso de pasar argumentos a una orden externa, donde normalmente debes entrecomillar las expansiones.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Expresión regular** | Patrón que describe una forma de texto para reconocer coincidencias. |
| **Código de salida** | Estado con el que termina una orden; 0 indica éxito según la convención de shell. |
| **Condición** | Prueba que selecciona un camino de ejecución; también puede ser el estado de una orden. |

!!! success "Para repasar"
    Primero comprueba la forma del dato; después realiza cálculos o decisiones. No confundas `=` de asignación, igualdad de texto y comparación numérica.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
