# 1. Primer script

## Crear-lo i executar-lo

```bash title="hola.sh"
#!/bin/bash
# Mostra una salutació amb l'usuari i la data
echo "Hola, $USER!"
echo "Hui és $(date +%d/%m/%Y)"
```

```bash
chmod +x hola.sh      # permís d'execució (una sola vegada)
./hola.sh             # executar-lo
```

| Forma d'executar | Què passa |
| ---------------- | --------- |
| `./hola.sh` | Crea un procés nou amb l'intèrpret del shebang. Necessita permís `x`. |
| `bash hola.sh` | Força Bash, encara que no tinga permís `x` ni shebang. |
| `source hola.sh` o `. hola.sh` | L'executa **dins del shell actual**: les variables i els `cd` es queden. |

!!! question "Per què `./` davant?"
    El shell només busca ordres en els directoris de `$PATH`, i el directori actual no hi és per seguretat. Amb `./` li dius la ruta exacta.

## El shebang

La primera línia, `#!/bin/bash`, indica quin programa ha d'interpretar el fitxer. Sense ella, el sistema usaria el shell per defecte (en Debian/Ubuntu és `dash`, que no entén moltes coses de Bash com `[[ ]]` o els arrays).

```bash
#!/bin/bash            # el més habitual
#!/usr/bin/env bash    # busca bash en el PATH (més portable)
```

## Comentaris

Tot el que va després de `#` (fora de cometes) s'ignora. Bona pràctica: una capçalera curta que diga què fa l'script i com s'usa.

```bash
#!/bin/bash
# copia_logs.sh — copia els logs del dia a /backup
# Ús: ./copia_logs.sh [directori_destí]
```

## Codi d'eixida

Tota ordre acaba amb un número: **0 vol dir que ha anat bé** i qualsevol altre valor (1–255) que ha fallat. El de l'última ordre està en `$?`.

```bash
ls /etc > /dev/null
echo $?        # 0
ls /no_existix
echo $?        # 2
```

Un script ha d'acabar amb `exit 0` si tot ha anat bé i amb `exit 1` (o un altre número) si hi ha hagut un error. Si no poses `exit`, el codi de l'script és el de l'última ordre.

## On guardar els scripts

```bash
mkdir -p ~/bin
mv hola.sh ~/bin/hola
# En Ubuntu, ~/bin s'afig al PATH automàticament si existix en iniciar sessió.
hola
```
