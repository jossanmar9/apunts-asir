# 9. Arrays

## Què és un array

Una variable normal guarda **un** valor. Un **array** (també *vector* o *llista*) guarda **molts valors** en una sola variable, cadascun en una posició numerada.

Imagina una fila de caixes numerades:

```
serveis:  [ ssh ] [ nginx ] [ cron ]
posició:     0        1        2
```

!!! warning "Es comença a comptar per 0"
    La primera posició és la **0**, no la 1.

## Crear-lo i llegir-lo

```bash
serveis=(ssh nginx cron)          # crear: valors entre parèntesis, separats per espais

echo "${serveis[0]}"              # ssh       → la posició 0
echo "${serveis[1]}"              # nginx     → la posició 1
echo "${serveis[-1]}"             # cron      → l'últim
echo "${serveis[@]}"              # ssh nginx cron → tots
echo "${#serveis[@]}"             # 3         → quants n'hi ha
```

Les claus `{ }` són **obligatòries** quan uses arrays.

| Vull... | S'escriu |
| ------- | -------- |
| un element | `${array[posició]}` |
| tots | `${array[@]}` |
| quants n'hi ha | `${#array[@]}` |
| les posicions | `${!array[@]}` |

## Modificar-lo

```bash
serveis+=(mariadb)            # afegir al final
serveis[1]="apache2"          # canviar la posició 1
unset 'serveis[0]'            # esborrar la posició 0
```

## Recórrer-lo amb un bucle

```bash
for s in "${serveis[@]}"; do
    echo "Servei: $s"
done
```

Si també vols la posició:

```bash
for i in "${!serveis[@]}"; do
    echo "Posició $i: ${serveis[$i]}"
done
```

!!! warning "Posa sempre `\"${array[@]}\"` entre cometes"
    Si algun valor té espais (`"Ana Puig"`), sense cometes es partiria en dos.

## Omplir-lo des d'un fitxer o una ordre

```bash
mapfile -t linies < fitxer.txt          # cada línia del fitxer → un element
fitxers=(/etc/*.conf)                   # tots els .conf de /etc
```

## Arrays associatius (amb noms en compte de números)

En un array normal les posicions són números (0, 1, 2...). En un **array associatiu** són **noms** (claus). És com un diccionari: busques per paraula.

```
ports:   ssh → 22    http → 80    https → 443
```

**Cal declarar-lo abans** amb `declare -A`:

```bash
declare -A ports              # obligatori!
ports[ssh]=22
ports[http]=80
ports[https]=443

echo "${ports[ssh]}"          # 22
echo "${!ports[@]}"           # ssh http https  → els noms (claus)
echo "${ports[@]}"            # 22 80 443       → els valors
```

Recórrer-lo:

```bash
for servei in "${!ports[@]}"; do
    echo "$servei usa el port ${ports[$servei]}"
done
```

### Exemple: comptar quantes vegades apareix cada cosa

```bash
declare -A compte
for fruita in poma pera poma plàtan poma pera; do
    compte[$fruita]=$(( ${compte[$fruita]:-0} + 1 ))
done

for f in "${!compte[@]}"; do
    echo "$f: ${compte[$f]}"
done
```

```console
poma: 3
pera: 2
plàtan: 1
```

`${compte[$fruita]:-0}` vol dir "el valor, o 0 si encara no existix".

## Ordenar un array

La manera fàcil és usar l'ordre `sort`:

```bash
numeros=(42 7 19 3 88)
ordenats=($(printf '%s\n' "${numeros[@]}" | sort -n))
echo "${ordenats[@]}"     # 3 7 19 42 88
```

- `printf '%s\n'` posa cada número en una línia.
- `sort -n` les ordena com a números.

??? example "Fer-ho a mà: mètode de la bombolla"

    De vegades l'exercici demana ordenar sense `sort`, per a practicar bucles:

    ```bash
    v=(42 7 19 3 88)
    n=${#v[@]}
    for (( i=0; i<n-1; i++ )); do              # n-1 passades
        for (( j=0; j<n-1-i; j++ )); do        # compara cada parella veïna
            if (( v[j] > v[j+1] )); then       # si estan al revés...
                tmp=${v[j]}                    # ...les intercanvia
                v[j]=${v[j+1]}
                v[j+1]=$tmp
            fi
        done
    done
    echo "${v[@]}"     # 3 7 19 42 88
    ```

    A cada passada, el número més gran "puja" fins al final, com una bombolla. Per això el bucle de dins es fa cada vegada més curt.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `echo $serveis[1]` mostra `ssh[1]` | Falten les claus | `${serveis[1]}` |
| L'array associatiu no guarda bé | No l'has declarat | `declare -A nom` abans |
| Comptes des de 1 i et salta el primer | Es comença per 0 | La primera posició és `[0]` |
| `serveis = (a b)` dona error | Espais al voltant de `=` | `serveis=(a b)` |

!!! success "Per a l'examen"
    ```bash
    arr=(a b c)                   # crear
    ${arr[0]}                     # primer (es compta des de 0)
    ${arr[@]}                     # tots
    ${#arr[@]}                    # quants
    arr+=(d)                      # afegir
    for x in "${arr[@]}"; do ...; done

    declare -A mapa               # associatiu: declarar SEMPRE
    mapa[clau]=valor
    ${mapa[clau]}                 # valor
    ${!mapa[@]}                   # totes les claus
    ```
