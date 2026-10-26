# Xuleta de Git

> Consulta ràpida. La teoria completa està en la [secció de Git i GitHub](../git/index.md).

## Configuració (una vegada)

```bash
git config --global user.name "El teu nom"
git config --global user.email "correu@exemple.com"
git config --global init.defaultBranch main
git config --global pull.rebase false
ssh-keygen -t ed25519 -C "correu@exemple.com"     # clau SSH → copiar ~/.ssh/id_ed25519.pub a GitHub
ssh -T git@github.com                             # comprovar
```

## Començar

```bash
git clone git@github.com:usuari/repo.git          # repositori que ja existix
git init                                          # carpeta nova
git remote add origin git@github.com:usuari/repo.git
git push -u origin main                           # primera pujada
```

## Flux diari

```bash
git pull                          # 1. baixar el més nou
git status                        # 2. què ha canviat
git add fitxer  /  git add .      # 3. preparar
git commit -m "Missatge clar"     # 4. guardar
git push                          # 5. pujar
```

## Mirar

| Ordre | Fa |
| ----- | -- |
| `git status` / `git status -s` | estat dels fitxers |
| `git log --oneline --graph --all` | historial amb branques |
| `git diff` / `git diff --staged` | canvis sense / amb add |
| `git show ID` | què va canviar en un commit |
| `git remote -v` | a on apunta el remot |
| `git branch -a` | totes les branques |

## Branques

```bash
git switch -c nova                # crear i canviar
git switch main                   # canviar
git push -u origin nova           # pujar-la la primera vegada
git merge nova                    # (estant en main) fusionar
git branch -d nova                # esborrar
git merge --abort                 # cancel·lar una fusió amb conflictes
```

**Conflicte**: editar el fitxer → llevar `<<<<<<<` `=======` `>>>>>>>` → `git add` → `git commit`

## Pull Request

1. `git switch main && git pull`
2. `git switch -c bloc-de-feina`
3. `add` + `commit` · `git push -u origin bloc-de-feina`
4. GitHub → **Compare & pull request** (cap a `main`)
5. Canvis demanats → commit + push en la **mateixa** branca
6. **Merge** → `git switch main && git pull && git branch -d bloc-de-feina`

## Desfer

| Vull... | Ordre |
| ------- | ----- |
| descartar canvis d'un fitxer | `git restore fitxer` |
| desfer un `add` | `git restore --staged fitxer` |
| corregir l'últim commit (sense push) | `git commit --amend` |
| desfer un commit **pujat** | `git revert ID` |
| desfer l'últim commit local, conservant canvis | `git reset --soft HEAD~1` |
| guardar canvis a mitges | `git stash` · `git stash pop` |
| deixar de controlar un fitxer | `git rm --cached fitxer` |
| recuperar alguna cosa "perduda" | `git reflog` |

## Errors freqüents

| Missatge | Solució |
| -------- | ------- |
| `! [rejected] ... (fetch first)` | `git pull` i després `git push` |
| `divergent branches` | `git config --global pull.rebase false` |
| `remote origin already exists` | `git remote set-url origin URL` |
| `has no upstream branch` | `git push -u origin nom-branca` |
| `not a git repository` | no estàs en la carpeta, o falta `.git` |
| Demana contrasenya | usa SSH: `git remote set-url origin git@github.com:u/r.git` |
| `Permission denied (publickey)` | clau SSH no afegida a GitHub |

!!! warning "Mai"
    - `git push --force` en `main`
    - pujar `.env` o contrasenyes (posa'ls en `.gitignore`)
    - substituir la carpeta del projecte (es perd `.git`): copia el contingut per damunt
