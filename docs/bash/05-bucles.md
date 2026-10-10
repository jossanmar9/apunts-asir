# 5. Bucles

## `for` sobre una llista

```bash
for servei in ssh nginx cron; do
    systemctl is-active --quiet "$servei" && echo "$servei: actiu" || echo "$servei: parat"
done
```

A cada volta, la variable agafa el valor següent de la llista. La llista pot vindre de:

```bash
for f in *.log; do ...; done              # fitxers del directori actual
for f in "$dir"/*.conf; do ...; done      # fitxers d'un altre directori
for arg in "$@"; do ...; done             # arguments de l'script
for i in {1..10}; do ...; done            # rang
for i in {0..100..5}; do ...; done        # rang amb pas
for u in $(cut -d: -f1 /etc/passwd); do ...; done   # eixida d'una ordre
```

!!! warning "Si el patró no troba res"
    `for f in *.log` amb cap `.log` fa una volta amb `f='*.log'` literal. Protegix-te amb `[ -e "$f" ] || continue` al principi del bucle, o activa `shopt -s nullglob`.

## `for` estil C

```bash
for (( i=1; i<=10; i++ )); do
    echo "7 x $i = $(( 7 * i ))"
done
```

## `while`: mentre siga cert

```bash
compte=5
while (( compte > 0 )); do
    echo "$compte..."
    sleep 1
    (( compte-- ))
done
echo "Ja!"
```

Si oblides modificar la variable de la condició, tens un bucle infinit (++ctrl+c++ per a parar-lo).

## `until`: fins que siga cert

```bash
until [[ $port =~ ^[0-9]+$ ]] && (( port >= 1 && port <= 65535 )); do
    read -p "Port (1-65535): " port
done
```

## Llegir un fitxer línia a línia ⭐

La forma correcta (respecta espais i barres invertides):

```bash
while IFS= read -r linia; do
    echo "→ $linia"
done < fitxer.txt
```

Amb camps separats per un caràcter (per exemple `:` en `/etc/passwd`):

```bash
while IFS=: read -r usuari _ uid gid _ home shell; do
    if (( uid >= 1000 )) && [ "$shell" != "/usr/sbin/nologin" ]; then
        echo "$usuari → $home"
    fi
done < /etc/passwd
```

`_` és una variable "llixó" per als camps que no t'interessen.

!!! danger "No faces `cat fitxer | while read ...` si vols guardar resultats"
    La tuberia executa el bucle en un subshell: les variables que modifiques dins es perden en eixir. Amb `done < fitxer` no passa.

    ```bash
    total=0
    while read -r n; do (( total += n )); done < numeros.txt
    echo "$total"      # correcte
    ```

## `break` i `continue`

```bash
for f in /var/log/*.log; do
    [ -s "$f" ] || continue        # salta els buits
    if grep -q "CRITICAL" "$f"; then
        echo "Primer amb errors crítics: $f"
        break                      # ix del bucle
    fi
done
```

## Bucles infinits controlats

```bash
while true; do
    echo "1) Llistar  2) Eixir"
    read -p "> " op
    case $op in
        1) ls ;;
        2) break ;;
    esac
done
```
