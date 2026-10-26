# 10. PowerShell per a sysadmin

Els cmdlets més útils per a administrar Windows. La majoria necessiten obrir PowerShell **com a administrador**.

## Serveis

```powershell
Get-Service                                        # tots
Get-Service -Name Spooler                          # un en concret
Get-Service | Where-Object Status -eq "Running"    # els que estan en marxa
Start-Service -Name Spooler                        # arrancar
Stop-Service -Name Spooler                         # parar
Restart-Service -Name Spooler                      # reiniciar
Set-Service -Name Spooler -StartupType Automatic   # que arranque amb Windows
```

`StartupType` pot ser `Automatic`, `Manual` o `Disabled`.

## Processos

```powershell
Get-Process                                         # tots
Get-Process -Name notepad                           # per nom
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5   # els que més CPU usen
Stop-Process -Name notepad                          # tancar per nom
Stop-Process -Id 1234                               # tancar per PID
Start-Process notepad                               # obrir un programa
```

## Informació del sistema

```powershell
Get-ComputerInfo | Select-Object CsName, OsName, OsVersion, CsTotalPhysicalMemory
Get-CimInstance Win32_OperatingSystem | Select-Object Caption, LastBootUpTime
Get-CimInstance Win32_LogicalDisk -Filter "DriveType=3" |
    Select-Object DeviceID,
        @{ Name = "Total GB"; Expression = { [math]::Round($_.Size / 1GB, 1) } },
        @{ Name = "Lliure GB"; Expression = { [math]::Round($_.FreeSpace / 1GB, 1) } }
Get-Volume                                          # els volums (discos)
```

## Xarxa

```powershell
Get-NetIPAddress -AddressFamily IPv4               # les IPs (com ipconfig)
Get-NetAdapter                                     # targetes de xarxa
Test-Connection 8.8.8.8 -Count 2                   # ping
Test-NetConnection servidor01 -Port 3389           # està obert el port 3389?
Resolve-DnsName google.com                         # consulta DNS (com nslookup)
```

## Usuaris i grups locals

```powershell
Get-LocalUser                                       # usuaris de l'equip
Get-LocalGroup                                      # grups

$clau = Read-Host "Contrasenya" -AsSecureString
New-LocalUser -Name "pep" -Password $clau -FullName "Pep Roig"
Add-LocalGroupMember -Group "Administradors" -Member "pep"   # en Windows en anglés: "Administrators"
Disable-LocalUser -Name "pep"                       # deshabilitar
Remove-LocalUser -Name "pep"                        # esborrar
```

## Registres d'esdeveniments (Event Viewer)

```powershell
Get-WinEvent -LogName System -MaxEvents 20                       # els 20 últims del sistema
Get-WinEvent -FilterHashtable @{ LogName = "System"; Level = 2 } -MaxEvents 10   # només errors
Get-WinEvent -FilterHashtable @{ LogName = "Security"; Id = 4625 } -MaxEvents 10  # inicis de sessió fallits
```

| Level | Significa |
| ----- | --------- |
| 1 | Crític |
| 2 | Error |
| 3 | Avís |
| 4 | Informació |

## Tasques programades

```powershell
$accio  = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File C:\scripts\backup.ps1"
$quan   = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -TaskName "Backup diari" -Action $accio -Trigger $quan -User "SYSTEM"

Get-ScheduledTask -TaskName "Backup*"
```

És l'equivalent del `cron` de Linux.

## Administració remota

```powershell
Enable-PSRemoting -Force                            # activar-la en l'equip remot (una vegada)
Enter-PSSession -ComputerName servidor01            # entrar (com ssh)
Invoke-Command -ComputerName srv01, srv02 -ScriptBlock { Get-Service Spooler }   # executar en diversos
```

## Directori Actiu

Cal el mòdul **ActiveDirectory** (ve amb les eines RSAT o en un controlador de domini).

```powershell
Import-Module ActiveDirectory
```

### Usuaris

```powershell
Get-ADUser -Identity pgarcia                                # un usuari
Get-ADUser -Identity pgarcia -Properties *                  # amb totes les propietats
Get-ADUser -Filter *                                        # tots
Get-ADUser -Filter "Enabled -eq 'False'"                    # els deshabilitats
Get-ADUser -Filter * -SearchBase "OU=Alumnes,DC=institut,DC=local"   # els d'una OU

New-ADUser -Name "Pep Garcia" `
    -GivenName "Pep" -Surname "Garcia" `
    -SamAccountName "pgarcia" `
    -UserPrincipalName "pgarcia@institut.local" `
    -Path "OU=Alumnes,DC=institut,DC=local" `
    -AccountPassword (Read-Host "Contrasenya" -AsSecureString) `
    -ChangePasswordAtLogon $true `
    -Enabled $true

Set-ADUser -Identity pgarcia -Department "ASIR"               # modificar
Disable-ADAccount -Identity pgarcia                           # deshabilitar
Unlock-ADAccount -Identity pgarcia                            # desbloquejar
Set-ADAccountPassword -Identity pgarcia -Reset -NewPassword (Read-Host -AsSecureString)
Remove-ADUser -Identity pgarcia                               # esborrar
```

El caràcter `` ` `` al final de línia permet continuar l'ordre en la línia següent.

### Grups i unitats organitzatives

```powershell
New-ADGroup -Name "ASIR2" -GroupScope Global -Path "OU=Grups,DC=institut,DC=local"
Add-ADGroupMember -Identity "ASIR2" -Members pgarcia, aperez
Get-ADGroupMember -Identity "ASIR2"
Remove-ADGroupMember -Identity "ASIR2" -Members pgarcia

New-ADOrganizationalUnit -Name "Alumnes" -Path "DC=institut,DC=local"
Get-ADOrganizationalUnit -Filter *
```

### Alta massiva des d'un CSV

```powershell title="alta-ad.ps1"
# alumnes.csv:  Nom,Cognom,Usuari,Grup
Import-Module ActiveDirectory

$domini = "DC=institut,DC=local"
$clauInicial = ConvertTo-SecureString "Canvia-la.2026" -AsPlainText -Force

foreach ($a in Import-Csv alumnes.csv) {
    # Crear l'usuari dins de l'OU Alumnes
    New-ADUser -Name "$($a.Nom) $($a.Cognom)" `
        -GivenName $a.Nom -Surname $a.Cognom `
        -SamAccountName $a.Usuari `
        -UserPrincipalName "$($a.Usuari)@institut.local" `
        -Path "OU=Alumnes,$domini" `
        -AccountPassword $clauInicial `
        -ChangePasswordAtLogon $true `
        -Enabled $true

    # Afegir-lo al seu grup
    Add-ADGroupMember -Identity $a.Grup -Members $a.Usuari
    Write-Host "Creat $($a.Usuari) en el grup $($a.Grup)"
}
```

!!! success "Per a l'examen"
    | Vull... | Cmdlet |
    | ------- | ------ |
    | serveis | `Get-Service`, `Start-/Stop-/Restart-Service`, `Set-Service -StartupType` |
    | processos | `Get-Process`, `Stop-Process -Name / -Id` |
    | discos | `Get-CimInstance Win32_LogicalDisk`, `Get-Volume` |
    | xarxa | `Get-NetIPAddress`, `Test-Connection`, `Test-NetConnection -Port` |
    | usuaris locals | `Get-/New-/Remove-LocalUser`, `Add-LocalGroupMember` |
    | events | `Get-WinEvent -LogName System -MaxEvents 20` |
    | remot | `Enter-PSSession`, `Invoke-Command` |
    | AD usuaris | `Get-/New-/Set-/Remove-ADUser`, `Disable-ADAccount` |
    | AD grups | `New-ADGroup`, `Add-ADGroupMember`, `Get-ADGroupMember` |
    | AD OU | `New-ADOrganizationalUnit` |
