# 11. find, grep i xargs

Tres eines per a **buscar**:

| Eina | Busca... |
| ---- | -------- |
| `grep` | **text dins** dels fitxers |
| `find` | **fitxers** (per nom, mida, data...) |
| `xargs` | no busca: passa una llista (per exemple, la de `find`) a una altra ordre |

## `grep`: buscar text dins dels fitxers

`grep` mostra les línies que contenen el text que busques:

```bash
grep "ERROR" app.log            # les línies d'app.log que contenen ERROR
```

### Opcions més útils

| Opció | Què fa | Exemple |
| ----- | ------ | ------- |
| `-i` | no distingix majúscules | `grep -i "error" app.log` |
| `-v` | les línies que **no** contenen el text | `grep -v "^#" config` |
| `-c` | **compta** quantes línies coincidixen | `grep -c "ERROR" app.log` |
| `-n` | mostra el número de línia | `grep -n "ERROR" app.log` |
| `-r` | busca en tots els fitxers d'una carpeta | `grep -r "Listen" /etc/apache2` |
| `-l` | només mostra el nom dels fitxers | `grep -rl "password" .` |
| `-w` | paraula sencera (`root` però no `chroot`) | `grep -w "root" /etc/passwd` |
| `-q` | no mostra res, només diu si ho ha trobat (per a `if`) | `if grep -q "ana" f; then` |
| `-E` | permet expressions regulars avançades (<code>&#124;</code>, `+`) | <code>grep -E "ERROR&#124;WARN" app.log</code> |

### Patrons: buscar formes, no paraules exactes

Les **expressions regulars** són una manera de descriure "formes" de text. Les bàsiques:

| Símbol | Significa | Exemple | Troba |
| ------ | --------- | ------- | ----- |
| `^` | principi de línia | `^#` | línies que comencen per `#` |
| `$` | final de línia | `bash$` | línies que acaben en `bash` |
| `.` | qualsevol caràcter | `c.t` | `cat`, `cot`, `c9t` |
| `*` | el d'abans, 0 o més vegades | `ab*c` | `ac`, `abc`, `abbbc` |
| `[abc]` | un d'eixos caràcters | `[Ee]rror` | `Error`, `error` |
| `[0-9]` | un dígit | `[0-9][0-9]` | dos dígits seguits |
| `[^0-9]` | qualsevol cosa que **no** siga dígit | | |

```bash
grep "^ana:" /etc/passwd        # la línia de l'usuari ana (comença per "ana:")
grep -v "^$" fitxer             # les línies que NO estan buides
grep -v "^#" fitxer | grep -v "^$"   # sense comentaris ni línies buides
```

## `find`: buscar fitxers

```bash
find ON -CRITERI VALOR
```

```bash
find /home -name "*.pdf"        # tots els .pdf dins de /home (i subcarpetes)
```

!!! warning "Posa el patró entre cometes"
    `find . -name *.txt` pot fallar. Escriu sempre `find . -name "*.txt"`.

### Criteris més útils

| Criteri | Busca | Exemple |
| ------- | ----- | ------- |
| `-name "x"` | per nom | `find . -name "*.log"` |
| `-iname "x"` | per nom, sense distingir majúscules | `find . -iname "*.jpg"` |
| `-type f` | només fitxers | `find /tmp -type f` |
| `-type d` | només carpetes | `find /home -type d` |
| `-size +100M` | més grans de 100 MB (`-` = menys) | `find / -size +100M` |
| `-mtime +7` | modificats fa més de 7 dies (`-7` = menys) | `find /tmp -mtime +7` |
| `-user ana` | d'un usuari | `find /home -user ana` |
| `-empty` | buits | `find . -empty` |
| `-maxdepth 1` | sense entrar en subcarpetes | `find . -maxdepth 1 -type f` |

Es poden combinar (s'han de complir tots):

```bash
find /var/log -type f -name "*.log" -mtime +30      # logs de fa més de 30 dies
find / -type f -size +1G 2> /dev/null               # fitxers de més d'1 GB (sense errors)
```

### Fer alguna cosa amb el que troba

```bash
find /tmp -name "*.tmp" -delete                       # esborrar-los
find . -name "*.sh" -exec chmod +x {} \;              # donar permís a cadascun
```

Amb `-exec`, `{}` es canvia per cada fitxer trobat i `\;` marca el final de l'ordre.

## `xargs`: passar una llista a una altra ordre

Algunes ordres (com `rm`, `cp`, `chmod`) no llegixen per una tuberia: necessiten els noms com a arguments. `xargs` fa de pont: agafa la llista que li arriba i la posa com a arguments de l'ordre.

```bash
find . -name "*.tmp" | rm          # ❌ rm no llig de la tuberia
find . -name "*.tmp" | xargs rm    # ✅ xargs converteix la llista en: rm fitxer1 fitxer2 ...
```

Més exemples:

```bash
find . -name "*.sh" | xargs grep -n "TODO"      # busca "TODO" en tots els .sh
cat servidors.txt | xargs -n1 ping -c1          # un ping per cada servidor (-n1 = un a un)
```

!!! warning "Noms amb espais"
    `xargs` separa per espais. Si els noms de fitxer poden tindre espais, usa:
    `find . -name "*.txt" -print0 | xargs -0 ...`

## Exemple: buscar una paraula en tots els scripts

Busca una paraula en tots els `.sh` de la carpeta actual i subcarpetes, i mostra el fitxer, el número de línia i el text:

```bash title="busca.sh"
#!/bin/bash
# Ús: ./busca.sh paraula

# Comprova que s'ha passat la paraula
if [ $# -ne 1 ]; then
    echo "Ús: $0 paraula" >&2
    exit 1
fi

# find troba els .sh → xargs els passa a grep → grep busca la paraula
# grep -n mostra: fitxer:línia:text
find . -type f -name "*.sh" -print0 |
    xargs -0 grep -n -- "$1" |
    while IFS=: read -r fitxer linia text; do        # separa els 3 trossos per :
        printf "%-30s %4s  %s\n" "$fitxer" "$linia" "$text"
    done
```

El `--` abans de `"$1"` evita problemes si la paraula comença per `-`.

!!! success "Per a l'examen"
    | Vull... | S'escriu |
    | ------- | -------- |
    | línies que contenen X | `grep "X" f` |
    | comptar-les | `grep -c "X" f` |
    | les que NO contenen X | `grep -v "X" f` |
    | comprovar si hi és (per a `if`) | `grep -q "X" f` |
    | buscar en una carpeta | `grep -r "X" carpeta` |
    | línies que comencen per X | `grep "^X" f` |
    | fitxers per nom | `find carpeta -name "*.log"` |
    | només fitxers / carpetes | `-type f` / `-type d` |
    | més grans de... | `-size +100M` |
    | més vells de N dies | `-mtime +N` |
    | executar una ordre amb cada un | `-exec ordre {} \;` o <code>&#124; xargs ordre</code> |
