# 11. find, grep i xargs

## `grep`: buscar text

```bash
grep "ERROR" app.log           # línies que contenen ERROR
grep -i "error" app.log        # sense distingir majúscules
grep -v "^#" sshd_config       # les que NO comencen per #
grep -c "ERROR" app.log        # quantes línies
grep -n "ERROR" app.log        # amb número de línia
grep -r "Listen" /etc/apache2  # recursiu
grep -rl "password" .          # només els noms de fitxer
grep -w "root" /etc/passwd     # paraula sencera
grep -E "ERROR|WARN" app.log   # expressions regulars esteses
grep -o "[0-9]\+\.[0-9]\+\.[0-9]\+\.[0-9]\+" access.log   # només el tros que coincidix
grep -A2 -B1 "Failed" auth.log # 2 línies després i 1 abans
grep -q "^pep:" /etc/passwd && echo existix   # silenciós, per a if
```

### Expressions regulars bàsiques

| Patró | Significa |
| ----- | --------- |
| `^` | principi de línia |
| `$` | final de línia |
| `.` | qualsevol caràcter |
| `*` | 0 o més del caràcter anterior |
| `+` | 1 o més (amb `-E`) |
| `[abc]` | un d'eixos |
| `[^abc]` | qualsevol menys eixos |
| `[0-9]` | un dígit |
| `\b` | límit de paraula |

## `find`: buscar fitxers

```bash
find /var/log -name "*.log"            # per nom (amb cometes!)
find . -iname "*.JPG"                  # sense distingir majúscules
find . -type f                         # només fitxers (d = directoris)
find / -size +100M 2>/dev/null         # més de 100 MB
find /tmp -mtime +7                    # modificats fa més de 7 dies
find /home -user pep                   # d'un usuari
find . -perm -o+w                      # escrivibles per a tots
find . -maxdepth 1 -type d             # sense entrar en subdirectoris
find . -empty                          # buits
find . -name "*.tmp" -delete           # esborrar-los
find . -name "*.sh" -exec chmod +x {} \;   # una ordre per fitxer
find . -name "*.sh" -exec chmod +x {} +    # una ordre amb tots (més ràpid)
```

Combinar condicions: `-a` (i, per defecte), `-o` (o), `!` (no), i parèntesis escapats:

```bash
find . \( -name "*.log" -o -name "*.tmp" \) -mtime +30
```

## `xargs`: convertir una llista en arguments

Algunes ordres no lligen de stdin, volen arguments. `xargs` agafa el que li arriba per la tuberia i ho posa com a arguments:

```bash
find . -name "*.tmp" | xargs rm
cat servidors.txt | xargs -n1 ping -c1     # una execució per línia
echo "a b c" | xargs -n1                   # un per línia
find . -name "*.sh" | xargs grep -n "TODO" # busca en tots els .sh
ls *.txt | xargs -I{} cp {} /backup/{}.bak # {} = cada element
```

!!! warning "Noms amb espais"
    `xargs` separa per espais. Si els noms poden tindre espais, usa `find ... -print0 | xargs -0 ...`.

## Exemple: buscar una paraula en tots els `.sh`

Mostra nom de fitxer, número de línia i el text, recorrent subdirectoris:

```bash title="busca.sh"
#!/bin/bash
[ $# -eq 1 ] || { echo "Ús: $0 paraula" >&2; exit 1; }

find . -type f -name "*.sh" -print0 |
    xargs -0 grep -n -- "$1" |
    while IFS=: read -r fitxer linia text; do
        printf "%-30s %4s  %s\n" "$fitxer" "$linia" "$text"
    done
```

El `--` evita que una paraula que comence per `-` es prenga com a opció de `grep`.
