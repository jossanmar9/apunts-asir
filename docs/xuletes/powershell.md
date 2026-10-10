# Xuleta de PowerShell

> Consulta ràpida. La teoria completa està en la [secció de PowerShell](../powershell/index.md).

## Bàsics

```powershell
Get-Help Get-Process -Examples       # ajuda amb exemples
Get-Command *service*                # buscar cmdlets
Get-Process | Get-Member             # propietats d'un objecte
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser   # permetre scripts
.\script.ps1                         # executar un script
```

## Variables i text

```powershell
$nom = "Ana"                         # sempre amb $
[int]$n = Read-Host "Número"         # demanar (Read-Host torna text)
Write-Host "Hola $nom"               # mostrar
Write-Host "Mida: $($f.Length)"      # propietat o càlcul dins del text
"Línia 1`nLínia 2"                   # salt de línia amb `n
"{0} té {1:N2} €" -f $nom, 3.5       # format
$env:USERNAME  $HOME  $true  $false  $null
```

## Operadors

| Tipus | Operadors |
| ----- | --------- |
| Aritmètics | `+ - * / %` · `[math]::Round(x, 2)` |
| Comparació | `-eq -ne -gt -ge -lt -le` |
| Text | `-like "*.txt"` · `-match "^\d+$"` |
| Llistes | `-contains` · `-in` |
| Lògics | `-and -or -not` |
| Text | `-split ":"` · `-join ","` · `-replace "a","b"` |

## Condicionals

```powershell
if ($a -gt 5) { ... } elseif ($a -eq 5) { ... } else { ... }

switch ($opcio) {
    1       { ... }
    "text"  { ... }
    default { ... }
}
```

## Bucles

```powershell
foreach ($x in $llista) { ... }
$llista | ForEach-Object { $_ }
for ($i = 1; $i -le 10; $i++) { ... }
foreach ($i in 1..10) { ... }
while ($cond) { ... }
do { ... } while ($cond)
do { ... } until ($cond)
break / continue
```

## Arrays i taules hash

```powershell
$a = "x", "y", "z"      $a[0]  $a[-1]  $a.Count  $a += "w"
$h = @{ ssh = 22; http = 80 }
$h["ssh"]  $h.ssh  $h["dns"] = 53  $h.Remove("http")  $h.Keys  $h.ContainsKey("x")
[PSCustomObject]@{ Nom = "Ana"; Edat = 30 }
```

## Tuberies

```powershell
... | Where-Object Status -eq "Running"
... | Where-Object { $_.CPU -gt 10 -and $_.Name -like "s*" }
... | Select-Object Name, Id -First 5
... | Sort-Object CPU -Descending
... | Measure-Object Length -Sum -Average
... | Group-Object Status
... | Format-Table -AutoSize          # sempre l'últim
... | Export-Csv f.csv -NoTypeInformation
Import-Csv f.csv
```

## Funcions i scripts

```powershell
function Verb-Nom {
    param(
        [Parameter(Mandatory)][string]$A,
        [int]$B = 10,
        [switch]$C
    )
    return $resultat
}
Verb-Nom -A "x" -B 5 -C               # SENSE parèntesis ni comes
```

## Fitxers

```powershell
Test-Path ruta
New-Item ruta -ItemType Directory     # o File
Copy-Item a b [-Recurse]   Move-Item a b   Rename-Item a nou   Remove-Item a [-Recurse]
Get-ChildItem ruta -Recurse -File -Filter *.log
Get-Content f [-Tail 10] [-Wait]
Set-Content f "x"   Add-Content f "x"
Select-String -Path *.log -Pattern "ERROR"     # com grep
... -WhatIf                                    # provar sense fer-ho
```

## Errors

```powershell
try {
    Get-Content f -ErrorAction Stop
} catch {
    Write-Host $_.Exception.Message
}
-ErrorAction SilentlyContinue                  # amagar l'error
```

## Equivalències amb Bash

| Bash | PowerShell |
| ---- | ---------- |
| `ls` | `Get-ChildItem` (`ls`, `dir`) |
| `cd` | `Set-Location` (`cd`) |
| `cat` | `Get-Content` (`cat`) |
| `grep` | `Select-String` |
| `ps` | `Get-Process` (`ps`) |
| `kill` | `Stop-Process` |
| `cp` / `mv` / `rm` | `Copy-Item` / `Move-Item` / `Remove-Item` |
| `echo` | `Write-Host` / `Write-Output` |
| `read` | `Read-Host` |
| `man` | `Get-Help` |
| `wc -l` | `Measure-Object` · `.Count` |
| `sort` / `head` | `Sort-Object` / `Select-Object -First` |

## Sysadmin

```powershell
Get-Service  Start-Service  Stop-Service  Restart-Service  Set-Service -StartupType Automatic
Get-Process  Stop-Process -Name x / -Id 1234
Get-CimInstance Win32_LogicalDisk          # discos
Get-NetIPAddress  Test-Connection host  Test-NetConnection host -Port 443
Get-LocalUser  New-LocalUser  Add-LocalGroupMember -Group G -Member U
Get-WinEvent -LogName System -MaxEvents 20
Enter-PSSession srv01   Invoke-Command -ComputerName srv01 -ScriptBlock { ... }
```

## Directori Actiu

```powershell
Import-Module ActiveDirectory
Get-ADUser -Filter * -SearchBase "OU=Alumnes,DC=institut,DC=local"
New-ADUser -Name "Pep Garcia" -SamAccountName pgarcia -Path "OU=..." `
    -AccountPassword (Read-Host -AsSecureString) -Enabled $true
Set-ADUser  Disable-ADAccount  Unlock-ADAccount  Remove-ADUser
New-ADGroup -Name G -GroupScope Global   Add-ADGroupMember -Identity G -Members u1, u2
New-ADOrganizationalUnit -Name Alumnes -Path "DC=institut,DC=local"
```
