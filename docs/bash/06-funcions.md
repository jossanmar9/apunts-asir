# 6. Funcions

## Què és una funció

Una **funció** és un tros de codi amb nom que pots executar quantes vegades vulgues només escrivint el seu nom. És com crear la teua pròpia ordre.

Serveix per a:

- **No repetir codi**: si fas el mateix en tres llocs, ho poses en una funció i la crides tres vegades.
- **Ordenar** l'script en trossos amb nom clar.

## Crear-la i usar-la

```bash
saluda() {                 # crear una funció anomenada "saluda"
    echo "Hola!"
    echo "Benvingut"
}

saluda                     # executar-la (es diu "cridar-la")
saluda                     # la pots cridar les vegades que vulgues
```

- El nom, seguit de `()`, i el codi entre claus `{ }`.
- Per a cridar-la, només el nom, **sense parèntesis**.
- **S'ha de crear abans de cridar-la**: Bash llig de dalt a baix.

## Passar-li dades

Les funcions poden rebre dades, igual que un script rep arguments. Dins de la funció, les dades estan en `$1`, `$2`, etc.:

```bash
saluda() {
    echo "Hola, $1!"            # $1 és el primer valor que li passes
}

saluda "Ana"       # Hola, Ana!
saluda "Pep"       # Hola, Pep!
```

!!! warning "`$1` dins i fora de la funció són coses diferents"
    Dins d'una funció, `$1` és el primer argument **de la funció**, no el de l'script. Si necessites el de l'script, passa'l: `saluda "$1"`.

## Tornar un resultat

Ací hi ha una cosa que confon molt. En Bash hi ha **dues maneres** de "tornar" alguna cosa d'una funció, i serveixen per a coses diferents:

### Per a tornar una dada (un número, un text) → `echo`

La funció **mostra** el resultat amb `echo`, i qui la crida el **captura** amb `$( )`:

```bash
doble() {
    echo $(( $1 * 2 ))      # "mostra" el doble
}

resultat=$(doble 5)         # captura el que mostra → resultat = 10
echo "El doble és $resultat"
```

### Per a dir si ha anat bé o malament → `return`

`return` torna un **codi d'eixida** (0 = bé, altre = malament), igual que qualsevol ordre. S'usa per a preguntes de sí o no:

```bash
es_parell() {
    if [ $(( $1 % 2 )) -eq 0 ]; then
        return 0        # sí (bé)
    else
        return 1        # no (malament)
    fi
}

if es_parell 4; then
    echo "4 és parell"
fi
```

| Vull... | Dins la funció | Fora |
| ------- | -------------- | ---- |
| una **dada** (número, text) | `echo valor` | `var=$(funcio)` |
| un **sí/no** | `return 0` / `return 1` | `if funcio; then` |

!!! danger "`return` no serveix per a tornar números"
    `return` només accepta de 0 a 255 i serveix per a dir bé/malament. Per a tornar el resultat d'un càlcul, usa `echo`.

## Variables locals

Normalment, si crees o canvies una variable dins d'una funció, també canvia fora. Això pot trencar coses sense que te n'adones:

```bash
total=100

suma() {
    total=0                    # ❌ xafa el total de fora!
    ...
}
```

Amb `local`, la variable només existix dins de la funció:

```bash
total=100

suma() {
    local total=0              # ✅ esta és una altra variable, només de dins
    for n in "$@"; do
        total=$(( total + n ))
    done
    echo "$total"
}

echo "$(suma 1 2 3)"   # 6
echo "$total"          # 100 (no s'ha tocat)
```

**Regla: posa `local` a les variables que crees dins d'una funció.**

## Funcions útils per a qualsevol script

Pots copiar-les directament:

```bash
# Mostra un error i acaba l'script
error() {
    echo "ERROR: $*" >&2
    exit 1
}

# Mostra un missatge amb l'hora davant
log() {
    echo "[$(date +%H:%M:%S)] $*"
}

# Pregunta sí/no. Torna 0 si diu sí
confirma() {
    read -p "$1 (s/n) " resposta
    [ "$resposta" = "s" ]
}
```

Usar-les:

```bash
[ $# -eq 1 ] || error "Has de passar una carpeta"

if confirma "Segur que vols esborrar $1?"; then
    rm -r "$1"
    log "Esborrat $1"
fi
```

- `$*` són tots els arguments junts (el missatge sencer).
- `>&2` envia el missatge per l'eixida d'errors ([tema 7](07-redireccions.md)).

## Guardar funcions en un altre fitxer

Si tens funcions que uses en molts scripts, les pots guardar en un fitxer a banda i carregar-les amb `source`:

```bash title="funcions.sh"
error() { echo "ERROR: $*" >&2; exit 1; }
```

```bash title="script.sh"
#!/bin/bash
source ./funcions.sh          # carrega les funcions del fitxer
error "Prova"                 # ja la pots usar
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `command not found` en cridar-la | La crides abans de crear-la | Posa les funcions al principi |
| `saluda()` en cridar-la no fa res | Has posat parèntesis | Crida-la sense: `saluda` |
| `return 300` torna un número estrany | `return` només va de 0 a 255 | Per a dades, usa `echo` |
| Una variable de fora canvia sola | La funció la modifica | Usa `local` dins de la funció |

!!! success "Per a l'examen"
    ```bash
    nom_funcio() {
        local var=$1          # $1, $2... = arguments de la funció
        echo "resultat"       # tornar una DADA
        return 0              # tornar BÉ (0) o MALAMENT (1)
    }

    nom_funcio arg1 arg2      # cridar-la (sense parèntesis)
    r=$(nom_funcio 5)         # capturar la dada
    if nom_funcio 5; then     # usar el sí/no
    ```

    - Crear-la **abans** de cridar-la
    - `local` per a les variables de dins
