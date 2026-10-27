# UT1 · 5. Errores, depuración y scripts de administración

## El estado de un comando es información

En shell, 0 indica éxito y otros valores indican otros resultados. `grep` devuelve 1 cuando no encuentra coincidencias: no siempre representa una avería. `$?` cambia con el siguiente comando; a menudo resulta más claro escribir `if comando; then ...`.

`set -u` detecta variables no definidas. `set -e` puede detener el script ante determinados fallos, pero tiene excepciones en condicionales y otras construcciones. `set -o pipefail` hace visible un fallo en una tubería que terminaría con un último comando correcto. Ninguna opción sustituye el tratamiento de los errores esperables.

## De un enunciado a una solución que puedas justificar

Empieza escribiendo una llamada concreta y su salida. Si el programa recibe un archivo, decide si la ruta llega como argumento o se pregunta por teclado; son interfaces distintas. Después describe lo que debe ocurrir cuando falta la ruta, apunta a un directorio o no puede leerse.

La solución no empieza por una colección de órdenes que conoces. Empieza por una secuencia con propósito: recibir la entrada, validarla, ejecutar una transformación, comprobar su resultado y presentar una respuesta. El mismo método sirve para una entrega y para un examen, porque permite explicar cada decisión.

Prueba primero una transformación pequeña con datos que conozcas. Cuando funcione, conviértela en una función o intégrala en el programa. Añade el siguiente paso y repite. Si escribes todo de una vez, un fallo puede tener demasiadas causas posibles y te costará localizarlo.

## Qué comprueba cada nivel de revisión

`bash -n` detecta problemas de estructura y sintaxis: un `fi` ausente o un bloque mal formado. No demuestra que la ruta exista ni que el cálculo sea correcto. `bash -x` sí ejecuta y muestra las expansiones: puede revelar un argumento vacío o una orden construida de forma distinta a la esperada.

Un analizador como ShellCheck detecta muchos patrones problemáticos, como expansiones sin comillas. Tampoco conoce todo el significado del ejercicio. Finalmente, los casos de prueba comprueban comportamiento con datos concretos. Necesitas distinguir estos niveles para no dar por correcto un programa solo porque la sintaxis es válida.

Durante la depuración, imprime el dato con límites visibles: `echo "DEBUG: archivo=[$archivo]" >&2`. Los corchetes ayudan a ver un dato vacío o espacios sobrantes. Retira o controla estos mensajes cuando dejen de hacer falta.

## Por qué `set -e` no reemplaza los `if`

`set -e` tiene reglas y excepciones según el contexto de ejecución. Una orden usada como condición de un `if`, por ejemplo, puede fallar sin que eso signifique terminar inmediatamente el script: precisamente estás utilizando su resultado para decidir.

Además, algunas órdenes devuelven un estado no cero como resultado normal de una consulta. Que `grep` no encuentre coincidencias puede ser una respuesta esperable. El programa debe decidir si significa «no hay resultados», «faltan datos obligatorios» o una situación que requiere terminar.

Con una tubería, el estado habitual corresponde a la última orden. `pipefail` permite que un fallo anterior también afecte al resultado global. Aun así debes explicar qué harás cuando ese resultado sea no cero: mostrar una ayuda, continuar con otra entrada, reintentar o detenerte.

## Un registro útil cuenta qué ocurrió, no solo que algo falló

Un mensaje como «error» no identifica la operación ni el dato que la provocó. «No se puede leer el archivo indicado: notas.txt» permite actuar. Mantén los resultados normales por stdout y los errores por stderr para que quien llame al programa pueda separarlos.

No confundas el mensaje con el código de salida. Una orden puede imprimir algo y fallar; otra puede no imprimir nada y terminar correctamente. Si necesitas guardar el código en una variable, hazlo antes de ejecutar otra orden que sustituya `$?`.

## Preparar pruebas de examen y de consulta

Para cada programa, combina un caso normal, un límite y al menos un error de entrada. Prueba también espacios en nombres si el programa trabaja con rutas. Escribe qué esperas antes de ejecutarlo: mirar una salida y decidir después que «parece bien» es una comprobación más débil.

Una tabla de seguimiento muestra el estado de variables importantes después de cada paso. Si puedes reconstruirla a mano con datos pequeños, podrás explicar por qué funciona el script y detectar dónde diverge una ejecución real. Esa comprensión es lo que permite adaptar la técnica a un enunciado diferente, sin copiar una solución de clase.

## Problema explicado paso a paso: informe de líneas de un documento

Recibir un archivo de texto y mostrar cuántas líneas tiene, incluido un nombre con espacios. No copia archivos ni crea usuarios.

```bash
#!/bin/bash
set -u
if (( $# != 1 )); then
    echo 'Uso: bash informe.sh archivo' >&2
    exit 1
fi
archivo=$1
if [[ ! -f "$archivo" || ! -r "$archivo" ]]; then
    echo 'Se necesita un archivo ordinario que se pueda leer.' >&2
    exit 2
fi
if lineas=$(wc -l < "$archivo"); then
    echo "Documento: $archivo"
    echo "Líneas: $lineas"
else
    echo 'No se ha podido completar el recuento.' >&2
    exit 3
fi
```

### Prueba guiada

Crea `texto corto.txt` con estas dos órdenes. La primera escribe la primera línea y la segunda añade la siguiente:

```bash
echo "primera" > "texto corto.txt"
echo "segunda" >> "texto corto.txt"
```

| Llamada | Resultado esperado |
| --- | --- |
| `bash informe.sh "texto corto.txt"` | 2 líneas; estado 0 |
| `bash informe.sh ausente.txt` | Aviso de archivo; estado 2 |
| `bash informe.sh` | Ayuda; estado 1 |

`wc -l` cuenta saltos de línea. Un último fragmento sin salto final no aumenta el recuento. Esa diferencia puede explicar una aparente discrepancia con lo que ves en un editor.

El segundo `if` contempla que el comando falle aunque se haya superado la comprobación previa: entre comprobar y leer, el estado del archivo podría cambiar.

## Cómo depurarlo

`bash -n informe.sh` comprueba la sintaxis sin ejecutar el contenido. `bash -x informe.sh "texto corto.txt"` muestra los comandos expandidos mientras los ejecuta; evita utilizar trazas sobre secretos. Si tienes ShellCheck, `shellcheck informe.sh` ayuda a detectar problemas habituales.

`trap 'echo "Fin del laboratorio" >&2' EXIT` ejecuta una acción al salir. También puedes capturar señales o `ERR` según el caso. Utiliza `trap` para limpieza y diagnóstico conscientes, no para ocultar un fallo.

## Aplicación a tareas de administración

Un script de copias combina comprobación del origen, comando de archivado, estado y log. Un lector de CSV debe separar campos sin dividir los espacios, por ejemplo con `while IFS=';' read -r nombre zona; do ...; done < datos.csv` para un formato simple sin comillas internas. Un formato CSV general requiere un lector adecuado.

En gestión de usuarios o servicios, separa **consultar**, **decidir** y **modificar**. Prueba primero la lógica con datos de laboratorio y mensajes de lo que haría. No necesitas ejecutar altas masivas para entender un `if`. Al interpretar un sondeo, recuerda también que una IP que no responde a ping no queda demostrada como libre: puede filtrar ICMP.

## Método de trabajo recuperado de los apuntes anteriores

Antes de programar, escribe una llamada de ejemplo y su resultado esperado. Divide después el trabajo en leer, comprobar, transformar y presentar. Prueba cada parte por separado y añade las comprobaciones antes de conectarlas.

Una función de error evita repetir mensajes y salidas en scripts más largos:

```bash
#!/bin/bash
error() {
    echo "ERROR: $*" >&2
    exit 1
}
(( $# == 1 )) || error "Uso: bash revisar.sh archivo"
[[ -f "$1" ]] || error "No es un archivo ordinario: $1"
echo "Preparado para revisar: $1"
```

Con un archivo existente, imprime la ruta. Sin argumento, termina con código 1 y una indicación de uso. La validación ocurre antes de leer `$1` como dato de trabajo.

## Procesos, permisos y señales en el contexto de un script

Un proceso es un programa en ejecución; su PID permite identificarlo. Una señal comunica un evento al proceso: SIGTERM solicita terminar y SIGKILL fuerza la terminación sin permitir limpieza. `trap` puede tratar determinadas señales, pero no SIGKILL.

Los permisos `r`, `w` y `x` significan lectura, escritura y ejecución; en directorios, `x` permite atravesarlos. `chmod u+x informe.sh` añade ejecución al propietario. `root` es la cuenta administradora y `sudo` ejecuta una orden con la identidad autorizada por su configuración; no necesitas elevar permisos para practicar sobre tus propios archivos.

Esto aporta contexto a Bash; el desarrollo completo de procesos, servicios y administración de directorio se incorporará cuando exista el material de esas unidades.

## Ejercicios para practicar

Intenta resolverlos antes de abrir la solución. Puedes consultar la teoría; después repite alguno sin mirar para comprobar qué recuerdas. Las pistas y soluciones están cerradas para que elijas cuándo verlas.

### 1. Revisa una dependencia antes de usarla

Escribe un script que compruebe si `wc` está disponible. Si lo está, muestra `Herramienta disponible`; si no, escribe un error por stderr y termina con código 2. No instales nada desde el script.

??? tip "Pista"
    `command -v` proporciona un estado que puede utilizar directamente el `if`.

??? success "Solución paso a paso"
    ```bash
    #!/bin/bash
    if command -v wc >/dev/null 2>&1; then
        echo 'Herramienta disponible'
    else
        echo 'Falta la herramienta wc' >&2
        exit 2
    fi
    ```

    Con `wc` disponible termina normalmente con estado cero. El otro camino informa por el canal de errores y utiliza un código que permite al programa que llama reconocer el fallo.

### 2. Conserva el código de una operación

Una comprobación falla y después haces `echo 'Comprobado'`. Al consultar `$?`, obtienes 0. Escribe una secuencia que guarde el estado de `false` antes del mensaje y muestre después ese estado guardado. No uses `set -e` en esta prueba.

??? tip "Pista"
    Cada orden actualiza `$?`; la asignación debe hacerse inmediatamente después de la que interesa.

??? success "Solución paso a paso"
    ```bash
    false
    estado=$?
    echo 'Comprobado'
    echo "Estado de la prueba: $estado"
    ```

    El estado mostrado es 1. El `echo` intermedio no modifica la variable `estado`, aunque sí cambia el significado del `$?` que consultarías después.

### 3. Organiza una investigación

Un script debe procesar dos nombres con espacios, pero recibe cuatro palabras. Explica qué revisarías en la llamada, cómo comprobarías el número de argumentos y qué prueba repetirías después de corregirlo. No cambies el formato de los nombres para ocultar el error.

??? tip "Pista"
    Distingue los datos de cómo la shell los separa antes de ejecutar el script.

??? success "Solución paso a paso"
    1. Revisaría si cada nombre completo está entre comillas al llamar al script.
    2. Observaría `$#` y recorrería `"$@"` con `for argumento in "$@"; do echo "<$argumento>"; done`.
    3. Repetiría la misma llamada con los nombres entrecomillados y comprobaría que hay exactamente dos argumentos completos.

    Cambiar nombres para quitarles espacios evita la prueba, pero no corrige el tratamiento de datos válidos con espacios.

## Palabras clave de este tema

| Término | Significado en este tema |
| --- | --- |
| **Proceso y PID** | Programa en ejecución e identificador que permite distinguirlo. |
| **Señal** | Notificación enviada a un proceso para comunicar un evento o pedir una acción. |
| **Permisos** | Reglas de lectura, escritura y ejecución aplicables a usuarios y grupos. |
| **root y sudo** | Cuenta administradora y herramienta para ejecutar con la identidad permitida por su política. |
| **Servicio o demonio** | Proceso que atiende trabajo en segundo plano; su gestión depende del sistema de inicio. |
| **Directorio Activo (Active Directory)** | Servicio de directorio de Windows que centraliza identidades y recursos; su administración completa corresponde a una unidad posterior. |
| **Paquete y repositorio de paquetes** | Software preparado para instalar y fuente desde la que se distribuye; no equivalen a un repositorio Git. |

!!! success "Para repasar"
    Una comprobación debe producir una decisión y un fallo debe quedar visible. Antes de ejecutar un script, identifica qué modifica y qué necesita para funcionar.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
