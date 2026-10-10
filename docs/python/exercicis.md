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
    grau = float(input("Temperatura: "))                        # float: pot tindre decimals
    unitat = input("En quina unitat està? (C/F): ").strip().upper()   # lleva espais i passa a majúscula

    if unitat == "C":
        fahrenheit = grau * 9 / 5 + 32                          # fórmula de C a F
        print(f"{grau} °C = {fahrenheit:.1f} °F")               # .1f → 1 decimal
    elif unitat == "F":
        celsius = (grau - 32) * 5 / 9                           # fórmula de F a C
        print(f"{grau} °F = {celsius:.1f} °C")
    else:
        print("Unitat desconeguda")
    ```

    `.strip().upper()` accepta `c`, `C` o ` c ` igual.

### 2. Estadística de notes

Demana notes fins que l'usuari prema Intro sense escriure res. Mostra la mitjana i quants suspesos, aprovats, notables i excel·lents hi ha, amb el percentatge.

??? success "Solució"

    ```python title="notes.py"
    notes = []                                       # llista buida on guardarem les notes

    # Demanem notes fins que l'usuari prema Intro sense escriure res
    while True:
        text = input("Nota (Intro per a acabar): ")
        if text == "":                               # si no ha escrit res...
            break                                    # ...acabem
        nota = float(text)
        if 0 <= nota <= 10:
            notes.append(nota)                       # afegim la nota a la llista
        else:
            print("La nota ha d'estar entre 0 i 10")

    if not notes:                                    # si la llista està buida
        print("No has introduït cap nota")
    else:
        # Diccionari per a comptar quantes notes hi ha de cada categoria
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

        mitjana = sum(notes) / len(notes)
        print(f"\nAlumnes: {len(notes)}  Mitjana: {mitjana:.2f}")
        for nom, quants in categories.items():
            percentatge = quants / len(notes)
            print(f"{nom:<11}{quants:>3}  ({percentatge:.0%})")   # :.0% → percentatge sense decimals
    ```

    - `while True` amb `break` repetix fins que l'usuari deixa la resposta buida.
    - Un diccionari fa de comptador: una clau per categoria i el valor és quantes n'hi ha.
    - `{x:.0%}` mostra un número com 0.4 en forma de percentatge (40%).

### 3. Any de traspàs

Fes una funció que diga si un any és de traspàs.

??? success "Solució"

    ```python title="traspas.py"
    def es_traspas(any_):
        """Torna True si l'any és de traspàs.

        Regla: divisible per 4, EXCEPTE els acabats en 00,
        que només ho són si també són divisibles per 400.
        """
        return any_ % 4 == 0 and (any_ % 100 != 0 or any_ % 400 == 0)

    for a in (1900, 2000, 2024, 2026):
        if es_traspas(a):
            print(a, "és de traspàs")
        else:
            print(a, "no és de traspàs")
    ```

    La regla completa: divisible per 4, **excepte** els anys acabats en 00, que només ho són si són divisibles per 400 (2000 sí, 1900 no).

### 4. Màxim comú divisor

Calcula el MCD de dos números amb l'algorisme d'Euclides, i amb ell el mínim comú múltiple.

??? success "Solució"

    ```python title="mcd.py"
    def mcd(a, b):
        """Màxim comú divisor amb l'algorisme d'Euclides."""
        # Mentre b no siga 0: a passa a ser b, i b passa a ser el residu de a / b
        while b != 0:
            a, b = b, a % b          # les dues assignacions alhora
        return a                     # quan b és 0, a és el MCD

    def mcm(a, b):
        """Mínim comú múltiple: a * b / mcd(a, b)."""
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
        """n! = 1 * 2 * 3 * ... * n, amb un bucle."""
        resultat = 1
        for i in range(2, n + 1):    # de 2 fins a n (inclòs)
            resultat *= i            # multiplica pel següent
        return resultat

    def factorial_recursiu(n):
        """n! = n * (n-1)!, la funció es crida a si mateixa."""
        if n <= 1:                   # cas base: 0! = 1! = 1
            return 1
        return n * factorial_recursiu(n - 1)

    def combinatori(n, m):
        """Formes de triar m elements de n: n! / (m! * (n-m)!)"""
        return factorial_iteratiu(n) // (factorial_iteratiu(m) * factorial_iteratiu(n - m))

    print(factorial_iteratiu(5), factorial_recursiu(5))   # 120 120
    print(combinatori(49, 6))                             # 13983816 (combinacions de la primitiva)
    ```

    La versió recursiva és més semblant a la definició matemàtica, però per a números molt grans (més de ~1000) supera el límit de recursió de Python. La iterativa no té eixe problema.

### 6. Fibonacci

Torna els *n* primers termes de la successió de Fibonacci (cada terme és la suma dels dos anteriors).

??? success "Solució"

    ```python title="fibonacci.py"
    def fibonacci(n):
        """Torna una llista amb els n primers termes de Fibonacci."""
        termes = []
        a, b = 0, 1                  # els dos primers termes
        for _ in range(n):           # _ perquè no necessitem el número de volta
            termes.append(a)
            a, b = b, a + b          # el següent és la suma dels dos anteriors
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

    # Invertir sense [::-1]: posem cada lletra DAVANT de les que ja tenim
    invertit = ""
    for lletra in text:
        invertit = lletra + invertit

    # Comptar vocals: recorrem el text en minúscules i comptem les que són vocal
    vocals = 0
    for c in text.lower():
        if c in "aeiouàèéíòóúü":
            vocals += 1

    print(f"Al revés:   {invertit}")
    print(f"Majúscules: {text.upper()}")
    print(f"Longitud:   {len(text)}  Vocals: {vocals}")

    # Palíndrom: es llig igual al revés (sense comptar espais ni majúscules)
    net = text.lower().replace(" ", "")
    if net == net[::-1]:
        print("És un palíndrom")
    else:
        print("No és un palíndrom")
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
            break                    # el 0 indica que s'ha acabat
        nums.append(n)

    if nums:                         # si s'ha escrit almenys un número
        parells = 0
        senars = 0
        for n in nums:
            if n % 2 == 0:           # residu 0 en dividir per 2 → parell
                parells += n
            else:
                senars += n
        print(f"Suma: {sum(nums)}  Mitjana: {sum(nums) / len(nums):.2f}  Major: {max(nums)}")
        print(f"Suma dels parells: {parells}  Suma dels senars: {senars}")
    ```

    Per a saber si un número és parell es mira el residu de dividir-lo per 2: `n % 2 == 0`.

### 9. Tipus de triangle

Demana tres costats, comprova que formen un triangle i diu si és equilàter, isòsceles o escalé, amb la seua àrea.

??? success "Solució"

    ```python title="triangle.py"
    # Demanem els 3 costats i els ordenem de menor a major (a <= b <= c)
    costats = []
    for i in (1, 2, 3):
        costats.append(float(input(f"Costat {i}: ")))
    a, b, c = sorted(costats)

    # Perquè siga un triangle, els dos menuts han de sumar més que el gran
    if a + b <= c:
        print("Amb eixos costats no es pot fer un triangle")
    else:
        if a == b == c:
            tipus = "equilàter"      # tres iguals
        elif a == b or b == c:
            tipus = "isòsceles"      # dos iguals
        else:
            tipus = "escalé"         # tots diferents

        # Àrea amb la fórmula d'Heró (només cal saber els costats)
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5     # ** 0.5 = arrel quadrada
        print(f"Triangle {tipus}, àrea {area:.2f}")
    ```

    Ordenar els costats simplifica les comprovacions: n'hi ha prou amb mirar si els dos menuts sumen més que el gran.

### 10. Equació de segon grau

Resol *ax² + bx + c = 0* (només solucions reals).

??? success "Solució"

    ```python title="equacio.py"
    import math                      # per a math.sqrt (arrel quadrada)

    print("ax² + bx + c = 0")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    if a == 0:
        print("No és de segon grau")
    else:
        disc = b ** 2 - 4 * a * c    # el discriminant diu quantes solucions hi ha
        if disc > 0:                 # dues solucions
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            x2 = (-b - math.sqrt(disc)) / (2 * a)
            print(f"Dues solucions: {x1:g} i {x2:g}")
        elif disc == 0:              # una solució
            print(f"Una solució doble: {-b / (2 * a):g}")
        else:                        # disc negatiu: l'arrel no existix en els reals
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

    # Comprovem que ens han passat el nom del fitxer
    if len(sys.argv) != 2:
        sys.exit(f"Ús: {sys.argv[0]} <fitxer>")

    linies = paraules = caracters = 0        # tres comptadors a 0
    try:
        with open(sys.argv[1], encoding="utf-8") as f:
            for linia in f:                  # recorrem línia a línia
                linies += 1
                paraules += len(linia.split())   # split() talla en paraules
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

    FITXER = Path("agenda.json")             # on es guarden les dades

    def carrega():
        """Llig l'agenda del fitxer. Si no existix, torna una agenda buida."""
        if FITXER.exists():
            return json.loads(FITXER.read_text(encoding="utf-8"))
        return {}

    def guarda(agenda):
        """Guarda l'agenda en el fitxer en format JSON."""
        FITXER.write_text(json.dumps(agenda, indent=2, ensure_ascii=False), encoding="utf-8")

    def main():
        agenda = carrega()                   # diccionari: nom → {telefon, correu}
        while True:
            print("\n1) Afegir  2) Buscar  3) Llistar  4) Esborrar  5) Eixir")
            opcio = input("> ").strip()
            match opcio:
                case "1":
                    nom = input("Nom: ").strip()
                    telefon = input("Telèfon: ")
                    correu = input("Correu: ")
                    agenda[nom] = {"telefon": telefon, "correu": correu}
                    guarda(agenda)
                case "2":
                    text = input("Buscar: ").lower()
                    for nom, dades in agenda.items():
                        if text in nom.lower():          # busca sense distingir majúscules
                            print(f"{nom}: {dades['telefon']}  {dades['correu']}")
                case "3":
                    for nom in sorted(agenda):           # en ordre alfabètic
                        print(f"{nom:<20}{agenda[nom]['telefon']:<12}{agenda[nom]['correu']}")
                case "4":
                    nom = input("Nom a esborrar: ")
                    if nom in agenda:
                        del agenda[nom]
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
    - `if nom in agenda` comprova que el contacte existix abans d'esborrar-lo amb `del`.
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
        """'192.168.10.77' → un sol número de 32 bits."""
        a, b, c, d = (int(x) for x in ip.split("."))
        # Cada octet es desplaça (<<) a la seua posició dins dels 32 bits
        return (a << 24) | (b << 16) | (c << 8) | d

    def int_a_ip(n):
        """Un número de 32 bits → '192.168.10.77'."""
        # Traiem cada octet desplaçant cap a la dreta i quedant-nos amb 8 bits (& 255)
        return ".".join(str((n >> despl) & 255) for despl in (24, 16, 8, 0))

    def calcula(cidr):
        ip, prefix = cidr.split("/")         # "192.168.10.77/26" → "192.168.10.77" i "26"
        prefix = int(prefix)
        # Màscara: tants 1 com diga el prefix, i la resta 0
        mascara = (0xFFFFFFFF << (32 - prefix)) & 0xFFFFFFFF
        xarxa = ip_a_int(ip) & mascara                      # posa a 0 els bits de host
        broadcast = xarxa | (~mascara & 0xFFFFFFFF)         # posa a 1 els bits de host
        return {
            "Màscara": int_a_ip(mascara),
            "Xarxa": int_a_ip(xarxa),
            "Broadcast": int_a_ip(broadcast),
            "Primer host": int_a_ip(xarxa + 1),
            "Últim host": int_a_ip(broadcast - 1),
            "Hosts": 2 ** (32 - prefix) - 2,                # totes menys xarxa i broadcast
        }

    cidr = input("IP/prefix (p. ex. 192.168.10.77/26): ")
    for clau, valor in calcula(cidr).items():
        print(f"{clau:<12} {valor}")

    # Comprovació amb el mòdul estàndard ipaddress
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
        """Ordena una llista pel mètode de la bombolla."""
        v = nums.copy()                      # treballem sobre una còpia
        n = len(v)
        for i in range(n - 1):               # n-1 passades
            canvis = False
            for j in range(n - 1 - i):       # compara cada parella de veïns
                if v[j] > v[j + 1]:          # si estan en mal ordre...
                    v[j], v[j + 1] = v[j + 1], v[j]   # ...els intercanvia
                    canvis = True
            if not canvis:                   # si no hi ha hagut cap canvi, ja està ordenada
                break
        return v

    def cerca_binaria(v, buscat):
        """Torna la posició de buscat en la llista ORDENADA v, o -1 si no hi és."""
        esq, dre = 0, len(v) - 1             # busquem entre esq i dre
        while esq <= dre:
            mig = (esq + dre) // 2           # mirem el del mig
            if v[mig] == buscat:
                return mig
            if v[mig] < buscat:
                esq = mig + 1                # està en la meitat de la dreta
            else:
                dre = mig - 1                # està en la meitat de l'esquerra
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
        """Les files passen a ser columnes."""
        files = len(m)
        columnes = len(m[0])
        resultat = []
        for c in range(columnes):
            nova_fila = []
            for f in range(files):
                nova_fila.append(m[f][c])
            resultat.append(nova_fila)
        return resultat

    def multiplica(a, b):
        """Multiplica dues matrius quadrades: cada element és fila de a × columna de b."""
        n = len(a)
        resultat = []
        for i in range(n):
            fila = []
            for j in range(n):
                suma = 0
                for k in range(n):
                    suma += a[i][k] * b[k][j]
                fila.append(suma)
            resultat.append(fila)
        return resultat

    def mostra(m):
        for fila in m:
            print(" ".join(f"{x:4}" for x in fila))

    mostra(transposa([[1, 2, 3], [4, 5, 6]]))
    print()
    mostra(multiplica([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    ```

    Per a multiplicar matrius calen tres bucles: `i` recorre les files del resultat, `j` les columnes, i `k` fa la suma de *fila de a × columna de b*.

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

    # El llindar es pot passar per argument; si no, 80 %
    LLINDAR = int(sys.argv[1]) if len(sys.argv) > 1 else 80

    # df -P llista els sistemes de fitxers; -x exclou els virtuals que no interessen
    r = subprocess.run(["df", "-P", "-x", "tmpfs", "-x", "devtmpfs", "-x", "squashfs", "-x", "overlay"],
                       capture_output=True, text=True)
    # Ens quedem amb l'última columna (punt de muntatge), saltant la capçalera
    punts = [linia.split()[-1] for linia in r.stdout.splitlines()[1:]]

    alertes = 0
    print(f"{'PUNT':<20}{'TOTAL':>9}{'USAT':>9}{'%':>6}")
    for punt in punts:
        total, usat, _ = shutil.disk_usage(punt)     # espai en bytes
        percent = usat / total * 100
        if percent >= LLINDAR:
            marca = "  ⚠️"
            alertes += 1
        else:
            marca = ""
        print(f"{punt:<20}{total / 1e9:>8.1f}G{usat / 1e9:>8.1f}G{percent:>5.0f}%{marca}")

    # Codi d'eixida: 1 si hi ha alguna alerta (útil per a cron o altres scripts)
    sys.exit(1 if alertes else 0)
    ```

    `df -P` mostra una línia per cada disc; d'ella només traiem el punt de muntatge (l'última columna). Les xifres les calcula `shutil.disk_usage`.

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

    # Arguments: origen, destí i (opcional) quantes còpies conservar
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("origen", type=Path)
    p.add_argument("desti", type=Path)
    p.add_argument("-k", "--conserva", type=int, default=7, help="còpies a conservar (7)")
    args = p.parse_args()

    if not args.origen.is_dir():
        p.error(f"{args.origen} no és un directori")       # mostra l'error i ix
    args.desti.mkdir(parents=True, exist_ok=True)          # crea el destí si cal

    # Nom amb data i hora: Documents_20261010_174118
    nom = f"{args.origen.name}_{datetime.now():%Y%m%d_%H%M%S}"
    fitxer = shutil.make_archive(str(args.desti / nom), "gztar", root_dir=args.origen)
    print(f"Creat {fitxer} ({Path(fitxer).stat().st_size / 1024:.1f} KiB)")

    # Rotació: llistem les còpies ordenades (per la data del nom) i esborrem les velles
    copies = sorted(args.desti.glob(f"{args.origen.name}_*.tar.gz"))
    for vella in copies[:-args.conserva]:                  # totes menys les N últimes
        vella.unlink()                                     # esborrar el fitxer
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
        """Bàñez → Banez"""
        return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()

    def login(nom, cognom):
        """Inicials del nom + primer cognom: Maria Josep, Pons Ferrer → mjpons"""
        inicials = "".join(paraula[0] for paraula in nom.split())
        return sense_accents(inicials + cognom.split()[0]).lower()

    def contrasenya(longitud=12):
        """Contrasenya aleatòria segura amb lletres i números."""
        caracters = string.ascii_letters + string.digits
        return "".join(secrets.choice(caracters) for _ in range(longitud))

    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("csv")
    p.add_argument("--aplica", action="store_true", help="crea'ls de veritat (si no, només simula)")
    args = p.parse_args()

    with open(args.csv, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):                     # cada fila: {"nom":..., "cognom":..., "grup":...}
            usuari = login(fila["nom"], fila["cognom"])
            clau = contrasenya()
            ordres = [
                ["groupadd", "-f", fila["grup"]],          # crea el grup (-f: sense error si ja existix)
                ["useradd", "-m", "-s", "/bin/bash", "-g", fila["grup"],
                 "-c", f"{fila['nom']} {fila['cognom']}", usuari],
            ]
            if args.aplica:                                # mode real (cal ser root)
                for ordre in ordres:
                    subprocess.run(ordre, check=True)
                subprocess.run(["chpasswd"], input=f"{usuari}:{clau}", text=True, check=True)
                subprocess.run(["chage", "-d", "0", usuari], check=True)   # canviar en el primer login
            else:                                          # mode simulació: només mostra
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

    # Quines extensions van a cada carpeta
    TIPUS = {
        "Imatges": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
        "Documents": {".pdf", ".docx", ".odt", ".txt", ".md", ".xlsx", ".pptx"},
        "Comprimits": {".zip", ".tar", ".gz", ".7z", ".rar"},
        "Instal·ladors": {".deb", ".iso", ".appimage", ".exe", ".msi"},
    }

    def categoria(fitxer):
        """Torna el nom de la carpeta on ha d'anar el fitxer."""
        for nom, extensions in TIPUS.items():
            if fitxer.suffix.lower() in extensions:        # .JPG i .jpg compten igual
                return nom
        return "Altres"

    # Carpeta: la passada per argument, o ~/Descàrregues
    carpeta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.home() / "Descàrregues"

    moguts = 0
    for fitxer in carpeta.iterdir():
        if not fitxer.is_file() or fitxer.name.startswith("."):   # saltem carpetes i ocults
            continue
        desti = carpeta / categoria(fitxer)
        desti.mkdir(exist_ok=True)                         # crea la subcarpeta si no existix

        # Si ja hi ha un fitxer amb el mateix nom, afegim _1, _2... per no xafar-lo
        nou = desti / fitxer.name
        n = 1
        while nou.exists():
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
