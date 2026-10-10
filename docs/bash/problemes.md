# Problemes resolts

Problemes de dificultat creixent. Intenta'ls primer tu i obri la solució només quan t'hages encallat o per a comparar. Cada solució comprova els arguments, com hauries de fer sempre.

## Nivell bàsic

### 1. Nom en format «cognoms, nom»

Fes un script que reba per argument un nom de tres paraules (*nom cognom1 cognom2*) i el mostre com a *cognom1 cognom2, nom*.

```console
$ ./nom.sh Laura Pons Ferrer
Pons Ferrer, Laura
```

??? success "Solució"

    ```bash title="nom.sh"
    #!/bin/bash
    # Ús: ./nom.sh Nom Cognom1 Cognom2
    if [ $# -ne 3 ]; then
        echo "Ús: $0 nom cognom1 cognom2" >&2
        exit 1
    fi
    nom=$1
    cognom1=$2
    cognom2=$3
    echo "$cognom1 $cognom2, $nom"
    ```

    Cada paraula és un paràmetre posicional. Guardar-los en variables amb nom fa el codi molt més llegible que usar `$1 $2 $3` directament.

### 2. Endevina el número

El número secret és 4. L'usuari passa un número per argument i l'script li diu si ha encertat o si el secret és major o menor.

```console
$ ./endevina.sh 5
NO! El número secret és menor
```

??? success "Solució"

    ```bash title="endevina.sh"
    #!/bin/bash
    # Ús: ./endevina.sh <número>
    secret=4

    [ $# -eq 1 ] || { echo "Ús: $0 <número>" >&2; exit 1; }
    [[ $1 =~ ^[0-9]+$ ]] || { echo "'$1' no és un número" >&2; exit 1; }

    if (( $1 == secret )); then
        echo "Encertat!"
    elif (( secret < $1 )); then
        echo "NO! El número secret és menor"
    else
        echo "NO! El número secret és major"
    fi
    ```

    **Ampliació**: número aleatori entre 1 i 100, demanat per teclat fins que l'encerte, comptant els intents:

    ```bash title="endevina2.sh"
    #!/bin/bash
    secret=$(( RANDOM % 100 + 1 ))
    intents=0

    while true; do
        read -rp "Número (1-100): " n
        [[ $n =~ ^[0-9]+$ ]] || { echo "Escriu un número"; continue; }
        (( intents++ ))
        if (( n < secret )); then
            echo "Més amunt"
        elif (( n > secret )); then
            echo "Més avall"
        else
            echo "Encertat en $intents intents!"
            break
        fi
    done
    ```

    `$RANDOM % 100` dona un número de 0 a 99; sumant 1, de 1 a 100.

### 3. El major de dos números

Rep dos enters per argument i diu quin és el major i quin el menor (o si són iguals).

??? success "Solució"

    ```bash title="major.sh"
    #!/bin/bash
    [ $# -eq 2 ] || { echo "Ús: $0 n1 n2" >&2; exit 1; }
    for n in "$1" "$2"; do
        [[ $n =~ ^-?[0-9]+$ ]] || { echo "'$n' no és un enter" >&2; exit 1; }
    done

    if (( $1 > $2 )); then
        echo "El major és $1 i el menor $2"
    elif (( $1 < $2 )); then
        echo "El major és $2 i el menor $1"
    else
        echo "Són iguals"
    fi
    ```

    L'expressió regular `^-?[0-9]+$` accepta enters negatius: un `-` opcional i un o més dígits.

### 4. Compte enrere

Compte enrere des del número que es passa per argument (10 si no se'n passa cap), esperant un segon entre número i número.

??? success "Solució"

    ```bash title="compte.sh"
    #!/bin/bash
    inici=${1:-10}
    [[ $inici =~ ^[0-9]+$ ]] || { echo "Ús: $0 [segons]" >&2; exit 1; }

    for (( i=inici; i>0; i-- )); do
        printf "\r%3d " "$i"
        sleep 1
    done
    printf "\rTemps!\n"
    ```

    `\r` torna el cursor al principi de la línia sense baixar, així els números se sobreescriuen i fa l'efecte d'animació.

### 5. Sumar o multiplicar tots els arguments

El primer argument és `sumar` o `multiplicar`. La resta són números, tants com vulga l'usuari.

```console
$ ./calcula.sh sumar 1 2 3 4
1+2+3+4 = 10  (4 números)
$ ./calcula.sh multiplicar 2 3 4
2x3x4 = 24  (3 números)
```

??? success "Solució"

    ```bash title="calcula.sh"
    #!/bin/bash
    # Ús: ./calcula.sh sumar|multiplicar n1 n2 ...
    us() { echo "Ús: $0 sumar|multiplicar n1 [n2 ...]" >&2; exit 1; }

    [ $# -ge 2 ] || us
    operacio=$1
    shift

    case $operacio in
        sumar)       resultat=0; simbol="+" ;;
        multiplicar) resultat=1; simbol="x" ;;
        *)           us ;;
    esac

    for n in "$@"; do
        [[ $n =~ ^-?[0-9]+$ ]] || { echo "'$n' no és un enter" >&2; exit 1; }
        if [ "$operacio" = sumar ]; then
            (( resultat += n ))
        else
            (( resultat *= n ))
        fi
    done

    operacions=$(IFS="$simbol"; echo "$*")
    echo "$operacions = $resultat  ($# números)"
    ```

    - `shift` lleva l'operació i deixa en `"$@"` només els números.
    - El valor inicial és 0 per a sumar i **1** per a multiplicar (amb 0 sempre donaria 0).
    - `IFS="$simbol"; echo "$*"` uneix els arguments amb eixe caràcter. Es fa dins de `$( )` perquè el canvi d'`IFS` no afecte la resta de l'script.

## Nivell mitjà: fitxers

### 6. Usuaris que són persones

A partir de `/etc/passwd` (o una còpia passada per argument), llista només els usuaris reals: UID de 1000 en amunt i amb un shell que permeta entrar.

```console
$ ./usuaris.sh
USUARI          UID  HOME                 SHELL
ana            1000  /home/ana            /bin/bash
pep            1001  /home/pep            /bin/zsh
```

??? success "Solució"

    ```bash title="usuaris.sh"
    #!/bin/bash
    # Llista els usuaris que són persones (UID >= 1000 i amb shell d'accés)
    fitxer=${1:-/etc/passwd}
    [ -r "$fitxer" ] || { echo "No puc llegir $fitxer" >&2; exit 1; }

    printf "%-12s %6s  %-20s %s\n" USUARI UID HOME SHELL
    while IFS=: read -r usuari _ uid _ _ home shell; do
        (( uid >= 1000 && uid < 65534 )) || continue
        case $shell in
            */nologin|*/false) continue ;;
        esac
        printf "%-12s %6d  %-20s %s\n" "$usuari" "$uid" "$home" "$shell"
    done < "$fitxer"
    ```

    - `IFS=: read -r usuari _ uid _ _ home shell` parteix cada línia pels `:`. Els camps que no ens interessen van a `_`.
    - `nobody` té UID 65534: per això el límit superior.
    - Els comptes de servei tenen `/usr/sbin/nologin` o `/bin/false` com a shell.

### 7. Percentatge de salaris per ofici

Cada línia del fitxer té *Nom Cognom Ofici Salari*. L'script rep el fitxer i un ofici i diu quin percentatge del total de salaris cobren els d'eixe ofici.

```text title="salaris.txt"
Juan García mecànic 2000
Toni Tomàs comercial 1800
Fernando Martínez directiu 2200
Dolores Fuertes secretària 1800
Sara Goza directiu 2300
```

```console
$ ./salaris.sh salaris.txt directiu
Els 2 de 'directiu' cobren 4500 € de 10100 € (44.55 %)
```

??? success "Solució"

    ```bash title="salaris.sh"
    #!/bin/bash
    # Ús: ./salaris.sh <fitxer> <ofici>
    # Format de cada línia: Nom Cognom Ofici Salari
    [ $# -eq 2 ] || { echo "Ús: $0 fitxer ofici" >&2; exit 1; }
    fitxer=$1
    ofici=$2
    [ -r "$fitxer" ] || { echo "No puc llegir $fitxer" >&2; exit 1; }

    total=0
    total_ofici=0
    persones=0
    while read -r nom cognom feina salari; do
        (( total += salari ))
        if [ "$feina" = "$ofici" ]; then
            (( total_ofici += salari ))
            (( persones++ ))
        fi
    done < "$fitxer"

    (( persones > 0 )) || { echo "Ningú té l'ofici '$ofici'"; exit 0; }

    percent=$(echo "scale=2; $total_ofici * 100 / $total" | bc)
    echo "Els $persones de '$ofici' cobren $total_ofici € de $total € ($percent %)"
    ```

    `read` reparteix els quatre camps en variables directament. El percentatge té decimals, així que el calculem amb `bc` (multiplicant per 100 **abans** de dividir).

    El mateix amb `awk`, que és l'eina natural per a fitxers en columnes:

    ```bash title="salaris_awk.sh"
    #!/bin/bash
    awk -v ofici="$2" '
        { total += $4 }
        $3 == ofici { part += $4; n++ }
        END {
            if (n == 0) { print "Ningú té eixe ofici"; exit }
            printf "%d persones, %d € de %d € (%.2f %%)\n", n, part, total, part * 100 / total
        }' "$1"
    ```

### 8. Sumar la mida dels fitxers (fer el que fa `du`)

Suma la mida de tots els fitxers del directori indicat i dels seus subdirectoris.

??? success "Solució"

    ```bash title="mides.sh"
    #!/bin/bash
    # Suma la mida de tots els fitxers del directori (i subdirectoris), com du
    dir=${1:-.}
    [ -d "$dir" ] || { echo "No és un directori: $dir" >&2; exit 1; }

    total=0
    fitxers=0
    while IFS= read -r -d '' f; do
        mida=$(stat -c %s "$f")
        (( total += mida ))
        (( fitxers++ ))
    done < <(find "$dir" -type f -print0)

    echo "$fitxers fitxers, $total bytes ($(( total / 1024 )) KiB)"
    ```

    `find -print0` i `read -d ''` separen els noms per un caràcter nul, així funcionen fins i tot noms amb espais. `stat -c %s` dona la mida en bytes.

    Si l'enunciat obliga a traure les mides de `ls -l` (la columna 5) i retallar amb `cut`:

    ```bash title="mides_ls.sh"
    #!/bin/bash
    # Mateixa idea però traient la mida de ls -l (columna 5) amb tr i cut
    dir=${1:-.}
    total=0
    while read -r linia; do
        [[ $linia == -* ]] || continue          # només fitxers normals
        mida=$(echo "$linia" | tr -s ' ' | cut -d' ' -f5)
        (( total += mida ))
    done < <(ls -lR "$dir")
    echo "$total bytes"
    ```

    `tr -s ' '` comprimix els espais repetits perquè `cut` (que només admet un separador) trobe la columna correcta.

### 9. Comandes pendents per client

Un fitxer guarda les comandes amb el format `client:article:quantitat:servit` (`s` o `n`). Mostra, per a cada client, el total d'unitats i si ho té tot servit.

```text title="comandes.txt"
Montse:calcetins:12:s
Pere:botes:2:n
Montse:canyes:1:s
Joan:esquers:50:s
Pere:calcetins:4:s
Joan:botes:1:n
```

```console
$ ./comandes.sh
CLIENT      UNITATS  ESTAT
Joan             51  1 línies pendents
Montse           13  tot servit
Pere              6  1 línies pendents
```

??? success "Solució"

    ```bash title="comandes.sh"
    #!/bin/bash
    # Format: client:article:quantitat:servit(s/n)
    fitxer=${1:-comandes.txt}
    [ -r "$fitxer" ] || { echo "No puc llegir $fitxer" >&2; exit 1; }

    declare -A unitats pendents

    while IFS=: read -r client article quantitat servit; do
        (( unitats[$client] += quantitat ))
        [ "$servit" = n ] && (( pendents[$client]++ ))
    done < "$fitxer"

    printf "%-10s %8s  %s\n" CLIENT UNITATS ESTAT
    for client in "${!unitats[@]}"; do
        if (( ${pendents[$client]:-0} == 0 )); then
            estat="tot servit"
        else
            estat="${pendents[$client]} línies pendents"
        fi
        printf "%-10s %8d  %s\n" "$client" "${unitats[$client]}" "$estat"
    done | sort
    ```

    Dos arrays associatius amb el client com a clau: un acumula unitats i l'altre compta línies pendents. `${pendents[$client]:-0}` val 0 si el client no té cap pendent.

## Nivell avançat

### 10. Estalvis contra el preu de l'or

Una persona té 4.000 € i estalvia 200 € al mes. Vol comprar un lingot d'or que hui val 12.000 €, però l'or puja un 0,5 % cada mes. Quants mesos tardarà?

??? success "Solució"

    ```bash title="or.sh"
    #!/bin/bash
    # Quants mesos cal estalviar per a comprar un lingot d'or si el preu també puja?
    estalvis=4000        # €
    mensual=200          # € que estalvia cada mes
    preu=12000           # € que val el lingot hui
    puja=0.5             # % que puja l'or cada mes

    mes=0
    while (( $(echo "$estalvis < $preu" | bc) )); do
        (( mes++ ))
        estalvis=$(( estalvis + mensual ))
        preu=$(echo "scale=2; $preu * (100 + $puja) / 100" | bc)
        if (( mes == 600 )); then
            echo "En 50 anys no hi arriba: l'or puja més ràpid que els estalvis"
            exit 1
        fi
    done

    echo "Ho aconseguix en $mes mesos ($(( mes / 12 )) anys i $(( mes % 12 )) mesos)"
    echo "Tindrà $estalvis € i el lingot valdrà $preu €"
    ```

    ```console
    $ ./or.sh
    Ho aconseguix en 62 mesos (5 anys i 2 mesos)
    Tindrà 16400 € i el lingot valdrà 16348.12 €
    ```

    - La comparació de decimals es fa amb `bc`, que torna 1 o 0; `(( ))` ho interpreta com a cert o fals.
    - Compte amb `scale`: `bc` aplica els decimals a **cada operació**. `1 + 0.5 / 100` amb `scale=2` dona `1.00` perquè `0.5/100 = 0.005` es retalla a `0.00`. Per això calculem `preu * (100 + puja) / 100`.
    - El límit de 600 mesos evita un bucle infinit si l'or puja més ràpid que els estalvis (prova amb `puja=1.5`).

### 11. Gràfica de càrrega del sistema

Mostra cada segon la càrrega mitjana de l'últim minut com una barra de `#`.

```console
$ ./carrega.sh 3
17:35:12  0.38 |#######
17:35:13  0.41 |########
17:35:14  1.02 |####################
```

??? success "Solució"

    ```bash title="carrega.sh"
    #!/bin/bash
    # Gràfica de la càrrega del sistema (mitjana d'1 minut) cada segon
    mostres=${1:-10}

    for (( i=1; i<=mostres; i++ )); do
        carrega=$(cut -d' ' -f1 /proc/loadavg)        # p. ex. 0.38
        barres=$(echo "$carrega * 20 / 1" | bc)       # 0.38 → 7 barres
        (( barres > 60 )) && barres=60
        grafica=""
        for (( b=0; b<barres; b++ )); do grafica+="#"; done
        printf "%s %5s |%s\n" "$(date +%T)" "$carrega" "$grafica"
        sleep 1
    done
    ```

    La càrrega es pot traure d'`uptime`, però `/proc/loadavg` és més fàcil de retallar: el primer camp és la mitjana d'1 minut.

### 12. Gestor de processos

Menú per a triar quins processos veure (meus, del terminal o tots). Després demana un PID i una acció (matar, parar o continuar) i demana confirmació abans de fer-la.

??? success "Solució"

    ```bash title="processos.sh"
    #!/bin/bash
    # Mostra processos filtrats i permet matar, parar o continuar-ne un

    PS3="Quins processos vols veure? "
    select filtre in "Meus" "Amb terminal" "Tots" "Eixir"; do
        case $REPLY in
            1) ps -u "$USER" -o pid,stat,etime,cmd ;;
            2) ps -o pid,tty,stat,cmd -t "$(tty)" ;;
            3) ps -eo pid,user,stat,cmd --sort=-%cpu | head -20 ;;
            4) exit 0 ;;
            *) echo "Opció no vàlida"; continue ;;
        esac
        break
    done

    read -rp "PID del procés: " pid
    [[ $pid =~ ^[0-9]+$ ]] || { echo "PID no vàlid" >&2; exit 1; }
    ps -p "$pid" &> /dev/null || { echo "No existix el procés $pid" >&2; exit 1; }

    PS3="Què vols fer amb el $pid? "
    select accio in "Matar" "Parar" "Continuar" "Res"; do
        case $REPLY in
            1) senyal=TERM ;;
            2) senyal=STOP ;;
            3) senyal=CONT ;;
            4) exit 0 ;;
            *) echo "Opció no vàlida"; continue ;;
        esac
        break
    done

    read -rp "Segur que vols enviar $senyal a $pid? (s/n) " r
    if [[ $r =~ ^[sS] ]]; then
        kill -s "$senyal" "$pid" && echo "Fet"
    else
        echo "Cancel·lat"
    fi
    ```

    | Acció | Senyal | Equivalent |
    | ----- | ------ | ---------- |
    | Matar | `TERM` (15) | `kill PID` |
    | Parar | `STOP` (19) | ++ctrl+z++ |
    | Continuar | `CONT` (18) | `fg` / `bg` |

    Un procés parat no reacciona a `TERM` fins que el continues. Per a matar-lo igualment: `kill -KILL PID` (`kill -9`).

    Amb finestres gràfiques es pot fer el mateix canviant `select` i `read` per `zenity --list`, `zenity --entry` i `zenity --question` (vegeu el [tema 8](08-lectura.md)).

### 13. Buscar una paraula en tots els scripts

Està resolt en el [tema 11](11-find-grep-xargs.md#exemple-buscar-una-paraula-en-tots-els-sh).
