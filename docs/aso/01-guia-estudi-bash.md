# UT1 · Guía de estudio de Bash

Esta página es una **guía de repaso para estudiar** la UT1. No sustituye los apartados detallados: los ordena, destaca lo que conviene dominar y utiliza ejemplos cortos.

## 1. Estructura mínima de un script

```bash
#!/bin/bash
echo "Hola mundo"
```

```bash
chmod +x script.sh
./script.sh
# o bien
bash script.sh
```

`#!/bin/bash` indica el intérprete. Para ejecutar con `./script.sh` hace falta permiso de ejecución.

## 2. Variables, comillas y entrada

```bash
nombre="Jose"
echo "Hola $nombre"
read -r -p "Nombre del usuario: " usuario
echo "Usuario: $usuario"
```

!!! warning "Error típico"
    `nombre = "Jose"` es incorrecto. En una asignación no hay espacios alrededor de `=`.

Regla práctica: cuando pasas una variable a una orden, normalmente usa `"$variable"` para conservar espacios.

Variables de entorno que conviene reconocer: `$HOME`, `$USER`, `$PATH`, `$PWD`, `$SHELL`, `$HOSTNAME`.

## 3. Parámetros

Si ejecutas:

```bash
./alta.sh pepe 25
```

Dentro del script:

```bash
echo "$0"  # nombre del script
echo "$1"  # pepe
echo "$2"  # 25
echo "$#"  # número de parámetros
echo "$@"  # todos los parámetros
```

Validación típica:

```bash
if (( $# != 2 )); then
    echo "Uso: $0 usuario edad" >&2
    exit 1
fi
```

## 4. Arrays

```bash
servidores=("web01" "db01" "backup01")
echo "${servidores[0]}"
echo "${servidores[@]}"
echo "${#servidores[@]}"
```

Recorrerlos:

```bash
for servidor in "${servidores[@]}"; do
    echo "$servidor"
done
```

## 5. Matemáticas

Para enteros, la forma recomendada es `$(( ... ))` o `(( ... ))`:

```bash
usados=70
total=100
libres=$((total - usados))
echo "$libres"
```

Para decimales, el material utiliza `bc`:

```bash
resultado=$(echo "scale=2; 10 / 3" | bc)
echo "$resultado"
```

## 6. Tests: archivos, cadenas y números

### Archivos

```bash
[[ -e "$ruta" ]]  # existe
[[ -f "$ruta" ]]  # archivo regular
[[ -d "$ruta" ]]  # directorio
[[ -r "$ruta" ]]  # legible
[[ -w "$ruta" ]]  # escritura
[[ -x "$ruta" ]]  # ejecutable
[[ -s "$ruta" ]]  # tamaño > 0
```

### Cadenas

```bash
[[ -z "$nombre" ]]       # vacía
[[ -n "$nombre" ]]       # no vacía
[[ "$a" == "$b" ]]      # iguales
[[ "$a" != "$b" ]]      # diferentes
```

### Números

| Operador | Significado |
|---|---|
| `-eq` | igual |
| `-ne` | diferente |
| `-lt` | menor |
| `-le` | menor o igual |
| `-gt` | mayor |
| `-ge` | mayor o igual |

```bash
if [[ $ocupacion -ge 90 ]]; then
    echo "Alerta"
fi
```

Con `[[ ... ]]` puedes combinar condiciones con `&&` y `||`.

## 7. Manipulación de cadenas

```bash
archivo="informe_final.pdf"
echo "${archivo:0:7}"  # informe
echo "${archivo%.*}"   # informe_final
echo "${archivo##*.}"  # pdf
echo "${#archivo}"     # longitud
```

Estas expansiones son muy útiles para tratar nombres de archivos sin invocar herramientas externas.

## 8. `if`, `elif`, `else`

```bash
if [[ $nota -ge 9 ]]; then
    echo "Excelente"
elif [[ $nota -ge 5 ]]; then
    echo "Aprobado"
else
    echo "Suspenso"
fi
```

Piensa siempre: **¿qué condición quiero comprobar y qué ocurre en cada caso?**

## 9. `case`

Es útil cuando una variable puede tener varias opciones conocidas:

```bash
case "$1" in
    iniciar)
        echo "Iniciando"
        ;;
    parar)
        echo "Parando"
        ;;
    *)
        echo "Opción desconocida"
        ;;
esac
```

## 10. Bucles

### `for`

```bash
for usuario in ana juan pedro; do
    echo "$usuario"
done
```

```bash
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```

### `while`

```bash
contador=1
while [[ $contador -le 5 ]]; do
    echo "$contador"
    ((contador++))
done
```

### `until`

Se repite **hasta que** la condición es cierta:

```bash
contador=1
until [[ $contador -gt 5 ]]; do
    echo "$contador"
    ((contador++))
done
```

`continue` salta a la siguiente iteración; `break` sale del bucle.

## 11. Funciones

```bash
comprobar_usuario() {
    if id "$1" &>/dev/null; then
        return 0
    fi
    return 1
}

if comprobar_usuario "alumno"; then
    echo "Existe"
else
    echo "No existe"
fi
```

Una función debe definirse antes de utilizarla. Sus argumentos también son `$1`, `$2`... `return` devuelve un **código de salida**, no una cadena.

Para obtener un valor:

```bash
sumar() {
    echo $(($1 + $2))
}

resultado=$(sumar 4 6)
```

## 12. `grep` y expresiones regulares

Patrones básicos:

| Patrón | Significado |
|---|---|
| `^` | inicio de línea |
| `$` | final de línea |
| `.` | cualquier carácter |
| `[0-9]` | un dígito |
| `[A-Z]` | una mayúscula |
| `[^0-9]` | cualquier carácter que no sea un dígito |

Con `grep -E` tienes regex extendidas: `+`, `?`, `{n}`, `{n,m}`, `|` y `( )`.

```bash
grep '^root' /etc/passwd
grep 'bash$' /etc/passwd
grep -E 'error|fallo' sistema.log
grep -E '^[0-9]{4}$' codigos.txt
```

En Bash puedes validar directamente con `=~`:

```bash
if [[ $puerto =~ ^[0-9]{1,5}$ ]]; then
    echo "Formato numérico correcto"
fi
```

## 13. Herramientas de texto que debes saber combinar

```bash
grep -i "error" sistema.log
cut -d: -f1 /etc/passwd
awk -F: '{print $1, $3}' /etc/passwd
sort nombres.txt
sort nombres.txt | uniq -c
tr '[:lower:]' '[:upper:]' < nombres.txt
find . -type f -name "*.log"
```

`cut` funciona bien con un delimitador claro. `awk` es mejor cuando quieres trabajar con columnas y condiciones.

## 14. `sed`

```bash
sed 's/http/https/' config.txt
sed 's/http/https/g' config.txt
sed '/error/d' log.txt
sed '/^$/d' archivo.txt
sed -n '3,7p' archivo.txt
```

`-i` modifica el archivo real:

```bash
sed -i.bak 's/antiguo/nuevo/g' config.txt
```

Esto crea una copia `.bak` antes de modificar.

## 15. Pipes y redirecciones

```bash
ps -ef | grep ssh
comando > archivo.txt
comando >> archivo.txt
comando 2> errores.log
comando &> todo.log
```

`>` sustituye; `>>` añade. La pipe `|` envía la salida de una orden a la entrada de la siguiente.

## 16. Errores y depuración

Todo comando devuelve un código: **0 = éxito**, otro valor = error.

```bash
ls /etc/passwd
echo "$?"
```

Para depurar:

```bash
bash -x script.sh
```

Otras herramientas del tema:

```bash
set -e
set -u
trap 'echo "Interrumpido"; exit 1' SIGINT SIGTERM
```

## 17. Ejemplo integrador

Script que recibe un directorio y cuenta los `.log`:

```bash
#!/bin/bash

if (( $# != 1 )); then
    echo "Uso: $0 directorio" >&2
    exit 1
fi

ruta=$1

if [[ ! -d "$ruta" ]]; then
    echo "El directorio no existe" >&2
    exit 2
fi

cantidad=$(find "$ruta" -type f -name '*.log' | wc -l)
echo "Archivos .log: $cantidad"
```

Aquí combinas parámetros, `if`, test de directorio, sustitución de comandos, `find`, pipe y `wc`.

## Qué priorizaría para el examen

1. Saber leer un script y predecir qué hará.
2. `$1`, `$#`, `"$@"`, variables y comillas.
3. `[[ ... ]]`: archivos, cadenas y comparaciones numéricas.
4. `if`, `case`, `for`, `while` y funciones.
5. Pipes y redirecciones.
6. `grep` + regex, `awk`, `cut` y `sed`.
7. Código de salida `$?` y diagnóstico de errores.
8. Combinarlo en scripts cortos de administración.

!!! tip "Cómo estudiarla"
    Lee un apartado, cierra los apuntes y escribe un ejemplo de 5-10 líneas de memoria. Después haz los ejercicios de la UT1 sin mirar la solución.