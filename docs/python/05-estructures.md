# 5. Estructures de dades

Una variable normal guarda **un** valor. Les **estructures de dades** guarden **molts valors** junts. Python en té quatre:

| Tipus | Com s'escriu | Per a què | Exemple |
| ----- | ------------ | --------- | ------- |
| **Llista** | `[ ]` | una col·lecció ordenada que pot canviar | llista de serveis |
| **Tupla** | `( )` | com una llista però que no pot canviar | unes coordenades |
| **Diccionari** | `{clau: valor}` | buscar per nom | port de cada servei |
| **Conjunt** | `{ }` | valors sense repetir | IPs úniques |

## Llistes

### Crear i llegir

```python
serveis = ["ssh", "nginx", "cron"]

serveis[0]          # 'ssh'    → la primera (es compta des de 0)
serveis[-1]         # 'cron'   → l'última
serveis[0:2]        # ['ssh', 'nginx'] → un tros
len(serveis)        # 3        → quants elements té
"ssh" in serveis    # True     → hi és?
```

Funciona igual que amb les lletres d'un text ([tema 3](03-cadenes.md)).

### Afegir, canviar i esborrar

```python
serveis.append("mariadb")     # afegir al final
serveis.insert(0, "ufw")      # afegir en una posició concreta
serveis[1] = "apache2"        # canviar el de la posició 1
serveis.remove("cron")        # esborrar per valor
ultim = serveis.pop()         # traure l'últim (i guardar-lo)
```

### Ordenar

```python
nums = [42, 7, 19, 3]
nums.sort()                     # ordena la llista → [3, 7, 19, 42]
nums.sort(reverse=True)         # de major a menor
ordenada = sorted(nums)         # crea una còpia ordenada (la original no canvia)
```

### Calcular coses

```python
notes = [7, 4, 9, 6]
sum(notes)                  # 26  → suma
max(notes)                  # 9   → la major
min(notes)                  # 4   → la menor
sum(notes) / len(notes)     # 6.5 → mitjana
```

### Recórrer-la

```python
for servei in serveis:
    print(servei)
```

### Construir una llista a poc a poc

Molt habitual: començar amb una llista buida i anar afegint:

```python
aprovats = []                    # llista buida
for nota in [7, 4, 9, 3, 6]:
    if nota >= 5:
        aprovats.append(nota)    # afegix les aprovades
print(aprovats)                  # [7, 9, 6]
```

### Comprensió de llistes: el mateix en una línia

```python
aprovats = [nota for nota in notes if nota >= 5]
dobles = [n * 2 for n in nums]
```

Es llig: "*`nota`, **per a cada** `nota` **de** `notes`, **si** `nota >= 5`*". És una forma curta del bucle anterior. No és obligatori usar-la: el bucle normal fa el mateix.

### Llistes dins de llistes (matrius)

```python
taula = [[1, 2, 3],
         [4, 5, 6]]
taula[1][2]          # 6 → fila 1, columna 2
```

## Tuples

Com una llista, però amb parèntesis i **no es pot modificar** després de crear-la. S'usa per a dades que van juntes i no han de canviar:

```python
punt = (3, 5)
usuari = ("ana", 1000, "/bin/bash")
```

### Desempaquetar: repartir els valors en variables

```python
nom, uid, shell = usuari
# nom = "ana", uid = 1000, shell = "/bin/bash"
```

Molt útil quan una funció torna diversos valors.

## Diccionaris

Un **diccionari** guarda parelles **clau → valor**. En compte de buscar per posició (0, 1, 2...), busques per **nom**. Com un diccionari de veritat: busques la paraula i trobes la definició.

```python
ports = {
    "ssh": 22,
    "http": 80,
    "https": 443,
}
```

### Llegir

```python
ports["ssh"]              # 22
ports["ftp"]              # ❌ KeyError: la clau no existix
ports.get("ftp")          # None (no dona error)
ports.get("ftp", 21)      # 21 → si no existix, torna el valor per defecte
"ssh" in ports            # True → existix la clau?
```

### Afegir, canviar, esborrar

```python
ports["dns"] = 53         # si no existix, l'afig; si existix, la canvia
del ports["http"]         # esborrar
```

### Recórrer

```python
for servei, port in ports.items():
    print(f"{servei} → {port}")

for servei in ports:              # només les claus
    print(servei)
```

| S'escriu | Torna |
| -------- | ----- |
| `d.keys()` | les claus |
| `d.values()` | els valors |
| `d.items()` | les parelles (clau, valor) |

### Exemple molt habitual: comptar coses

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.1"]

compte = {}                                # diccionari buit
for ip in ips:
    compte[ip] = compte.get(ip, 0) + 1     # suma 1 (si no existia, parteix de 0)

print(compte)    # {'10.0.0.1': 3, '10.0.0.2': 1}
```

La mateixa cosa amb una eina de Python que ja ho fa:

```python
from collections import Counter
compte = Counter(ips)
compte.most_common(1)      # [('10.0.0.1', 3)] → el que més es repetix
```

### Diccionaris dins de diccionaris

```python
servidors = {
    "web01": {"ip": "10.0.0.10", "ram": 8},
    "db01":  {"ip": "10.0.0.20", "ram": 16},
}
servidors["web01"]["ip"]     # '10.0.0.10'
```

## Conjunts

Un **conjunt** (`set`) és una col·lecció **sense repetits** i sense ordre. Serveix per a:

- **Llevar duplicats** d'una llista.
- **Comparar** dos grups.

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1"]
unics = set(ips)        # {'10.0.0.1', '10.0.0.2'}
len(unics)              # 2 IPs diferents
```

```python
necessaris = {"git", "curl", "vim"}
instalats = {"git", "vim", "htop"}

necessaris - instalats      # {'curl'}  → els que falten
necessaris & instalats      # {'git', 'vim'}  → els que estan en tots dos
necessaris | instalats      # tots junts, sense repetir
```

## ⚠️ Compte amb les còpies

```python
a = [1, 2, 3]
b = a            # ❌ b NO és una còpia: és un altre nom per a la MATEIXA llista
b.append(4)
print(a)         # [1, 2, 3, 4] → a també ha canviat!

c = a.copy()     # ✅ ara sí, una còpia independent
```

## Quina estructura use?

| Necessite... | Usa |
| ------------ | --- |
| una llista d'elements en ordre | **llista** `[ ]` |
| buscar un valor pel seu nom | **diccionari** `{ : }` |
| llevar repetits o comparar grups | **conjunt** `set()` |
| unes dades fixes que van juntes | **tupla** `( )` |

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `IndexError: list index out of range` | Posició que no existix | Va de 0 a `len(l) - 1` |
| `KeyError: 'ftp'` | Clau que no existix en el diccionari | `d.get("ftp")` o comprova `if "ftp" in d` |
| La llista original ha canviat | Has fet `b = a` | `b = a.copy()` |
| `l = l.sort()` deixa `l` en `None` | `.sort()` no torna res | Només `l.sort()` o `l = sorted(l)` |

!!! success "Per a l'examen"
    ```python
    l = [1, 2, 3]
    l[0]  l[-1]  len(l)  x in l
    l.append(x)  l.remove(x)  l.pop()  l.sort()
    sum(l)  max(l)  min(l)
    nova = [x for x in l if x > 1]

    d = {"a": 1}
    d["a"]  d.get("z", 0)  d["b"] = 2  del d["a"]
    for k, v in d.items(): ...
    d[k] = d.get(k, 0) + 1          # comptar

    set(l)                          # llevar repetits
    a - b   a & b   a | b           # diferència, intersecció, unió
    ```
