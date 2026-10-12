# Consells de programadors

Una selecció d'idees del llibre *100 cosas que todo programador debería saber* (inspirat en *97 Things Every Programmer Should Know*), explicades amb paraules nostres i aplicades a scripts de Bash, Python, PowerShell i PHP. Entre parèntesis, la persona a qui el llibre atribuïx cada idea.

## 1. El codi es llig molt més que s'escriu (Guido van Rossum)

Passes molt més temps **llegint** codi (el teu de la setmana passada, el d'un company) que escrivint-lo. Escriu pensant en qui l'haurà de llegir: tu d'ací a uns mesos.

```bash
# ❌ Què és $a? Què fa?
for a in $(ls /home); do du -sh /home/$a; done

# ✅ S'entén llegint-lo
for usuari in /home/*/; do
    du -sh "$usuari"
done
```

**La prova**: llig-lo en veu alta. Si sona com una frase que s'entén, està bé.

## 2. Els noms expliquen la intenció (Robert C. Martin)

Un bon nom estalvia un comentari.

```python
# ❌
d = 7
for f in fs:
    if edat(f) > d: ...

# ✅
DIES_A_CONSERVAR = 7
for copia in copies:
    if dies_des_de(copia) > DIES_A_CONSERVAR: ...
```

- Variables: el **què** (`total_alumnes`, `fitxer_log`). Funcions: un **verb** (`crear_usuari`, `comprova_disc`).
- En PowerShell, la convenció ja t'ajuda: `Verb-Nom` (`Get-Service`, `New-LocalUser`).

## 3. Una funció fa una sola cosa (Robert C. Martin)

Si una funció valida, calcula, escriu un fitxer i envia un correu, és difícil de provar i d'arreglar. Divideix-la: la funció principal es llig com un índex.

```bash
main() {
    comprova_permisos
    crea_carpeta_copies
    fes_copia "/home"
    esborra_copies_velles 7
}
```

## 4. Divideix el problema fins que cada part siga trivial (Edsger W. Dijkstra)

Un problema difícil és un conjunt de problemes fàcils que encara no has separat. Abans d'escriure codi, escriu els passos en paraules (o en comentaris) i resol-los un a un, **provant cada pas**. Vegeu [el mètode](../bash/metode.md).

## 5. Fes que funcione, després fes-ho bé (Kent Beck)

L'ordre és: **que funcione** → **que estiga ben fet** (noms, funcions, sense repetir) → **que vaja ràpid** (només si cal). No intentes fer-ho perfecte a la primera: primer una versió senzilla que funcione, i després la millores.

## 6. La simplicitat és la base de la fiabilitat (Dijkstra)

El codi més senzill és el que menys falla. Si hi ha una forma clara i una d'«enginyosa», tria la clara. Depurar és més difícil que escriure el codi (Brian Kernighan): si l'escrius al límit de la teua intel·ligència, no seràs capaç de depurar-lo.

```python
# ❌ «Enginyós»
r=[x*2 for x in l if not x%2]

# ✅ Clar
parells = [n for n in numeros if n % 2 == 0]
dobles = [n * 2 for n in parells]
```

## 7. Explícit millor que implícit (Guido van Rossum)

Que el codi diga el que fa, sense haver d'endevinar.

```bash
set -euo pipefail                 # que l'script s'ature si alguna cosa falla
rm -rf -- "${CARPETA:?no definida}"/*   # si $CARPETA està buida, s'atura (i no esborra /*)
```

```powershell
Remove-Item -Path $Carpeta -Recurse -WhatIf      # primer, mira què faria
```

## 8. El millor error és el que s'explica sol (Evan Czaplicki)

Quan el teu script falla, que diga **què** ha passat i **com** arreglar-ho.

```bash
# ❌
[[ -f "$1" ]] || exit 1

# ✅
if [[ ! -f "$1" ]]; then
    echo "Error: no trobe el fitxer '$1'." >&2
    echo "Ús: $0 fitxer_usuaris.txt" >&2
    exit 1
fi
```

## 9. Per a arreglar un error, primer reproduïx-lo (Julia Evans)

No canvies coses a l'atzar esperant que funcione. Observa → fes una hipòtesi → **fes que falle sempre igual** → arregla → comprova. Si un error «a vegades passa», encara no l'entens.

## 10. Si ho fas tres vegades, automatitza-ho (Jeff Atwood)

La primera vegada aprens, la segona confirmes, la tercera és hora d'un script. És el sentit de saber Bash, PowerShell, Python, Docker Compose o Ansible.

## 11. Git és la teua màquina del temps (Julia Evans, Linus Torvalds)

Un missatge de commit és l'única explicació que tindràs d'ací a uns mesos de **per què** vas canviar alguna cosa.

```bash
# ❌
git commit -m "fix"
git commit -m "canvis"

# ✅
git commit -m "Corregix la còpia quan la carpeta té espais"
git commit -m "Afig la validació del correu al formulari de contacte"
```

- Commits **menuts** i amb una sola idea.
- Titular curt (unes 50 lletres), en present: *Afig*, *Corregix*, *Esborra*.
- Vegeu [Git](../git/index.md).

## 12. La terminal és el teu superpoder (Jessie Frazelle)

Tot el que fas amb el ratolí es pot fer, repetir i automatitzar des del terminal. Com més còmode estigues en Bash i PowerShell, més ràpid treballaràs. I els **contenidors** permeten provar programes sense embrutar el teu sistema: `docker run --rm -it ubuntu bash`.

## 13. La seguretat comença en el codi (Parisa Tabriz)

Les tres regles que eviten la majoria de problemes en una aplicació web ([PHP](../php/index.md)):

1. **Valida** el que arriba de l'usuari.
2. **Escapa** el que mostres (`htmlspecialchars`).
3. **Prepara** les consultes a la base de dades (mai concatenar).

I mai contrasenyes dins del codi ni en Git.

## 14. El codi de la IA s'ha de revisar (Andrej Karpathy)

La IA genera codi que «funciona» però que pot ser insegur o incorrecte (SQL concatenat, dades sense escapar, claus d'exemple que pareixen reals). És una ajuda molt bona, però **tu** has d'entendre i revisar cada línia, i provar-la. Les bases que aprens en el cicle són el que et permet saber si el que proposa és bo.

## 15. No reinventes la roda (Kent C. Dodds)

Abans de fer un script de 100 línies, mira si ja hi ha una ordre o un mòdul que ho fa (`rsync`, `find -mtime`, `pathlib`, `Get-ChildItem -Recurse`). Excepte si l'estàs fent **per a aprendre**: aleshores, fes-la!

## 16. Aprén fent, i aprén en públic (Limor Fried, Cassidy Williams)

- La millor manera d'aprendre és **construir** alguna cosa teua: un script que t'estalvie feina, una web en Docker, un CRUD en PHP.
- Comparteix el que aprens (un README en el teu GitHub, explicar-ho a un company): explicar-ho t'obliga a entendre-ho, i reps correccions.
- No cal ser expert per a ensenyar: només cal saber una cosa que algú altre encara no sap.

## 17. Pregunta el que no saps, encara que semble obvi (Julia Evans)

Tothom té dubtes «bàsics». Pregunta de manera **concreta** («Què passa exactament quan escric `ls` i prem Intro?») i apunta el que aprens.

## 18. Cuida la teua salut (Cassidy Williams)

Cremar-se no demostra que treballes molt: demostra que alguna cosa no va bé. Descansa, dorm, i no medeixes el teu valor per les hores davant de la pantalla.

!!! success "En una frase"
    Codi **clar** (bons noms, funcions menudes, errors que s'expliquen), fet **pas a pas** i provant, guardat en **Git** amb bons missatges, **segur** per defecte, i aprenent **fent**.
