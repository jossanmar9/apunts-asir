# Git i GitHub

## Git i GitHub no són el mateix

| | Git | GitHub |
| - | --- | ------ |
| Què és | un **programa** que guarda l'historial de canvis d'una carpeta | una **web** on guardes còpies dels teus repositoris de Git |
| On funciona | en el teu ordinador | en Internet (github.com) |
| Per a què | tornar a versions anteriors, treballar en branques... | compartir, fer còpia de seguretat, col·laborar, entregar pràctiques |
| Alternatives | — | GitLab, Bitbucket, Gitea |

Pots usar Git sense GitHub (tot en local). GitHub sense Git no té sentit.

## Per què s'usa

- **Historial**: cada vegada que guardes (fas un *commit*), Git recorda com estava tot. Pots tornar enrere quan vulgues.
- **Còpia de seguretat**: si el teu ordinador es trenca, el codi està en GitHub.
- **Treballar en equip**: diverses persones poden canviar el mateix projecte sense xafar-se.
- **Entregar pràctiques**: el professor veu els teus commits, les branques i les *Pull Requests*.

## Ordre recomanat

| Tema | Què aprens |
| ---- | ---------- |
| [1. Conceptes i configuració](01-configuracio.md) | com funciona Git per dins, instal·lar-lo, configurar-lo, claus SSH |
| [2. El treball diari](02-treball-diari.md) | `status`, `add`, `commit`, `log`, `diff`, `.gitignore` |
| [3. GitHub](03-github.md) | `clone`, `push`, `pull`, connectar un repositori local amb GitHub |
| [4. Branques](04-branques.md) | crear branques, fusionar-les i resoldre conflictes |
| [5. Pull Requests](05-pull-requests.md) | el flux de treball de les entregues: branca → PR → revisió → merge |
| [6. Desfer canvis](06-desfer.md) | `restore`, `amend`, `revert`, `reset`, `stash` |

Després: [casos pràctics](casos.md) amb els problemes que més passen i com resoldre'ls.

!!! tip "Durant un examen"
    Cada tema acaba amb el requadre verd **«Per a l'examen»**. La [xuleta de Git](../xuletes/git.md) ho resumix tot en una pàgina.

!!! note "Missatges en valencià"
    Si el teu sistema està en valencià o català, Git mostrarà els missatges traduïts (*«S'ha inicialitzat un repositori buit»*, *«no hi ha res a cometre»*...). En estos apunts es mostren en anglés, que és com els trobaràs en la majoria de llocs, amb la traducció quan cal.
