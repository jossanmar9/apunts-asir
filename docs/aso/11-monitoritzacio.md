# UT2 · 5. Monitorització, logs i diagnòstic

Administrar no és només iniciar i parar processos. També cal saber **què està passant**, trobar el coll de botella i consultar registres.

## Tres tipus d'informació

- **Mètriques**: valors numèrics al llarg del temps: CPU, memòria, E/S...
- **Logs**: missatges amb marca temporal sobre esdeveniments.
- **Estat actual**: fotografia del sistema en un moment concret.

## Començar per `top`

```bash
top
```

És una primera ullada útil per veure CPU, memòria, swap i processos que destaquen.

## `vmstat`

```bash
vmstat 1
```

Mostra periòdicament informació sobre processos, memòria, paginació, E/S i CPU. És útil per saber si el problema sembla general i si hi ha pressió de memòria o espera.

## `iostat`

```bash
iostat
```

Ajuda a estudiar CPU i dispositius d'E/S. Si sospites que el disc és el coll de botella, és una eina adequada per aprofundir.

## `sar`

`sar` permet consultar estadístiques de rendiment del sistema. El tema el presenta com una eina de mètriques junt amb `top` i `vmstat`.

## Una seqüència fàcil de recordar

Quan «el servidor va lent»:

```text
1. top      → què destaca ara?
2. vmstat   → CPU, memòria, espera, E/S?
3. iostat   → el problema apunta als discos?
4. logs     → hi ha errors que expliquen el símptoma?
```

No és una recepta universal, però és una bona seqüència de diagnòstic per a la unitat.

## `journalctl`

Consultar el journal:

```bash
journalctl
```

Filtrar per una unitat:

```bash
journalctl -u ssh
```

Últimes 50 entrades:

```bash
journalctl -u ssh -n 50
```

Seguir els missatges mentre apareixen:

```bash
journalctl -f
```

## Logs tradicionals

També trobaràs registres en `/var/log`. Pots combinar les eines de la UT1:

```bash
grep -i "error" /var/log/syslog
tail -n 50 /var/log/syslog
```

Això és important: **UT2 reutilitza Bash**. Pipes, `grep`, redireccions i scripts continuen sent eines d'administració.

## `logrotate`

Els logs poden créixer indefinidament. `logrotate` permet rotar-los per conservar històric sense mantindre un únic fitxer enorme.

Conceptualment:

```text
app.log
app.log.1
app.log.2.gz
...
```

## Exemple de diagnòstic d'un servei

Suposa que SSH no respon:

```bash
systemctl status ssh
ps -C sshd -o pid,stat,%cpu,%mem,cmd
journalctl -u ssh -n 50
```

Cada ordre respon una pregunta diferent:

1. `systemctl status` → està actiu el servei?
2. `ps` → existeixen els processos i en quin estat estan?
3. `journalctl` → què ha registrat el servei?

## Què prioritzaria per a l'examen de la UT2

1. Procés, PID, PPID i estats `R`, `S`, `D`, `T`, `Z`.
2. `ps`, `pstree`, `top`, `pgrep`.
3. Primer/segon pla: `&`, `jobs`, `fg`, `bg`, ++ctrl+z++.
4. `SIGTERM` vs `SIGKILL`.
5. `nice` i `renice`.
6. Concepte de servei i `systemctl`.
7. Diferència entre `start` i `enable`.
8. Sintaxi de `cron` i diferència `cron`/`at`.
9. `journalctl` i `/var/log`.
10. Saber plantejar una seqüència de diagnòstic.

!!! tip "Forma de practicar"
    Obri dos terminals. En un crea processos amb `sleep`, posa'ls en segon pla i canvia'n l'estat; en l'altre observa'ls amb `ps`, `pstree` i `top`. Aprendràs molt més ràpid que memoritzant la taula d'ordres.