# UT2 · 1. Procesos en Linux

## ¿Qué es un proceso?

Un **proceso** es una instancia de un programa que se está ejecutando. Si abres una aplicación o ejecutas una orden, el sistema crea un proceso.

Linux guarda información de cada proceso: PID, PID del padre, estado, prioridad, memoria y archivos abiertos, entre otros datos.

| Concepto | Significado |
|---|---|
| PID | identificador único del proceso |
| PPID | PID del proceso padre |
| estado | situación actual del proceso |
| prioridad | preferencia de CPU |
| descriptores | archivos abiertos por el proceso |

## Estados que debes reconocer

- `R` — Running: ejecutándose o preparado para ejecutarse.
- `S` — Sleeping: esperando un evento; puede ser interrumpido.
- `D` — espera no interrumpible, habitualmente relacionada con E/S.
- `T` — Stopped/Traced: proceso detenido o depurado.
- `Z` — Zombie: ya ha terminado, pero todavía conserva una entrada en la tabla de procesos.
- `X` — Dead: estado transitorio mientras desaparece del sistema.

!!! tip "Idea para recordarlo"
    Un `Z` no es un programa que continúe trabajando: **ya ha terminado**, pero el sistema todavía conserva temporalmente su entrada.

## `ps`: fotografía de los procesos

```bash
ps
ps -e
ps -f
ps -ef
```

`ps` muestra procesos. `-e` incluye todos los procesos y `-f` proporciona información ampliada.

Ejemplo útil:

```bash
ps -u alumno -o pid,stat,%cpu,%mem,cmd
```

Muestra los procesos de `alumno` con las columnas que nos interesan.

Buscar por nombre:

```bash
ps -C bash -o pid,user,%cpu,cmd
pgrep bash
pgrep -a bash
```

`pgrep` es especialmente cómodo cuando solo quieres encontrar PID asociados a un nombre.

## `pstree`

```bash
pstree
```

Muestra los procesos como un árbol y ayuda a entender la relación **padre → hijo**.

## `top` y `htop`

`top` actualiza la información continuamente y permite ver consumo de CPU, memoria, swap y procesos activos.

```bash
top
```

Para obtener, sin entrar en `top`, los cinco procesos que más CPU consumen:

```bash
ps -eo pid,user,%cpu,comm --sort=-%cpu | head -n 6
```

`--sort=-%cpu` ordena de mayor a menor. `head -n 6` deja la cabecera y cinco procesos.

## Ejemplo de diagnóstico

Si un equipo va lento:

```bash
ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head
```

No mates inmediatamente el primer proceso. Primero identifícalo, comprueba quién lo ha iniciado y si el consumo es esperable. Administrar procesos también consiste en **diagnosticar antes de actuar**.