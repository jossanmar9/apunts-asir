# UT2 · 2. Control de processos, senyals i prioritats

## Primer i segon pla

En primer pla, la terminal espera que el procés acabe. Amb `&` el llances en segon pla:

```bash
sleep 300 &
```

```bash
jobs
```

`jobs` mostra els treballs de la shell actual.

Per suspendre un procés en primer pla: ++ctrl+z++.

```bash
bg %1
fg %1
```

`bg` continua un treball suspés en segon pla; `fg` el porta al primer pla.

## Senyals i `kill`

`kill` envia una **senyal** a un procés. No significa necessàriament «matar».

```bash
kill -15 2345
```

Senyals principals del tema:

| Senyal | Ús |
|---|---|
| `SIGHUP` / `-1` | habitualment recarregar/reiniciar segons el programa |
| `SIGTERM` / `-15` | demanar una finalització ordenada |
| `SIGKILL` / `-9` | finalització immediata i forçada |

Regla pràctica del material: prova primer `SIGTERM` i reserva `SIGKILL` per a quan siga necessari.

```bash
kill -15 2345
ps -p 2345
kill -9 2345
```

`killall` treballa per nom:

```bash
killall nom_programa
```

!!! warning
    No uses `kill -9` com a primera opció per costum. El procés no té oportunitat de tancar fitxers ni alliberar recursos ordenadament.

## Comprovar si un PID existeix

```bash
ps -p 2345
echo "$?"
```

Un codi `0` indica que `ps` ha trobat el procés; un altre codi indica que no.

## `nice` i `renice`

El valor **nice** va de `-20` a `19`.

- Valor nice més baix → més prioritat.
- Valor nice més alt → menys prioritat.
- Un usuari normal pot reduir la prioritat dels seus processos augmentant el nice.
- `root` pot utilitzar tot el rang.

Iniciar amb prioritat diferent:

```bash
nice -n 10 sleep 300 &
```

Canviar-la després:

```bash
renice -n 15 -p 2345
sudo renice -n -5 -p 2345
```

Veure el valor:

```bash
ps -o pid,ni,cmd -p 2345
```

## `$!`: PID de l'últim procés en segon pla

```bash
sleep 300 &
pid=$!
echo "$pid"
ps -p "$pid" -o pid,stat,ni,cmd
```

És molt útil en scripts perquè no has d'endevinar el PID.

## `nohup`

Per a una tasca llarga que ha de continuar encara que tanques la sessió:

```bash
nohup ./copia.sh &
```

## `lsof`

`lsof` permet veure fitxers oberts pels processos. És útil, per exemple, quan no pots desmuntar un recurs perquè algun procés l'està utilitzant.

## Exemple complet

```bash
sleep 600 &
pid=$!
echo "PID: $pid"
renice -n 10 -p "$pid"
ps -p "$pid" -o pid,stat,ni,cmd
kill -15 "$pid"
```

Ací practiques segon pla, `$!`, prioritat, consulta i finalització ordenada.