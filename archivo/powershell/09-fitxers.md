# 9. Fitxers i errors

## Fitxers i carpetes

En PowerShell, fitxers i carpetes són **items**. Els cmdlets acaben en `-Item`:

| Vull... | Cmdlet | Àlies |
| ------- | ------ | ----- |
| llistar | `Get-ChildItem` | `ls`, `dir` |
| crear | `New-Item` | `ni` |
| copiar | `Copy-Item` | `cp`, `copy` |
| moure / reanomenar | `Move-Item` / `Rename-Item` | `mv` / `ren` |
| esborrar | `Remove-Item` | `rm`, `del` |
| comprovar si existix | `Test-Path` | — |

```powershell
New-Item -Path C:\proves -ItemType Directory              # crear carpeta
New-Item -Path C:\proves\notes.txt -ItemType File         # crear fitxer buit
Copy-Item C:\proves\notes.txt C:\proves\copia.txt         # copiar
Copy-Item C:\proves C:\backup -Recurse                    # copiar carpeta sencera
Move-Item C:\proves\copia.txt C:\temp\                    # moure
Rename-Item C:\proves\notes.txt apunts.txt                # reanomenar
Remove-Item C:\proves\apunts.txt                          # esborrar fitxer
Remove-Item C:\proves -Recurse                            # ⚠️ esborrar carpeta amb tot
Test-Path C:\proves                                       # True o False
```

!!! tip "`-WhatIf`: provar sense fer-ho"
    Molts cmdlets que canvien coses accepten `-WhatIf`, que mostra **què faria** sense fer-ho:
    ```powershell
    Remove-Item C:\temp\* -Recurse -WhatIf
    ```

### Llistar i buscar

```powershell
Get-ChildItem C:\Windows                        # el contingut
Get-ChildItem C:\Windows -File                  # només fitxers
Get-ChildItem C:\Windows -Directory             # només carpetes
Get-ChildItem C:\Users -Recurse -Filter *.pdf   # tots els .pdf, també en subcarpetes
Get-ChildItem C:\temp | Where-Object LastWriteTime -lt (Get-Date).AddDays(-30)   # de fa més de 30 dies
```

Propietats útils de cada fitxer: `Name`, `FullName` (ruta completa), `Length` (mida en bytes), `Extension`, `LastWriteTime`, `CreationTime`.

## Llegir fitxers

```powershell
Get-Content C:\proves\notes.txt              # tot el fitxer (una línia per element)
Get-Content C:\proves\notes.txt -TotalCount 5   # les 5 primeres línies (com head)
Get-Content C:\proves\notes.txt -Tail 5         # les 5 últimes (com tail)
Get-Content C:\logs\app.log -Wait               # va mostrant les noves (com tail -f)
```

Recórrer línia a línia:

```powershell
foreach ($linia in Get-Content C:\proves\noms.txt) {
    Write-Host "Nom: $linia"
}
```

### Buscar text dins de fitxers: `Select-String`

És l'equivalent de `grep`:

```powershell
Select-String -Path C:\logs\*.log -Pattern "ERROR"             # línies amb ERROR
Select-String -Path app.log -Pattern "error" -CaseSensitive    # distingint majúscules
(Select-String -Path app.log -Pattern "ERROR").Count           # quantes
```

## Escriure fitxers

| Cmdlet | Fa |
| ------ | -- |
| `Set-Content` | escriu (⚠️ **esborra** el que hi havia) |
| `Add-Content` | **afig** al final |
| `Out-File` | guarda l'eixida d'una ordre |

```powershell
Set-Content -Path notes.txt -Value "Primera línia"
Add-Content -Path notes.txt -Value "Segona línia"
Get-Process | Out-File processos.txt
"$(Get-Date) - Còpia feta" | Add-Content registre.log
```

## Fitxers CSV

```powershell
# usuaris.csv:
# Nom,Grup
# ana,ASIR
# pep,SMX

$usuaris = Import-Csv usuaris.csv
foreach ($u in $usuaris) {
    Write-Host "$($u.Nom) és de $($u.Grup)"     # cada columna és una propietat
}

$usuaris | Export-Csv copia.csv -NoTypeInformation
```

Si el separador és `;`: `Import-Csv usuaris.csv -Delimiter ";"`.

## Controlar errors

Quan un cmdlet falla, PowerShell mostra un error en roig, però **normalment continua** amb la línia següent.

### `-ErrorAction`: què fer si un cmdlet falla

```powershell
Get-Item C:\noexistix -ErrorAction SilentlyContinue    # no mostra l'error i continua
Get-Item C:\noexistix -ErrorAction Stop                # para (i es pot capturar amb try)
```

| Valor | Fa |
| ----- | -- |
| `Continue` | mostra l'error i continua (per defecte) |
| `SilentlyContinue` | no mostra res i continua |
| `Stop` | para: es converteix en un error que pot capturar `try` |

### `try` / `catch`

```powershell
try {
    $contingut = Get-Content C:\config.txt -ErrorAction Stop
    Write-Host "Llegit correctament"
}
catch {
    Write-Host "No s'ha pogut llegir: $($_.Exception.Message)" -ForegroundColor Red
}
finally {
    Write-Host "Açò s'executa sempre"
}
```

- El codi que pot fallar va en `try`.
- Si falla, s'executa `catch`. Dins, `$_` és l'error.
- `finally` és opcional i s'executa sempre.

!!! danger "Cal `-ErrorAction Stop` perquè funcione el `try`"
    Molts errors de cmdlets **no** salten al `catch` si no poses `-ErrorAction Stop`. És l'error més típic amb `try`/`catch` en PowerShell.

### Validar el que escriu l'usuari

```powershell
do {
    $text = Read-Host "Edat"
    $edat = $text -as [int]                 # si no és un número, torna $null
    if ($null -eq $edat) { Write-Host "Això no és un número" }
} while ($null -eq $edat)
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| He perdut el contingut d'un fitxer | `Set-Content` esborra | `Add-Content` per a afegir |
| El `catch` no s'executa mai | Falta `-ErrorAction Stop` | Afig-lo al cmdlet de dins del `try` |
| `Remove-Item` pregunta confirmació | La carpeta té contingut | `-Recurse` (i compte!) |
| Ruta amb espais no funciona | Sense cometes | `"C:\Program Files\..."` |

!!! success "Per a l'examen"
    ```powershell
    Test-Path ruta                                   # existix?
    New-Item ruta -ItemType Directory / File         # crear
    Copy-Item  Move-Item  Rename-Item  Remove-Item   # copiar, moure, reanomenar, esborrar
    Get-ChildItem ruta -Recurse -Filter *.txt        # buscar
    Get-Content f                                    # llegir
    Set-Content f "x"  /  Add-Content f "x"          # escriure / afegir
    Select-String -Path f -Pattern "x"               # buscar text (grep)
    Import-Csv f.csv  /  Export-Csv f.csv -NoTypeInformation

    try {
        ... -ErrorAction Stop
    } catch {
        $_.Exception.Message
    }
    ```
    - `-WhatIf` per a provar sense fer-ho
