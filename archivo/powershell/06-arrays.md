# 6. Arrays i taules hash

## Arrays: llistes de valors

Un **array** guarda molts valors en una variable, cadascun en una posició numerada **des de 0**.

### Crear-lo

```powershell
$serveis = "Spooler", "WinRM", "wuauserv"     # separats per comes
$serveis = @("Spooler", "WinRM", "wuauserv")  # el mateix amb @( )
$buit = @()                                   # array buit
$numeros = 1..10                              # de l'1 al 10
```

### Llegir-lo

```powershell
$serveis[0]          # Spooler  → el primer
$serveis[1]          # WinRM
$serveis[-1]         # wuauserv → l'últim
$serveis[0..1]       # els dos primers
$serveis.Count       # 3        → quants n'hi ha
$serveis             # tots
```

### Afegir elements

```powershell
$serveis += "BITS"      # afig al final
```

!!! note "Esborrar d'un array"
    Els arrays normals no tenen una manera directa d'esborrar. Es crea un de nou filtrant:
    ```powershell
    $serveis = $serveis | Where-Object { $_ -ne "WinRM" }
    ```

### Recórrer-lo

```powershell
foreach ($s in $serveis) {
    Write-Host $s
}
```

### Comprovar si conté un valor

```powershell
$serveis -contains "WinRM"      # True
"WinRM" -in $serveis            # True
```

### Ordenar i calcular

```powershell
$notes = 7, 4, 9, 6
$notes | Sort-Object                    # 4 6 7 9
$notes | Sort-Object -Descending        # 9 7 6 4
($notes | Measure-Object -Sum -Average -Maximum -Minimum)
```

`Measure-Object` calcula la suma, la mitjana, el màxim i el mínim d'una vegada:

```powershell
$estad = $notes | Measure-Object -Sum -Average -Maximum
$estad.Sum          # 26
$estad.Average      # 6.5
$estad.Maximum      # 9
```

## Taules hash: clau → valor

Una **taula hash** (*hashtable*) guarda parelles **clau → valor**. Busques per **nom** en compte de per posició. És l'equivalent dels diccionaris de Python o dels arrays associatius de Bash.

### Crear-la

```powershell
$ports = @{
    ssh   = 22
    http  = 80
    https = 443
}
```

Amb `@{ }` i cada parella en una línia (o separades per `;` en una sola línia).

### Llegir-la

```powershell
$ports["ssh"]           # 22
$ports.ssh              # 22 (forma curta)
$ports.Keys             # les claus: ssh, http, https
$ports.Values           # els valors: 22, 80, 443
$ports.Count            # 3
$ports.ContainsKey("ftp")   # False → existix eixa clau?
```

### Afegir, canviar, esborrar

```powershell
$ports["dns"] = 53          # afig (o canvia si ja existia)
$ports.ftp = 21             # el mateix, forma curta
$ports.Remove("http")       # esborra
```

### Recórrer-la

```powershell
foreach ($servei in $ports.Keys) {
    Write-Host "$servei → $($ports[$servei])"
}
```

O amb `GetEnumerator()`, que dona cada parella amb `.Key` i `.Value`:

```powershell
$ports.GetEnumerator() | Sort-Object Value | ForEach-Object {
    Write-Host "$($_.Key) usa el port $($_.Value)"
}
```

### Exemple: comptar quantes vegades apareix cada cosa

```powershell
$fruites = "poma", "pera", "poma", "plàtan", "poma"
$compte = @{}

foreach ($f in $fruites) {
    if ($compte.ContainsKey($f)) {
        $compte[$f]++               # ja existia: suma 1
    } else {
        $compte[$f] = 1             # primera vegada
    }
}
$compte                             # poma 3, pera 1, plàtan 1
```

La manera ràpida, amb un cmdlet que ja ho fa:

```powershell
$fruites | Group-Object | Select-Object Name, Count
```

## Objectes personalitzats: `[PSCustomObject]`

Quan vols guardar diverses dades d'una mateixa cosa (com una fila d'una taula), crea un objecte:

```powershell
$usuari = [PSCustomObject]@{
    Nom   = "Ana"
    Grup  = "ASIR"
    Edat  = 30
}
$usuari.Nom         # Ana
```

Una llista d'objectes es mostra com una taula i es pot exportar a CSV ([tema 7](07-tuberies.md)):

```powershell
$llista = @(
    [PSCustomObject]@{ Nom = "Ana"; Nota = 8 }
    [PSCustomObject]@{ Nom = "Pep"; Nota = 6 }
)
$llista | Sort-Object Nota -Descending
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| Comptes des de 1 i et salta el primer | Les posicions comencen per 0 | El primer és `[0]` |
| `Index was outside the bounds of the array` | Posició que no existix | Va de 0 a `.Count - 1` |
| `$h = {a=1}` no és una taula hash | Falta l'`@` | `@{ a = 1 }` |
| `$ports.Remove()` en un array | Només funciona en taules hash | Filtra amb `Where-Object` |

!!! success "Per a l'examen"
    ```powershell
    $a = "x", "y", "z"          # array
    $a[0]  $a[-1]  $a.Count
    $a += "w"                   # afegir
    $a -contains "x"
    $a | Sort-Object
    $a | Measure-Object -Sum -Average

    $h = @{ clau = "valor"; altra = 2 }   # taula hash
    $h["clau"]   $h.clau
    $h["nova"] = 3              # afegir
    $h.Remove("clau")
    $h.Keys   $h.ContainsKey("x")
    foreach ($k in $h.Keys) { $h[$k] }

    [PSCustomObject]@{ Nom = "Ana"; Edat = 30 }   # objecte
    ```
