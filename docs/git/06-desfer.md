# 6. Desfer canvis

Una de les coses bones de Git és que quasi tot es pot desfer. Però hi ha diverses ordres i cada una és per a una situació diferent.

## Quina use?

| Vull desfer... | Ordre | Perilla? |
| -------------- | ----- | -------- |
| els canvis d'un fitxer que **encara no he afegit** | `git restore fitxer` | ⚠️ perds eixos canvis |
| un `git add` (traure del staging) | `git restore --staged fitxer` | ✅ no perds res |
| el **missatge** de l'últim commit (o afegir-hi un fitxer oblidat) | `git commit --amend` | ✅ si encara no l'has pujat |
| un commit que **ja he pujat** a GitHub | `git revert ID` | ✅ segur |
| l'últim commit, **conservant** els canvis | `git reset --soft HEAD~1` | ✅ si no l'has pujat |
| l'últim commit **i els seus canvis** | `git reset --hard HEAD~1` | ⛔ perds la feina |
| guardar canvis a mitges per a més tard | `git stash` | ✅ |

## Canvis que encara no estan en un commit

### Descartar els canvis d'un fitxer

```bash
git restore script.sh       # torna el fitxer a com estava en l'últim commit
git restore .               # tots els fitxers modificats
```

!!! danger "No es pot desfer"
    Els canvis que descartes amb `git restore` no estaven guardats en cap commit: **es perden**.

### Traure un fitxer del staging

Has fet `git add` d'un fitxer que no volies en el pròxim commit:

```bash
git restore --staged fitxer.txt     # deixa de estar preparat, però conserva els canvis
```

### Esborrar fitxers nous que no vols

```bash
git clean -n        # mostra què esborraria (sense esborrar)
git clean -f        # esborra els fitxers no controlats
```

## Corregir l'últim commit: `--amend`

```bash
git commit --amend -m "Missatge corregit"      # canviar el missatge
```

T'has oblidat d'afegir un fitxer:

```bash
git add fitxer_oblidat.sh
git commit --amend --no-edit       # l'afig a l'últim commit sense canviar el missatge
```

!!! warning "Només si encara no has fet push"
    `--amend` reescriu el commit. Si ja estava en GitHub, el següent push serà rebutjat. En eixe cas, fes simplement un commit nou.

## Desfer un commit ja pujat: `git revert`

`revert` **no esborra** el commit: en crea un de **nou** que fa just el contrari. L'historial queda intacte, i per això és **segur** amb commits que ja estan en GitHub.

```bash
git log --oneline
```

```console
6dc31db Afig la funció de backup      ← este és el que vull desfer
875bfc6 Corregix la validació
155969d Primer commit
```

```bash
git revert 6dc31db
git push
```

```console
decf75b Revert "Afig la funció de backup"
6dc31db Afig la funció de backup
875bfc6 Corregix la validació
```

## Tornar enrere commits locals: `git reset`

`reset` mou la branca a un commit anterior. **Només per a commits que encara NO has pujat.**

`HEAD~1` vol dir "un commit abans d'on estic"; `HEAD~3`, tres abans.

| Ordre | Els commits | Els canvis dels fitxers |
| ----- | ----------- | ----------------------- |
| `git reset --soft HEAD~1` | es desfan | es queden **en staging** (preparats) |
| `git reset HEAD~1` | es desfan | es queden en la carpeta (sense `add`) |
| `git reset --hard HEAD~1` | es desfan | ⛔ **s'esborren** |

L'ús més habitual: *«he fet un commit massa prompte, vull tornar-lo a fer»*:

```bash
git reset --soft HEAD~1     # desfà el commit, conserva els canvis preparats
# ... canvies el que vulgues ...
git commit -m "Ara sí, el commit bo"
```

!!! danger "`git reset --hard` és perillós"
    Esborra els canvis per a sempre (quasi: vegeu `reflog` baix). Abans d'usar-lo, fes `git status` i assegura't que no hi ha res que vulgues conservar.

## `stash`: guardar canvis temporalment

Estàs a mitges d'alguna cosa i necessites canviar de branca o fer `pull`, però encara no vols fer commit:

```bash
git stash                  # guarda els canvis en un "calaix" i deixa la carpeta neta
git switch altra-branca    # fas el que necessites...
git switch -               # torna a la branca anterior
git stash pop              # recupera els canvis del calaix
```

```bash
git stash list             # veure què hi ha guardat
git stash drop             # esborrar l'últim stash sense aplicar-lo
git stash -u               # incloure també fitxers nous (no controlats)
```

## La xarxa de seguretat: `git reflog`

`reflog` guarda **tots els moviments** que has fet (commits, resets, canvis de branca...), també els que ja no apareixen en `git log`. Si has fet un `reset --hard` i te n'has penedit:

```bash
git reflog
```

```console
875bfc6 HEAD@{0}: reset: moving to HEAD~1
6dc31db HEAD@{1}: commit: Afig la funció de backup     ← el commit "perdut"
```

```bash
git reset --hard 6dc31db    # tornar a eixe punt
```

## Veure versions antigues

```bash
git show 875bfc6                    # què va canviar en un commit
git show 875bfc6:script.sh          # com era un fitxer en eixe commit
git restore --source=875bfc6 script.sh   # recuperar el fitxer tal com era
```

!!! success "Per a l'examen"
    | Situació | Ordre |
    | -------- | ----- |
    | descartar canvis d'un fitxer (sense add) | `git restore fitxer` |
    | desfer un `git add` | `git restore --staged fitxer` |
    | corregir l'últim commit (sense push) | `git commit --amend` |
    | desfer un commit **pujat** | `git revert ID` ✅ |
    | desfer l'últim commit **local** conservant canvis | `git reset --soft HEAD~1` |
    | guardar canvis a mitges | `git stash` / `git stash pop` |
    | recuperar alguna cosa "perduda" | `git reflog` |
    - Pujat a GitHub → **revert**. Només local → **reset** o **amend**.
