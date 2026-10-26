# Com resoldre un problema

La majoria de vegades que un script no ix, el problema no és Bash: és que s'ha començat a escriure codi abans d'entendre què es demanava. Este és un mètode que funciona.

## 1. Converteix l'enunciat en un exemple d'ús

Abans de pensar en codi, escriu **com es cridarà l'script i què ha de respondre** quan estiga acabat:

```console
$ ./nom.sh Laura Pons Ferrer
Pons Ferrer, Laura
```

Si no saps escriure este exemple, encara no has entés l'enunciat. Torna a llegir-lo. Pregunta't també:

- Les dades arriben **per argument** (`$1`) o **per teclat** (`read`) o **d'un fitxer**?
- Què ha de passar si falten arguments o són incorrectes?

## 2. Simplifica

Resol primer una versió més fàcil i amplia-la després:

| Enunciat complet | Versió simple per a començar |
| ---------------- | ---------------------------- |
| Sumar tots els números d'un fitxer i calcular percentatges per ofici | Mostrar cada línia del fitxer |
| Endevinar un número aleatori amb intents | Comparar amb un número fix (4) |
| Gestionar processos amb menú i confirmació | Mostrar els processos de l'usuari |

Pots canviar l'enunciat a la teua manera mentre proves. Quan la versió simple funcione, torna a l'original.

## 3. Avança en passos que puguen provar-se

No escrigues 40 línies i després executes. Escriu 3 línies, executa, comprova. Afig 3 més.

```bash
#!/bin/bash
while read -r linia; do
    echo "LLEGIT: [$linia]"     # pas 1: llig bé el fitxer?
done < salaris.txt
```

Quan funcione, substituïx l'`echo` per la lògica real.

!!! tip "Treballa amb dues finestres"
    Editor obert en una, terminal en l'altra. Guarda, executa, mira, corregix. No tanques l'editor cada vegada.

## 4. Si falla, primer entén per què

No canvies coses a l'atzar fins que funcione. Esbrina **què** està passant:

```bash
bash -x script.sh              # mostra cada ordre amb els valors reals
echo "DEBUG: n=[$n]" >&2       # mira què val la variable de veritat
```

Errors típics que ixen així:

- Una variable buida perquè has escrit el nom diferent (`$totla`).
- Un espai que falta en `[ "$a" -gt 5 ]` o que sobra en `a = 5`.
- Un `read` que llig la línia sencera perquè el separador no és el que creies.
- Una variable modificada dins d'un `cat f | while`, que es perd en eixir (vegeu el [tema 5](05-bucles.md)).

## 5. Fes-lo robust al final

Quan el cas normal funcione, afig les comprovacions: nombre d'arguments, si el fitxer existix, si els números són números ([tema 12](12-robustesa.md)).

## Esquelet de partida

```bash
#!/bin/bash
# Què fa:
# Ús:      ./script.sh <arg>
# Exemple: ./script.sh 5  →  ...

# 1. Comprovar arguments
[ $# -eq 1 ] || { echo "Ús: $0 <arg>" >&2; exit 1; }

# 2. Variables amb nom clar
dada=$1

# 3. Lògica (començar per la versió simple)

# 4. Resultat
```
