# Consejos de programación

Una selección de ideas sobre programación clara, práctica y mantenimiento del código, aplicada a Bash, Python, PowerShell y PHP. Conserva los temas de la sección anterior del repositorio, con explicaciones en castellano. Las referencias entre paréntesis recogen las atribuciones utilizadas en aquella selección.

## 1. El código se lee mucho más de lo que se escribe (Guido van Rossum)

Pasas tiempo leyendo código propio y ajeno. Escribe pensando también en quien tenga que entenderlo dentro de unos meses.

```bash
# ❌ Nombres poco claros y división incorrecta de nombres con espacios
for a in $(ls /home); do du -sh /home/$a; done

# ✅ El recorrido y la intención se entienden mejor
for usuario in /home/*/; do
    du -sh "$usuario"
done
```

Léelo en voz alta: ¿puedes explicar qué recorre y qué hace con cada elemento?

## 2. Los nombres explican la intención (Robert C. Martin)

Un nombre preciso puede ahorrar un comentario. Estos fragmentos son esquemas: las colecciones y las funciones tendrían que definirse en el programa completo.

```python
# ❌ Poco contexto
d = 7
for f in fs:
    if edad(f) > d: ...

# ✅ La regla queda visible
DIAS_A_CONSERVAR = 7
for copia in copias:
    if dias_desde(copia) > DIAS_A_CONSERVAR: ...
```

Usa nombres de datos para las variables, como `total_alumnos` o `archivo_log`, y acciones para las funciones, como `crear_usuario` o `comprobar_disco`. En PowerShell, los cmdlets siguen la forma `Verbo-Sustantivo`, como `Get-Service`.

## 3. Una función tiene una responsabilidad clara (Robert C. Martin)

Si valida, calcula, escribe archivos y envía mensajes, resulta difícil probarla. Divide responsabilidades para que el flujo principal se lea como un índice. Este ejemplo es pseudocódigo de shell con funciones todavía por implementar:

```bash
main() {
    comprobar_permisos
    crear_carpeta_copias
    hacer_copia "/home"
    borrar_copias_antiguas 7
}
```

## 4. Divide el problema en partes manejables (Edsger W. Dijkstra)

Antes de programar, escribe los pasos y resuélvelos uno a uno, **probando cada paso**. Consulta el [método complementario](../bash/metode.md).

## 5. Haz que funcione y después mejóralo (Kent Beck)

Empieza por una versión sencilla que cumpla el objetivo. Después mejora nombres, funciones y duplicaciones. Optimiza cuando exista una necesidad concreta y puedas medirla.

## 6. La sencillez ayuda a mantener la fiabilidad (Dijkstra)

Elige una solución que puedas explicar y depurar. Una expresión compacta no es necesariamente más clara.

```python
numeros = [1, 2, 3, 4]

# ❌ La intención cuesta más de leer
r = [x * 2 for x in numeros if not x % 2]

# ✅ Dos pasos con nombres descriptivos
pares = [n for n in numeros if n % 2 == 0]
dobles = [n * 2 for n in pares]
print(dobles)  # [4, 8]
```

## 7. Haz explícitas las decisiones (Guido van Rossum)

El programa debe mostrar qué presupone y cómo actúa. Opciones como `set -u` o `pipefail` ayudan, pero debes entender sus efectos y tratar los fallos esperables.

```bash
# Comprobar una ruta antes de trabajar con ella
if [[ -z "${CARPETA_TRABAJO:-}" ]]; then
    printf 'Falta definir CARPETA_TRABAJO\n' >&2
    exit 1
fi
```

En PowerShell, muchas operaciones admiten `-WhatIf` para consultar qué harían antes de ejecutarlas:

```powershell
Remove-Item -Path $Carpeta -Recurse -WhatIf
```

## 8. El mensaje de error debe ayudar (Evan Czaplicki)

Explica qué ha ocurrido y cómo continuar.

```bash
if [[ ! -f "${1:-}" ]]; then
    printf 'Error: indica un archivo existente.\n' >&2
    printf 'Uso: %s archivo_usuarios.txt\n' "$0" >&2
    exit 1
fi
```

## 9. Para corregir un fallo, reprodúcelo primero (Julia Evans)

Observa, formula una hipótesis, consigue reproducir el fallo, corrige y vuelve a comprobar. Cambiar cosas al azar puede ocultar el problema sin entenderlo.

## 10. Si lo repites, considera automatizarlo (Jeff Atwood)

La repetición revela oportunidades para practicar scripts y ahorrar pasos. Antes de automatizar, entiende el procedimiento manual y cómo detectar sus errores.

## 11. Git conserva el motivo de los cambios (Julia Evans, Linus Torvalds)

Un mensaje útil explica por qué cambió el proyecto.

```bash
# ❌ Poco informativo
git commit -m "fix"

# ✅ Cambio concreto
git commit -m "Corrige la copia de carpetas con espacios"
git commit -m "Añade la validación del correo al formulario"
```

Haz commits pequeños y coherentes, con un título breve en presente: «Añade», «Corrige» o «Elimina». Consulta el [tema independiente de Git y GitHub](../git-github/index.md).

## 12. El terminal permite repetir procesos (Jessie Frazelle)

Conocer el terminal ayuda a repetir tareas y automatizarlas. Los contenedores permiten probar programas en entornos separados; por ejemplo, `docker run --rm -it ubuntu bash` abre una shell en un contenedor temporal, si Docker está disponible.

## 13. La seguridad empieza al escribir el código (Parisa Tabriz)

Tres hábitos para aplicaciones web:

1. **Valida** lo que llega del usuario.
2. **Escapa** los datos al insertarlos en el contexto de salida correspondiente.
3. **Prepara** las consultas a la base de datos en lugar de concatenar entradas.

Mantén las credenciales reales fuera del código y del historial de Git.

## 14. Revisa el código generado por IA (Andrej Karpathy)

Una respuesta puede parecer correcta y contener un fallo lógico o de seguridad. Entiende las decisiones, revisa los datos que recibe y prueba casos correctos e incorrectos. Las bases que estudias te permiten valorar la propuesta.

## 15. Comprueba si ya existe una herramienta (Kent C. Dodds)

Antes de escribir un script largo, revisa comandos o módulos como `rsync`, `find`, `pathlib` o `Get-ChildItem`. Si el objetivo es aprender a implementar algo, construir una versión propia también puede ser un buen ejercicio.

## 16. Aprende construyendo y explicando (Limor Fried, Cassidy Williams)

Crea algo útil a pequeña escala: un script, una web local o una aplicación sencilla. Documenta lo aprendido y explícalo; las preguntas de otra persona pueden revelar detalles que no habías entendido.

## 17. Pregunta lo que no sepas (Julia Evans)

Formula dudas concretas: «¿Qué ocurre cuando escribo `ls` y pulso Intro?». Anota la respuesta y prepara una prueba que te permita comprobarla.

## 18. Cuida tu salud (Cassidy Williams)

Descansa y organiza un ritmo sostenible. Tu aprendizaje no se mide solo por las horas delante de la pantalla.

!!! success "Para repasar"
    Código claro, responsabilidades pequeñas, pruebas paso a paso, mensajes útiles y cambios guardados en Git. Aprende haciendo y revisando lo que haces.
