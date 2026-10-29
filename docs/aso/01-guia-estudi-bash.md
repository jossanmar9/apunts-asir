# UT1 · Guia d'estudi de Bash

Aquesta pàgina és una **guia de repàs per a estudiar** la UT1. No substitueix els apartats detallats: els ordena, destaca el que convé dominar i usa exemples curts.

## 1. Estructura mínima d'un script

```bash
#!/bin/bash
echo "Hola món"
```

```bash
chmod +x script.sh
./script.sh
# o bé
bash script.sh
```

`#!/bin/bash` indica l'intèrpret. Per executar amb `./script.sh` cal permís d'execució.

## 2. Variables, cometes i entrada

```bash
nom="Jose"
echo "Hola $nom"
read -r -p "Nom de l'usuari: " usuari
echo "Usuari: $usuari"
```

!!! warning "Error típic"
    `nom = "Jose"` és incorrecte. En una assignació no hi ha espais al voltant de `=`.

Regla pràctica: quan passes una variable a una ordre, normalment usa `"$variable"` per conservar espais.

Variables d'entorn que convé reconéixer: `$HOME`, `$USER`, `$PATH`, `$PWD`, `$SHELL`, `$HOSTNAME`.

## 3. Paràmetres

Si executes:

```bash
./alta.sh pepe 25
```

Dins del script:

```bash
echo "$0"  # nom del script
echo "$1"  # pepe
echo "$2"  # 25
echo "$#"  # nombre de paràmetres
echo "$@"  # tots els paràmetres
```

Validació típica:

```bash
if (( $# != 2 )); then
    echo "Ús: $0 usuari edat" >&2
    exit 1
fi
```

## 4. Arrays

```bash
servidors=("web01" "db01" "backup01")
echo "${servidors[0]}"
echo "${servidors[@]}"
echo "${#servidors[@]}"
```

Recórrer-los:

```bash
for servidor in "${servidors[@]}"; do
    echo "$servidor"
done
```

## 5. Matemàtiques

Per a enters, la forma recomanada és `$(( ... ))` o `(( ... ))`:

```bash
usats=70
total=100
lliures=$((total - usats))
echo "$lliures"
```

Per a decimals, el material usa `bc`:

```bash
resultat=$(echo "scale=2; 10 / 3" | bc)
echo "$resultat"
```

## 6. Tests: fitxers, cadenes i números

### Fitxers

```bash
[[ -e "$ruta" ]]  # existeix
[[ -f "$ruta" ]]  # fitxer regular
[[ -d "$ruta" ]]  # directori
[[ -r "$ruta" ]]  # llegible
[[ -w "$ruta" ]]  # escriptura
[[ -x "$ruta" ]]  # executable
[[ -s "$ruta" ]]  # mida > 0
```

### Cadenes

```bash
[[ -z "$nom" ]]       # buida
[[ -n "$nom" ]]       # no buida
[[ "$a" == "$b" ]]   # iguals
[[ "$a" != "$b" ]]   # diferents
```

### Números

| Operador | Significat |
|---|---|
| `-eq` | igual |
| `-ne` | diferent |
| `-lt` | menor |
| `-le` | menor o igual |
| `-gt` | major |
| `-ge` | major o igual |

```bash
if [[ $ocupacio -ge 90 ]]; then
    echo "Alerta"
fi
```

Amb `[[ ... ]]` pots combinar condicions amb `&&` i `||`.

## 7. Manipulació de cadenes

```bash
fitxer="informe_final.pdf"
echo "${fitxer:0:7}"  # informe
echo "${fitxer%.*}"   # informe_final
echo "${fitxer##*.}"  # pdf
echo "${#fitxer}"     # longitud
```

Aquestes expansions són molt útils per tractar noms de fitxers sense invocar eines externes.

## 8. `if`, `elif`, `else`

```bash
if [[ $nota -ge 9 ]]; then
    echo "Excel·lent"
elif [[ $nota -ge 5 ]]; then
    echo "Aprovat"
else
    echo "Suspés"
fi
```

Pensa sempre: **quina condició vull comprovar i què passa en cada cas?**

## 9. `case`

És útil quan una variable pot tindre diverses opcions conegudes:

```bash
case "$1" in
    iniciar)
        echo "Iniciant"
        ;;
    parar)
        echo "Parant"
        ;;
    *)
        echo "Opció desconeguda"
        ;;
esac
```

## 10. Bucles

### `for`

```bash
for usuari in anna joan pere; do
    echo "$usuari"
done
```

```bash
for ((i=1; i<=5; i++)); do
    echo "$i"
done
```

### `while`

```bash
contador=1
while [[ $contador -le 5 ]]; do
    echo "$contador"
    ((contador++))
done
```

### `until`

Es repeteix **fins que** la condició és certa:

```bash
contador=1
until [[ $contador -gt 5 ]]; do
    echo "$contador"
    ((contador++))
done
```

`continue` salta a la iteració següent; `break` ix del bucle.

## 11. Funcions

```bash
comprovar_usuari() {
    if id "$1" &>/dev/null; then
        return 0
    fi
    return 1
}

if comprovar_usuari "alumne"; then
    echo "Existeix"
else
    echo "No existeix"
fi
```

Una funció s'ha de definir abans d'usar-la. Els seus arguments també són `$1`, `$2`... `return` retorna un **codi d'eixida**, no una cadena.

Per obtindre un valor:

```bash
sumar() {
    echo $(($1 + $2))
}

resultat=$(sumar 4 6)
```

## 12. `grep` i expressions regulars

Patrons bàsics:

| Patró | Significat |
|---|---|
| `^` | inici de línia |
| `$` | final de línia |
| `.` | qualsevol caràcter |
| `[0-9]` | un dígit |
| `[A-Z]` | una majúscula |
| `[^0-9]` | qualsevol caràcter que no siga dígit |

Amb `grep -E` tens regex esteses: `+`, `?`, `{n}`, `{n,m}`, `|` i `( )`.

```bash
grep '^root' /etc/passwd
grep 'bash$' /etc/passwd
grep -E 'error|fallo' sistema.log
grep -E '^[0-9]{4}$' codis.txt
```

En Bash pots validar directament amb `=~`:

```bash
if [[ $port =~ ^[0-9]{1,5}$ ]]; then
    echo "Format numèric correcte"
fi
```

## 13. Eines de text que has de saber combinar

```bash
grep -i "error" sistema.log
cut -d: -f1 /etc/passwd
awk -F: '{print $1, $3}' /etc/passwd
sort noms.txt
sort noms.txt | uniq -c
tr '[:lower:]' '[:upper:]' < noms.txt
find . -type f -name "*.log"
```

`cut` va bé amb un delimitador clar. `awk` és millor quan vols treballar amb columnes i condicions.

## 14. `sed`

```bash
sed 's/http/https/' config.txt
sed 's/http/https/g' config.txt
sed '/error/d' log.txt
sed '/^$/d' fitxer.txt
sed -n '3,7p' fitxer.txt
```

`-i` modifica el fitxer real:

```bash
sed -i.bak 's/antic/nou/g' config.txt
```

Això crea una còpia `.bak` abans de modificar.

## 15. Pipes i redireccions

```bash
ps -ef | grep ssh
comanda > fitxer.txt
comanda >> fitxer.txt
comanda 2> errors.log
comanda &> tot.log
```

`>` substitueix; `>>` afegeix. La pipe `|` envia la sortida d'una ordre a l'entrada de la següent.

## 16. Errors i depuració

Tot comandament retorna un codi: **0 = èxit**, un altre valor = error.

```bash
ls /etc/passwd
echo "$?"
```

Per depurar:

```bash
bash -x script.sh
```

Altres eines del tema:

```bash
set -e
set -u
trap 'echo "Interromput"; exit 1' SIGINT SIGTERM
```

## 17. Exemple integrador

Script que rep un directori i compta els `.log`:

```bash
#!/bin/bash

if (( $# != 1 )); then
    echo "Ús: $0 directori" >&2
    exit 1
fi

ruta=$1

if [[ ! -d "$ruta" ]]; then
    echo "El directori no existeix" >&2
    exit 2
fi

quantitat=$(find "$ruta" -type f -name '*.log' | wc -l)
echo "Fitxers .log: $quantitat"
```

Ací combines paràmetres, `if`, test de directori, substitució de comandes, `find`, pipe i `wc`.

## Què prioritzaria per a l'examen

1. Saber llegir un script i predir què farà.
2. `$1`, `$#`, `"$@"`, variables i cometes.
3. `[[ ... ]]`: fitxers, cadenes i comparacions numèriques.
4. `if`, `case`, `for`, `while` i funcions.
5. Pipes i redireccions.
6. `grep` + regex, `awk`, `cut` i `sed`.
7. Codi d'eixida `$?` i diagnòstic d'errors.
8. Combinar-ho en scripts curts d'administració.

!!! tip "Com estudiar-la"
    Llig un apartat, tanca els apunts i escriu un exemple de 5-10 línies de memòria. Després fes els exercicis de la UT1 sense mirar la solució.