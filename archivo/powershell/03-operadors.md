# 3. Operadors

## Aritmètics

| Operació | Símbol | Exemple | Resultat |
| -------- | ------ | ------- | -------- |
| Sumar | `+` | `7 + 2` | `9` |
| Restar | `-` | `7 - 2` | `5` |
| Multiplicar | `*` | `7 * 2` | `14` |
| Dividir | `/` | `7 / 2` | `3.5` ✅ (sí que fa decimals) |
| Residu | `%` | `7 % 2` | `1` |

A diferència de Bash, PowerShell **sí que fa decimals** directament i no cal res especial per a calcular:

```powershell
$a = 10
$b = 4
$a / $b                 # 2.5
[math]::Round(10/3, 2)  # 3.33 → arredonir a 2 decimals
[math]::Pow(2, 10)      # 1024 → potència
[math]::Sqrt(16)        # 4    → arrel quadrada
[math]::Floor(7/2)      # 3    → divisió entera (arredonir cap avall)
```

### Modificar una variable

```powershell
$i = 0
$i++           # suma 1
$i += 5        # suma 5
$i -= 2        # resta 2
$i *= 3        # multiplica per 3
```

### Unitats de mida

PowerShell entén `KB`, `MB`, `GB`, `TB`. Molt útil per a mides de fitxers i discos:

```powershell
1GB                       # 1073741824
$mida = 5368709120
$mida / 1GB               # 5
"{0:N2} GB" -f ($mida / 1GB)   # "5.00 GB"
```

## Comparació

**Igual que en Bash**, PowerShell usa abreviatures en lloc de `=`, `<`, `>`:

| Operador | Significa | Exemple | Resultat |
| -------- | --------- | ------- | -------- |
| `-eq` | igual | `5 -eq 5` | `True` |
| `-ne` | diferent | `5 -ne 3` | `True` |
| `-gt` | major | `5 -gt 3` | `True` |
| `-ge` | major o igual | `5 -ge 5` | `True` |
| `-lt` | menor | `5 -lt 3` | `False` |
| `-le` | menor o igual | `3 -le 5` | `True` |

!!! danger "No uses `=`, `>` ni `<` per a comparar"
    - `=` **guarda** un valor.
    - `>` **redirigix** a un fitxer: `if ($a > 5)` crea un fitxer anomenat `5`!

### Comparar text

```powershell
"hola" -eq "HOLA"        # True  → per defecte NO distingix majúscules
"hola" -ceq "HOLA"       # False → amb c davant (case-sensitive) sí que distingix
```

### Buscar dins del text

| Operador | Comprova | Exemple | Resultat |
| -------- | -------- | ------- | -------- |
| `-like` | si coincidix amb un patró (`*` = qualsevol cosa) | `"informe.pdf" -like "*.pdf"` | `True` |
| `-notlike` | el contrari | `"a.txt" -notlike "*.pdf"` | `True` |
| `-match` | si coincidix amb una expressió regular | `"tel: 600123" -match "\d+"` | `True` |

```powershell
if ($fitxer -like "*.log") { ... }                     # acaba en .log?
if ($ip -match "^\d+\.\d+\.\d+\.\d+$") { ... }         # té forma d'IP?
```

### Buscar en una llista

| Operador | Comprova | Exemple |
| -------- | -------- | ------- |
| `-contains` | la llista conté el valor? | `$serveis -contains "ssh"` |
| `-in` | el valor està en la llista? | `"ssh" -in $serveis` |

```powershell
$admins = "ana", "pep"
if ($usuari -in $admins) { Write-Host "És administrador" }
```

## Lògics

| Operador | Significa | Exemple |
| -------- | --------- | ------- |
| `-and` | les dues | `$edat -ge 18 -and $edat -lt 65` |
| `-or` | almenys una | `$dia -eq "dissabte" -or $dia -eq "diumenge"` |
| `-not` o `!` | el contrari | `-not (Test-Path $fitxer)` |

## Operacions amb text

```powershell
$nom = "Ana"
"Hola " + $nom              # unir → "Hola Ana"
"-" * 20                    # repetir → "--------------------"
$nom.Length                 # 3 → llargària
```

### Mètodes del text

Com en Python, el text té funcions incloses (s'usen amb un punt):

| Mètode | Exemple | Resultat |
| ------ | ------- | -------- |
| `.ToUpper()` | `"hola".ToUpper()` | `HOLA` |
| `.ToLower()` | `"HOLA".ToLower()` | `hola` |
| `.Trim()` | `"  hola ".Trim()` | `hola` |
| `.Replace(a, b)` | `"1.000".Replace(".", "")` | `1000` |
| `.Substring(inici, n)` | `"PowerShell".Substring(0, 5)` | `Power` |
| `.StartsWith(x)` | `"hola".StartsWith("ho")` | `True` |
| `.EndsWith(x)` | `"a.log".EndsWith(".log")` | `True` |
| `.Contains(x)` | `"error de disc".Contains("disc")` | `True` |
| `.Split(sep)` | `"a:b:c".Split(":")` | `a`, `b`, `c` |

### Operadors de text

```powershell
"a:b:c" -split ":"              # talla → a, b, c
"a", "b", "c" -join ", "        # uneix → "a, b, c"
"hola món" -replace "món", "a tots"   # substituïx → "hola a tots"
```

### Donar format: `-f`

Per a posar valors dins d'un text amb format (decimals, alineació):

```powershell
"{0} té {1} anys" -f "Ana", 30          # Ana té 30 anys
"{0:N2}" -f 3.14159                     # 3.14 → 2 decimals
"{0:P1}" -f 0.256                       # 25.6 % → percentatge
"{0,-10}|{1,5}" -f "ana", 1000          # "ana       | 1000" → alinear
```

`{0}` és el primer valor, `{1}` el segon... `,-10` vol dir 10 espais alineat a l'esquerra; `,5` 5 espais a la dreta.

!!! note "Coma o punt decimal"
    El resultat de `{0:N2}` o `{0:P1}` depén de l'idioma de Windows: en castellà o valencià ix amb coma (`3,14`, `25,6 %`); en anglés, amb punt.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `if ($a > 5)` crea un fitxer | `>` és redirecció | `-gt` |
| `if ($a = 5)` sempre és cert | `=` guarda | `-eq` |
| `"Hola" -eq "hola"` dona `True` | No distingix majúscules | `-ceq` si vols distingir |
| `-contains` no troba un tros de text | `-contains` és per a llistes | Per a text: `-like "*tros*"` o `.Contains()` |

!!! success "Per a l'examen"
    | Vull... | S'escriu |
    | ------- | -------- |
    | comparar números o text | `-eq -ne -gt -ge -lt -le` |
    | patró amb `*` | `-like "*.log"` |
    | expressió regular | `-match "^\d+$"` |
    | està en una llista | `$x -in $llista` |
    | i / o / no | `-and` / `-or` / `-not` |
    | arredonir | `[math]::Round(x, 2)` |
    | tallar / unir | `-split ":"` / `-join ","` |
    | substituir | `-replace "a", "b"` |
    | format | `"{0:N2}" -f $x` |
