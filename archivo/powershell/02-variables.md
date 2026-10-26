# 2. Variables i tipus

## Variables

Una **variable** guarda un valor amb un nom. En PowerShell **sempre** porten `$` davant, tant per a guardar com per a llegir (diferent de Bash):

```powershell
$nom = "Ana"          # guardar
$edat = 30
Write-Host $nom       # llegir → Ana
```

- Es poden posar espais al voltant de `=` (a diferència de Bash).
- No distingixen majúscules: `$nom` i `$NOM` són la mateixa variable.

### Variables que ja existixen

| Variable | Conté |
| -------- | ----- |
| `$HOME` | la teua carpeta personal |
| `$PWD` | la carpeta on estàs |
| `$env:USERNAME` | el teu usuari (variables d'entorn: `$env:NOM`) |
| `$env:COMPUTERNAME` | nom de l'ordinador |
| `$true` / `$false` | cert / fals |
| `$null` | res (buit) |
| `$PSVersionTable` | versió de PowerShell |

Veure totes les variables: `Get-Variable`.

## Mostrar informació

### `Write-Host`: mostrar per pantalla

```powershell
Write-Host "Hola, món"
Write-Host "Error greu" -ForegroundColor Red          # amb color
Write-Host "Sense salt de línia " -NoNewline
```

### `Write-Output`: tornar un resultat

```powershell
Write-Output "Hola"
"Hola"                    # el mateix: un valor solt es mostra sol
```

La diferència: `Write-Host` **només mostra** per pantalla. `Write-Output` **envia el valor** per la tuberia (es pot guardar o passar a una altra ordre). En funcions que tornen resultats, usa `Write-Output` (o simplement el valor).

## Text i variables: cometes

```powershell
$nom = "Pep"
Write-Host "Hola $nom"          # Hola Pep    → cometes DOBLES: substituïx la variable
Write-Host 'Hola $nom'          # Hola $nom   → cometes SIMPLES: tal qual
```

Igual que en Bash. Per a posar una **expressió** dins del text (una propietat, un càlcul, una ordre), cal `$( )`:

```powershell
$fitxer = Get-Item C:\Windows\notepad.exe
Write-Host "Mida: $fitxer.Length"        # ❌ mostra el fitxer i després ".Length"
Write-Host "Mida: $($fitxer.Length)"     # ✅ mostra la mida
Write-Host "El doble de 5 és $(5 * 2)"   # ✅ 10
```

El caràcter d'escapament és l'accent greu **`` ` ``** (en Bash era `\`):

| S'escriu | Significa |
| -------- | --------- |
| `` `n `` | salt de línia |
| `` `t `` | tabulador |
| `` `$ `` | un `$` literal |

```powershell
Write-Host "Línia 1`nLínia 2"
```

## Demanar dades: `Read-Host`

```powershell
$nom = Read-Host "Com et dius"
Write-Host "Hola, $nom"
```

PowerShell afig `: ` automàticament al final del missatge.

Per a contrasenyes (no es veu el que s'escriu):

```powershell
$clau = Read-Host "Contrasenya" -AsSecureString
```

!!! danger "`Read-Host` torna sempre TEXT"
    ```powershell
    $n = Read-Host "Número"      # escrius 5
    $n * 2                       # 55  ❌ repetix el text
    [int]$n * 2                  # 10  ✅
    ```

## Tipus de dades

| Tipus | Exemple | Per a |
| ----- | ------- | ----- |
| `[string]` | `"hola"` | text |
| `[int]` | `42` | enters |
| `[double]` | `3.14` | decimals |
| `[bool]` | `$true`, `$false` | cert / fals |
| `[datetime]` | `Get-Date` | dates |
| `[array]` | `1, 2, 3` | llistes |
| `[hashtable]` | `@{a=1}` | taules clau-valor |

Saber el tipus d'una variable:

```powershell
$x = 42
$x.GetType().Name       # Int32
```

### Fixar el tipus d'una variable

Si poses el tipus davant en crear la variable, PowerShell converteix el valor i **sempre** el mantindrà:

```powershell
[int]$edat = Read-Host "Edat"      # converteix el text a enter
$edat + 1                          # suma de veritat

[int]$x = 5
$x = "hola"                        # ❌ error: no es pot convertir "hola" a enter
```

### Convertir un valor

```powershell
[int]"42"           # 42
[double]"3,5"       # ⚠️ depén de la configuració regional: millor "3.5"
[string]42          # "42"
"42" -as [int]      # 42 (si no es pot, torna $null en compte de donar error)
```

!!! note "Decimals"
    En el codi, els decimals s'escriuen amb **punt**: `3.14`.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `nom = "Ana"` → `nom is not recognized` | Falta el `$` | `$nom = "Ana"` |
| `"5" * 2` dona `55` | Era text | `[int]` davant |
| `"Mida: $f.Length"` mostra coses estranyes | Les propietats no s'expandixen soles | `"Mida: $($f.Length)"` |
| `"Línia 1\nLínia 2"` no fa salt | L'escapament és `` ` `` | ``"Línia 1`nLínia 2"`` |

!!! success "Per a l'examen"
    ```powershell
    $var = valor                       # sempre amb $ (guardar i llegir)
    Write-Host "Hola $var"             # mostrar
    Write-Host "Mida: $($obj.Length)"  # propietat o càlcul dins del text
    $x = Read-Host "Missatge"          # demanar (torna TEXT)
    [int]$n = Read-Host "Número"       # demanar un número
    $x.GetType().Name                  # quin tipus és
    $env:USERNAME                      # variable d'entorn
    ```
    - Escapament: `` `n `` (salt de línia), no `\n`
