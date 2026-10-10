# 9. Arrays

## Arrays indexats

```bash
serveis=(ssh nginx cron)
serveis+=(mariadb)                # afegir al final

echo "${serveis[0]}"              # ssh (es compta des de 0)
echo "${serveis[-1]}"             # mariadb (l'últim)
echo "${serveis[@]}"              # tots
echo "${#serveis[@]}"             # quants: 4
echo "${!serveis[@]}"             # índexs: 0 1 2 3
echo "${serveis[@]:1:2}"          # nginx cron (des de l'1, 2 elements)
unset 'serveis[1]'                # esborrar un element
```

Recórrer-lo:

```bash
for s in "${serveis[@]}"; do
    echo "$s"
done

for i in "${!serveis[@]}"; do
    echo "$i → ${serveis[$i]}"
done
```

!!! warning "Sempre `\"${array[@]}\"` amb cometes"
    Si un element té espais, sense cometes es partiria en diversos.

Omplir un array des d'una ordre o fitxer:

```bash
mapfile -t linies < fitxer.txt        # una línia per element
mapfile -t usuaris < <(cut -d: -f1 /etc/passwd)
fitxers=(/etc/*.conf)                  # resultat d'un patró
```

## Arrays associatius (mapes)

Les claus són text. **Cal declarar-los** amb `declare -A`:

```bash
declare -A ports
ports[ssh]=22
ports[http]=80
ports[https]=443

echo "${ports[ssh]}"          # 22
echo "${!ports[@]}"           # claus (en ordre qualsevol)
[[ -v ports[ftp] ]] || echo "ftp no està"

for servei in "${!ports[@]}"; do
    echo "$servei → ${ports[$servei]}"
done
```

### Exemple: comptar ocurrències

```bash
declare -A compte
while IFS=: read -r _ _ _ _ _ _ shell; do
    (( compte[$shell]++ ))
done < /etc/passwd

for s in "${!compte[@]}"; do
    echo "${compte[$s]} $s"
done | sort -rn
```

## Ordenar un array

```bash
numeros=(42 7 19 3 88)
mapfile -t ordenats < <(printf '%s\n' "${numeros[@]}" | sort -n)
echo "${ordenats[@]}"     # 3 7 19 42 88
```

??? example "Ordenació per bombolla (per a entendre els bucles)"

    ```bash
    v=(42 7 19 3 88)
    n=${#v[@]}
    for (( i=0; i<n-1; i++ )); do
        for (( j=0; j<n-1-i; j++ )); do
            if (( v[j] > v[j+1] )); then
                tmp=${v[j]}; v[j]=${v[j+1]}; v[j+1]=$tmp
            fi
        done
    done
    echo "${v[@]}"
    ```

    A cada passada, el més gran "flota" fins al final. Per això el bucle intern es fa cada vegada més curt (`n-1-i`).
