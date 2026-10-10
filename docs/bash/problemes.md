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

    # Comprovem que ens han passat exactament 3 arguments
    if [ $# -ne 3 ]; then
        echo "Ús: $0 nom cognom1 cognom2" >&2
        exit 1
    fi

    # Guardem cada argument en una variable amb nom clar
    nom=$1
    cognom1=$2
    cognom2=$3

    # Els mostrem en l'ordre que demana l'enunciat
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
    secret=4                                 # el número que s'ha d'endevinar

    # Comprovem que hi ha 1 argument i que és un número
    [ $# -eq 1 ] || { echo "Ús: $0 <número>" >&2; exit 1; }
    [[ $1 =~ ^[0-9]+$ ]] || { echo "'$1' no és un número" >&2; exit 1; }

    # Comparem el número de l'usuari ($1) amb el secret
    if (( $1 == secret )); then
        echo "Encertat!"
    elif (( secret < $1 )); then             # l'usuari ha dit un número massa gran
        echo "NO! El número secret és menor"
    else                                     # l'usuari ha dit un número massa menut
        echo "NO! El número secret és major"
    fi
    ```

    **Ampliació**: número aleatori entre 1 i 100, demanat per teclat fins que l'encerte, comptant els intents:

    ```bash title="endevina2.sh"
    #!/bin/bash
    secret=$(( RANDOM % 100 + 1 ))           # número a l'atzar entre 1 i 100
    intents=0                                # comptador d'intents

    while true; do                           # repetim fins que l'encerte (break)
        read -rp "Número (1-100): " n
        # Si no és un número, avisem i tornem a preguntar sense comptar l'intent
        [[ $n =~ ^[0-9]+$ ]] || { echo "Escriu un número"; continue; }
        (( intents++ ))                      # sumem 1 intent
        if (( n < secret )); then
            echo "Més amunt"
        elif (( n > secret )); then
            echo "Més avall"
        else
            echo "Encertat en $intents intents!"
            break                            # ix del bucle
        fi
    done
    ```

    `$RANDOM % 100` dona un número de 0 a 99; sumant 1, de 1 a 100.

### 3. El major de dos números

Rep dos enters per argument i diu quin és el major i quin el menor (o si són iguals).

??? success "Solució"

    ```bash title="major.sh"
    #!/bin/bash
    # Ús: ./major.sh n1 n2

    [ $# -eq 2 ] || { echo "Ús: $0 n1 n2" >&2; exit 1; }

    # Comprovem que tots dos són enters (poden ser negatius)
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
    # Ús: ./compte.sh [segons]   (10 si no se n'indica cap)
    inici=${1:-10}                           # $1, o 10 si està buit
    [[ $inici =~ ^[0-9]+$ ]] || { echo "Ús: $0 [segons]" >&2; exit 1; }

    # Comptem cap enrere: des d'inici fins a 1
    for (( i=inici; i>0; i-- )); do
        printf "\r%3d " "$i"                 # \r torna al principi de la línia
        sleep 1                              # espera 1 segon
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

    # Funció que mostra com s'usa i ix amb error
    us() { echo "Ús: $0 sumar|multiplicar n1 [n2 ...]" >&2; exit 1; }

    [ $# -ge 2 ] || us                       # cal l'operació i almenys un número
    operacio=$1                              # guardem l'operació...
    shift                                    # ...i la llevem: ara "$@" només té números

    # Valor inicial: 0 per a sumar, 1 per a multiplicar (amb 0 sempre donaria 0)
    case $operacio in
        sumar)       resultat=0; simbol="+" ;;
        multiplicar) resultat=1; simbol="x" ;;
        *)           us ;;
    esac

    # Recorrem tots els números i anem acumulant
    for n in "$@"; do
        [[ $n =~ ^-?[0-9]+$ ]] || { echo "'$n' no és un enter" >&2; exit 1; }
        if [ "$operacio" = sumar ]; then
            (( resultat += n ))
        else
            (( resultat *= n ))
        fi
    done

    # Unim els números amb el símbol (+ o x) per a mostrar l'operació
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
    fitxer=${1:-/etc/passwd}                 # el fitxer passat, o /etc/passwd
    [ -r "$fitxer" ] || { echo "No puc llegir $fitxer" >&2; exit 1; }

    printf "%-12s %6s  %-20s %s\n" USUARI UID HOME SHELL    # capçalera de la taula

    # Llegim línia a línia, separant els camps per ":"
    # Format: usuari:x:uid:gid:nom:home:shell  (els que no volem van a _)
    while IFS=: read -r usuari _ uid _ _ home shell; do
        # Els usuaris de persones tenen UID entre 1000 i 65533
        (( uid >= 1000 && uid < 65534 )) || continue
        # Si el shell no permet entrar, no és una persona: el saltem
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

    total=0          # suma de tots els salaris
    total_ofici=0    # suma dels salaris de l'ofici buscat
    persones=0       # quantes persones tenen eixe ofici

    # read reparteix els 4 camps de cada línia en 4 variables
    while read -r nom cognom feina salari; do
        (( total += salari ))                # tots sumen al total
        if [ "$feina" = "$ofici" ]; then     # si és de l'ofici buscat...
            (( total_ofici += salari ))      # ...suma al seu total
            (( persones++ ))                 # ...i compta la persona
        fi
    done < "$fitxer"

    (( persones > 0 )) || { echo "Ningú té l'ofici '$ofici'"; exit 0; }

    # El percentatge té decimals → bc. Multipliquem per 100 ABANS de dividir
    percent=$(echo "scale=2; $total_ofici * 100 / $total" | bc)
    echo "Els $persones de '$ofici' cobren $total_ofici € de $total € ($percent %)"
    ```

    `read` reparteix els quatre camps en variables directament. El percentatge té decimals, així que el calculem amb `bc` (multiplicant per 100 **abans** de dividir).

    El mateix amb `awk`, que és l'eina natural per a fitxers en columnes:

    ```bash title="salaris_awk.sh"
    #!/bin/bash
    # Ús: ./salaris_awk.sh <fitxer> <ofici>
    # awk separa cada línia en columnes: $3 = ofici, $4 = salari
    awk -v ofici="$2" '
        { total += $4 }                      # cada línia: suma el salari al total
        $3 == ofici { part += $4; n++ }      # si és de l ofici: suma a part i compta
        END {                                # al final, mostra el resultat
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
    dir=${1:-.}                              # el directori passat, o l'actual
    [ -d "$dir" ] || { echo "No és un directori: $dir" >&2; exit 1; }

    total=0
    fitxers=0
    # find troba tots els fitxers; -print0 i read -d '' permeten noms amb espais
    while IFS= read -r -d '' f; do
        mida=$(stat -c %s "$f")              # mida del fitxer en bytes
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
    # ls -lR llista recursivament; cada línia d'un fitxer comença per "-"
    while read -r linia; do
        [[ $linia == -* ]] || continue       # saltem carpetes, capçaleres, línies buides
        # tr -s ' ' deixa un sol espai entre columnes; cut agafa la 5 (la mida)
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
    # Format de cada línia: client:article:quantitat:servit(s/n)
    fitxer=${1:-comandes.txt}
    [ -r "$fitxer" ] || { echo "No puc llegir $fitxer" >&2; exit 1; }

    # Dos arrays associatius amb el nom del client com a clau
    declare -A unitats      # unitats[client] = total d'unitats demanades
    declare -A pendents     # pendents[client] = línies encara no servides

    while IFS=: read -r client article quantitat servit; do
        (( unitats[$client] += quantitat ))
        [ "$servit" = n ] && (( pendents[$client]++ ))
    done < "$fitxer"

    printf "%-10s %8s  %s\n" CLIENT UNITATS ESTAT
    for client in "${!unitats[@]}"; do       # recorrem tots els clients (les claus)
        # ${pendents[$client]:-0} → 0 si el client no té cap pendent
        if (( ${pendents[$client]:-0} == 0 )); then
            estat="tot servit"
        else
            estat="${pendents[$client]} línies pendents"
        fi
        printf "%-10s %8d  %s\n" "$client" "${unitats[$client]}" "$estat"
    done | sort                              # ordenem per nom de client
    ```

    Dos arrays associatius amb el client com a clau: un acumula unitats i l'altre compta línies pendents. `${pendents[$client]:-0}` val 0 si el client no té cap pendent.

## Nivell avançat

### 10. Estalvis contra el preu de l'or

Una persona té 4.000 € i estalvia 200 € al mes. Vol comprar un lingot d'or que hui val 12.000 €, però l'or puja un 0,5 % cada mes. Quants mesos tardarà?

??? success "Solució"

    ```bash title="or.sh"
    #!/bin/bash
    # Quants mesos cal estalviar per a comprar un lingot d'or si el preu també puja?
    estalvis=4000        # € que té ara
    mensual=200          # € que estalvia cada mes
    preu=12000           # € que val el lingot hui
    puja=0.5             # % que puja l'or cada mes

    mes=0
    # Repetim mentre els estalvis siguen menors que el preu.
    # bc torna 1 (cert) o 0 (fals), i (( )) ho entén com a condició
    while (( $(echo "$estalvis < $preu" | bc) )); do
        (( mes++ ))
        estalvis=$(( estalvis + mensual ))                         # un mes més d'estalvi
        preu=$(echo "scale=2; $preu * (100 + $puja) / 100" | bc)   # el preu puja un 0,5 %
        if (( mes == 600 )); then                                  # límit de seguretat: 50 anys
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
    mostres=${1:-10}                         # quantes mesures fer (10 per defecte)

    for (( i=1; i<=mostres; i++ )); do
        carrega=$(cut -d' ' -f1 /proc/loadavg)      # primer número de /proc/loadavg, p. ex. 0.38
        barres=$(echo "$carrega * 20 / 1" | bc)     # 0.38 → 7 barres ("/ 1" lleva els decimals)
        (( barres > 60 )) && barres=60              # que no passe de 60 caràcters

        grafica=""
        for (( b=0; b<barres; b++ )); do grafica+="#"; done     # construïm la barra
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

    # 1. Menú per a triar quins processos mostrar
    PS3="Quins processos vols veure? "
    select filtre in "Meus" "Amb terminal" "Tots" "Eixir"; do
        case $REPLY in
            1) ps -u "$USER" -o pid,stat,etime,cmd ;;                 # els de l'usuari
            2) ps -o pid,tty,stat,cmd -t "$(tty)" ;;                  # els d'este terminal
            3) ps -eo pid,user,stat,cmd --sort=-%cpu | head -20 ;;    # els 20 que més CPU usen
            4) exit 0 ;;
            *) echo "Opció no vàlida"; continue ;;
        esac
        break                                                         # ja hem mostrat: ixim del menú
    done

    # 2. Demanar el PID i comprovar que existix
    read -rp "PID del procés: " pid
    [[ $pid =~ ^[0-9]+$ ]] || { echo "PID no vàlid" >&2; exit 1; }
    ps -p "$pid" &> /dev/null || { echo "No existix el procés $pid" >&2; exit 1; }

    # 3. Menú per a triar l'acció
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

    # 4. Confirmar abans de fer-ho
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
