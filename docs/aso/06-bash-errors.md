# UT1 · 5. Errores, depuración y scripts de administración

## El estado de un comando es información

En shell, 0 indica éxito y otros valores indican otros resultados. `grep` devuelve 1 cuando no encuentra coincidencias: no siempre representa una avería. `$?` cambia con el siguiente comando; a menudo resulta más claro escribir `if comando; then ...`.

`set -u` detecta variables no definidas. `set -e` puede detener el script ante determinados fallos, pero tiene excepciones en condicionales y otras construcciones. `set -o pipefail` hace visible un fallo en una tubería que terminaría con un último comando correcto. Ninguna opción sustituye el tratamiento de los errores esperables.

## Ejemplo resuelto: informe de líneas de un documento

**Problema propio:** recibir un archivo de texto y mostrar cuántas líneas tiene, incluido un nombre con espacios. No copia archivos ni crea usuarios.

```bash
#!/usr/bin/env bash
set -u
if (( $# != 1 )); then
    printf 'Uso: bash informe.sh archivo\n' >&2
    exit 1
fi
archivo=$1
if [[ ! -f "$archivo" || ! -r "$archivo" ]]; then
    printf 'Se necesita un archivo ordinario que se pueda leer.\n' >&2
    exit 2
fi
if lineas=$(wc -l < "$archivo"); then
    printf 'Documento: %s\nLíneas: %s\n' "$archivo" "$lineas"
else
    printf 'No se ha podido completar el recuento.\n' >&2
    exit 3
fi
```

### Prueba guiada

Crea `texto corto.txt` con `printf 'primera\nsegunda\n' > "texto corto.txt"`.

| Llamada | Resultado esperado |
| --- | --- |
| `bash informe.sh "texto corto.txt"` | 2 líneas; estado 0 |
| `bash informe.sh ausente.txt` | Aviso de archivo; estado 2 |
| `bash informe.sh` | Ayuda; estado 1 |

`wc -l` cuenta saltos de línea. Un último fragmento sin salto final no aumenta el recuento. Esa diferencia puede explicar una aparente discrepancia con lo que ves en un editor.

El segundo `if` contempla que el comando falle aunque se haya superado la comprobación previa: entre comprobar y leer, el estado del archivo podría cambiar.

## Cómo depurarlo

`bash -n informe.sh` comprueba la sintaxis sin ejecutar el contenido. `bash -x informe.sh "texto corto.txt"` muestra los comandos expandidos mientras los ejecuta; evita utilizar trazas sobre secretos. Si tienes ShellCheck, `shellcheck informe.sh` ayuda a detectar problemas habituales.

`trap 'printf "Fin del laboratorio\n" >&2' EXIT` ejecuta una acción al salir. También puedes capturar señales o `ERR` según el caso. Utiliza `trap` para limpieza y diagnóstico conscientes, no para ocultar un fallo.

## Aplicación a tareas de administración

Un script de copias combina comprobación del origen, comando de archivado, estado y log. Un lector de CSV debe separar campos sin dividir los espacios, por ejemplo con `while IFS=';' read -r nombre zona; do ...; done < datos.csv` para un formato simple sin comillas internas. Un formato CSV general requiere un lector adecuado.

En gestión de usuarios o servicios, separa **consultar**, **decidir** y **modificar**. Prueba primero la lógica con datos de laboratorio y mensajes de lo que haría. No necesitas ejecutar altas masivas para entender un `if`. Al interpretar un sondeo, recuerda también que una IP que no responde a ping no queda demostrada como libre: puede filtrar ICMP.

!!! success "Para repasar"
    Una comprobación debe producir una decisión y un fallo debe quedar visible. Antes de ejecutar un script, identifica qué modifica y qué necesita para funcionar.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
