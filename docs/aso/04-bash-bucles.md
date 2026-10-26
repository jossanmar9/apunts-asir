# UT1 · 3. Bucles y funciones: repetir sin duplicar

## ¿Cuándo conviene cada bucle?

`for` recorre una colección conocida. `while` repite mientras una condición es verdadera. `until` repite mientras es falsa. `break` sale del bucle y `continue` pasa a la siguiente vuelta. En todos los casos debes poder explicar la condición de finalización.

## Construir un bucle a partir de su condición de parada

Un bucle ahorra repetir instrucciones, pero también obliga a definir cómo avanza el trabajo. Antes del código, escribe tres cosas: qué valor tiene el estado inicial, qué se hace en una vuelta y qué cambio acerca el programa al final.

En un `for` sobre una lista, la propia lista limita las vueltas. En un `while`, tú debes cambiar algún dato o recibir una nueva entrada que pueda volver falsa la condición. En un `until`, el cuerpo se repite hasta que la condición pasa a ser verdadera. No es una instrucción que espere mágicamente a que el sistema cambie por sí solo.

```bash
paso=1
while (( paso <= 3 )); do
    printf 'Preparación %s\n' "$paso"
    paso=$((paso + 1))
done
printf 'Valor al terminar: %s\n' "$paso"
```

La salida enumera preparaciones 1, 2 y 3, y termina mostrando 4. La cuarta comprobación se hace, pero el cuerpo ya no se ejecuta. Esta diferencia entre comprobar y ejecutar explica muchos errores de una vuelta de más o de menos.

Un contador se inicia antes del bucle si debe conservar el progreso. Si vuelves a poner `paso=1` dentro del cuerpo en cada vuelta, lo reinicias y puedes impedir que llegue a la parada.

## Distinguir detener la búsqueda de omitir un elemento

`continue` salta el resto del cuerpo y pasa a la siguiente vuelta. `break` termina el bucle más cercano. En bucles anidados no termina automáticamente toda la aplicación.

Piensa en revisar una lista de carpetas: una entrada no válida puede omitirse con `continue`; encontrar el elemento exacto que buscabas puede justificar `break`. Si usas `break` para saltar una entrada incorrecta, abandonarías todas las que todavía faltan por revisar.

Al anidar recorridos, el número de vueltas se multiplica. Tres zonas y cuatro turnos generan doce combinaciones. Escribe qué representa cada variable y evita reutilizar el mismo nombre para las dos, porque perderías el significado del recorrido exterior.

## Crear una función y llamarla son dos acciones distintas

La definición `nombre() { ...; }` enseña a Bash una orden reutilizable. El cuerpo no se ejecuta por aparecer en el archivo: lo ejecutas escribiendo `nombre argumentos`, sin paréntesis en la llamada.

Los parámetros posicionales se refieren a la llamada actual. Dentro de `etiqueta "Azul"`, `$1` significa `Azul`, aunque el script haya recibido antes otros argumentos. Si necesitas entregar un argumento del script a una función, debes pasárselo explícitamente.

```bash
mostrar_ficha() {
    local titulo=$1
    local zona=${2:-sin_asignar}
    printf 'Ficha: %s; zona: %s\n' "$titulo" "$zona"
}
mostrar_ficha 'Mapa antiguo' 'Sala azul'
mostrar_ficha 'Plano pequeño'
```

La primera llamada muestra ambos datos. La segunda utiliza `sin_asignar` porque no recibe un segundo argumento. `local` evita sustituir por accidente variables del mismo nombre en el código que llama a la función.

## Datos y estado: dos canales para dos preguntas

Una función puede producir un texto y además indicar si pudo completar su tarea. Los datos se escriben por stdout; el estado se devuelve con `return`. Quien llama puede capturar los primeros y comprobar el segundo.

```bash
formar_codigo() {
    if [[ ! "$1" =~ ^[A-Z]{2}$ ]]; then
        printf 'Se necesitan dos letras mayúsculas\n' >&2
        return 1
    fi
    printf 'FICHA-%s\n' "$1"
}
if codigo=$(formar_codigo 'AZ'); then
    printf 'Código recibido: %s\n' "$codigo"
fi
```

El resultado es `Código recibido: FICHA-AZ`. Si pruebas con `Az`, la función escribe un error por stderr y el `if` no entra. Capturar stdout no implica que la operación haya ido bien; por eso se comprueba el estado.

Si añades mensajes de depuración por stdout, también acabarán dentro de `codigo`. Mantén ahí solo el dato que has prometido devolver y utiliza stderr para diagnóstico. Esta separación permite reutilizar una función sin tener que limpiar su salida cada vez.

## Problema explicado paso a paso: preparar etiquetas de estanterías

Queremos cuatro etiquetas, excepto la tercera, que está fuera de servicio. Una función crea cada etiqueta para que el formato esté en un único lugar.

```bash
#!/usr/bin/env bash
etiqueta() {
    local numero=$1
    printf 'ESTANTERIA-%02d\n' "$numero"
}
for numero in 1 2 3 4; do
    if (( numero == 3 )); then
        continue
    fi
    etiqueta "$numero"
done
```

**Salida esperada:** `ESTANTERIA-01`, `ESTANTERIA-02` y `ESTANTERIA-04`, cada una en una línea.

1. La función se define antes de llamarla.
2. Dentro de la función, `$1` es el primer argumento de **la función**, no necesariamente el del script.
3. `local` limita la variable a la función. `%02d` formatea el entero con al menos dos cifras.
4. `continue` omite la etiqueta 3, pero permite que el recorrido continúe con 4.

## `while` y `until` con seguimiento

```bash
#!/usr/bin/env bash
pendientes=3
while (( pendientes > 0 )); do
    printf 'Cajas pendientes: %s\n' "$pendientes"
    pendientes=$((pendientes - 1))
done

revisadas=0
until (( revisadas == 2 )); do
    revisadas=$((revisadas + 1))
    printf 'Revisión %s completada\n' "$revisadas"
done
```

El `while` muestra 3, 2 y 1. El `until` muestra las revisiones 1 y 2: cuando la condición pasa a ser verdadera, ya no entra. Cambiar `until` por `while` sin negar la condición altera completamente el comportamiento.

## Función que calcula y función que comprueba

Bash distingue **datos por stdout** y **estado por return**:

```bash
#!/usr/bin/env bash
nombre_etiqueta() {
    printf 'CAJA-%s\n' "$1"
}
es_codigo() {
    [[ "$1" =~ ^[A-Z]{2}[0-9]{2}$ ]]
}
nombre=$(nombre_etiqueta 'AB42')
if es_codigo 'AB42'; then
    printf '%s es válido\n' "$nombre"
fi
```

`$(...)` captura el texto. La función de comprobación devuelve el estado del último comando: 0 si el patrón coincide. `return 250` es un código de estado, no una forma de devolver un texto ni un cálculo arbitrario.

Si separas funciones en un archivo propio, `source ./funciones.sh` las carga en la shell actual; ejecutar `bash funciones.sh` inicia una shell hija y no deja las definiciones disponibles en la shell que la llamó.

| Error | Causa y corrección |
| --- | --- |
| Bucle infinito | No cambia la variable que decide la parada. |
| El valor capturado contiene mensajes sobrantes | La función imprime depuración por stdout; envíala a stderr. |
| `return` truncado | Los estados tienen un rango limitado; utiliza stdout para los datos. |

## Leer un archivo línea a línea sin romper sus datos

Este patrón de los apuntes anteriores es útil para procesar listados. Mantiene espacios, barras y la última línea aunque no termine con salto:

```bash
#!/usr/bin/env bash
while IFS= read -r linea || [[ -n "$linea" ]]; do
    printf 'Recibido: [%s]\n' "$linea"
done < notas.txt
```

Para probarlo, crea `notas.txt` con dos líneas: `Sala azul` y `Pendiente de revisar`. Obtendrás una línea `Recibido: [...]` por cada una. `IFS=` evita recortar o separar por espacios; `-r` conserva las barras; `< notas.txt` conecta el archivo con la entrada del bucle.

En Bash, un bucle colocado después de una tubería suele ejecutarse en una subshell. Si cuentas dentro de `cat notas.txt | while ...`, el contador puede no conservar su valor fuera del bucle. La redirección anterior evita esa dificultad.

## Menú que se repite hasta terminar

```bash
#!/usr/bin/env bash
while true; do
    read -r -p 'Escribe ver o salir: ' opcion || break
    case "$opcion" in
        ver) printf 'La consulta está preparada\n' ;;
        salir) break ;;
        *) printf 'Opción no reconocida\n' ;;
    esac
done
```

Con las entradas `ver`, `otra` y `salir`, se muestran el mensaje de consulta y el aviso de opción incorrecta; la tercera termina el bucle. La comprobación de `read` también permite salir si se cierra la entrada. Si quieres un menú numerado, `select` lo genera; `REPLY` contiene la respuesta escrita y la variable elegida contiene el texto de la opción.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Bucle infinito** | Repetición que no alcanza una parada; en terminal se suele interrumpir con Ctrl+C. |
| **Iteración** | Cada ejecución del cuerpo de un bucle. |
| **Variable local** | Dato limitado al ámbito de una función mediante `local` en Bash. |
| **Subshell** | Shell hija cuyo estado, como variables modificadas, no se traslada automáticamente a la shell que la inició. |

!!! success "Para repasar"
    Una función debe tener una tarea clara. Dibuja qué recibe, qué imprime y qué estado devuelve.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
