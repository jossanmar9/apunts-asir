# UT1 · 4. Archivos, tuberías, filtros y expresiones regulares

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **stdin, stdout y stderr** | Canales de entrada, salida normal y error, numerados 0, 1 y 2. |
| **Redirección** | Conexión de un canal con un archivo u otro destino mediante operadores como `>` o `<`. |
| **Tubería** | Conexión de stdout de una orden con stdin de la siguiente mediante `\|`. |
| **`/dev/null`** | Destino especial que descarta lo que se escribe en él. |

## Conectar comandos

Un comando dispone de entrada estándar, salida estándar y salida de error. `>` crea o sobrescribe; `>>` añade; `2>` redirige errores; `|` envía stdout a la entrada del siguiente comando. El error no entra automáticamente en la tubería.

`grep` selecciona líneas, `cut` extrae campos, `sort` ordena, `uniq` agrupa repeticiones consecutivas y `wc` cuenta. `awk` trabaja bien con campos y `sed` con transformaciones de texto. `find` busca entradas del sistema de archivos según nombre, tipo u otras propiedades.

## Caso resuelto: resumen de incidencias de un taller

Crea un archivo de prueba `taller.log`:

```text
INFO|madera|llegada
ERROR|pintura|falta material
ERROR|madera|pieza rota
INFO|pintura|revisión
ERROR|pintura|ventilación
```

**Objetivo propio:** contar errores por zona.

```bash
grep '^ERROR|' taller.log | cut -d'|' -f2 | sort | uniq -c
```

### ¿Qué ocurre en cada tramo?

1. `grep` conserva tres líneas que comienzan por `ERROR|`. En este patrón básico, `|` es un carácter literal.
2. `cut` obtiene el segundo campo: pintura, madera, pintura.
3. `sort` junta las dos apariciones de pintura.
4. `uniq -c` cuenta cada grupo: un error de madera y dos de pintura. El orden y los espacios de presentación pueden depender de la configuración regional.

Sin ordenar, las dos líneas de pintura no serían consecutivas y no formarían un único grupo.

Para guardar el resumen sin borrar el log:

```bash
grep '^ERROR|' taller.log | cut -d'|' -f2 | sort | uniq -c > resumen.txt
```

`resumen.txt` es la salida. No utilices el mismo archivo como entrada y como destino de `>`: podría vaciarse antes de leerlo.

## Otras formas de preguntar sobre el mismo archivo

```bash
awk -F'|' '$1 == "ERROR" {print $2 ": " $3}' taller.log
sed 's/^INFO|/AVISO|/' taller.log
wc -l < taller.log
```

`awk` selecciona según el primer campo y muestra los otros dos. `sed` imprime una versión transformada, sin modificar el archivo porque no utiliza `-i`. `wc` devuelve 5 líneas si el archivo tiene el salto de línea final.

## ¿Patrón de nombre o expresión regular?

`find . -type f -name '*.log'` busca nombres con un patrón de shell; las comillas evitan que la shell lo expanda antes. `grep -E '^(ERROR|AVISO)\|' archivo` utiliza una expresión regular extendida: la alternancia es `|` y la barra con `\|` busca el separador literal.

| Elemento de una expresión regular | Lectura |
| --- | --- |
| `^` / `$` | Inicio / final de línea |
| `[0-9]` | Una cifra |
| `.` | Un carácter cualquiera |
| `\.` | Un punto literal |
| `+` con `-E` | Una o más repeticiones |

Un patrón con cuatro grupos de una a tres cifras detecta la **forma** de una IPv4, pero no garantiza que cada octeto esté entre 0 y 255. No confundas reconocer una forma con validar todo su significado.

## Redirecciones: importa el orden

Los descriptores 0, 1 y 2 corresponden a stdin, stdout y stderr. En `programa > salida.log 2>&1`, primero se conecta stdout al archivo y después stderr al mismo destino. Invertirlo (`2>&1 > salida.log`) puede dejar stderr apuntando al terminal.

`tee resumen.txt` permite ver y guardar una salida; `tee -a resumen.txt` añade. Un *here-document* crea una entrada de varias líneas. Si entrecomillas el delimitador, no se expanden las variables:

```bash
cat <<'FIN'
El texto $USER se conserva literalmente.
FIN
```

### Caso resuelto: buscar en archivos con espacios en el nombre

Prepara una carpeta `fichas` con `sala azul.txt`, cuyo contenido sea `material frágil`, y `sala gris.txt`, con `material normal`.

```bash
find fichas -type f -name '*.txt' -exec grep -HnF -- 'frágil' {} +
```

Resultado esperado: una coincidencia en `fichas/sala azul.txt:1:material frágil`. `find` localiza archivos, `-exec` los pasa como argumentos y `grep -HnF` muestra nombre, línea y coincidencia literal. No se divide `sala azul.txt` en dos argumentos.

Otra opción, con GNU `xargs`, es `find fichas -type f -name '*.txt' -print0 | xargs -0 -r grep -HnF -- 'frágil'`. El carácter nulo separa nombres de forma fiable y `-r` evita ejecutar `grep` sin archivos. La disponibilidad de `-r` depende de la implementación. No uses `find ... | rm`: `rm` necesita argumentos, no una lista por stdin.

| Necesitas buscar… | Opción útil |
| --- | --- |
| Sin distinguir mayúsculas | `grep -i` |
| Líneas que no coinciden | `grep -v` |
| Coincidencia silenciosa para un `if` | `grep -q` |
| Texto literal, sin regex | `grep -F` |
| Archivos sin bajar a subcarpetas | `find carpeta -maxdepth 1 -type f` |
| Archivos vacíos | `find carpeta -type f -empty` |

Las opciones `-size`, `-mtime` y `-user` añaden criterios de tamaño, antigüedad y propietario. Revisa primero la selección con `-print` antes de asociarle una modificación.

!!! success "Para repasar"
    Prueba cada tramo de la tubería por separado. Si el resultado es incorrecto, localiza el primer tramo donde los datos dejan de ser los esperados.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
