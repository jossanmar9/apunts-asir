# Exercicis resolts

Intenta'ls abans d'obrir la solució. Totes les solucions estan comentades línia a línia.

!!! tip "Com executar-los"
    Guarda el codi en un fitxer `.ps1` i executa'l amb `.\nom.ps1`. Si dona l'error *running scripts is disabled*, mira el [tema 1](01-primers-passos.md#2-permetre-lexecucio-de-scripts).

## Nivell bàsic

### 1. Calcular l'edat

Demana el nom i l'any de naixement, calcula l'edat i diu si és major d'edat. Si no ho és, quants anys li falten.

```console
Com et dius: Ana
En quin any vas nàixer: 2000
Hola, Ana. Tens (o faràs) 26 anys.
Eres major d'edat.
```

??? success "Solució"

    ```powershell title="edat.ps1"
    # Demana el nom i l'any de naixement i calcula l'edat
    $nom = Read-Host "Com et dius"
    [int]$naixement = Read-Host "En quin any vas nàixer"     # [int] converteix el text a número

    $any = (Get-Date).Year                  # l'any actual
    $edat = $any - $naixement

    Write-Host "Hola, $nom. Tens (o faràs) $edat anys."

    if ($edat -ge 18) {
        Write-Host "Eres major d'edat."
    } else {
        Write-Host "Eres menor d'edat. Et falten $(18 - $edat) anys per als 18."
    }
    ```

    `(Get-Date).Year` és l'any actual. Els parèntesis fan que primer s'execute `Get-Date` i després se'n llija la propietat `Year`.

### 2. Calculadora amb menú

Menú amb les quatre operacions i una opció per a eixir. Es repetix fins que l'usuari trie eixir. No ha de deixar dividir per zero.

??? success "Solució"

    ```powershell title="calculadora.ps1"
    # Calculadora amb menú que es repetix fins que l'usuari tria eixir
    do {
        Write-Host ""
        Write-Host "1) Sumar   2) Restar   3) Multiplicar   4) Dividir   5) Eixir"
        $opcio = Read-Host "Tria una opció"

        if ($opcio -in "1", "2", "3", "4") {            # només demanem números si cal
            [double]$a = Read-Host "Primer número"
            [double]$b = Read-Host "Segon número"
        }

        switch ($opcio) {
            "1" { Write-Host "$a + $b = $($a + $b)" }
            "2" { Write-Host "$a - $b = $($a - $b)" }
            "3" { Write-Host "$a x $b = $($a * $b)" }
            "4" {
                if ($b -eq 0) {
                    Write-Host "No es pot dividir per zero" -ForegroundColor Red
                } else {
                    Write-Host "$a / $b = $([math]::Round($a / $b, 2))"
                }
            }
            "5" { Write-Host "Adéu!" }
            default { Write-Host "Opció no vàlida" }
        }
    } while ($opcio -ne "5")                            # repetix mentre no trie 5
    ```

    - `do { } while` perquè el menú s'ha de mostrar **almenys una vegada**.
    - `$opcio -in "1", "2", "3", "4"` evita demanar números si l'opció és eixir o no és vàlida.
    - `[double]` permet decimals.

### 3. Parell i taula de multiplicar

Script que rep un número com a paràmetre, diu si és parell i mostra la seua taula de multiplicar.

```console
.\taula.ps1 -Numero 7
7 és imparell
7 x  1 =   7
7 x  2 =  14
...
```

??? success "Solució"

    ```powershell title="taula.ps1"
    # Diu si un número és parell i mostra la seua taula de multiplicar
    param(
        [Parameter(Mandatory)]
        [int]$Numero                         # si no es passa, PowerShell el pregunta
    )

    if ($Numero % 2 -eq 0) {                 # residu 0 en dividir per 2 → parell
        Write-Host "$Numero és parell"
    } else {
        Write-Host "$Numero és imparell"
    }

    foreach ($i in 1..10) {
        Write-Host ("{0} x {1,2} = {2,3}" -f $Numero, $i, ($Numero * $i))   # alineat amb -f
    }
    ```

    Com que el paràmetre és `Mandatory`, si executes `.\taula.ps1` sense res, PowerShell el pregunta. `{1,2}` reserva 2 espais per al número, així els resultats queden alineats.

### 4. Endevina el número

El programa pensa un número de l'1 al 100 i l'usuari l'ha d'endevinar. Després de cada intent li diu si és més amunt o més avall, i al final quants intents ha necessitat.

??? success "Solució"

    ```powershell title="endevina.ps1"
    # Joc d'endevinar un número entre 1 i 100
    $secret = Get-Random -Minimum 1 -Maximum 101     # Maximum NO s'inclou: 1..100
    $intents = 0

    do {
        $text = Read-Host "Número (1-100)"
        $n = $text -as [int]                         # $null si no és un número
        if ($null -eq $n) {
            Write-Host "Escriu un número"
            continue                                 # torna a preguntar sense comptar l'intent
        }
        $intents++
        if ($n -lt $secret) {
            Write-Host "Més amunt"
        } elseif ($n -gt $secret) {
            Write-Host "Més avall"
        }
    } until ($n -eq $secret)                         # repetix fins que l'encerte

    Write-Host "Encertat en $intents intents!" -ForegroundColor Green
    ```

    - `Get-Random -Maximum 101` dona números **fins a 100**: el màxim no s'inclou.
    - `-as [int]` torna `$null` si el text no és un número, en compte de donar error.
    - `do { } until` repetix **fins que** encerte.

### 5. Estadística de notes

Amb una llista de notes, mostra la mitjana, la màxima i la mínima, i quantes notes hi ha de cada categoria amb el seu percentatge.

```console
Alumnes: 6  Mitjana: 6.33  Màxima: 9.5  Mínima: 3
Suspés       2  (33 %)
Aprovat      1  (17 %)
Notable      2  (33 %)
Excel·lent   1  (17 %)
```

??? success "Solució"

    ```powershell title="notes.ps1"
    # Estadística d'una llista de notes
    $notes = 4, 6.5, 8, 9.5, 3, 7

    # Measure-Object calcula diverses coses d'una vegada
    $estad = $notes | Measure-Object -Average -Maximum -Minimum
    Write-Host ("Alumnes: {0}  Mitjana: {1:N2}  Màxima: {2}  Mínima: {3}" -f `
        $notes.Count, $estad.Average, $estad.Maximum, $estad.Minimum)

    # Taula hash per a comptar quantes notes hi ha de cada categoria
    $categories = [ordered]@{ "Suspés" = 0; "Aprovat" = 0; "Notable" = 0; "Excel·lent" = 0 }
    foreach ($n in $notes) {
        if ($n -lt 5)     { $categories["Suspés"]++ }
        elseif ($n -lt 7) { $categories["Aprovat"]++ }
        elseif ($n -lt 9) { $categories["Notable"]++ }
        else              { $categories["Excel·lent"]++ }
    }

    foreach ($c in $categories.Keys) {
        $percent = $categories[$c] / $notes.Count
        Write-Host ("{0,-11}{1,3}  ({2:P0})" -f $c, $categories[$c], $percent)
    }
    ```

    - `Measure-Object` calcula diverses estadístiques d'una vegada.
    - `[ordered]@{ }` és una taula hash que **manté l'ordre** en què afiges les claus (una normal les pot mostrar desordenades).
    - El `` ` `` al final d'una línia fa que l'ordre continue en la següent.

## Nivell mitjà: fitxers

### 6. Paraules més repetides

Rep un fitxer de text i mostra les 5 paraules (de més de 3 lletres) que més es repetixen.

```console
.\paraules.ps1 -Fitxer text.txt
Paraules en total: 10

Count Name
----- ----
    5 servidor
    1 bases
    1 caigut
...
```

??? success "Solució"

    ```powershell title="paraules.ps1"
    # Mostra les 5 paraules que més es repetixen en un fitxer de text
    param(
        [Parameter(Mandatory)]
        [string]$Fitxer
    )

    if (-not (Test-Path $Fitxer)) {
        Write-Host "No existix el fitxer $Fitxer" -ForegroundColor Red
        exit 1
    }

    $text = Get-Content $Fitxer -Raw                 # -Raw: tot el fitxer com un sol text
    $paraules = $text.ToLower() -split "\W+" |       # talla per tot el que no siga lletra o número
        Where-Object { $_.Length -gt 3 }             # només paraules de més de 3 lletres

    Write-Host "Paraules en total: $($paraules.Count)"
    $paraules |
        Group-Object |                               # agrupa les iguals i compta
        Sort-Object Count -Descending |
        Select-Object -First 5 Count, Name
    ```

    - `-Raw` llig tot el fitxer com un sol text (sense `-Raw`, seria una llista de línies).
    - `-split "\W+"` talla per qualsevol cosa que no siga lletra o número (espais, punts, comes...).
    - `Group-Object` agrupa les paraules iguals i en compta quantes n'hi ha.

### 7. Informe dels fitxers més grans

Busca els N fitxers més grans d'una carpeta (i subcarpetes), els mostra amb la mida en MB i guarda l'informe en un CSV.

??? success "Solució"

    ```powershell title="grans.ps1"
    # Informe dels fitxers més grans d'una carpeta, exportat a CSV
    param(
        [string]$Carpeta = $HOME,                    # per defecte, la carpeta personal
        [int]$Quants = 10,
        [string]$Eixida = "fitxers_grans.csv"
    )

    $fitxers = Get-ChildItem -Path $Carpeta -Recurse -File -ErrorAction SilentlyContinue |
        Sort-Object Length -Descending |
        Select-Object -First $Quants FullName,
            @{ Name = "MB"; Expression = { [math]::Round($_.Length / 1MB, 2) } },   # mida en MB
            LastWriteTime

    $fitxers | Format-Table -AutoSize                # mostrar per pantalla
    $fitxers | Export-Csv $Eixida -NoTypeInformation # i guardar en CSV
    Write-Host "Informe guardat en $Eixida"
    ```

    - `@{ Name = "MB"; Expression = { ... } }` crea una columna nova calculada.
    - `-ErrorAction SilentlyContinue` amaga els errors de carpetes on no tens permís.
    - El CSV es pot obrir directament amb Excel.

### 8. Netejar fitxers antics

Esborra els fitxers d'una carpeta que tinguen més de N dies. Amb `-Simula`, només ha de mostrar què esborraria.

```console
.\neteja.ps1 -Carpeta C:\temp -Dies 30 -Simula
Esborraria: C:\temp\vell.txt
1 fitxers
```

??? success "Solució"

    ```powershell title="neteja.ps1"
    # Esborra els fitxers d'una carpeta més antics que N dies
    param(
        [Parameter(Mandatory)]
        [string]$Carpeta,
        [int]$Dies = 30,
        [switch]$Simula                              # amb -Simula només mostra, no esborra
    )

    if (-not (Test-Path $Carpeta -PathType Container)) {
        Write-Host "No és una carpeta: $Carpeta" -ForegroundColor Red
        exit 1
    }

    $limit = (Get-Date).AddDays(-$Dies)              # la data de fa N dies
    $vells = Get-ChildItem $Carpeta -File -Recurse | Where-Object LastWriteTime -lt $limit

    if (-not $vells) {
        Write-Host "No hi ha fitxers de més de $Dies dies"
        exit 0
    }

    foreach ($f in $vells) {
        if ($Simula) {
            Write-Host "Esborraria: $($f.FullName)"
        } else {
            Remove-Item $f.FullName
            Write-Host "Esborrat:   $($f.FullName)"
        }
    }
    Write-Host "$($vells.Count) fitxers"
    ```

    - `(Get-Date).AddDays(-30)` és la data de fa 30 dies.
    - `[switch]$Simula` val `$true` si poses `-Simula` en executar-lo.
    - **Prova sempre primer amb `-Simula`** abans d'esborrar de veritat.

### 9. Còpia de seguretat amb rotació

Comprimix una carpeta en un `.zip` amb la data i l'hora al nom, i conserva només les N còpies més recents.

```console
.\backup.ps1 -Origen C:\Users\ana\Documents -Desti D:\copies -Conserva 7
Creat D:\copies\Documents_20261010_183044.zip
Esborrada Documents_20261003_183040.zip
```

??? success "Solució"

    ```powershell title="backup.ps1"
    # Còpia comprimida d'una carpeta amb la data al nom; conserva només les N últimes
    param(
        [Parameter(Mandatory)][string]$Origen,
        [Parameter(Mandatory)][string]$Desti,
        [int]$Conserva = 7
    )

    if (-not (Test-Path $Origen -PathType Container)) {
        Write-Host "L'origen no és una carpeta" -ForegroundColor Red
        exit 1
    }
    New-Item -Path $Desti -ItemType Directory -Force | Out-Null      # crea el destí si cal

    $nomCarpeta = Split-Path $Origen -Leaf                            # nom de la carpeta sense la ruta
    $data = Get-Date -Format "yyyyMMdd_HHmmss"                        # 20261010_183000
    $zip = Join-Path $Desti "$nomCarpeta`_$data.zip"                  # `_ perquè _ no s'unisca al nom de la variable

    Compress-Archive -Path "$Origen/*" -DestinationPath $zip
    Write-Host "Creat $zip"

    # Rotació: ordenem les còpies per data i esborrem les que sobren
    $copies = Get-ChildItem $Desti -Filter "$nomCarpeta`_*.zip" | Sort-Object Name
    $sobren = $copies.Count - $Conserva
    if ($sobren -gt 0) {
        $copies | Select-Object -First $sobren | ForEach-Object {
            Remove-Item $_.FullName
            Write-Host "Esborrada $($_.Name)"
        }
    }
    ```

    - `Split-Path -Leaf` torna l'últim tros d'una ruta (el nom de la carpeta).
    - `Join-Path` unix trossos de ruta posant la barra correcta.
    - Com que el nom porta la data en format `yyyyMMdd_HHmmss`, ordenar per nom és el mateix que ordenar per data.
    - Per a executar-lo cada nit, crea una tasca programada ([tema 10](10-sysadmin.md#tasques-programades)).

## Per a sysadmin

### 10. Alerta d'espai en disc

Mostra l'espai de cada disc i marca en roig els que passen d'un percentatge (80 % per defecte). Ha d'acabar amb codi 1 si n'hi ha algun en alerta.

??? success "Solució"

    ```powershell title="disc.ps1"
    # Mostra l'espai de cada disc i avisa dels que passen d'un percentatge
    param([int]$Llindar = 80)

    $alertes = 0
    Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Used -ne $null -and ($_.Used + $_.Free) -gt 0 } |
        ForEach-Object {
            $total = $_.Used + $_.Free
            $percent = $_.Used / $total * 100
            $text = "{0,-15} {1,8:N1} GB {2,5:N0} %" -f $_.Root, ($total / 1GB), $percent
            if ($percent -ge $Llindar) {
                Write-Host "$text  ALERTA" -ForegroundColor Red
                $alertes++
            } else {
                Write-Host $text
            }
        }

    if ($alertes -gt 0) { exit 1 } else { exit 0 }    # codi d'eixida útil per a tasques programades
    ```

    `Get-PSDrive -PSProvider FileSystem` torna les unitats (C:, D:...) amb l'espai usat (`Used`) i lliure (`Free`). El codi d'eixida (`exit 1`) permet que una tasca programada o un altre script sàpiga si hi ha hagut alerta.

### 11. Vigilar serveis

Comprova si una llista de serveis està en marxa i arranca els que estiguen parats. **Només Windows**, com a administrador.

??? success "Solució"

    ```powershell title="serveis.ps1"
    # Comprova que uns serveis estan en marxa i arranca els que estiguen parats
    # (només Windows; cal executar-lo com a administrador per a arrancar-los)
    $serveis = "Spooler", "W32Time", "WinRM"

    foreach ($nom in $serveis) {
        $s = Get-Service -Name $nom -ErrorAction SilentlyContinue
        if (-not $s) {
            Write-Host "$nom no existix en este equip" -ForegroundColor Yellow
            continue
        }
        if ($s.Status -eq "Running") {
            Write-Host "$nom està en marxa" -ForegroundColor Green
        } else {
            Write-Host "$nom està parat. Arrancant..." -ForegroundColor Yellow
            try {
                Start-Service -Name $nom -ErrorAction Stop
                Write-Host "  $nom arrancat"
            } catch {
                Write-Host "  No s'ha pogut arrancar: $($_.Exception.Message)" -ForegroundColor Red
            }
        }
    }
    ```

    - `-ErrorAction SilentlyContinue` en `Get-Service`: si el servei no existix, torna `$null` en compte de donar error.
    - `try`/`catch` amb `-ErrorAction Stop` per si no es pot arrancar (falta de permisos, servei deshabilitat...).

### 12. Alta d'usuaris locals des d'un CSV

Llig un CSV amb nom, cognom i grup, genera el login (inicials + primer cognom, sense accents) i una contrasenya aleatòria, i crea els usuaris. Per defecte, només ha de **simular**.

??? success "Solució"

    ```text title="usuaris.csv"
    Nom,Cognom,Grup
    Maria Josep,Pons Ferrer,Usuaris
    Àngela,Bàñez,Administradors
    ```

    ```powershell title="alta-locals.ps1"
    # Crea usuaris locals a partir d'un CSV (Nom,Cognom,Grup)
    # Sense -Aplica només mostra el que faria. Amb -Aplica cal ser administrador (només Windows).
    param(
        [Parameter(Mandatory)][string]$Csv,
        [switch]$Aplica
    )

    function Get-Login {
        param([string]$Nom, [string]$Cognom)
        # Inicials del nom + primer cognom, en minúscules i sense accents
        $inicials = ($Nom -split " " | ForEach-Object { $_[0] }) -join ""
        $login = ($inicials + ($Cognom -split " ")[0]).ToLower()
        # Llevar accents: separar la lletra de l'accent i quedar-se només amb la lletra
        $normal = $login.Normalize([Text.NormalizationForm]::FormD)
        return ($normal -replace "\p{Mn}", "")
    }

    function New-Contrasenya {
        $caracters = [char[]]"ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
        return -join (1..12 | ForEach-Object { Get-Random -InputObject $caracters })
    }

    foreach ($fila in Import-Csv $Csv) {
        $login = Get-Login -Nom $fila.Nom -Cognom $fila.Cognom
        $clau = New-Contrasenya

        if ($Aplica) {
            $segura = ConvertTo-SecureString $clau -AsPlainText -Force
            New-LocalUser -Name $login -Password $segura -FullName "$($fila.Nom) $($fila.Cognom)" | Out-Null
            Add-LocalGroupMember -Group $fila.Grup -Member $login
            Write-Host "Creat $login en $($fila.Grup)"
        } else {
            Write-Host "SIMULA: New-LocalUser -Name $login -FullName '$($fila.Nom) $($fila.Cognom)'"
            Write-Host "SIMULA: Add-LocalGroupMember -Group $($fila.Grup) -Member $login"
        }
        Write-Host ("{0,-12} {1}" -f $login, $clau)
    }
    ```

    - `.Normalize(FormD)` separa cada lletra del seu accent, i `-replace "\p{Mn}", ""` esborra els accents: *Bàñez* → *banez*.
    - La contrasenya s'ha de passar a `New-LocalUser` com a `SecureString`, per això el `ConvertTo-SecureString`.
    - Amb `-Aplica` crea els usuaris de veritat: cal executar-lo **com a administrador** en Windows. Per a fer-ho en el Directori Actiu, mira l'exemple d'[alta massiva en AD](10-sysadmin.md#alta-massiva-des-dun-csv).

    ```console
    .\alta-locals.ps1 -Csv usuaris.csv
    SIMULA: New-LocalUser -Name mjpons -FullName 'Maria Josep Pons Ferrer'
    SIMULA: Add-LocalGroupMember -Group Usuaris -Member mjpons
    mjpons       QVxYF3b4cdWa
    ...
    ```
