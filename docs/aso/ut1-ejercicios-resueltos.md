## Ejercicios resueltos paso a paso · UT1

### Bash · Guía y estructura de scripts

#### Ejercicio 1 · Primer script
```bash
#!/usr/bin/env bash
echo "Hola desde Bash"
```
La primera línea indica qué intérprete debe ejecutar el archivo. `echo` escribe texto. Después de guardar, `chmod +x script.sh` añade permiso de ejecución y `./script.sh` lo ejecuta desde el directorio actual.

#### Ejercicio 2 · Ver el código de salida
```bash
ls /tmp
echo $?
```
`ls /tmp` ejecuta una orden. `$?` contiene el código de salida de la última orden: normalmente `0` significa éxito y un valor distinto de cero indica error.

#### Ejercicio 3 · Comentarios
```bash
# Directorio que vamos a revisar
ruta="/var/log"
echo "$ruta"
```
`#` inicia un comentario. `ruta=...` asigna sin espacios alrededor de `=` y `"$ruta"` expande el valor protegiendo espacios.

### Bash · Datos, variables y argumentos

#### Ejercicio 1 · Variables
```bash
servidor="web01"
puerto=8080
echo "Servidor: $servidor - Puerto: $puerto"
```
La asignación no lleva `$`; el `$` se usa al leer el contenido. Las comillas dobles permiten expandir variables.

#### Ejercicio 2 · Argumentos
```bash
#!/usr/bin/env bash
echo "Script: $0"
echo "Primer argumento: $1"
echo "Número de argumentos: $#"
```
`$0` es el nombre del script, `$1` el primer argumento y `$#` cuenta cuántos argumentos recibió.

#### Ejercicio 3 · Operación aritmética
```bash
a=8
b=3
resultado=$((a + b))
echo "$resultado"
```
`$((...))` crea un contexto aritmético. Bash suma los valores numéricos y guarda `11` en `resultado`.

### Bash · Decisiones

#### Ejercicio 1 · Comprobar un archivo
```bash
archivo="/etc/hosts"
if [[ -f "$archivo" ]]; then
    echo "Existe y es un archivo"
else
    echo "No existe"
fi
```
`[[ ... ]]` evalúa una condición; `-f` comprueba archivo regular. `then` abre el bloque verdadero y `fi` cierra el `if`.

#### Ejercicio 2 · Comparar números
```bash
uso=85
if (( uso >= 80 )); then
    echo "Aviso"
fi
```
`(( ... ))` permite comparaciones aritméticas sin `$` delante de la variable. Con 85, `uso >= 80` es verdadero.

#### Ejercicio 3 · Validar argumento
```bash
if [[ -z "$1" ]]; then
    echo "Falta el nombre de usuario"
    exit 1
fi
```
`-z` comprueba si la cadena está vacía. `exit 1` termina el script indicando error.

### Bash · Bucles

#### Ejercicio 1 · Recorrer servicios
```bash
for servicio in ssh nginx cron; do
    echo "Servicio: $servicio"
done
```
`for` asigna cada palabra a `servicio`; `do` inicia el cuerpo y `done` lo termina.

#### Ejercicio 2 · Contador while
```bash
n=1
while (( n <= 3 )); do
    echo "$n"
    ((n++))
done
```
`while` repite mientras la condición sea verdadera. `((n++))` incrementa el contador y evita un bucle infinito.

#### Ejercicio 3 · Leer líneas
```bash
while IFS= read -r linea; do
    echo "Leído: $linea"
done < usuarios.txt
```
La redirección `<` alimenta el bucle desde el archivo. `read -r` lee cada línea sin interpretar barras invertidas y `IFS=` evita recortes no deseados.

### Bash · Procesamiento de texto

#### Ejercicio 1 · Filtrar con grep
```bash
grep "ERROR" aplicacion.log
```
`grep` recorre las líneas y muestra las que contienen `ERROR`. El archivo es la entrada y las líneas coincidentes son la salida.

#### Ejercicio 2 · Extraer una columna
```bash
cut -d: -f1 /etc/passwd
```
`-d:` establece `:` como delimitador y `-f1` selecciona el primer campo: los nombres de usuario.

#### Ejercicio 3 · Encadenar órdenes
```bash
grep "ERROR" aplicacion.log | wc -l
```
`|` conecta la salida de `grep` con la entrada de `wc`. `wc -l` cuenta líneas; el resultado es el número de errores encontrados.

### Bash · Errores y robustez

#### Ejercicio 1 · Comprobar una orden
```bash
if cp origen.txt copia.txt; then
    echo "Copia correcta"
else
    echo "La copia ha fallado" >&2
fi
```
`if` puede evaluar directamente el código de salida de `cp`. `>&2` envía el mensaje de error a la salida estándar de errores.

#### Ejercicio 2 · Modo estricto
```bash
#!/usr/bin/env bash
set -euo pipefail
archivo="$1"
echo "$archivo"
```
`-e` detiene ante errores, `-u` detecta variables no definidas y `pipefail` hace visible un fallo dentro de una tubería. Es útil, pero hay que entender sus efectos.

#### Ejercicio 3 · Validar antes de actuar
```bash
archivo="$1"
if [[ ! -f "$archivo" ]]; then
    echo "No existe: $archivo" >&2
    exit 1
fi
wc -l "$archivo"
```
`!` niega la condición. El script comprueba la precondición antes de ejecutar `wc`, evitando trabajar con una ruta inválida.