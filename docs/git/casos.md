# Casos pràctics

Problemes reals que passen treballant amb Git i GitHub, i com resoldre'ls pas a pas.

## Em demana usuari i contrasenya, i la contrasenya no funciona

GitHub no accepta la contrasenya del compte en el terminal. El remot està en HTTPS.

```bash
git remote -v
# origin  https://github.com/usuari/repo.git (fetch)   ← HTTPS
```

**Solució**: configura una clau SSH ([tema 1](01-configuracio.md#configurar-ssh-recomanat)) i canvia el remot:

```bash
git remote set-url origin git@github.com:usuari/repo.git
git remote -v          # ara ha de dir git@github.com:...
git push
```

## `error: remote origin already exists`

Has fet `git remote add origin ...` en un repositori que ja tenia el remot. No cal afegir-lo: com a molt, canviar-lo.

```bash
git remote -v                               # mira a on apunta
git remote set-url origin URL_CORRECTA      # canvia-la si no és la bona
```

## He substituït la carpeta del projecte i Git diu «not a git repository»

En reemplaçar la carpeta sencera, s'ha perdut la carpeta oculta `.git` (on hi ha l'historial i la connexió amb GitHub).

**Si la versió de GitHub és la que val**: torna a clonar i copia damunt els fitxers nous.

```bash
cd ~/Institut
mv projecte projecte_nou                         # aparta la carpeta sense .git
git clone git@github.com:usuari/projecte.git     # recupera el repositori
cp -r projecte_nou/. projecte/                   # copia els fitxers nous DAMUNT
cd projecte
git status                                       # veuràs els canvis
git add -A && git commit -m "Actualitza el projecte" && git push
```

**Si vols que la carpeta nova substituïsca tot el de GitHub** (perdent l'historial):

```bash
git init
git branch -M main
git remote add origin git@github.com:usuari/projecte.git
git add . && git commit -m "Nova versió"
git push -u origin main --force                  # sobreescriu GitHub
```

!!! tip "Per a no tornar-hi a caure"
    Per a actualitzar un projecte, **copia el contingut per damunt** (`cp -r nou/. projecte/`), no substituïsques la carpeta.

!!! warning "El terminal es queda en la carpeta esborrada"
    Si esborres o mous una carpeta mentre el terminal està dins, el terminal continua "dins" de la carpeta vella (que pot estar en la paperera). Fes `cd` de nou a la ruta abans de continuar, i comprova-ho amb `pwd`.

## Push rebutjat: `! [rejected] ... (fetch first)`

En GitHub hi ha commits que no tens (d'un company, d'un altre ordinador o editats des de la web).

```bash
git pull               # baixa i ajunta
git push               # ara sí
```

Si `pull` diu *divergent branches*: `git config --global pull.rebase false` i torna a fer `git pull`.

## Conflicte en fer `pull` o `merge`

```console
CONFLICT (content): Merge conflict in README.md
```

1. Obri el fitxer, busca `<<<<<<<`.
2. Deixa el text bo i esborra les línies `<<<<<<<`, `=======` i `>>>>>>>`.
3. `git add README.md`
4. `git commit -m "Resol el conflicte"`
5. `git push`

Si vols tornar enrere: `git merge --abort`. Detalls en el [tema 4](04-branques.md#conflictes).

## He treballat en `main` i havia de ser en una branca

**Si encara no has fet commit**: crea la branca ara; els canvis van amb tu.

```bash
git switch -c ut3-practica      # els canvis sense commit passen a la branca nova
git add . && git commit -m "..."
git push -u origin ut3-practica
```

**Si ja has fet commit (però no push)**:

```bash
git branch ut3-practica          # 1. crea una branca que apunta als teus commits
git reset --hard origin/main     # 2. torna main a com està en GitHub
git switch ut3-practica          # 3. continua en la branca: els commits estan ací
git push -u origin ut3-practica
```

**Si ja has fet push a `main`**: pregunta al professor. Normalment es deixa com està i a partir d'ara es treballa amb branques.

## He pujat un fitxer amb contrasenyes

1. **Canvia immediatament les contrasenyes** que hi havia. Encara que esborres el fitxer, queda en l'historial de GitHub i algú pot haver-lo vist.
2. Lleva'l del repositori (però no de la carpeta) i ignora'l a partir d'ara:

    ```bash
    git rm --cached .env
    echo ".env" >> .gitignore
    git add .gitignore
    git commit -m "Lleva .env del repositori"
    git push
    ```

3. Crea un `.env.example` amb els noms de les variables però sense els valors de veritat.

## M'he equivocat en el missatge de l'últim commit

**Si no has fet push**:

```bash
git commit --amend -m "Missatge correcte"
```

**Si ja l'has pujat**: deixa-ho estar (no compensa reescriure l'historial per un missatge).

## M'he oblidat d'afegir un fitxer a l'últim commit

**Si no has fet push**:

```bash
git add fitxer_oblidat
git commit --amend --no-edit
```

**Si ja l'has pujat**: un commit nou, `git commit -m "Afig fitxer oblidat"`.

## Vull tornar un fitxer a com estava fa uns commits

```bash
git log --oneline fitxer.sh                # quins commits l'han tocat
git restore --source=875bfc6 fitxer.sh     # recuperar-lo com estava en eixe commit
git commit -am "Recupera la versió anterior de fitxer.sh"
```

## `HEAD detached`

Has fet `git checkout ID_DE_COMMIT` (o `git switch --detach`) per a mirar una versió antiga. Estàs "fora" de qualsevol branca.

```bash
git switch main          # tornar a la branca
```

Si has fet canvis que vols conservar: `git switch -c nova-branca` abans d'eixir.

## La PR diu «This branch has conflicts that must be resolved»

`main` ha canviat mentre treballaves en la branca i toca les mateixes línies.

```bash
git switch la-meua-branca
git pull origin main           # porta els canvis de main a la teua branca
# resol els conflictes (edita, git add, git commit)
git push                       # la PR s'actualitza i ja es pot fusionar
```

## Vull veure com estava el projecte abans, sense perdre res

```bash
git log --oneline                # busca el commit
git switch --detach 875bfc6      # mira els fitxers com estaven
git switch main                  # torna al present
```
