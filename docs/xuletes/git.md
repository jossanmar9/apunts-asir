# Xuleta de Git

## Flux diari

```bash
git pull                      # baixa canvis
git status                    # què ha canviat
git add .                     # prepara tot
git commit -m "Missatge"      # guarda
git push                      # puja a GitHub
```

## Comandaments útils

| Comandament | Què fa |
| ----------- | ------ |
| `git clone URL` | Clona un repositori |
| `git log --oneline --graph` | Historial compacte |
| `git diff` | Canvis no preparats |
| `git switch -c branca` | Crea i canvia de branca |
| `git merge branca` | Fusiona una branca |
| `git restore fitxer` | Descarta canvis d'un fitxer |
| `git restore --staged fitxer` | Trau del staging |
| `git commit --amend` | Corregeix l'últim commit |
| `git stash` / `git stash pop` | Guarda i recupera canvis temporals |
| `git remote -v` | Mostra els remots |

!!! warning "Abans de `push --force`"
    Només en branques teues: reescriu l'historial del remot.
