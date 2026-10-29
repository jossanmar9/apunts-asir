# UT2 · 1. Processos en Linux

## Què és un procés?

Un **procés** és una instància d'un programa que s'està executant. Si obris una aplicació o executes una ordre, el sistema crea un procés.

Linux guarda informació de cada procés: PID, PID del pare, estat, prioritat, memòria i fitxers oberts, entre altres dades.

| Concepte | Significat |
|---|---|
| PID | identificador únic del procés |
| PPID | PID del procés pare |
| estat | situació actual del procés |
| prioritat | preferència de CPU |
| descriptors | fitxers oberts pel procés |

## Estats que has de reconéixer

- `R` — Running: executant-se o preparat per executar-se.
- `S` — Sleeping: esperant un esdeveniment; pot ser interromput.
- `D` — espera no interrompible, habitualment relacionada amb E/S.
- `T` — Stopped/Traced: procés detingut o depurat.
- `Z` — Zombie: ja ha acabat, però encara conserva una entrada en la taula de processos.
- `X` — Dead: estat transitori mentre desapareix del sistema.

!!! tip "Idea per recordar-ho"
    Un `Z` no és un programa que continue treballant: **ja ha acabat**, però el sistema encara conserva temporalment la seua entrada.

## `ps`: fotografia dels processos

```bash
ps
ps -e
ps -f
ps -ef
```

`ps` mostra processos. `-e` inclou tots els processos i `-f` dona informació ampliada.

Exemple útil:

```bash
ps -u alumne -o pid,stat,%cpu,%mem,cmd
```

Mostra els processos d'`alumne` amb les columnes que ens interessen.

Buscar per nom:

```bash
ps -C bash -o pid,user,%cpu,cmd
pgrep bash
pgrep -a bash
```

`pgrep` és especialment còmode quan només vols trobar PID associats a un nom.

## `pstree`

```bash
pstree
```

Mostra els processos com un arbre i ajuda a entendre la relació **pare → fill**.

## `top` i `htop`

`top` actualitza la informació contínuament i permet veure consum de CPU, memòria, swap i processos actius.

```bash
top
```

Per obtindre, sense entrar en `top`, els cinc processos que més CPU gasten:

```bash
ps -eo pid,user,%cpu,comm --sort=-%cpu | head -n 6
```

`--sort=-%cpu` ordena de major a menor. `head -n 6` deixa la capçalera i cinc processos.

## Exemple de diagnòstic

Si un equip va lent:

```bash
ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head
```

No mates immediatament el primer procés. Primer identifica'l, comprova qui l'ha iniciat i si el consum és esperable. Administrar processos és també **diagnosticar abans d'actuar**.