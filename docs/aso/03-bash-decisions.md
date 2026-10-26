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

## Ejemplo resuelto: comprobar una reserva de butacas

**Problema propio:** una sala de prueba tiene 12 butacas libres. El script acepta una cantidad entre 1 y 12, escrita con una o dos cifras sin ceros iniciales.

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

!!! success "Para repasar"
    Primero comprueba la forma del dato; después realiza cálculos o decisiones. No confundas `=` de asignación, igualdad de texto y comparación numérica.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
