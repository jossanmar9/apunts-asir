# Bash scripting

## Què és açò?

Quan obris un **terminal** en Linux i escrius ordres com `ls` o `cd`, qui les entén i les executa és un programa anomenat **shell**. El shell més habitual és **Bash**.

Un **script** és simplement un fitxer de text on escrius diverses ordres, una darrere l'altra. Quan l'executes, Bash les fa totes en ordre, com si les escrigueres tu a mà.

!!! example "Exemple de la vida real"
    Cada dia has de copiar els logs a una carpeta, comprimir-los i esborrar els vells. Són 5 ordres. En compte d'escriure-les cada matí, les poses en un fitxer `backup.sh` i executes només eixe fitxer.

A més d'ordres soltes, un script pot **prendre decisions** (si passa açò, fes allò), **repetir coses** (per a cada fitxer, fes...) i **guardar dades** en variables. Això és el que s'aprén en estos temes.

## Ordre recomanat

Si no has fet mai res, segueix-los en ordre: cada tema usa coses dels anteriors.

| Tema | Què aprens |
| ---- | ---------- |
| [1. Primer script](01-primer-script.md) | crear un script, donar-li permisos i executar-lo |
| [2. Variables i paràmetres](02-variables.md) | guardar dades i rebre-les en executar l'script |
| [3. Aritmètica i comparacions](03-expressions.md) | fer comptes i comparar números, textos i fitxers |
| [4. Condicionals](04-condicionals.md) | prendre decisions amb `if` i `case` |
| [5. Bucles](05-bucles.md) | repetir ordres amb `for`, `while` i `until` |
| [6. Funcions](06-funcions.md) | agrupar codi per a reutilitzar-lo |
| [7. Redireccions i tuberies](07-redireccions.md) | guardar l'eixida en fitxers i encadenar ordres |
| [8. Llegir dades](08-lectura.md) | demanar coses a l'usuari amb `read` i menús |
| [9. Arrays](09-arrays.md) | guardar moltes dades en una sola variable |
| [10. Processar text](10-text.md) | retallar, ordenar i filtrar text |
| [11. find, grep i xargs](11-find-grep-xargs.md) | buscar fitxers i text dins dels fitxers |
| [12. Scripts robustos](12-robustesa.md) | comprovar errors i depurar |

Després: [com resoldre un problema](metode.md) pas a pas i [problemes resolts](problemes.md) per a practicar.

Si et trobes una paraula que no entens (*argument*, *procés*, *stdout*...), mira el [glossari](../glossari.md).

!!! tip "Com estudiar açò"
    Obri un terminal al costat i **prova cada exemple**. Canvia algun valor i torna a executar-lo. Bash s'aprén fent, no només llegint.

!!! tip "Durant un examen"
    Cada tema acaba amb un requadre verd **«Per a l'examen»** amb el més important. Si tens pressa, ves directament allí. La [xuleta de Bash](../xuletes/bash.md) ho resumix tot en una pàgina.
