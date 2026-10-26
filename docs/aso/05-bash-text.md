# UT1 · 4. Fitxers, tuberies, filtres i expressions regulars

## Connectar ordres

Una ordre disposa d'entrada estàndard, eixida estàndard i eixida d'error. `>` crea o sobreescriu; `>>` afegeix; `2>` redirigeix errors; `|` envia stdout a l'entrada de l'ordre següent. L'error no entra automàticament en la tuberia.

`grep` selecciona línies, `cut` extrau camps, `sort` ordena, `uniq` agrupa repeticions consecutives i `wc` compta. `awk` treballa bé amb camps i `sed` amb transformacions de text. `find` busca entrades del sistema de fitxers segons nom, tipus o altres propietats.

## Cas resolt: resum d'incidències d'un taller

Crea un fitxer de prova `taller.log`:

```text
INFO|fusta|arribada
ERROR|pintura|falta material
ERROR|fusta|peça trencada
INFO|pintura|revisió
ERROR|pintura|ventilació
```

**Objectiu nou:** comptar errors per zona.

```bash
grep '^ERROR|' taller.log | cut -d'|' -f2 | sort | uniq -c
```

### Què passa en cada tram?

1. `grep` conserva tres línies que comencen per `ERROR|`. En aquest patró bàsic, `|` és un caràcter literal.
2. `cut` obté el segon camp: pintura, fusta, pintura.
3. `sort` junta les dues aparicions de pintura.
4. `uniq -c` compta cada grup: un error de fusta i dos de pintura. L'ordre i els espais de la presentació poden dependre de la configuració regional.

Sense ordenar, les dues línies de pintura no serien consecutives i no formarien un únic grup.

Per a guardar el resum sense esborrar el log:

```bash
grep '^ERROR|' taller.log | cut -d'|' -f2 | sort | uniq -c > resum.txt
```

`resum.txt` és l'eixida. No uses el mateix fitxer com a entrada i com a destinació de `>`: es podria buidar abans de llegir-lo.

## Altres maneres de preguntar sobre el mateix fitxer

```bash
awk -F'|' '$1 == "ERROR" {print $2 ": " $3}' taller.log
sed 's/^INFO|/AVIS|/' taller.log
wc -l < taller.log
```

`awk` selecciona segons el primer camp i mostra els altres dos. `sed` imprimeix una versió transformada, sense modificar el fitxer perquè no usa `-i`. `wc` dona 5 línies si el fitxer té el salt de línia final.

## Patró de nom o expressió regular?

`find . -type f -name '*.log'` busca noms amb un patró de shell; les cometes eviten que la shell l'expanda abans. `grep -E '^(ERROR|AVIS)\|' fitxer` usa una expressió regular estesa: l'alternança és `|` i la barra amb `\|` busca el separador literal.

| Element d'una expressió regular | Lectura |
| --- | --- |
| `^` / `$` | Inici / final de línia |
| `[0-9]` | Una xifra |
| `.` | Un caràcter qualsevol |
| `\.` | Un punt literal |
| `+` amb `-E` | Una o més repeticions |

Un patró amb quatre grups d'una a tres xifres detecta la **forma** d'una IPv4, però no garanteix que cada octet estiga entre 0 i 255. No confundisques reconéixer una forma amb validar tot el significat.

!!! success "Per a repassar"
    Prova cada tram de la tuberia per separat. Si el resultat és incorrecte, localitza el primer tram on les dades deixen de ser les esperades.

---

Font del temari: [apunts originals d’ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
