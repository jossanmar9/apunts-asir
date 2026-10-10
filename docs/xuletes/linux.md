# Ordres de Linux

## Fitxers i directoris

| Comandament | Què fa |
| ----------- | ------ |
| `ls -lah` | Llista amb detalls i ocults |
| `cd -` | Torna al directori anterior |
| `cp -r orig dest` | Copia recursivament |
| `mv a b` | Mou o reanomena |
| `rm -rf dir` | Esborra sense preguntar (compte!) |
| `find / -name "*.log"` | Busca fitxers per nom |
| `du -sh *` | Mida de cada element |
| `df -h` | Espai lliure als discos |

## Text

| Comandament | Què fa |
| ----------- | ------ |
| `grep -rni "text" dir/` | Busca text recursivament |
| `cut -d: -f1 /etc/passwd` | Talla columnes |
| `sort \| uniq -c` | Ordena i compta repetits |
| `wc -l` | Compta línies |
| `tail -f fitxer.log` | Segueix un log en directe |
| `sed 's/vell/nou/g'` | Substitueix text |
| `awk '{print $1}'` | Imprimeix la 1a columna |

## Usuaris i permisos

| Comandament | Què fa |
| ----------- | ------ |
| `sudo useradd -m -s /bin/bash pep` | Crea usuari amb home |
| `sudo passwd pep` | Canvia contrasenya |
| `sudo usermod -aG sudo pep` | Afig a un grup |
| `chmod 755 script.sh` | rwx r-x r-x |
| `chown usuari:grup fitxer` | Canvia propietari |
| `id`, `groups` | Qui soc i en quins grups |

## Processos i serveis

| Comandament | Què fa |
| ----------- | ------ |
| `ps aux \| grep nom` | Busca un procés |
| `top` / `htop` | Monitor en directe |
| `kill -9 PID` | Mata un procés |
| `systemctl status nom` | Estat d'un servei |
| `systemctl enable --now nom` | Activa i arranca |
| `journalctl -u nom -f` | Logs d'un servei |

## Xarxa

| Comandament | Què fa |
| ----------- | ------ |
| `ip a` | Interfícies i IPs |
| `ip r` | Taula d'encaminament |
| `ss -tulpn` | Ports en escolta |
| `ping -c 4 host` | Prova connectivitat |
| `dig domini` | Consulta DNS |
| `ssh usuari@host` | Connexió remota |
| `scp fitxer usuari@host:/ruta` | Copia per SSH |

!!! tip "Scripting"
    Per a la sintaxi de Bash (variables, if, bucles, funcions) mira la [xuleta de Bash](bash.md).
