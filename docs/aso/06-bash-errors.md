# UT1 · 5. Errors, depuració i scripts d'administració

## L'estat d'una ordre és informació

En shell, 0 indica èxit i altres valors indiquen altres resultats. `grep` retorna 1 quan no troba coincidències: no sempre representa una avaria. `$?` canvia amb la següent ordre; sovint és més clar escriure `if ordre; then ...`.

`set -u` detecta variables no definides. `set -e` pot aturar el script davant determinades fallades, però té excepcions en condicionals i altres construccions. `set -o pipefail` fa visible una fallada en una tuberia que acabaria amb una última ordre correcta. Cap opció substitueix tractar els errors esperables.

## Exemple resolt: informe de línies d'un document

**Problema nou:** rebre un fitxer de text i mostrar quantes línies té, inclòs un nom amb espais. No copia fitxers ni crea usuaris.

```bash
#!/usr/bin/env bash
set -u
if (( $# != 1 )); then
    printf 'Ús: bash informe.sh fitxer\n' >&2
    exit 1
fi
fitxer=$1
if [[ ! -f "$fitxer" || ! -r "$fitxer" ]]; then
    printf 'Cal un fitxer ordinari que es puga llegir.\n' >&2
    exit 2
fi
if linies=$(wc -l < "$fitxer"); then
    printf 'Document: %s\nLínies: %s\n' "$fitxer" "$linies"
else
    printf 'No s’ha pogut completar el recompte.\n' >&2
    exit 3
fi
```

### Prova guiada

Crea `text curt.txt` amb `printf 'primera\nsegona\n' > "text curt.txt"`.

| Crida | Resultat esperat |
| --- | --- |
| `bash informe.sh "text curt.txt"` | 2 línies; estat 0 |
| `bash informe.sh absent.txt` | Avís de fitxer; estat 2 |
| `bash informe.sh` | Ajuda; estat 1 |

`wc -l` compta salts de línia. Un últim fragment sense salt final no augmenta el recompte. Eixa distinció pot explicar una aparent diferència amb el que veus en un editor.

El segon `if` contempla que l'ordre falle encara que la comprovació prèvia haja passat: entre comprovar i llegir, l'estat del fitxer podria canviar.

## Com depurar-lo

`bash -n informe.sh` comprova sintaxi sense executar el contingut. `bash -x informe.sh "text curt.txt"` mostra les ordres expandides mentre les executa; evita usar traces sobre secrets. Si tens ShellCheck, `shellcheck informe.sh` ajuda a detectar problemes habituals.

`trap 'printf "Fi del laboratori\n" >&2' EXIT` executa una acció en eixir. També pots capturar senyals o `ERR` segons el cas. Usa `trap` per a neteja i diagnòstic conscient, no per a ocultar una fallada.

## Aplicació a tasques d'administració

Un script de còpies combina comprovació d'origen, ordre d'arxivat, estat i log. Un lector de CSV ha de separar camps sense partir els espais, per exemple amb `while IFS=';' read -r nom zona; do ...; done < dades.csv` per a un format simple sense cometes internes. Un format CSV general requereix un lector adequat.

En gestió d'usuaris o serveis, separa **consultar**, **decidir** i **modificar**. Prova primer la lògica amb dades de laboratori i missatges del que faria. No cal executar altes massives per a entendre un `if`. Per a interpretar un sondeig, recorda també que una IP que no respon a ping no queda demostrada com a lliure: pot filtrar ICMP.

!!! success "Per a repassar"
    Una comprovació ha de produir una decisió i una fallada ha de quedar visible. Abans d'executar un script, identifica què modifica i què necessita per a funcionar.

---

Font del temari: [apunts originals d’ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
