# UT2 · 5. Monitorización, logs y diagnóstico

Administrar no consiste solo en iniciar y detener procesos. También hay que saber **qué está pasando**, encontrar el cuello de botella y consultar registros.

## Tres tipos de información

- **Métricas**: valores numéricos a lo largo del tiempo: CPU, memoria, E/S...
- **Logs**: mensajes con marca temporal sobre acontecimientos.
- **Estado actual**: fotografía del sistema en un momento concreto.

## Empezar por `top`

```bash
top
```

Es una primera vista útil para ver CPU, memoria, swap y procesos que destacan.

## `vmstat`

```bash
vmstat 1
```

Muestra periódicamente información sobre procesos, memoria, paginación, E/S y CPU. Es útil para saber si el problema parece general y si hay presión de memoria o espera.

## `iostat`

```bash
iostat
```

Ayuda a estudiar CPU y dispositivos de E/S. Si sospechas que el disco es el cuello de botella, es una herramienta adecuada para profundizar.

## `sar`

`sar` permite consultar estadísticas de rendimiento del sistema. El tema lo presenta como una herramienta de métricas junto con `top` y `vmstat`.

## Una secuencia fácil de recordar

Cuando «el servidor va lento»:

```text
1. top      → ¿qué destaca ahora?
2. vmstat   → ¿CPU, memoria, espera, E/S?
3. iostat   → ¿el problema apunta a los discos?
4. logs     → ¿hay errores que expliquen el síntoma?
```

No es una receta universal, pero es una buena secuencia de diagnóstico para la unidad.

## `journalctl`

Consultar el journal:

```bash
journalctl
```

Filtrar por una unidad:

```bash
journalctl -u ssh
```

Últimas 50 entradas:

```bash
journalctl -u ssh -n 50
```

Seguir los mensajes mientras aparecen:

```bash
journalctl -f
```

## Logs tradicionales

También encontrarás registros en `/var/log`. Puedes combinar las herramientas de la UT1:

```bash
grep -i "error" /var/log/syslog
tail -n 50 /var/log/syslog
```

Esto es importante: **UT2 reutiliza Bash**. Pipes, `grep`, redirecciones y scripts continúan siendo herramientas de administración.

## `logrotate`

Los logs pueden crecer indefinidamente. `logrotate` permite rotarlos para conservar un histórico sin mantener un único archivo enorme.

Conceptualmente:

```text
app.log
app.log.1
app.log.2.gz
...
```

## Ejemplo de diagnóstico de un servicio

Supón que SSH no responde:

```bash
systemctl status ssh
ps -C sshd -o pid,stat,%cpu,%mem,cmd
journalctl -u ssh -n 50
```

Cada orden responde a una pregunta diferente:

1. `systemctl status` → ¿está activo el servicio?
2. `ps` → ¿existen los procesos y en qué estado están?
3. `journalctl` → ¿qué ha registrado el servicio?

## Qué priorizaría para el examen de la UT2

1. Proceso, PID, PPID y estados `R`, `S`, `D`, `T`, `Z`.
2. `ps`, `pstree`, `top`, `pgrep`.
3. Primer/segundo plano: `&`, `jobs`, `fg`, `bg`, ++ctrl+z++.
4. `SIGTERM` frente a `SIGKILL`.
5. `nice` y `renice`.
6. Concepto de servicio y `systemctl`.
7. Diferencia entre `start` y `enable`.
8. Sintaxis de `cron` y diferencia `cron`/`at`.
9. `journalctl` y `/var/log`.
10. Saber plantear una secuencia de diagnóstico.

!!! tip "Forma de practicar"
    Abre dos terminales. En uno crea procesos con `sleep`, ponlos en segundo plano y cambia su estado; en el otro obsérvalos con `ps`, `pstree` y `top`. Aprenderás mucho más rápido que memorizando la tabla de órdenes.