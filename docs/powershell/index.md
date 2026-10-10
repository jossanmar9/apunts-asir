# PowerShell

## Què és PowerShell?

**PowerShell** és el terminal i el llenguatge de scripts de Windows. És l'equivalent a Bash en Linux: serveix per a escriure ordres i automatitzar tasques (crear usuaris, gestionar serveis, revisar el disc...).

També existix per a Linux i Mac (PowerShell 7), però on més s'usa és per a administrar **Windows i Windows Server**: Directori Actiu, Exchange, Microsoft 365, Azure...

## La gran diferència amb Bash: objectes

En Bash, les ordres es passen **text** d'una a una altra i cal retallar-lo amb `cut`, `awk`...

En PowerShell, les ordres es passen **objectes**: dades amb propietats amb nom. Per exemple, `Get-Process` no torna línies de text, torna una llista de processos, i cada un té les propietats `Name`, `Id`, `CPU`...

```powershell
Get-Process | Where-Object CPU -gt 10 | Select-Object Name, CPU
```

Es llig quasi en anglés: *obtín els processos, on la CPU siga major que 10, i selecciona el nom i la CPU*. No cal retallar text.

## Ordre recomanat

| Tema | Què aprens |
| ---- | ---------- |
| [1. Primers passos](01-primers-passos.md) | obrir PowerShell, cmdlets, ajuda, primer script |
| [2. Variables i tipus](02-variables.md) | guardar dades, demanar-les i mostrar-les |
| [3. Operadors](03-operadors.md) | comptes, comparacions i operacions amb text |
| [4. Condicionals](04-condicionals.md) | `if` i `switch` |
| [5. Bucles](05-bucles.md) | `for`, `foreach`, `while`, `do` |
| [6. Arrays i taules hash](06-arrays.md) | guardar moltes dades |
| [7. Tuberies i objectes](07-tuberies.md) | filtrar, ordenar, exportar |
| [8. Funcions i paràmetres](08-funcions.md) | organitzar el codi, scripts amb arguments |
| [9. Fitxers i errors](09-fitxers.md) | llegir i escriure fitxers, `try`/`catch` |
| [10. PowerShell per a sysadmin](10-sysadmin.md) | serveis, processos, usuaris, Directori Actiu |

Després: [exercicis resolts](exercicis.md).

## Equivalències amb Bash

Si ja saps Bash, esta taula t'ajuda a ubicar-te:

| Què | Bash | PowerShell |
| --- | ---- | ---------- |
| Mostrar text | `echo "Hola"` | `Write-Host "Hola"` |
| Variable | `nom="Ana"` · `$nom` | `$nom = "Ana"` · `$nom` |
| Demanar dada | `read -p "Nom: " nom` | `$nom = Read-Host "Nom"` |
| Arguments | `$1`, `$#` | `$args[0]`, `$args.Count` (o `param()`) |
| Igual / major | `-eq`, `-gt` | `-eq`, `-gt` (els mateixos!) |
| Llistar fitxers | `ls` | `Get-ChildItem` (o `ls`, `dir`) |
| Llegir fitxer | `cat f` | `Get-Content f` |
| Buscar text | `grep` | `Select-String` / `Where-Object` |
| Processos | `ps` | `Get-Process` |
| Codi d'eixida | `$?` (número) | `$?` (True/False) · `$LASTEXITCODE` |
| Comentari | `#` | `#` |
| Extensió | `.sh` | `.ps1` |

!!! tip "Durant un examen"
    Cada tema acaba amb el requadre verd **«Per a l'examen»**. La [xuleta de PowerShell](../xuletes/powershell.md) ho resumix tot en una pàgina.
