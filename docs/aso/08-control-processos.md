# UT2 · 2. Control de procesos, señales y prioridades

## Primer y segundo plano

En primer plano, la terminal espera a que el proceso termine. Con `&` lo lanzas en segundo plano:

```bash
sleep 300 &
```

```bash
jobs
```

`jobs` muestra los trabajos de la shell actual.

Para suspender un proceso en primer plano: ++ctrl+z++.

```bash
bg %1
fg %1
```

`bg` continúa un trabajo suspendido en segundo plano; `fg` lo lleva al primer plano.

## Señales y `kill`

`kill` envía una **señal** a un proceso. No significa necesariamente «matar».

```bash
kill -15 2345
```

Señales principales del tema:

| Señal | Uso |
|---|---|
| `SIGHUP` / `-1` | habitualmente recargar/reiniciar según el programa |
| `SIGTERM` / `-15` | solicitar una finalización ordenada |
| `SIGKILL` / `-9` | finalización inmediata y forzada |

Regla práctica del material: prueba primero `SIGTERM` y reserva `SIGKILL` para cuando sea necesario.

```bash
kill -15 2345
ps -p 2345
kill -9 2345
```

`killall` trabaja por nombre:

```bash
killall nombre_programa
```

!!! warning
    No uses `kill -9` como primera opción por costumbre. El proceso no tiene oportunidad de cerrar archivos ni liberar recursos de forma ordenada.

## Comprobar si existe un PID

```bash
ps -p 2345
echo "$?"
```

Un código `0` indica que `ps` ha encontrado el proceso; otro código indica que no.

## `nice` y `renice`

El valor **nice** va de `-20` a `19`.

- Valor nice más bajo → más prioridad.
- Valor nice más alto → menos prioridad.
- Un usuario normal puede reducir la prioridad de sus procesos aumentando el nice.
- `root` puede utilizar todo el rango.

Iniciar con una prioridad diferente:

```bash
nice -n 10 sleep 300 &
```

Cambiarla después:

```bash
renice -n 15 -p 2345
sudo renice -n -5 -p 2345
```

Ver el valor:

```bash
ps -o pid,ni,cmd -p 2345
```

## `$!`: PID del último proceso en segundo plano

```bash
sleep 300 &
pid=$!
echo "$pid"
ps -p "$pid" -o pid,stat,ni,cmd
```

Es muy útil en scripts porque no tienes que adivinar el PID.

## `nohup`

Para una tarea larga que debe continuar aunque cierres la sesión:

```bash
nohup ./copia.sh &
```

## `lsof`

`lsof` permite ver archivos abiertos por los procesos. Es útil, por ejemplo, cuando no puedes desmontar un recurso porque algún proceso lo está utilizando.

## Ejemplo completo

```bash
sleep 600 &
pid=$!
echo "PID: $pid"
renice -n 10 -p "$pid"
ps -p "$pid" -o pid,stat,ni,cmd
kill -15 "$pid"
```

Aquí practicas segundo plano, `$!`, prioridad, consulta y finalización ordenada.