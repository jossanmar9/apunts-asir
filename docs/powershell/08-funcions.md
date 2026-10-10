# 8. Funcions i paràmetres

## Funcions

Una **funció** és un tros de codi amb nom que pots cridar quantes vegades vulgues.

```powershell
function Saluda {
    Write-Host "Hola!"
}

Saluda          # cridar-la (sense parèntesis)
```

Per costum, el nom segueix la forma **Verb-Nom** com els cmdlets: `Get-Espai`, `New-Usuari`...

### Paràmetres

La forma recomanada és amb un bloc `param( )`:

```powershell
function Saluda {
    param($Nom)
    Write-Host "Hola, $Nom!"
}

Saluda -Nom "Ana"       # passant el paràmetre pel nom
Saluda "Ana"            # o per posició
```

Diversos paràmetres, amb tipus i valor per defecte:

```powershell
function Get-Area {
    param(
        [double]$Base,
        [double]$Altura = 1      # si no es passa, val 1
    )
    return $Base * $Altura
}

Get-Area -Base 3 -Altura 4      # 12
Get-Area 3 4                    # 12
```

!!! danger "No es criden amb parèntesis i comes"
    ```powershell
    Get-Area(3, 4)        # ❌ passa UN sol paràmetre: la llista (3, 4)
    Get-Area 3 4          # ✅
    Get-Area -Base 3 -Altura 4   # ✅
    ```
    És l'error més típic per a qui ve d'altres llenguatges.

### Paràmetres obligatoris

```powershell
function New-Carpeta {
    param(
        [Parameter(Mandatory)]
        [string]$Ruta
    )
    New-Item -Path $Ruta -ItemType Directory
}

New-Carpeta            # com que és obligatori, PowerShell el pregunta
```

### Paràmetres sí/no: `[switch]`

```powershell
function Neteja {
    param(
        [string]$Carpeta,
        [switch]$Simula          # si es posa -Simula, val $true
    )
    if ($Simula) {
        Write-Host "Només simulant en $Carpeta"
    } else {
        Write-Host "Esborrant en $Carpeta"
    }
}

Neteja -Carpeta C:\temp -Simula
```

## Tornar resultats

En PowerShell, **tot el que una funció "deixa anar"** (valors solts, `Write-Output`, resultats d'ordres) és el que torna:

```powershell
function Get-Doble {
    param([int]$N)
    $N * 2               # este valor es torna
}

$r = Get-Doble 5         # $r = 10
```

`return` també funciona, i a més **acaba** la funció:

```powershell
function Test-Parell {
    param([int]$N)
    return ($N % 2 -eq 0)     # torna True o False
}

if (Test-Parell 4) { "És parell" }
```

!!! warning "`Write-Host` no torna res"
    `Write-Host` només mostra per pantalla. Si una funció fa `Write-Host $resultat`, el valor **no** es pot guardar en una variable. Per a tornar valors, usa el valor directament, `Write-Output` o `return`.

!!! warning "Tot es torna"
    Si dins de la funció hi ha una ordre que mostra alguna cosa (per exemple `New-Item`), eixe resultat també es torna, barrejat amb el teu. Per a evitar-ho: `New-Item ... | Out-Null`.

## Variables dins de les funcions

Les variables creades dins d'una funció només existixen dins:

```powershell
function Prova { $x = 5 }
Prova
$x          # buit: fora no existix
```

## Scripts amb paràmetres

Un script `.ps1` també pot tindre un bloc `param( )`. Ha de ser **el primer** del fitxer:

```powershell title="crea-carpetes.ps1"
param(
    [Parameter(Mandatory)]
    [string]$Ruta,
    [int]$Quantes = 3
)

for ($i = 1; $i -le $Quantes; $i++) {
    New-Item -Path "$Ruta\carpeta$i" -ItemType Directory | Out-Null
    Write-Host "Creada carpeta$i"
}
```

```powershell
.\crea-carpetes.ps1 -Ruta C:\proves -Quantes 5
.\crea-carpetes.ps1 C:\proves          # Quantes val 3
```

### La forma senzilla: `$args`

Sense `param`, els arguments estan en `$args` (com `$1`, `$2` en Bash):

```powershell
Write-Host "Has passat $($args.Count) arguments"
Write-Host "El primer és $($args[0])"
```

`param( )` és millor: dona noms clars, tipus i comprovacions.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `Funcio(1, 2)` no fa el que esperes | Passa una llista com a un sol paràmetre | `Funcio 1 2` o `Funcio -A 1 -B 2` |
| `The term 'Funcio' is not recognized` | La crides abans de definir-la | Posa la funció al principi |
| La variable queda buida en fer `$r = Funcio` | La funció usa `Write-Host` | Torna el valor (sense `Write-Host`) |
| La funció torna coses de més | Alguna ordre de dins mostra resultats | `\| Out-Null` en eixa ordre |
| `param` dona error en un script | No està en la primera línia | Posa `param( )` al principi (només poden anar comentaris abans) |

!!! success "Per a l'examen"
    ```powershell
    function Verb-Nom {
        param(
            [Parameter(Mandatory)][string]$A,     # obligatori
            [int]$B = 10,                         # amb valor per defecte
            [switch]$C                            # sí/no
        )
        ...
        return $resultat
    }

    Verb-Nom -A "x" -B 5 -C       # cridar (SENSE parèntesis ni comes)
    $r = Verb-Nom "x"
    ```
    - Scripts: `param( )` a la **primera línia**
    - `Write-Host` no torna valors
