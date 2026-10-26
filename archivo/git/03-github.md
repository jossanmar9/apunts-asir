# 3. GitHub

## Clonar un repositori

Si el repositori ja existix en GitHub (el teu, o una plantilla del professor):

```bash
git clone git@github.com:usuari/repositori.git
cd repositori
```

Això crea una carpeta amb tots els fitxers **i tot l'historial**, ja connectada amb GitHub (el remot `origin`). No cal fer `git init`.

!!! tip "On trobe la URL?"
    En la pàgina del repositori en GitHub: botó verd **Code** → pestanya **SSH** → copiar.

## Pujar un repositori local que encara no està en GitHub

1. En GitHub: **New repository**. Posa-li nom i **no marques** *Add a README*, *.gitignore* ni *license*: ha d'estar **buit**.
2. En el teu equip, dins de la carpeta del projecte:

```bash
git init                                                   # si encara no és un repositori
git add .
git commit -m "Primer commit"
git branch -M main                                         # assegurar que la branca es diu main
git remote add origin git@github.com:usuari/repositori.git # connectar amb GitHub
git push -u origin main                                    # pujar
```

`-u` (*upstream*) recorda que la teua branca `main` va amb `origin/main`. Només cal la primera vegada: després n'hi ha prou amb `git push`.

## Els remots

```bash
git remote -v                                    # veure a on apunta
git remote add origin URL                        # afegir-ne un
git remote set-url origin git@github.com:u/r.git # canviar la URL (per exemple, de HTTPS a SSH)
git remote remove origin                         # llevar-lo
```

## `push` i `pull`

| Ordre | Fa |
| ----- | -- |
| `git push` | **puja** els teus commits a GitHub |
| `git pull` | **baixa** els commits de GitHub i els ajunta amb els teus |
| `git fetch` | baixa la informació de GitHub **però no toca** els teus fitxers (per a mirar abans) |

!!! tip "La regla d'or"
    **Fes `git pull` abans de començar a treballar** i `git push` en acabar. Així sempre treballes sobre l'última versió i eviteu conflictes.

### Push rebutjat: algú ha pujat coses abans que tu

Si en GitHub hi ha commits que tu no tens (els ha pujat un company, o tu des d'un altre ordinador, o has editat un fitxer des de la web de GitHub), el push falla:

```console
$ git push
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'github.com:usuari/repo.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally.
```

**Solució**: primer baixa el que falta, després puja:

```bash
git pull
git push
```

!!! danger "No uses `git push --force` per a «arreglar-ho»"
    `--force` **sobreescriu** el que hi ha en GitHub amb el teu: esborra els commits dels altres. Només té sentit en casos molt concrets i en branques teues.

### `pull`: «You have divergent branches»

Si tant tu com GitHub teniu commits nous, les versions recents de Git et demanen com vols ajuntar-los:

```console
hint: You have divergent branches and need to specify how to reconcile them.
fatal: Need to specify how to reconcile divergent branches.
```

Configura-ho una vegada (la forma més senzilla, fusionant):

```bash
git config --global pull.rebase false
git pull
```

Git farà un **commit de fusió** (*merge*) que ajunta les dues línies:

```console
*   8d991c9 Merge branch 'main' of github.com:usuari/repo
|\
| * ce732d3 Canvi de Pep
* | 2eedc43 Canvi d'Ana
|/
* 155969d Primer commit
```

Si tots dos heu canviat **la mateixa línia del mateix fitxer**, hi haurà un **conflicte**: mira el [tema 4](04-branques.md#conflictes).

## Coses útils de GitHub

| Funció | Per a què |
| ------ | --------- |
| **README.md** | la pàgina de presentació del repositori (es mostra en la portada) |
| **Issues** | llista de tasques, errors o dubtes del projecte |
| **Pull Requests** | proposar canvis i revisar-los abans d'ajuntar-los ([tema 5](05-pull-requests.md)) |
| **Settings → Collaborators** | donar accés a altres persones (per exemple, al professor) |
| **Actions** | executar coses automàticament en cada push (per exemple, publicar una web) |
| **Pages** | publicar una web estàtica gratis des d'un repositori |
| **Releases** | publicar versions (v1.0, v2.0) |
| Repositori **privat** | només el veus tu i qui convides |
| **Plantilla** (*template*) | un repositori a partir del qual altres en creen el seu (com les plantilles d'entregues) |

### Markdown: el format dels README

```markdown
# Títol
## Subtítol

Text normal, **negreta**, *cursiva* i `codi`.

- Element d'una llista
- Un altre

1. Llista numerada
2. Segon

[Text de l'enllaç](https://exemple.com)
![Imatge](captura.png)

    ```bash
    echo "bloc de codi"
    ```
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `! [rejected] ... (fetch first)` | En GitHub hi ha commits que tu no tens | `git pull` i després `git push` |
| `Need to specify how to reconcile divergent branches` | No has configurat com fer el pull | `git config --global pull.rebase false` |
| `error: remote origin already exists` | Ja havies afegit el remot | `git remote set-url origin URL` |
| `fatal: The current branch X has no upstream branch` | Primera vegada que puges eixa branca | `git push -u origin X` |
| `src refspec main does not match any` | No has fet cap commit encara, o la branca es diu `master` | Fes un commit; `git branch -M main` |
| `repository not found` | URL mal escrita, o no tens accés al repositori privat | Revisa la URL; que t'hagen convidat |
| Et demana contrasenya | Remot HTTPS | Token, o canvia a SSH |

!!! success "Per a l'examen"
    ```bash
    git clone git@github.com:u/r.git           # descarregar un repositori
    git remote add origin URL                  # connectar un repo local amb GitHub
    git push -u origin main                    # primera pujada
    git push / git pull                        # pujar / baixar
    git remote -v / set-url origin URL         # veure / canviar el remot
    ```
    - **`git pull` abans de treballar, `git push` en acabar**
    - Push rebutjat → `git pull` i torna a fer push (**mai** `--force` en `main`)
    - Repositori nou en GitHub per a pujar-hi un local: **buit**, sense README
