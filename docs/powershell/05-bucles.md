# 5. Bucles

Un **bucle** repetix unes ordres. PowerShell en té cinc:

| Bucle | Quan usar-lo |
| ----- | ------------ |
| `foreach` | per a **cada element** d'una llista ⭐ (el més usat) |
| `for` | per a **comptar** (de 1 a 10...) |
| `while` | **mentre** siga cert (pot no executar-se cap vegada) |
| `do { } while` | **mentre** siga cert, però s'executa **almenys una vegada** |
| `do { } until` | **fins que** siga cert, almenys una vegada |

## `foreach`: per a cada element

```powershell
$serveis = "Spooler", "wuauserv", "WinRM"

foreach ($servei in $serveis) {
    Write-Host "Comprovant $servei"
}
```

La variable `$servei` agafa cada valor de la llista, un per volta.

Recórrer el resultat d'una ordre:

```powershell
foreach ($fitxer in Get-ChildItem C:\Windows\*.log) {
    Write-Host "$($fitxer.Name) ocupa $($fitxer.Length) bytes"
}
```

### `ForEach-Object`: la versió per a tuberies

Fa el mateix, però rep els elements per una tuberia. Dins, l'element actual és **`$_`**:

```powershell
Get-ChildItem C:\Windows\*.log | ForEach-Object {
    Write-Host "$($_.Name) ocupa $($_.Length) bytes"
}

1..5 | ForEach-Object { $_ * 2 }        # 2 4 6 8 10
```

`1..5` crea la llista 1, 2, 3, 4, 5.

## `for`: per a comptar

```powershell
for ($i = 1; $i -le 10; $i++) {
    Write-Host "7 x $i = $(7 * $i)"
}
```

Tres parts entre parèntesis, separades per `;`:

1. `$i = 1` → valor inicial
2. `$i -le 10` → es repetix mentre siga cert
3. `$i++` → què es fa al final de cada volta (sumar 1)

Moltes vegades és més fàcil amb `foreach` i un rang:

```powershell
foreach ($i in 1..10) { Write-Host "7 x $i = $(7 * $i)" }
```

## `while`: mentre siga cert

```powershell
$compte = 5
while ($compte -gt 0) {
    Write-Host $compte
    Start-Sleep -Seconds 1          # espera 1 segon
    $compte--                       # resta 1 (si no, no acabaria mai)
}
Write-Host "Ja!"
```

Si la condició ja és falsa al principi, **no s'executa cap vegada**.

## `do { } while` i `do { } until`

Comproven la condició **al final**, així que s'executen **almenys una vegada**. Ideals per a menús i per a demanar dades fins que siguen vàlides:

```powershell
do {
    $resposta = Read-Host "Vols continuar? (s/n)"
} until ($resposta -eq "s" -or $resposta -eq "n")
```

| | Repetix... |
| - | ---------- |
| `do { } while (cond)` | **mentre** la condició siga **certa** |
| `do { } until (cond)` | **fins que** la condició siga **certa** |

### Menú que es repetix

```powershell
do {
    Write-Host "1) Veure la data"
    Write-Host "2) Veure els processos"
    Write-Host "3) Eixir"
    $opcio = Read-Host "Tria"

    switch ($opcio) {
        1 { Get-Date }
        2 { Get-Process | Select-Object -First 10 }
        3 { Write-Host "Adéu" }
        default { Write-Host "Opció no vàlida" }
    }
} while ($opcio -ne 3)
```

## `break` i `continue`

| Paraula | Què fa |
| ------- | ------ |
| `break` | ix del bucle |
| `continue` | passa a la volta següent |

```powershell
foreach ($n in 1..10) {
    if ($n % 2 -eq 0) { continue }      # salta els parells
    if ($n -gt 7)     { break }         # acaba quan passa de 7
    Write-Host $n
}
# 1 3 5 7
```

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| No acaba mai | La variable de la condició no canvia | Modifica-la dins del bucle |
| `$_` està buit | `$_` només existix dins de `ForEach-Object` / `Where-Object` | En `foreach ($x in ...)` usa `$x` |
| `foreach` amb `in` sense parèntesis | Sintaxi | `foreach ($x in $llista) { }` |
| Un menú amb `while` no es mostra mai | La condició era falsa des del principi | Usa `do { } while` |

!!! success "Per a l'examen"
    ```powershell
    foreach ($x in $llista) { ... }              # cada element
    $llista | ForEach-Object { $_ ... }          # el mateix per tuberia ($_)
    for ($i = 1; $i -le 10; $i++) { ... }        # comptar
    foreach ($i in 1..10) { ... }                # comptar (més fàcil)
    while ($cond) { ... }                        # pot no executar-se
    do { ... } while ($cond)                     # almenys 1 vegada, mentre siga cert
    do { ... } until ($cond)                     # almenys 1 vegada, fins que siga cert
    ```
    - `break` ix · `continue` següent volta
