# Bash scripting

Un script de Bash és un fitxer de text amb ordres que el shell executa una darrere l'altra. Serveix per a automatitzar el que faries a mà en el terminal: crear usuaris, revisar logs, fer còpies de seguretat, vigilar el disc...

## Ordre recomanat

| Tema | Què aprens |
| ---- | ---------- |
| [1. Primer script](01-primer-script.md) | shebang, permisos, com s'executa |
| [2. Variables i paràmetres](02-variables.md) | variables, `$1`, `$#`, `"$@"`, cometes |
| [3. Aritmètica i comparacions](03-expressions.md) | `$(( ))`, `bc`, `[ ]`, `[[ ]]`, codis d'eixida |
| [4. Condicionals](04-condicionals.md) | `if`, `elif`, `case`, `&&` i `\|\|` |
| [5. Bucles](05-bucles.md) | `for`, `while`, `until`, llegir fitxers línia a línia |
| [6. Funcions](06-funcions.md) | `return` vs `echo`, `local`, `source` |
| [7. Redireccions i tuberies](07-redireccions.md) | `>`, `2>`, `/dev/null`, `\|`, here-doc, `tee` |
| [8. Llegir dades](08-lectura.md) | `read` i les seues opcions, menús amb `select` |
| [9. Arrays](09-arrays.md) | vectors indexats i associatius |
| [10. Processar text](10-text.md) | `${var#...}`, `cut`, `tr`, `sort`, `uniq`, `awk`, `sed` |
| [11. find, grep i xargs](11-find-grep-xargs.md) | buscar fitxers i text, passar llistes a ordres |
| [12. Scripts robustos](12-robustesa.md) | validar arguments, `set -euo pipefail`, `trap`, depurar |

Després: [com resoldre un problema](metode.md) pas a pas i una col·lecció de [problemes resolts](problemes.md).

!!! tip "Com estudiar açò"
    Obri un terminal al costat i prova **cada** exemple. Canvia valors, trenca'l a propòsit i mira què passa. Bash s'aprén executant, no llegint.
