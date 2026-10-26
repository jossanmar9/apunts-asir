# 1. Primer script

## Pas 1: crear el fitxer

Un script és un fitxer de text normal. El pots crear amb qualsevol editor. En el terminal, el més senzill és `nano`:

```bash
nano hola.sh
```

Escriu dins açò:

```bash title="hola.sh"
#!/bin/bash
# Este script saluda l'usuari i mostra la data
echo "Hola, $USER!"
echo "Hui és $(date +%d/%m/%Y)"
```

Per a guardar en `nano`: ++ctrl+o++, ++enter++ i ++ctrl+x++ per a eixir.

**Què fa cada línia:**

| Línia | Què vol dir |
| ----- | ----------- |
| `#!/bin/bash` | Diu al sistema que este fitxer l'ha d'executar Bash. Va **sempre** en la primera línia. |
| `# Este script...` | Un **comentari**. Tot el que va després de `#` Bash ho ignora. Serveix per a explicar el codi a qui el llig. |
| `echo "Hola, $USER!"` | `echo` mostra text per pantalla. `$USER` es canvia pel nom del teu usuari. |
| `echo "Hui és $(date ...)"` | `$(...)` executa l'ordre de dins i posa el resultat en eixe lloc. Ací, la data. |

!!! note "L'extensió `.sh`"
    No és obligatòria, però és una convenció que ajuda a saber que el fitxer és un script de shell.

## Pas 2: donar-li permís d'execució

En Linux, un fitxer no es pot executar si no té el **permís d'execució** (`x`). Els fitxers nous no el tenen. Cal donar-li'l una vegada:

```bash
chmod +x hola.sh
```

- `chmod` canvia els permisos d'un fitxer.
- `+x` vol dir "afig el permís d'execució".

Pots comprovar-ho amb `ls -l hola.sh`: veuràs una `x` en els permisos (`-rwxr-xr-x`).

## Pas 3: executar-lo

```bash
./hola.sh
```

```console
Hola, ana!
Hui és 10/10/2026
```

!!! question "Per què cal posar `./` davant?"
    Quan escrius una ordre (per exemple `ls`), el sistema la busca en uns directoris concrets (`/bin`, `/usr/bin`...). El directori on estàs ara **no** està en eixa llista, per seguretat. El `./` vol dir "en el directori actual", així li dius exactament on està.

### Altres formes d'executar-lo

| Forma | Quan usar-la |
| ----- | ------------ |
| `./hola.sh` | La normal. Necessita el permís `x`. |
| `bash hola.sh` | Funciona encara que no tinga el permís `x`. Útil per a provar ràpid. |
| `source hola.sh` | Executa l'script dins del terminal actual. Els canvis (variables, `cd`) es queden després. S'usa poc. |

## El codi d'eixida: com sap Linux si una ordre ha anat bé

Quan qualsevol ordre acaba, deixa un número amagat anomenat **codi d'eixida**:

- **0** vol dir que **ha anat bé**.
- **Qualsevol altre número** (1, 2, 127...) vol dir que **ha fallat**.

Es pot veure amb `echo $?` just després de l'ordre:

```bash
ls /etc
echo $?        # 0 → ha anat bé

ls /carpeta_que_no_existix
echo $?        # 2 → ha fallat
```

Per què és important? Perquè els scripts usen este número per a decidir què fer (ho veuràs en el [tema 4](04-condicionals.md)).

El teu script també pot acabar amb un codi:

```bash
exit 0    # acaba l'script i diu "tot bé"
exit 1    # acaba l'script i diu "hi ha hagut un error"
```

## Errors típics

| Error | Per què passa | Solució |
| ----- | ------------- | ------- |
| `Permission denied` | No té permís d'execució | `chmod +x script.sh` |
| `command not found` en fer `hola.sh` | Falta el `./` davant | `./hola.sh` |
| `No such file or directory` | No estàs en la carpeta de l'script | Fes `ls` per a comprovar-ho, o `cd` a la carpeta |
| L'script fa coses estranyes amb `[[` | Falta `#!/bin/bash` i s'executa amb un altre shell | Posa el shebang en la primera línia |

!!! success "Per a l'examen"
    - Primera línia sempre: `#!/bin/bash`
    - Comentaris amb `#`
    - Donar permís: `chmod +x script.sh` → executar: `./script.sh`
    - Mostrar text: `echo "text"`
    - Resultat d'una ordre dins d'un text: `$(ordre)`
    - `$?` = codi de l'última ordre. **0 = bé**, altre = error
    - Acabar l'script: `exit 0` (bé) / `exit 1` (error)
