# 4. Condicionals

## `if`: prendre decisions

```powershell
[int]$edat = Read-Host "Edat"

if ($edat -ge 18) {
    Write-Host "Eres major d'edat"
} else {
    Write-Host "Eres menor d'edat"
}
```

**L'estructura:**

- La condició va entre **parèntesis** `( )`.
- El codi que s'executa va entre **claus** `{ }`.
- No cal `then` ni `fi` (com en Bash): les claus marquen on comença i on acaba.

### Diverses opcions: `elseif`

```powershell
[double]$nota = Read-Host "Nota"

if ($nota -lt 5) {
    Write-Host "Suspés"
} elseif ($nota -lt 7) {
    Write-Host "Aprovat"
} elseif ($nota -lt 9) {
    Write-Host "Notable"
} else {
    Write-Host "Excel·lent"
}
```

S'escriu **`elseif`** (tot junt). PowerShell comprova les condicions de dalt a baix i executa **només la primera certa**.

### La condició pot ser una ordre

Qualsevol ordre que torne `True` o `False`:

```powershell
if (Test-Path "C:\dades") {                  # existix la carpeta?
    Write-Host "La carpeta existix"
}

if (-not (Test-Path "C:\dades")) {           # NO existix?
    New-Item -Path "C:\dades" -ItemType Directory
}
```

També funciona amb objectes: una llista buida o `$null` compten com a **fals**, i qualsevol cosa amb contingut com a **cert**:

```powershell
$proces = Get-Process -Name notepad -ErrorAction SilentlyContinue
if ($proces) {
    Write-Host "El Bloc de notes està obert"
} else {
    Write-Host "El Bloc de notes està tancat"
}
```

`-ErrorAction SilentlyContinue` evita que es mostre l'error si no el troba.

## `switch`: moltes opcions d'una mateixa variable

Equivalent al `case` de Bash. Més clar que molts `elseif` quan comparen la mateixa variable:

```powershell
$opcio = Read-Host "Tria (1-3)"

switch ($opcio) {
    1       { Write-Host "Has triat veure els processos" }
    2       { Write-Host "Has triat veure els serveis" }
    3       { Write-Host "Eixint..." }
    default { Write-Host "Opció no vàlida" }
}
```

- Cada opció: el valor i, entre claus, què fer.
- `default` és "qualsevol altra cosa" (com l'`else`).

### Amb patrons: `-Wildcard`

```powershell
switch -Wildcard ($fitxer) {
    "*.jpg" { "És una imatge" }
    "*.png" { "És una imatge" }
    "*.txt" { "És un text" }
    default { "Tipus desconegut" }
}
```

!!! warning "`switch` pot executar diverses opcions"
    Si un valor coincidix amb dues opcions, s'executen **les dues**. Per a parar en la primera, posa `break` dins de les claus: `{ "És una imatge"; break }`.

### Diversos valors en una opció

`switch` no té `a|b` com Bash. Pots usar una condició entre claus:

```powershell
switch ($dia) {
    { $_ -in "dissabte", "diumenge" } { "Cap de setmana" }
    default                           { "Dia laborable" }
}
```

`$_` és el valor que s'està comparant.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `if $a -gt 5 {` dona error | Falten els parèntesis | `if ($a -gt 5) {` |
| `else if` no funciona com esperes | S'escriu junt | `elseif` |
| La condició sempre és certa | Has posat `=` | `-eq` |
| `if ($a > 5)` crea un fitxer `5` | `>` és redirecció | `-gt` |
| El `switch` executa dues opcions | Coincidix amb totes dues | `break` dins de l'opció |

!!! success "Per a l'examen"
    ```powershell
    if ($a -gt 5) {
        ...
    } elseif ($a -eq 5) {
        ...
    } else {
        ...
    }

    switch ($var) {
        1       { ... }
        "text"  { ... }
        default { ... }
    }
    switch -Wildcard ($f) { "*.txt" { ... } }
    ```
    - Condició entre `( )`, codi entre `{ }`
    - `elseif` junt
    - `Test-Path` per a saber si existix un fitxer o carpeta
