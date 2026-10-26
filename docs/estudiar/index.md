# Cómo estudiar y aprender más rápido

Programar (Bash, PowerShell, Python, PHP) y utilizar herramientas como Git o Docker **se aprende haciendo**. Esta página propone un método sencillo para aprovechar mejor las horas de estudio y recordar más.

## 1. Haz, no te limites a leer

Leer unos apuntes puede dar la sensación de entenderlos. Escribir y probar por tu cuenta permite comprobarlo.

| ❌ Estudio pasivo | ✅ Estudio activo |
| --- | --- |
| Releer los apuntes tres veces | Leer **un** ejemplo y escribirlo en el terminal |
| Subrayar | Cambiar el ejemplo y observar qué ocurre |
| Ver vídeos uno detrás de otro | Hacer un ejercicio **sin mirar** la solución |
| Copiar la solución | Intentarlo 15 minutos y consultarla después |

!!! tip "La regla de los 15 minutos"
    Al empezar un tema, dedica los primeros 15 minutos a **hacer** algo que funcione: un `hola.sh` o un `docker run hello-world`. Una comprobación temprana ayuda a continuar con un objetivo concreto.

**La trampa de los tutoriales:** ver tutorial tras tutorial sin crear nada propio retrasa la práctica. Después de cada tutorial, haz **algo diferente** con lo que has aprendido.

## 2. Una sesión de estudio de 50 minutos

```text
 5 min   Recordar SIN mirar: ¿qué hice la última vez? Escríbelo.
25 min   Hacer: leer un apartado y probar CADA ejemplo en el terminal.
 5 min   Descansar lejos de la pantalla.
10 min   Resolver un ejercicio sin mirar la solución.
 5 min   Anotar en tu chuleta lo aprendido y los errores encontrados.
```

- Utiliza una **máquina virtual** para practicar y toma una **instantánea** antes de probar cambios importantes.
- Deja el **móvil fuera** de la mesa. Las interrupciones dificultan mantener la concentración.

## 3. Recordar sin mirar: recuperación activa

Intenta recuperar la información antes de volver a leerla. Así puedes distinguir lo que recuerdas de lo que solo reconoces al verlo.

- Antes de abrir los apuntes, pregúntate: *«¿Cómo era el bucle `for` en Bash?»*. Intenta escribirlo y compruébalo después.
- Tapa la solución de los ejercicios y vuelve a resolverlos unos días más tarde.
- Prepara **tarjetas** en papel o en una aplicación: pregunta delante y respuesta detrás.

| Delante | Detrás |
| --- | --- |
| Bash: comprobar si existe un archivo | `if [[ -f "$archivo" ]]; then ...` |
| Git: deshacer el último commit local sin perder los cambios | `git reset --soft HEAD~1` |
| Docker: ver también los contenedores detenidos | `docker ps -a` |
| PHP: escapar texto al insertarlo en HTML | `htmlspecialchars($x, ENT_QUOTES, 'UTF-8')` |

## 4. Repetición espaciada

Distribuye los repasos a lo largo de los días, en lugar de concentrarlos todos antes del examen.

```text
Día 0: aprender el tema       Día 1: repaso rápido de 10 minutos
Día 3: repasar                Día 7: repasar
Día 15: resolver un ejercicio del tema sin mirar
```

Es una pauta de partida, no un calendario obligatorio. Si recuerdas bien un concepto, separa más los repasos; si lo has olvidado, vuelve a practicarlo antes.

## 5. Explícalo con palabras sencillas

Si no consigues explicar un concepto con claridad, revisa qué parte te falta comprender.

1. Elige un concepto: *«¿Qué es un volumen de Docker?»*.
2. Explícalo en voz alta o por escrito a alguien que empieza.
3. Localiza dónde te atascas o necesitas una palabra técnica que tampoco puedes explicar.
4. Vuelve a ese apartado y repite la explicación.

Explicárselo a un compañero y responder a sus preguntas ayuda a detectar lagunas.

## 6. Aprovecha los errores

Cuando algo falla:

1. **Lee el mensaje completo.** Busca qué operación falla y dónde.
2. **Reprodúcelo:** intenta que falle de la misma manera.
3. **Divide:** prueba cada comando o parte del programa hasta localizar el fallo.
4. **Busca** el mensaje exacto entre comillas si necesitas más contexto.
5. **Anótalo:** error → causa → solución.

| Herramienta | Para qué sirve |
| --- | --- |
| `bash -x script.sh` | Ver cada comando mientras se ejecuta |
| [ShellCheck](https://www.shellcheck.net/) | Detectar problemas habituales en Bash |
| `print()` / `echo` / `Write-Host` | Inspeccionar variables en un punto |
| `php -l archivo.php` | Comprobar la sintaxis de PHP |
| `git status` | Conocer el estado del repositorio |
| `docker logs nombre` | Investigar qué ha ocurrido en un contenedor |

## 7. Problemas grandes → pasos pequeños

Un ejercicio difícil suele contener varias tareas que puedes abordar por separado.

!!! example "Preparar una copia de seguridad diaria y conservar siete días"
    1. Crear un archivo `tar` de una carpeta de prueba desde el terminal.
    2. Añadir la fecha al nombre con `$(date +%F)`.
    3. Guardar los comandos en un script y ejecutarlo.
    4. Localizar copias antiguas con `find -mtime +7`, revisando la selección antes de añadir `-delete`.
    5. Programar la ejecución con `cron`.

    Prueba cada paso antes de pasar al siguiente. La [guía de scripts y depuración de ASO](../aso/06-bash-errors.md) aplica este método a un programa completo.

## 8. Tu chuleta

Prepara una chuleta **propia** de una o dos páginas por lenguaje y complétala conforme practiques. Elegir qué anotar ya exige ordenar lo que sabes. Las tablas de consulta y los recuadros «Para repasar» de cada tema pueden servir como punto de partida.

Guarda tus ejercicios y scripts en un repositorio Git. Haz commits con mensajes claros al terminar cada cambio coherente. Practicarás Git y conservarás un historial de tu aprendizaje.

## 9. Pregunta con datos concretos

| ❌ Pregunta vaga | ✅ Pregunta concreta |
| --- | --- |
| «No me funciona Docker» | «`docker run -p 80:80 nginx` devuelve `port is already allocated`. ¿Qué significa?» |
| «¿Cómo funciona Git?» | «¿Qué ocurre al hacer `git commit` y dónde se guarda?» |
| «Mi script no funciona» | «Este `if` entra por `else` aunque el archivo existe. Este es el código y esta es la salida». |

Incluye **qué quieres hacer**, **qué has probado**, **qué esperabas** y **qué ocurrió**. Muchas veces, al escribirlo, ya encuentras una pista.

## 10. Utilizar la IA para aprender

La IA puede explicar errores y proponer práctica. Para aprender, necesitas seguir entendiendo las decisiones y comprobando los resultados por tu cuenta.

- Pide que te **explique** un error o un comando, o que proponga **ejemplos nuevos**.
- Resuelve tú el ejercicio y pide después una **revisión**.
- Lee el código línea a línea: debes poder explicar qué hace y por qué.
- Revisa y prueba las respuestas. Pueden contener errores o patrones inseguros, como SQL concatenado, HTML sin escapar o credenciales incrustadas.

## 11. Prepara el examen práctico

- Practica con el tiempo disponible en el examen y con las ayudas que permitan sus normas.
- Usa un entorno limpio, parecido al del examen.
- Aprende a consultar `man comando`, `comando --help`, `Get-Help`, `help()` de Python y la ayuda de Git o Docker.
- El día anterior, prioriza un repaso manejable y dormir lo suficiente.

## 12. Automatiza lo que repites

Si repites una tarea varias veces, plantéate convertirla en un script. Practica con problemas propios: ordenar archivos de prueba, preparar copias o crear usuarios de laboratorio en una máquina virtual.

## 13. Cuida el ritmo

Distribuye el trabajo y descansa. Una sesión breve y regular puede resultar más sostenible que una jornada agotadora al final de la semana. Si te bloqueas, anota lo que has probado y vuelve después de una pausa.

!!! success "Para repasar"
    Practica, recuerda sin mirar, reparte los repasos, explica con claridad, anota los errores, divide los problemas y conserva tus ejercicios en Git.

Más ideas sobre cómo escribir buen código: [Consejos de programación](consells.md).
