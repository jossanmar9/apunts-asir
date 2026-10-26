# UT1 · 3. Bucles y funciones: repetir sin duplicar

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Bucle infinito** | Repetición que no alcanza una parada; en terminal se suele interrumpir con Ctrl+C. |
| **Iteración** | Cada ejecución del cuerpo de un bucle. |
| **Variable local** | Dato limitado al ámbito de una función mediante `local` en Bash. |
| **Subshell** | Shell hija cuyo estado, como variables modificadas, no se traslada automáticamente a la shell que la inició. |

## ¿Cuándo conviene cada bucle?

`for` recorre una colección conocida. `while` repite mientras una condición es verdadera. `until` repite mientras es falsa. `break` sale del bucle y `continue` pasa a la siguiente vuelta. En todos los casos debes poder explicar la condición de finalización.

## Ejemplo resuelto: preparar etiquetas de estanterías

**Problema propio:** queremos cuatro etiquetas, excepto la tercera, que está fuera de servicio. Una función crea cada etiqueta para que el formato esté en un único lugar.

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

!!! success "Para repasar"
    Una función debe tener una tarea clara. Dibuja qué recibe, qué imprime y qué estado devuelve.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
