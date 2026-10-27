# UT1 · 1. Bash: scripts, variables, entrada y parámetros

## ¿Qué ejecuta Bash?

Una shell interpreta comandos. Un script guarda comandos en un archivo para que puedas repetir el proceso. La primera línea `#!/usr/bin/env bash` indica el intérprete cuando lo ejecutas directamente. Con `bash nombre.sh` eliges Bash explícitamente; con `./nombre.sh` necesitas permiso de ejecución, que puedes dar con `chmod u+x nombre.sh`.

En Bash, `nombre=valor` asigna y `$nombre` expande el valor. No pongas espacios alrededor de `=`. Las comillas dobles conservan los espacios de un dato, pero expanden variables; las simples tratan el contenido literalmente. Los comentarios comienzan con `#`.

## De una orden a un script: qué cambia realmente

Cuando escribes una orden en el terminal, Bash la interpreta en ese momento. Al guardar varias órdenes en un archivo no inventas un lenguaje distinto: preparas una secuencia para repetirla. El archivo no se ejecuta solo por terminar en `.sh`; necesitas indicar un intérprete o hacerlo ejecutable.

Puedes crear `ficha.sh` en un editor de texto, escribir la primera línea `#!/usr/bin/env bash` y guardar. `bash ficha.sh` inicia Bash y le entrega el archivo. `chmod u+x ficha.sh` permite después invocarlo como `./ficha.sh`. El `./` significa «búscalo en esta carpeta»: la carpeta actual no tiene por qué estar en `PATH`.

Si estás en otra carpeta, `bash ficha.sh` no busca el archivo junto al que tienes abierto en el editor. Parte del directorio de trabajo. Compruébalo con `pwd` y utiliza una ruta relativa o absoluta que corresponda. Esta distinción evita confundir un problema de localización con un error del código.

## Asignar, leer y delimitar una variable

Una variable permite dar un nombre a una información. Al asignar no se escribe `$`; al utilizar el valor se expande con `$`. Bash no necesita que declares de antemano que será texto o un número para estos casos sencillos.

```bash
nombre='Carpeta de láminas'
printf '%s\n' "$nombre"
base='lamina'
printf '%s\n' "${base}_revisada.txt"
```

La primera impresión muestra `Carpeta de láminas`. La segunda muestra `lamina_revisada.txt`. Las llaves delimitan dónde acaba el nombre: `$base_revisada` buscaría una variable llamada `base_revisada`, no uniría automáticamente el valor de `base` con ese sufijo.

Los nombres distinguen mayúsculas: `nombre` y `Nombre` no son la misma variable. Pueden contener letras, cifras y guiones bajos, pero no empezar por cifra. Usa nombres que expliquen el dato y evita ocupar nombres del sistema para otros fines.

## Por qué las comillas cambian los argumentos

Bash prepara los argumentos antes de llamar a una orden. Si expandes una variable sin comillas en una orden corriente, el resultado puede dividirse en palabras y tratar caracteres como `*` como patrones de nombres. Las comillas dobles mantienen el resultado como un argumento y permiten expandir variables. Las simples conservan el texto literalmente.

```bash
nombre='Láminas grandes'
printf '[%s]\n' "$nombre"
printf '[%s]\n' $nombre
printf '%s\n' 'El contenido de $nombre no se expande aquí'
```

La primera orden muestra `[Láminas grandes]`. La segunda imprime dos líneas, `[Láminas]` y `[grandes]`: el formato se aplica a dos argumentos. La tercera conserva los caracteres `$nombre`. No hay dos archivos ni dos variables diferentes: ha cambiado cómo la shell entrega el dato a la orden.

Este efecto importa al copiar, buscar o imprimir nombres con espacios. La regla práctica para pasar un dato como argumento es `"$variable"`. No añadas comillas al azar a toda la sintaxis: una expresión regular o un patrón pueden necesitar que parte de su sintaxis conserve su significado.

## Capturar la salida no es capturar el estado

`resultado=$(orden)` ejecuta una orden y captura su stdout, eliminando los saltos de línea finales. No captura automáticamente stderr. El código de salida sigue siendo otra información distinta, que puedes comprobar con un `if` o guardar inmediatamente.

```bash
fecha=$(date +%Y-%m-%d)
printf 'Fecha del informe: %s\n' "$fecha"
```

El valor de la fecha depende del día del equipo. No esperes el texto `date +%Y-%m-%d`: las comillas y `$()` indican operaciones distintas. Una variable normal tampoco se convierte en una variable de entorno hasta que la exportas; una shell hija recibe el entorno exportado, no todos los nombres internos de su padre.

## Qué significa recibir varios argumentos

En `bash ficha.sh "Sala azul" 3`, la shell entrega dos argumentos. Dentro del script, `$1` es `Sala azul`, `$2` es `3` y `$#` es 2. `"$@"` permite reenviar cada argumento manteniendo sus límites; `"$*"` los reúne en un solo texto separado normalmente por espacios.

Comprueba primero cuántos argumentos hay. Que una variable tenga texto no demuestra que exista el número correcto de argumentos: alguien puede pasar una cadena vacía explícita. `${1:-general}` utiliza `general` si el primer argumento no existe o está vacío; `${1-general}` solo lo hace cuando no existe.

`shift` retira el primer argumento posicional y desplaza los demás. Es útil cuando el primero indica una acción y el resto son sus datos. Antes de usarlo, comprueba que hay algo que retirar. No modifica la lista de argumentos de otra llamada independiente ni borra variables con nombres propios que ya hayas creado.

## Problema explicado paso a paso: etiqueta de una muestra de laboratorio

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

## Elegir entre argumentos y entrada interactiva

Si el enunciado dice «recibe una carpeta», la interfaz normal es `bash programa.sh carpeta`. Si dice «pregunta la carpeta», utiliza `read`. Un script programado sin una persona delante no debería quedarse esperando una respuesta por teclado.

| Variante de `read` | Cuándo utilizarla |
| --- | --- |
| `IFS= read -r linea` | Conservar espacios iniciales y barras invertidas |
| `read -r -s clave` | No mostrar lo que se escribe; añade después un salto de línea |
| `read -r -t 10 respuesta` | Esperar como máximo diez segundos y comprobar su estado |
| `read -r nombre resto` | Repartir una línea entre varias variables |

### Problema explicado paso a paso: conservar nombres con espacios en un array

```bash
#!/usr/bin/env bash
salas=('Azul cielo' 'Gris perla')
salas+=('Verde musgo')
for indice in "${!salas[@]}"; do
    printf '%s: %s\n' "$indice" "${salas[$indice]}"
done
```

La salida tiene tres líneas: `0: Azul cielo`, `1: Gris perla` y `2: Verde musgo`. `+=` añade sin sustituir lo anterior; `${!salas[@]}` recorre los índices existentes. Las comillas conservan cada nombre completo. `unset 'salas[1]'` eliminaría ese elemento, pero no renumeraría automáticamente los demás.

Para cargar un archivo de una entrada por línea, utiliza `mapfile -t salas < salas.txt` en una versión de Bash que disponga de `mapfile`. Es más seguro para espacios que `salas=($(cat salas.txt))`. Los arrays asociativos necesitan `declare -A` y permiten acceder por clave, como `capacidad[azul]=18`.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Conserva cada argumento

Escribe `argumentos.sh` para mostrar cuántos argumentos recibe y después imprimir cada uno entre `<` y `>`, en su propia línea. Prueba `bash argumentos.sh azul "gris claro"`. No utilices `read`.

??? tip "Pista"
    `$#` cuenta argumentos y `"$@"` conserva sus límites.

??? success "Solución paso a paso"
    ```bash
    #!/usr/bin/env bash
    printf 'Argumentos: %s\n' "$#"
    printf '<%s>\n' "$@"
    ```

    La salida es `Argumentos: 2`, `<azul>` y `<gris claro>`. Las comillas de la llamada agrupan el segundo argumento y las de `"$@"` mantienen esa agrupación al reenviarlo.

### 2. Genera un nombre sin tocar archivos

Recibe como único argumento un nombre terminado en `.csv`. Supón que el sufijo es correcto. Quita ese sufijo y construye el nombre acabado en `_revisado.csv`. Imprime el resultado sin crear ni renombrar ningún archivo. Prueba con `lista del club.csv`.

??? tip "Pista"
    Puedes quitar el sufijo con `${nombre%.csv}` y delimitar la variable al añadir texto.

??? success "Solución paso a paso"
    ```bash
    #!/usr/bin/env bash
    if (( $# != 1 )); then
        printf 'Uso: bash nombre.sh archivo.csv\n' >&2
        exit 1
    fi
    nombre=$1
    base=${nombre%.csv}
    printf '%s\n' "${base}_revisado.csv"
    ```

    El resultado es `lista del club_revisado.csv`. Primero validamos el número de argumentos; después transformamos texto. No hay ninguna operación de escritura sobre el sistema de archivos.

### 3. Añade y consulta una colección

Crea un array con `lunes` y `martes`, añade `jueves` y cambia el segundo elemento por `miércoles`. Muestra solo el último elemento y el número de elementos. No copies manualmente toda la lista otra vez.

??? tip "Pista"
    Los índices empiezan en cero. Añadir utiliza `+=` y cambiar un elemento utiliza su índice.

??? success "Solución paso a paso"
    ```bash
    #!/usr/bin/env bash
    dias=(lunes martes)
    dias+=(jueves)
    dias[1]='miércoles'
    printf 'Último: %s\n' "${dias[2]}"
    printf 'Cantidad: %s\n' "${#dias[@]}"
    ```

    La salida es `Último: jueves` y `Cantidad: 3`. Cambiar una posición no aumenta el tamaño; añadir un elemento sí.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Terminal y shell** | Interfaz de texto y programa que interpreta los comandos; son piezas diferentes. |
| **Comando y script** | Instrucción que ejecutas y archivo que reúne instrucciones. |
| **Shebang** | Primera línea `#!` que indica el intérprete al ejecutar directamente el archivo. |
| **Ruta absoluta y relativa** | Dirección desde la raíz o desde el directorio de partida; `.` es el actual y `..` el superior. |
| **Directorio y `~`** | Carpeta y abreviatura habitual de la carpeta personal en la shell. |
| **Argumento y opción** | Dato pasado al ejecutar; una opción modifica el comportamiento, habitualmente con `-` o `--`. |
| **Variable de entorno y PATH** | Dato heredable por procesos hijos y lista de directorios donde se buscan comandos. |

!!! success "Para repasar"
    Diferencia una variable, un argumento y una entrada por teclado. Sigue siempre cómo llegan los datos al programa.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
