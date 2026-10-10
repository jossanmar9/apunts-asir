# 1. Primers passos

## Obrir PowerShell

En Windows: menú Inici → escriu **PowerShell** → *Windows PowerShell*. Per a tasques d'administració, clic dret → **Executar com a administrador**.

Veuràs una cosa així:

```console
PS C:\Users\ana>
```

`PS` vol dir que estàs en PowerShell, i després ve la carpeta on estàs.

!!! note "Windows PowerShell 5.1 i PowerShell 7"
    Windows porta instal·lat **Windows PowerShell 5.1** (finestra blava). Hi ha una versió més nova, **PowerShell 7** (`pwsh`), que també funciona en Linux. Per al que s'explica ací, totes dues funcionen igual.

## Cmdlets: les ordres de PowerShell

Les ordres de PowerShell es diuen **cmdlets** (es pronuncia *command-lets*). Tots tenen la mateixa forma: **Verb-Nom**, en anglés:

| Cmdlet | Verb | Nom | Què fa |
| ------ | ---- | --- | ------ |
| `Get-Process` | Get (obtindre) | Process | mostra els processos |
| `Get-Service` | Get | Service | mostra els serveis |
| `Stop-Service` | Stop (parar) | Service | para un servei |
| `New-Item` | New (crear) | Item | crea un fitxer o carpeta |
| `Remove-Item` | Remove (esborrar) | Item | esborra |
| `Set-Location` | Set (establir) | Location | canvia de carpeta |

Saber els verbs més comuns t'ajuda a endevinar ordres: `Get-` (veure), `Set-` (canviar), `New-` (crear), `Remove-` (esborrar), `Start-` / `Stop-` (arrancar / parar).

!!! tip "Majúscules"
    PowerShell **no** distingix majúscules: `get-process`, `Get-Process` i `GET-PROCESS` són el mateix. Però el costum és escriure-ho com `Get-Process`.

### Paràmetres

Els cmdlets accepten paràmetres que comencen per `-`:

```powershell
Get-ChildItem -Path C:\Windows -Filter *.log
Get-Service -Name wuauserv
Get-Process -Name notepad
```

## Àlies: noms curts i coneguts

Per a facilitar-ho, molts cmdlets tenen **àlies** (noms alternatius), alguns iguals que en Linux o en CMD:

| Àlies | Cmdlet real | Fa |
| ----- | ----------- | -- |
| `ls`, `dir` | `Get-ChildItem` | llistar fitxers |
| `cd` | `Set-Location` | canviar de carpeta |
| `cat`, `type` | `Get-Content` | mostrar un fitxer |
| `cp`, `copy` | `Copy-Item` | copiar |
| `mv`, `move` | `Move-Item` | moure |
| `rm`, `del` | `Remove-Item` | esborrar |
| `cls`, `clear` | `Clear-Host` | netejar la pantalla |
| `ps` | `Get-Process` | processos |

En scripts és millor escriure el nom complet: s'entén millor.

## Obtindre ajuda

No cal saber-se tots els cmdlets. PowerShell té ajuda inclosa:

```powershell
Get-Help Get-Process              # ajuda d'un cmdlet
Get-Help Get-Process -Examples    # ⭐ només exemples (el més útil)
Get-Help Get-Process -Online      # obri l'ajuda en el navegador
Update-Help                       # descarrega l'ajuda completa (com a administrador)
```

Buscar cmdlets que no saps com es diuen:

```powershell
Get-Command *service*             # tots els que tenen "service" en el nom
Get-Command -Verb Get             # tots els que comencen per Get-
Get-Command -Noun Item            # tots els que acaben en -Item
```

Veure les propietats d'un objecte (vegeu el [tema 7](07-tuberies.md)):

```powershell
Get-Process | Get-Member          # quines propietats i mètodes té un procés
```

## El primer script

Un script de PowerShell és un fitxer de text amb extensió **`.ps1`**.

### 1. Crear-lo

Amb el Bloc de notes, **Visual Studio Code** (amb l'extensió *PowerShell*) o el **PowerShell ISE** (ve amb Windows: busca *PowerShell ISE* en el menú Inici).

```powershell title="hola.ps1"
# El meu primer script
$nom = Read-Host "Com et dius?"
Write-Host "Hola, $nom!"
Write-Host "Hui és $(Get-Date -Format 'dd/MM/yyyy')"
```

### 2. Permetre l'execució de scripts

Per seguretat, **Windows no deixa executar scripts per defecte**. Si ho intentes, ix l'error:

```console
hola.ps1 cannot be loaded because running scripts is disabled on this system.
```

Cal canviar la **política d'execució** una vegada (PowerShell com a administrador):

```powershell
Get-ExecutionPolicy                                   # veure la política actual
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser   # permetre els scripts locals
```

| Política | Significa |
| -------- | --------- |
| `Restricted` | no s'executa cap script (per defecte en Windows 10/11) |
| `RemoteSigned` | els scripts teus sí; els descarregats d'Internet han d'estar signats ⭐ |
| `Unrestricted` | tots (amb avís per als d'Internet) |
| `Bypass` | tots, sense avisos |

### 3. Executar-lo

```powershell
cd C:\Users\ana\scripts
.\hola.ps1
```

Igual que en Linux, cal posar **`.\`** davant per a executar un script de la carpeta actual.

!!! tip "PowerShell ISE"
    En el ISE pots escriure l'script en la part de dalt i prémer ++f5++ per a executar-lo tot, o seleccionar unes línies i prémer ++f8++ per a executar només eixes.

## Redireccions bàsiques

Igual que en Bash:

```powershell
Get-Process > processos.txt        # guarda en un fitxer (esborra el que hi havia)
Get-Date >> registre.txt           # afig al final
Get-ChildItem C:\noexistix 2> errors.txt    # guarda els errors
Get-ChildItem C:\noexistix 2> $null         # amaga els errors ($null és la "paperera")
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `running scripts is disabled on this system` | La política d'execució ho impedix | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `The term 'hola.ps1' is not recognized` | Falta `.\` davant | `.\hola.ps1` |
| `Access is denied` en una ordre d'administració | No has obert PowerShell com a administrador | Clic dret → Executar com a administrador |
| No recordes com es fa una cosa | — | `Get-Help cmdlet -Examples` |

!!! success "Per a l'examen"
    - Cmdlets: **Verb-Nom** (`Get-Service`, `Stop-Process`, `New-Item`)
    - No distingix majúscules
    - Ajuda: `Get-Help cmdlet -Examples` · buscar: `Get-Command *paraula*`
    - Propietats d'un objecte: `... | Get-Member`
    - Scripts: extensió `.ps1`, executar amb `.\script.ps1`
    - Permetre scripts: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
    - Comentaris amb `#`
