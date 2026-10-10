# Xuleta de PowerShell

## Equivalències amb Bash

| Bash | PowerShell |
| ---- | ---------- |
| `ls` | `Get-ChildItem` (`gci`, `ls`) |
| `cd` | `Set-Location` (`cd`) |
| `cat` | `Get-Content` (`gc`) |
| `grep` | `Select-String` (`sls`) |
| `ps` | `Get-Process` (`gps`) |
| `kill` | `Stop-Process` |
| `man` | `Get-Help` |
| `echo` | `Write-Output` |

## Bàsics

```powershell
Get-Command *service*                  # busca cmdlets
Get-Help Get-Service -Examples         # exemples d'ús
Get-Service | Where-Object Status -eq Running
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
$PSVersionTable                        # versió de PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Usuaris locals

```powershell
New-LocalUser -Name "pep" -Password (Read-Host -AsSecureString)
Add-LocalGroupMember -Group "Administradors" -Member "pep"
Get-LocalUser
```

## Directori Actiu

```powershell
Import-Module ActiveDirectory
Get-ADUser -Filter * -SearchBase "OU=Alumnes,DC=empresa,DC=local"
New-ADUser -Name "Pep Garcia" -SamAccountName pgarcia -Enabled $true `
  -AccountPassword (Read-Host -AsSecureString)
Get-ADGroupMember "Grup"
```
