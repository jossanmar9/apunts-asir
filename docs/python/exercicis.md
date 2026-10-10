# Exercicis resolts

Intenta'ls abans d'obrir la solució. Quan funcione el teu, compara: sovint hi ha una manera més curta o més clara.

## Nivell bàsic

### 1. Conversor de temperatura

Demana una temperatura i la seua unitat (C o F) i la convertix a l'altra.

```console
Temperatura: 36.6
En quina unitat està? (C/F): c
36.6 °C = 97.9 °F
```

??? success "Solució"

    ```python title="temperatura.py"
    grau = float(input("Temperatura: "))
    unitat = input("En quina unitat està? (C/F): ").strip().upper()

    if unitat == "C":
        print(f"{grau} °C = {grau * 9 / 5 + 32:.1f} °F")
    elif unitat == "F":
        print(f"{grau} °F = {(grau - 32) * 5 / 9:.1f} °C")
    else:
        print("Unitat desconeguda")
    ```

    `.strip().upper()` accepta `c`, `C` o ` c ` igual.

### 2. Estadística de notes

Demana notes fins que l'usuari prema Intro sense escriure res. Mostra la mitjana i quants suspesos, aprovats, notables i excel·lents hi ha, amb el percentatge.

??? success "Solució"

    ```python title="notes.py"
    notes = []
    while (text := input("Nota (Intro per a acabar): ")) != "":
        nota = float(text)
        if 0 <= nota <= 10:
            notes.append(nota)
        else:
            print("La nota ha d'estar entre 0 i 10")

    if not notes:
        print("No has introduït cap nota")
    else:
        categories = {"Suspés": 0, "Aprovat": 0, "Notable": 0, "Excel·lent": 0}
        for n in notes:
            if n < 5:
                categories["Suspés"] += 1
            elif n < 7:
                categories["Aprovat"] += 1
            elif n < 9:
                categories["Notable"] += 1
            else:
                categories["Excel·lent"] += 1

        print(f"\nAlumnes: {len(notes)}  Mitjana: {sum(notes) / len(notes):.2f}")
        for nom, quants in categories.items():
            print(f"{nom:<11}{quants:>3}  ({quants / len(notes):.0%})")
    ```

    - L'operador morsa `:=` llig i comprova en la mateixa línia.
    - Un diccionari fa de comptador per a cada categoria.
    - `{x:.0%}` mostra un tant per u com a percentatge.

### 3. Any de traspàs

Fes una funció que diga si un any és de traspàs.

??? success "Solució"

    ```python title="traspas.py"
    def es_traspas(any_):
        """Divisible per 4, excepte els seculars que no ho són per 400."""
        return any_ % 4 == 0 and (any_ % 100 != 0 or any_ % 400 == 0)

    for a in (1900, 2000, 2024, 2026):
        print(a, "és de traspàs" if es_traspas(a) else "no és de traspàs")
    ```

    La regla completa: divisible per 4, **excepte** els anys acabats en 00, que només ho són si són divisibles per 400 (2000 sí, 1900 no).

### 4. Màxim comú divisor

Calcula el MCD de dos números amb l'algorisme d'Euclides, i amb ell el mínim comú múltiple.

??? success "Solució"

    ```python title="mcd.py"
    def mcd(a, b):
        """Algorisme d'Euclides: mcd(a, b) = mcd(b, a % b) fins que b siga 0."""
        while b != 0:
            a, b = b, a % b
        return a

    def mcm(a, b):
        return a * b // mcd(a, b)

    print(mcd(48, 18))   # 6
    print(mcm(4, 6))     # 12
    ```

    `a, b = b, a % b` fa les dues assignacions alhora, sense variable temporal. Python també ho porta fet: `math.gcd(48, 18)`.

### 5. Factorial i nombre combinatori

Factorial d'un número de forma iterativa i recursiva, i el nombre combinatori *n sobre m*.

??? success "Solució"

    ```python title="factorial.py"
    def factorial_iteratiu(n):
        resultat = 1
        for i in range(2, n + 1):
            resultat *= i
        return resultat

    def factorial_recursiu(n):
        if n <= 1:
            return 1
        return n * factorial_recursiu(n - 1)

    def combinatori(n, m):
        """Formes de triar m elements de n: n! / (m! (n-m)!)"""
        return factorial_iteratiu(n) // (factorial_iteratiu(m) * factorial_iteratiu(n - m))

    print(factorial_iteratiu(5), factorial_recursiu(5))   # 120 120
    print(combinatori(49, 6))                             # 13983816 (la primitiva)
    ```

    La versió recursiva és més semblant a la definició matemàtica, però per a números molt grans (més de ~1000) supera el límit de recursió de Python. La iterativa no té eixe problema.

### 6. Fibonacci

Torna els *n* primers termes de la successió de Fibonacci (cada terme és la suma dels dos anteriors).

??? success "Solució"

    ```python title="fibonacci.py"
    def fibonacci(n):
        """Torna una llista amb els n primers termes."""
        termes = []
        a, b = 0, 1
        for _ in range(n):
            termes.append(a)
            a, b = b, a + b
        return termes

    print(fibonacci(12))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    ```

### 7. Jugar amb un text

Llig un text i mostra'l al revés (sense usar `[::-1]`), en majúscules, la longitud, les vocals i si és un palíndrom.

```console
Escriu un text: Dabale arroz a la zorra el abad
Al revés:  daba le arroz al a zorra elabaD
...
És un palíndrom
```

??? success "Solució"

    ```python title="cadena.py"
    text = input("Escriu un text: ")

    invertit = ""
    for lletra in text:
        invertit = lletra + invertit      # cada lletra va davant de les anteriors

    vocals = sum(1 for c in text.lower() if c in "aeiouàèéíòóúü")

    print(f"Al revés:  {invertit}")
    print(f"Majúscules: {text.upper()}")
    print(f"Longitud:  {len(text)}  Vocals: {vocals}")
    print("És un palíndrom" if text.lower().replace(" ", "") == invertit.lower().replace(" ", "") else "No és un palíndrom")
    ```

    Amb slicing seria `text[::-1]`, però fer-ho amb un bucle ajuda a entendre com es construïx una cadena pas a pas.

### 8. Sumar fins a zero

Demana números fins que s'escriga 0. Mostra la suma, la mitjana, el major i la suma dels parells i dels senars per separat.

??? success "Solució"

    ```python title="suma_fins_zero.py"
    nums = []
    while True:
        n = int(input("Número (0 per a acabar): "))
        if n == 0:
            break
        nums.append(n)

    if nums:
        parells = sum(n for n in nums if n % 2 == 0)
        senars = sum(n for n in nums if n % 2 != 0)
        print(f"Suma: {sum(nums)}  Mitjana: {sum(nums) / len(nums):.2f}  Major: {max(nums)}")
        print(f"Suma dels parells: {parells}  Suma dels senars: {senars}")
    ```

    `sum(n for n in nums if n % 2 == 0)` suma només els que complixen la condició, sense crear una llista intermèdia.

### 9. Tipus de triangle

Demana tres costats, comprova que formen un triangle i diu si és equilàter, isòsceles o escalé, amb la seua àrea.

??? success "Solució"

    ```python title="triangle.py"
    a, b, c = sorted(float(input(f"Costat {i}: ")) for i in (1, 2, 3))

    if a + b <= c:
        print("Amb eixos costats no es pot fer un triangle")
    else:
        if a == b == c:
            tipus = "equilàter"
        elif a == b or b == c:
            tipus = "isòsceles"
        else:
            tipus = "escalé"
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5     # fórmula d'Heró
        print(f"Triangle {tipus}, àrea {area:.2f}")
    ```

    Ordenar els costats simplifica les comprovacions: n'hi ha prou amb mirar si els dos menuts sumen més que el gran.

### 10. Equació de segon grau

Resol *ax² + bx + c = 0* (només solucions reals).

??? success "Solució"

    ```python title="equacio.py"
    import math

    print("ax² + bx + c = 0")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a == 0:
        print("No és de segon grau")
    else:
        disc = b ** 2 - 4 * a * c
        if disc > 0:
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            x2 = (-b - math.sqrt(disc)) / (2 * a)
            print(f"Dues solucions: {x1:g} i {x2:g}")
        elif disc == 0:
            print(f"Una solució doble: {-b / (2 * a):g}")
        else:
            print("No té solucions reals")
    ```

    El format `:g` lleva els zeros sobrants: `2.0` es mostra com `2`.

## Nivell mitjà

### 11. El teu propi `wc`

Rep un fitxer per argument i mostra'n les línies, paraules i caràcters.

```console
$ python3 wc.py prova.txt
      3 línies       6 paraules      31 caràcters  prova.txt
```

??? success "Solució"

    ```python title="wc.py"
    import sys

    if len(sys.argv) != 2:
        sys.exit(f"Ús: {sys.argv[0]} <fitxer>")

    try:
        with open(sys.argv[1], encoding="utf-8") as f:
            linies = paraules = caracters = 0
            for linia in f:
                linies += 1
                paraules += len(linia.split())
                caracters += len(linia)
    except FileNotFoundError:
        sys.exit(f"No existix: {sys.argv[1]}")

    print(f"{linies:>7} línies {paraules:>7} paraules {caracters:>7} caràcters  {sys.argv[1]}")
    ```

    El nostre compte de caràcters coincidix amb `wc -m`. El `wc` normal compta **bytes** i les lletres accentuades ocupen 2 bytes en UTF-8.

### 12. Agenda en JSON

Agenda de contactes amb menú (afegir, buscar, llistar, esborrar) que es guarde en un fitxer JSON per a no perdre les dades.

??? success "Solució"

    ```python title="agenda.py"
    import json
    from pathlib import Path

    FITXER = Path("agenda.json")

    def carrega():
        if FITXER.exists():
            return json.loads(FITXER.read_text(encoding="utf-8"))
        return {}

    def guarda(agenda):
        FITXER.write_text(json.dumps(agenda, indent=2, ensure_ascii=False), encoding="utf-8")

    def main():
        agenda = carrega()
        while True:
            print("\n1) Afegir  2) Buscar  3) Llistar  4) Esborrar  5) Eixir")
            opcio = input("> ").strip()
            match opcio:
                case "1":
                    nom = input("Nom: ").strip()
                    agenda[nom] = {"telefon": input("Telèfon: "), "correu": input("Correu: ")}
                    guarda(agenda)
                case "2":
                    text = input("Buscar: ").lower()
                    for nom, dades in agenda.items():
                        if text in nom.lower():
                            print(f"{nom}: {dades['telefon']}  {dades['correu']}")
                case "3":
                    for nom in sorted(agenda):
                        print(f"{nom:<20}{agenda[nom]['telefon']:<12}{agenda[nom]['correu']}")
                case "4":
                    nom = input("Nom a esborrar: ")
                    if agenda.pop(nom, None) is not None:
                        guarda(agenda)
                        print("Esborrat")
                    else:
                        print("No existix")
                case "5":
                    break
                case _:
                    print("Opció no vàlida")

    if __name__ == "__main__":
        main()
    ```

    - El diccionari té el nom com a clau i un altre diccionari amb les dades com a valor.
    - `agenda.pop(nom, None)` esborra i torna el valor, o `None` si no existia, sense donar error.
    - `ensure_ascii=False` guarda els accents tal qual en compte de `\u00e0`.

### 13. Calculadora de subxarxes

A partir d'una IP amb prefix (`192.168.10.77/26`) calcula la màscara, l'adreça de xarxa, el broadcast, el rang de hosts i quants n'hi ha.

```console
IP/prefix (p. ex. 192.168.10.77/26): 192.168.10.77/26
Màscara      255.255.255.192
Xarxa        192.168.10.64
Broadcast    192.168.10.127
Primer host  192.168.10.65
Últim host   192.168.10.126
Hosts        62
```

??? success "Solució"

    ```python title="subxarxa.py"
    import ipaddress

    def ip_a_int(ip):
        a, b, c, d = (int(x) for x in ip.split("."))
        return (a << 24) | (b << 16) | (c << 8) | d

    def int_a_ip(n):
        return ".".join(str((n >> despl) & 255) for despl in (24, 16, 8, 0))

    def calcula(cidr):
        ip, prefix = cidr.split("/")
        prefix = int(prefix)
        mascara = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
        xarxa = ip_a_int(ip) & mascara
        broadcast = xarxa | (~mascara & 0xFFFFFFFF)
        return {
            "Màscara": int_a_ip(mascara),
            "Xarxa": int_a_ip(xarxa),
            "Broadcast": int_a_ip(broadcast),
            "Primer host": int_a_ip(xarxa + 1),
            "Últim host": int_a_ip(broadcast - 1),
            "Hosts": 2 ** (32 - prefix) - 2,
        }

    cidr = input("IP/prefix (p. ex. 192.168.10.77/26): ")
    for clau, valor in calcula(cidr).items():
        print(f"{clau:<12} {valor}")

    # Comprovació amb la biblioteca estàndard
    xarxa = ipaddress.ip_interface(cidr).network
    print(f"\nipaddress diu: {xarxa}, broadcast {xarxa.broadcast_address}, {xarxa.num_addresses - 2} hosts")
    ```

    - Una IPv4 són 32 bits: es convertix a un enter desplaçant cada octet (`<<`) a la seua posició.
    - **Xarxa** = IP `&` màscara (posa a 0 els bits de host).
    - **Broadcast** = xarxa `|` (màscara invertida) (posa a 1 els bits de host).
    - `& 0xFFFFFFFF` talla a 32 bits, perquè en Python els enters no tenen mida fixa.

    Al final es comprova amb el mòdul estàndard `ipaddress`, que és el que usaries en un script real.

### 14. Ordenar i buscar

Ordena una llista amb el mètode de la bombolla i busca un element amb cerca binària.

??? success "Solució"

    ```python title="ordenacio.py"
    def bombolla(nums):
        v = nums.copy()
        n = len(v)
        for i in range(n - 1):
            canvis = False
            for j in range(n - 1 - i):
                if v[j] > v[j + 1]:
                    v[j], v[j + 1] = v[j + 1], v[j]
                    canvis = True
            if not canvis:          # ja està ordenada
                break
        return v

    def cerca_binaria(v, buscat):
        """Torna la posició de buscat en la llista ORDENADA v, o -1."""
        esq, dre = 0, len(v) - 1
        while esq <= dre:
            mig = (esq + dre) // 2
            if v[mig] == buscat:
                return mig
            if v[mig] < buscat:
                esq = mig + 1
            else:
                dre = mig - 1
        return -1

    dades = [42, 7, 19, 3, 88, 23, 15]
    ordenada = bombolla(dades)
    print(ordenada)                       # [3, 7, 15, 19, 23, 42, 88]
    print(cerca_binaria(ordenada, 23))    # 4
    print(cerca_binaria(ordenada, 5))     # -1
    ```

    - La bombolla compara parelles veïnes i les intercanvia; si en una passada no hi ha cap canvi, ja està ordenada.
    - La cerca binària només funciona amb llistes **ordenades**: mira el centre i descarta la meitat cada vegada. En una llista d'un milió d'elements troba qualsevol en uns 20 passos.
    - En la pràctica: `sorted()` i el mòdul `bisect`.

### 15. Matrius

Funcions per a transposar una matriu i multiplicar dues matrius quadrades.

??? success "Solució"

    ```python title="matrius.py"
    def transposa(m):
        return [[m[f][c] for f in range(len(m))] for c in range(len(m[0]))]

    def multiplica(a, b):
        n = len(a)
        return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    def mostra(m):
        for fila in m:
            print(" ".join(f"{x:4}" for x in fila))

    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    mostra(transposa([[1, 2, 3], [4, 5, 6]]))
    print()
    mostra(multiplica(a, b))
    ```

    Les comprensions niades es lligen de fora cap a dins: la de fora crea les files i la de dins els elements de cada fila.

## Per a sysadmin

### 16. Alerta d'espai en disc

Mostra l'ús de cada sistema de fitxers i marca els que superen un llindar (80 % per defecte). L'script ha d'acabar amb codi 1 si n'hi ha algun en alerta, per a poder usar-lo des de `cron` o un altre script.

??? success "Solució"

    ```python title="disc.py"
    #!/usr/bin/env python3
    """Mostra l'ús de cada sistema de fitxers i avisa dels que passen d'un llindar."""
    import shutil
    import subprocess
    import sys

    LLINDAR = int(sys.argv[1]) if len(sys.argv) > 1 else 80

    r = subprocess.run(["df", "-P", "-x", "tmpfs", "-x", "devtmpfs", "-x", "squashfs", "-x", "overlay"],
                       capture_output=True, text=True)
    punts = [linia.split()[-1] for linia in r.stdout.splitlines()[1:]]

    alertes = 0
    print(f"{'PUNT':<20}{'TOTAL':>9}{'USAT':>9}{'%':>6}")
    for punt in punts:
        total, usat, _ = shutil.disk_usage(punt)
        percent = usat / total * 100
        marca = "  ⚠️" if percent >= LLINDAR else ""
        alertes += percent >= LLINDAR
        print(f"{punt:<20}{total / 1e9:>8.1f}G{usat / 1e9:>8.1f}G{percent:>5.0f}%{marca}")

    sys.exit(1 if alertes else 0)
    ```

    `df -P` dona una eixida estable d'una línia per sistema; d'ella només traiem els punts de muntatge i les xifres les calcula `shutil.disk_usage`. `alertes += condicio` funciona perquè `True` val 1.

### 17. Còpies de seguretat amb rotació

Comprimix un directori en un `.tar.gz` amb la data i l'hora al nom, i conserva només les *N* còpies més recents.

??? success "Solució"

    ```python title="backup.py"
    #!/usr/bin/env python3
    """Còpia comprimida d'un directori amb data al nom; conserva només les N últimes."""
    import argparse
    import shutil
    from datetime import datetime
    from pathlib import Path

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("origen", type=Path)
    p.add_argument("desti", type=Path)
    p.add_argument("-k", "--conserva", type=int, default=7, help="còpies a conservar (7)")
    args = p.parse_args()

    if not args.origen.is_dir():
        p.error(f"{args.origen} no és un directori")
    args.desti.mkdir(parents=True, exist_ok=True)

    nom = f"{args.origen.name}_{datetime.now():%Y%m%d_%H%M%S}"
    fitxer = shutil.make_archive(str(args.desti / nom), "gztar", root_dir=args.origen)
    print(f"Creat {fitxer} ({Path(fitxer).stat().st_size / 1024:.1f} KiB)")

    copies = sorted(args.desti.glob(f"{args.origen.name}_*.tar.gz"))
    for vella in copies[:-args.conserva]:
        vella.unlink()
        print(f"Esborrada {vella.name}")
    ```

    ```console
    $ python3 backup.py ~/Documents /backup -k 7
    Creat /backup/Documents_20261010_174118.tar.gz (812.4 KiB)
    Esborrada Documents_20261003_020000.tar.gz
    ```

    Com que el nom porta la data en format `AAAAMMDD_HHMMSS`, ordenar alfabèticament és el mateix que ordenar per data: les primeres de la llista són les més velles. Per a fer-ho cada nit: `crontab -e` → `0 2 * * * /usr/bin/python3 /ruta/backup.py ...`

### 18. Alta massiva d'usuaris

Llig un CSV amb nom, cognom i grup, genera un login i una contrasenya aleatòria per a cada persona i crea els usuaris. Per defecte només ha de **simular** (mostrar les ordres).

??? success "Solució"

    ```text title="alumnes.csv"
    nom,cognom,grup
    Maria Josep,Pons Ferrer,asir2
    Àngela,Bàñez,profes
    ```

    ```python title="alta_usuaris.py"
    #!/usr/bin/env python3
    """Crea usuaris a partir d'un CSV amb les columnes: nom,cognom,grup"""
    import argparse
    import csv
    import secrets
    import shlex
    import string
    import subprocess
    import unicodedata

    def sense_accents(text):
        return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()

    def login(nom, cognom):
        """Maria Josep, Pons Ferrer → mjpons"""
        inicials = "".join(paraula[0] for paraula in nom.split())
        return sense_accents(inicials + cognom.split()[0]).lower()

    def contrasenya(longitud=12):
        caracters = string.ascii_letters + string.digits
        return "".join(secrets.choice(caracters) for _ in range(longitud))

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv")
    p.add_argument("--aplica", action="store_true", help="crea'ls de veritat (si no, només simula)")
    args = p.parse_args()

    with open(args.csv, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            usuari = login(fila["nom"], fila["cognom"])
            clau = contrasenya()
            ordres = [
                ["groupadd", "-f", fila["grup"]],
                ["useradd", "-m", "-s", "/bin/bash", "-g", fila["grup"],
                 "-c", f"{fila['nom']} {fila['cognom']}", usuari],
            ]
            if args.aplica:
                for ordre in ordres:
                    subprocess.run(ordre, check=True)
                subprocess.run(["chpasswd"], input=f"{usuari}:{clau}", text=True, check=True)
                subprocess.run(["chage", "-d", "0", usuari], check=True)   # canviar en el primer login
            else:
                for ordre in ordres:
                    print("SIMULA:", shlex.join(ordre))
            print(f"{usuari:<12} {clau}")
    ```

    - `secrets` genera valors aleatoris segurs per a contrasenyes (`random` no ho és).
    - `unicodedata.normalize("NFKD", ...)` separa les lletres dels accents per a poder-los llevar: *Bàñez* → *banez*.
    - `chage -d 0` obliga a canviar la contrasenya en el primer inici de sessió.
    - Amb `--aplica` cal executar-lo com a root: `sudo python3 alta_usuaris.py alumnes.csv --aplica`.

    ```console
    $ python3 alta_usuaris.py alumnes.csv
    SIMULA: groupadd -f asir2
    SIMULA: useradd -m -s /bin/bash -g asir2 -c 'Maria Josep Pons Ferrer' mjpons
    mjpons       gxJ5TWasgjmb
    ...
    ```

### 19. Ordenar la carpeta de descàrregues

Mou cada fitxer d'una carpeta a una subcarpeta segons el seu tipus (imatges, documents, comprimits...). Si ja hi ha un fitxer amb el mateix nom, no l'ha de xafar.

??? success "Solució"

    ```python title="ordena_descarregues.py"
    #!/usr/bin/env python3
    """Mou els fitxers d'una carpeta a subcarpetes segons el tipus."""
    import shutil
    import sys
    from pathlib import Path

    TIPUS = {
        "Imatges": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
        "Documents": {".pdf", ".docx", ".odt", ".txt", ".md", ".xlsx", ".pptx"},
        "Comprimits": {".zip", ".tar", ".gz", ".7z", ".rar"},
        "Instal·ladors": {".deb", ".iso", ".appimage", ".exe", ".msi"},
    }

    def categoria(fitxer):
        for nom, extensions in TIPUS.items():
            if fitxer.suffix.lower() in extensions:
                return nom
        return "Altres"

    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Descàrregues"
    moguts = 0
    for fitxer in carpeta.iterdir():
        if not fitxer.is_file() or fitxer.name.startswith("."):
            continue
        desti = carpeta / categoria(fitxer)
        desti.mkdir(exist_ok=True)
        nou = desti / fitxer.name
        n = 1
        while nou.exists():                     # no xafar si ja n'hi ha un amb el mateix nom
            nou = desti / f"{fitxer.stem}_{n}{fitxer.suffix}"
            n += 1
        shutil.move(fitxer, nou)
        moguts += 1
        print(f"{fitxer.name} → {desti.name}/")

    print(f"\n{moguts} fitxers ordenats")
    ```

    La taula `TIPUS` fa que afegir una categoria nova siga canviar dades, no codi. `suffix.lower()` fa que `.JPG` i `.jpg` es tracten igual.

### 20. Analitzar els intents d'accés SSH

Està resolt en el [tema 9](09-sysadmin.md#exemple-complet-analitzar-intents-dacces-ssh-fallits).
