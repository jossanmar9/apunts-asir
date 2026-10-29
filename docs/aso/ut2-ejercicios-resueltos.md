## Ejercicios resueltos paso a paso · UT2

### Procesos

#### Ejercicio 1 · Listar procesos
```bash
ps aux
```
`ps` muestra procesos; `a` incluye procesos de otros usuarios, `u` añade información de usuario y recursos, y `x` incluye procesos sin terminal. Observa PID, CPU y memoria.

#### Ejercicio 2 · Buscar un proceso
```bash
pgrep -a ssh
```
`pgrep` busca procesos por nombre y `-a` muestra también la línea de órdenes. Es más directo que filtrar manualmente una lista completa.

#### Ejercicio 3 · Ver procesos en tiempo real
```bash
top
```
`top` actualiza periódicamente la información. Permite observar carga, CPU, memoria y procesos que más recursos consumen.

### Control de procesos

#### Ejercicio 1 · Trabajo en segundo plano
```bash
sleep 300 &
jobs
```
`&` inicia `sleep` en segundo plano. `jobs` muestra los trabajos asociados a la shell actual.

#### Ejercicio 2 · Terminar correctamente
```bash
pgrep sleep
kill PID
```
Primero se localiza el PID. `kill` sin indicar señal envía `SIGTERM`, que solicita una terminación ordenada. Sustituye `PID` por el número real.

#### Ejercicio 3 · Prioridad
```bash
nice -n 10 comando
```
`nice` inicia un proceso con una prioridad modificada. Un valor *nice* mayor implica normalmente menor prioridad de CPU frente a otros procesos.

### systemd y servicios

#### Ejercicio 1 · Consultar estado
```bash
systemctl status ssh
```
`systemctl` habla con `systemd`; `status` solicita el estado y `ssh` identifica la unidad. Debes distinguir `active`, `inactive` y `failed`.

#### Ejercicio 2 · Iniciar y habilitar
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```
`start` lo inicia ahora. `enable` configura su arranque automático. Son acciones distintas y conviene no confundirlas.

#### Ejercicio 3 · Consultar registros
```bash
journalctl -u nginx --since today
```
`journalctl` consulta el diario de systemd; `-u nginx` filtra la unidad y `--since today` limita el periodo.

### Automatización

#### Ejercicio 1 · Cron diario
```cron
0 2 * * * /home/alumno/backup.sh
```
Los cinco campos significan minuto, hora, día del mes, mes y día de la semana. `0 2 * * *` ejecuta el script todos los días a las 02:00.

#### Ejercicio 2 · Script de copia
```bash
#!/usr/bin/env bash
fecha=$(date +%F)
tar -czf "/copias/etc-$fecha.tar.gz" /etc
```
`$(...)` captura la salida de `date`; `%F` genera una fecha tipo `2026-10-29`; `tar -czf` crea un archivo comprimido con `/etc`.

#### Ejercicio 3 · Comprobar antes de automatizar
```bash
#!/usr/bin/env bash
set -e
mkdir -p /copias
tar -czf /copias/etc.tar.gz /etc
```
`mkdir -p` garantiza que el destino exista y no falla si ya existe. `set -e` hace que el script no continúe tras un error no controlado.

### Monitorización

#### Ejercicio 1 · Memoria
```bash
free -h
```
`free` muestra memoria RAM y swap; `-h` usa unidades legibles. Fíjate especialmente en memoria disponible, no solo en la columna `free`.

#### Ejercicio 2 · Disco
```bash
df -h /
```
`df` informa del uso de sistemas de archivos; `-h` usa GB/MB y `/` limita la consulta al sistema donde está la raíz.

#### Ejercicio 3 · Carga y tiempo encendido
```bash
uptime
```
`uptime` muestra cuánto tiempo lleva encendido el sistema, usuarios conectados y medias de carga. Las tres medias corresponden aproximadamente a 1, 5 y 15 minutos.

!!! warning "Administración segura"
    En los ejercicios con `sudo`, `kill`, servicios o copias, identifica primero qué recurso vas a modificar. En administración de sistemas, entender el efecto de una orden es parte del ejercicio.