# 7. Tuberies i objectes

Este és el tema que fa PowerShell diferent. Si l'entens, podràs fer en una línia coses que en Bash en necessiten moltes.

## Tot són objectes

Quan executes `Get-Service`, el que veus en pantalla **pareix** text, però en realitat són **objectes**: cada servei és una "fitxa" amb camps (propietats) com `Name`, `Status`, `DisplayName`...

```powershell
$s = Get-Service -Name Spooler
$s.Name           # Spooler
$s.Status         # Running
$s.DisplayName    # Print Spooler
```

### Quines propietats té un objecte?

```powershell
Get-Service | Get-Member -MemberType Property
```

`Get-Member` mostra totes les propietats (dades) i mètodes (accions) d'un objecte. Úsa'l sempre que no sàpies com es diu una propietat.

```powershell
Get-Service Spooler | Select-Object *       # mostra TOTES les propietats amb el seu valor
```

## La tuberia `|`

Igual que en Bash, `|` passa el resultat d'una ordre a la següent. La diferència és que passa **objectes**, no text. Per això la següent ordre pot accedir directament a les propietats.

Dins de la tuberia, l'objecte actual és **`$_`** (o `$PSItem`).

## Els cmdlets que més usaràs en tuberies

| Cmdlet | Fa | Equivalent en Bash |
| ------ | -- | ------------------ |
| `Where-Object` | **filtrar** (quedar-se amb els que complixen una condició) | `grep` |
| `Select-Object` | **triar** propietats, o els primers/últims | `cut`, `head`, `tail` |
| `Sort-Object` | **ordenar** | `sort` |
| `Measure-Object` | **comptar**, sumar, mitjana | `wc -l`, `awk` |
| `Group-Object` | **agrupar** i comptar | `sort \| uniq -c` |
| `ForEach-Object` | fer una cosa **amb cada un** | `while read` |
| `Format-Table` | mostrar en **taula** | `column` |
| `Export-Csv` | guardar en **CSV** | — |

### `Where-Object`: filtrar

```powershell
Get-Service | Where-Object Status -eq "Running"           # els serveis en marxa
Get-Process | Where-Object CPU -gt 100                    # processos que han usat més de 100 s de CPU
Get-ChildItem C:\Windows | Where-Object Length -gt 1MB    # fitxers de més d'1 MB
```

Per a condicions més complexes, la forma amb claus i `$_`:

```powershell
Get-Service | Where-Object { $_.Status -eq "Stopped" -and $_.StartType -eq "Automatic" }
```

Àlies: `?` o `where`.

### `Select-Object`: triar què vols veure

```powershell
Get-Process | Select-Object Name, Id, CPU              # només eixes propietats
Get-Process | Select-Object -First 5                   # els 5 primers
Get-Process | Select-Object -Last 3                    # els 3 últims
Get-ChildItem | Select-Object -ExpandProperty Name     # només els noms, com a text
```

Una propietat calculada (inventada per tu):

```powershell
Get-ChildItem | Select-Object Name, @{ Name = "MB"; Expression = { [math]::Round($_.Length / 1MB, 2) } }
```

### `Sort-Object`: ordenar

```powershell
Get-Process | Sort-Object CPU -Descending              # de major a menor CPU
Get-ChildItem | Sort-Object Length                     # per mida
Get-ChildItem | Sort-Object LastWriteTime -Descending  # els més recents primer
```

### Combinar-ho tot

```powershell
# Els 5 processos que més memòria usen
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 Name, WorkingSet

# Els 10 fitxers més grans d'una carpeta i subcarpetes
Get-ChildItem C:\Users -Recurse -File -ErrorAction SilentlyContinue |
    Sort-Object Length -Descending |
    Select-Object -First 10 FullName, Length
```

Es pot partir una tuberia en diverses línies si cada línia acaba en `|`.

### `Measure-Object`: comptar i sumar

```powershell
(Get-Process).Count                                     # quants processos hi ha
Get-ChildItem C:\Windows -File | Measure-Object Length -Sum   # mida total
```

### `Group-Object`: agrupar i comptar

```powershell
Get-Service | Group-Object Status
```

```console
Count Name     Group
----- ----     -----
  102 Stopped  {...}
   98 Running  {...}
```

## Mostrar el resultat

```powershell
Get-Process | Format-Table Name, Id, CPU -AutoSize    # taula ajustada
Get-Service Spooler | Format-List *                   # una propietat per línia
Get-Process | Out-GridView                            # finestra amb filtre (només Windows)
```

!!! warning "`Format-` sempre al final"
    `Format-Table` i `Format-List` converteixen els objectes en text per a mostrar-los. Després ja no es poden filtrar ni exportar. Posa'ls sempre **l'últim** de la tuberia.

## Guardar el resultat

```powershell
Get-Process | Out-File processos.txt                       # com a text
Get-Service | Export-Csv serveis.csv -NoTypeInformation    # com a CSV (s'obri en Excel)
Get-Service | ConvertTo-Html | Out-File serveis.html       # com a pàgina web
Get-Process | ConvertTo-Json | Out-File p.json             # com a JSON
```

I per a llegir-los després:

```powershell
$dades = Import-Csv serveis.csv
$dades | Where-Object Status -eq "Running"
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| No sé com es diu una propietat | — | `... \| Get-Member` |
| Després de `Format-Table` no puc exportar | `Format-` ho convertix en text | Posa `Format-*` al final |
| `Where-Object { Status -eq "Running" }` no filtra | Falta `$_.` dins de les claus | `{ $_.Status -eq "Running" }` |
| El CSV té una primera línia estranya `#TYPE` | Windows PowerShell 5.1 l'afig | `-NoTypeInformation` |

!!! success "Per a l'examen"
    ```powershell
    ... | Get-Member                                  # quines propietats té
    ... | Where-Object Prop -eq "valor"               # filtrar
    ... | Where-Object { $_.A -gt 5 -and $_.B -eq "x" }
    ... | Select-Object Prop1, Prop2                  # triar propietats
    ... | Select-Object -First 5                      # els primers
    ... | Sort-Object Prop -Descending                # ordenar
    ... | Measure-Object Prop -Sum -Average           # sumar / mitjana
    ... | Group-Object Prop                           # agrupar i comptar
    ... | Export-Csv f.csv -NoTypeInformation         # guardar CSV
    Import-Csv f.csv                                  # llegir CSV
    ```
    - `$_` = l'objecte actual dins de la tuberia
    - `Format-Table` sempre **l'últim**
