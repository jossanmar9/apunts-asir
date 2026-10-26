# UT1 · 3. Bucles i funcions: repetir sense duplicar

## Quan convé cada bucle?

`for` recorre una col·lecció coneguda. `while` repeteix mentre una condició és certa. `until` repeteix mentre és falsa. `break` ix del bucle i `continue` passa a la volta següent. En tots els casos has de poder explicar la condició de finalització.

## Exemple resolt: preparar etiquetes de prestatgeries

**Problema nou:** volem quatre etiquetes, excepte la tercera, que està fora de servei. Una funció crea cada etiqueta perquè el format estiga en un únic lloc.

```bash
#!/usr/bin/env bash
etiqueta() {
    local numero=$1
    printf 'PRESTATGE-%02d\n' "$numero"
}
for numero in 1 2 3 4; do
    if (( numero == 3 )); then
        continue
    fi
    etiqueta "$numero"
done
```

**Eixida esperada:** `PRESTATGE-01`, `PRESTATGE-02` i `PRESTATGE-04`, cadascun en una línia.

1. La funció es defineix abans de cridar-la.
2. Dins de la funció, `$1` és el primer argument de **la funció**, no necessàriament el del script.
3. `local` limita la variable a la funció. `%02d` formata l'enter amb almenys dues xifres.
4. `continue` salta l'etiqueta 3, però deixa que el recorregut continue amb 4.

## `while` i `until` amb seguiment

```bash
#!/usr/bin/env bash
pendents=3
while (( pendents > 0 )); do
    printf 'Caixes pendents: %s\n' "$pendents"
    pendents=$((pendents - 1))
done

revisades=0
until (( revisades == 2 )); do
    revisades=$((revisades + 1))
    printf 'Revisió %s completada\n' "$revisades"
done
```

El `while` mostra 3, 2 i 1. El `until` mostra revisions 1 i 2: quan la condició passa a ser certa, ja no entra. Canviar `until` per `while` sense negar la condició altera completament el comportament.

## Funció que calcula i funció que comprova

Bash diferencia **dades per stdout** i **estat per return**:

```bash
#!/usr/bin/env bash
nom_etiqueta() {
    printf 'CAIXA-%s\n' "$1"
}
es_codi() {
    [[ "$1" =~ ^[A-Z]{2}[0-9]{2}$ ]]
}
nom=$(nom_etiqueta 'AB42')
if es_codi 'AB42'; then
    printf '%s és vàlid\n' "$nom"
fi
```

`$(...)` captura el text. La funció de comprovació retorna l'estat de l'última ordre: 0 si el patró coincideix. `return 250` és un codi d'estat, no una manera de retornar un text ni un càlcul arbitrari.

Si separes funcions en un fitxer propi, `source ./funcions.sh` les carrega en la shell actual; executar `bash funcions.sh` inicia una shell filla i no deixa les definicions disponibles en la mare.

| Error | Causa i correcció |
| --- | --- |
| Bucle infinit | No canvia la variable que decideix la parada. |
| Valor capturat conté missatges sobrants | La funció imprimeix depuració per stdout; envia-la a stderr. |
| `return` truncat | Els estats tenen rang limitat; usa stdout per a dades. |

!!! success "Per a repassar"
    Una funció ha de tindre una tasca clara. Dibuixa què rep, què imprimeix i quin estat retorna.

---

Font del temari: [apunts originals d’ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
