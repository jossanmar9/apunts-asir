# UT1 · 1. Bash: scripts, variables, entrada y parámetros

## ¿Qué ejecuta Bash?

Una shell interpreta comandos. Un script guarda comandos en un archivo para que puedas repetir el proceso. La primera línea `#!/usr/bin/env bash` indica el intérprete cuando lo ejecutas directamente. Con `bash nombre.sh` eliges Bash explícitamente; con `./nombre.sh` necesitas permiso de ejecución, que puedes dar con `chmod u+x nombre.sh`.

En Bash, `nombre=valor` asigna y `$nombre` expande el valor. No pongas espacios alrededor de `=`. Las comillas dobles conservan los espacios de un dato, pero expanden variables; las simples tratan el contenido literalmente. Los comentarios comienzan con `#`.

## Ejemplo resuelto: etiqueta de una muestra de laboratorio

Guarda `etiqueta.sh`:

```bash
#!/usr/bin/env bash
if (( $# != 2 )); then
    printf 'Uso: bash etiqueta.sh muestra responsable\n' >&2
    exit 1
fi
muestra=$1
responsable=$2
read -r -p 'Ubicación de la muestra: ' ubicacion
printf 'Muestra: %s\nResponsable: %s\nUbicación: %s\n' \
    "$muestra" "$responsable" "$ubicacion"
```

Ejecuta `bash etiqueta.sh "Roca volcánica" "Laia Ferrer"` y escribe `Armario azul`.

**Resultado esperado:** tres líneas con la muestra, el nombre completo y la ubicación. Las comillas hacen que cada frase sea un argumento. Sin ellas, el número de argumentos cambiaría y el script mostraría la ayuda.

### Paso a paso

1. `$#` cuenta argumentos. Si no son dos, el mensaje va a la salida de error con `>&2` y el código final es 1.
2. `$1` y `$2` son los datos de la llamada. `$0` es el nombre con el que se ha invocado el script.
3. `read -r` lee una línea sin tratar las barras invertidas como escapes.
4. `printf` utiliza un formato fijo y datos separados. `%s` sustituye texto y `\n` introduce un salto de línea.

## Variables que conviene reconocer

| Expresión | Significado |
| --- | --- |
| `"$@"` | Todos los argumentos, conservando cada uno |
| `$?` | Código del último comando, que cambia al ejecutar el siguiente |
| `$$` | Identificador del proceso de la shell |
| `${nombre:-alternativa}` | Alternativa si no existe o está vacío |
| `$(comando)` | Captura la salida estándar del comando |

Una variable de shell no pasa necesariamente a los procesos hijos. `export COLOR_FICHA=azul` la incorpora al entorno de los nuevos procesos. `printenv COLOR_FICHA` la consulta. Utiliza nombres propios del script: no sobrescribas `PATH` con una ruta de trabajo, porque dejarías de localizar comandos.

## Transformar texto y guardar colecciones

```bash
#!/usr/bin/env bash
archivo='muestra.version.txt'
printf '%s\n' "${archivo%.txt}" "${archivo:0:7}"
salas=('Sala azul cielo' 'Sala gris')
printf '%s\n' "${salas[0]}" "${#salas[@]}"
```

El primer bloque muestra `muestra.version` y `muestra`. `%` elimina el sufijo que coincide con el patrón; `${texto#patron}` elimina un prefijo; las versiones dobles `%%` y `##` eliminan la coincidencia más larga. `${texto:inicio:longitud}` extrae una subcadena. Los arrays indexados comienzan en cero y `"${salas[@]}"` conserva cada elemento.

| Error | Solución |
| --- | --- |
| `nombre = valor` | Escribe `nombre=valor`. |
| Un nombre con espacios se divide | Utiliza `"$nombre"` al pasarlo a un comando. |
| Argumentos vacíos o desplazados | Revisa las comillas en la llamada y `$#`. |

!!! success "Para repasar"
    Diferencia una variable, un argumento y una entrada por teclado. Sigue siempre cómo llegan los datos al programa.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
