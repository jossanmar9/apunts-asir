# UT1 · 2. Càlculs, comprovacions i decisions en Bash

## Tres tipus de comprovació

Per a enters, `(( expressio ))` permet calcular i comparar. Per a text i fitxers, `[[ condicio ]]` és còmode en Bash. La forma clàssica `[ condicio ]` també existeix i exigeix espais al voltant dels claudàtors i operands ben separats.

| Necessitat | Expressió de Bash |
| --- | --- |
| Fitxer ordinari | `[[ -f "$ruta" ]]` |
| Directori | `[[ -d "$ruta" ]]` |
| Existeix una entrada | `[[ -e "$ruta" ]]` |
| Enllaç simbòlic | `[[ -L "$ruta" ]]` |
| Text buit / no buit | `[[ -z "$text" ]]` / `[[ -n "$text" ]]` |
| Text igual | `[[ "$text" == "obert" ]]` |
| Enter almenys 3 | `(( quantitat >= 3 ))` |

`-e` pot ser fals en un enllaç trencat: usa també `-L` si vols detectar qualsevol enllaç. `&&` significa «i», `||` significa «o» i `!` nega una condició. Una ordre amb codi 0 es considera correcta o certa en un `if`.

## Exemple resolt: comprovar una reserva de butaques

**Problema nou:** una sala de prova té 12 butaques lliures. El script accepta una quantitat entre 1 i 12, escrita amb una o dues xifres sense zeros inicials.

```bash
#!/usr/bin/env bash
peticio=${1:-}
if [[ ! "$peticio" =~ ^[1-9][0-9]?$ ]]; then
    printf 'Escriu una quantitat d’una o dues xifres, sense zero inicial.\n' >&2
    exit 1
fi
lliures=12
if (( peticio > lliures )); then
    printf 'No hi ha prou butaques.\n'
elif (( peticio == lliures )); then
    printf 'La sala queda completa.\n'
else
    resten=$((lliures - peticio))
    printf 'Reserva acceptada. Queden %s butaques.\n' "$resten"
fi
```

### Segueix tres entrades

| Crida | Condició | Eixida esperada |
| --- | --- | --- |
| `bash butaques.sh 5` | 5 < 12 | Queden 7 butaques |
| `bash butaques.sh 12` | 12 = 12 | Sala completa |
| `bash butaques.sh 13` | 13 > 12 | No hi ha prou butaques |
| `bash butaques.sh cinc` | No passa el patró | Missatge d'entrada incorrecta |

La validació es fa **abans** de l'aritmètica. `^` i `$` ancoren tot el text; `[1-9]` és la primera xifra i `[0-9]?` permet una segona opcional. El patró sense cometes a la dreta de `=~` és una expressió regular, no text literal.

## Aritmètica i opcions de menú

`$((7 / 2))` dona 3: l'aritmètica ordinària de Bash és entera. `%` calcula el residu. Per a decimals pots usar `bc`, si està instal·lat:

```bash
printf 'scale=2; 7 / 2\n' | bc
```

Resultat: `3.50`. `scale` controla decimals en la divisió; no és una regla universal d'arrodoniment monetari. `expr` i `let` apareixen en scripts antics, però `$((...))` acostuma a ser més llegible.

Per a opcions concretes, `case` evita cadenes llargues d'igualtats:

```bash
accio=${1:-ajuda}
case "$accio" in
    resum) printf 'Mostra el resum de la sala\n' ;;
    ajuda) printf 'Opcions: resum, ajuda\n' ;;
    *) printf 'Opció desconeguda\n' >&2; exit 1 ;;
esac
```

!!! success "Per a repassar"
    Primer comprova la forma de la dada; després fes càlculs o decisions. No confongues `=` d'assignació, igualtat de text i comparació numèrica.

---

Font del temari: [apunts originals d’ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
