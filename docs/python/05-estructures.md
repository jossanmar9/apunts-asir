# 5. Estructures de dades

| Tipus | Exemple | Ordenada | Mutable | Repetits |
| ----- | ------- | :------: | :-----: | :------: |
| `list` | `[1, 2, 2]` | ✅ | ✅ | ✅ |
| `tuple` | `(1, 2, 2)` | ✅ | ❌ | ✅ |
| `dict` | `{"a": 1}` | ✅ (ordre d'inserció) | ✅ | claus no |
| `set` | `{1, 2}` | ❌ | ✅ | ❌ |

## Llistes

```python
serveis = ["ssh", "nginx", "cron"]

serveis[0]              # 'ssh'
serveis[-1]             # 'cron'
serveis[1:]             # ['nginx', 'cron']
len(serveis)            # 3
"ssh" in serveis        # True

serveis.append("mariadb")      # afig al final
serveis.insert(0, "ufw")       # afig en una posició
serveis.extend(["a", "b"])     # afig diversos
serveis.remove("cron")         # esborra per valor (el primer)
ultim = serveis.pop()          # trau l'últim i el torna
del serveis[0]                 # esborra per posició
serveis.index("nginx")         # posició
serveis.count("ssh")           # quantes vegades
serveis.sort()                 # ordena la llista (la modifica)
ordenada = sorted(serveis)     # torna una còpia ordenada
serveis.reverse()
```

```python
nums = [4, 8, 15, 16, 23, 42]
sum(nums), max(nums), min(nums)   # 108 42 4
sum(nums) / len(nums)             # mitjana
sorted(nums, reverse=True)
sorted(noms, key=len)             # ordenar per longitud
sorted(noms, key=str.lower)       # sense distingir majúscules
```

### Llistes de llistes

```python
matriu = [[1, 2, 3],
          [4, 5, 6]]
matriu[1][2]          # 6 → fila 1, columna 2
for fila in matriu:
    print(" ".join(str(x) for x in fila))
```

## Comprensions

Crear una llista nova a partir d'una altra en una sola línia:

```python
quadrats = [x ** 2 for x in range(10)]
parells  = [x for x in nums if x % 2 == 0]
noms     = [l.split(":")[0] for l in open("/etc/passwd")]
majus    = [s.upper() for s in serveis]
```

Es llig: "*x al quadrat **per a cada** x **de** range(10)*".

## Tuples

Com una llista però **no es pot modificar**. S'usen per a dades que van juntes:

```python
punt = (3, 5)
usuari = ("ana", 1000, "/bin/bash")

nom, uid, shell = usuari       # desempaquetar
x, *resta = [1, 2, 3, 4]       # x=1, resta=[2, 3, 4]
```

Una funció que "torna diversos valors" en realitat torna una tupla.

## Diccionaris

Parelles **clau → valor**. Busques per clau, no per posició.

```python
ports = {"ssh": 22, "http": 80, "https": 443}

ports["ssh"]                  # 22
ports["ftp"]                  # KeyError!
ports.get("ftp")              # None (no dona error)
ports.get("ftp", 21)          # 21 (valor per defecte)
ports["dns"] = 53             # afig o modifica
del ports["http"]             # esborra
"ssh" in ports                # True (busca en les CLAUS)
len(ports)

for servei, port in ports.items():
    print(f"{servei:<8}{port}")

list(ports.keys())            # ['ssh', 'https', 'dns']
list(ports.values())          # [22, 443, 53]
```

### Comptar coses (molt habitual)

```python
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.1"]

compte = {}
for ip in ips:
    compte[ip] = compte.get(ip, 0) + 1
# {'10.0.0.1': 3, '10.0.0.2': 1}

# O amb la biblioteca estàndard:
from collections import Counter
Counter(ips).most_common(1)   # [('10.0.0.1', 3)]
```

### Diccionaris niats

```python
servidors = {
    "web01": {"ip": "10.0.0.10", "rols": ["nginx", "php"]},
    "db01":  {"ip": "10.0.0.20", "rols": ["mariadb"]},
}
servidors["web01"]["ip"]          # '10.0.0.10'
for nom, info in servidors.items():
    print(nom, info["ip"], ", ".join(info["rols"]))
```

Comprensió de diccionari: `{s: len(s) for s in serveis}`.

## Conjunts

Sense ordre i **sense repetits**. Ideals per a llevar duplicats i comparar grups:

```python
a = {"ssh", "nginx", "cron"}
b = {"ssh", "mariadb"}

a | b      # unió: tots
a & b      # intersecció: {'ssh'}
a - b      # diferència: {'nginx', 'cron'}
a ^ b      # els que estan en un però no en tots dos

unics = set(ips)        # llevar duplicats
a.add("ufw")
a.discard("cron")       # no dona error si no hi és
```

!!! example "Quins paquets falten?"
    ```python
    necessaris = {"git", "curl", "vim", "htop"}
    instalats = {"git", "vim"}
    print(necessaris - instalats)   # {'curl', 'htop'}
    ```

## Compte amb les còpies

```python
a = [1, 2, 3]
b = a           # b NO és una còpia: és el MATEIX objecte
b.append(4)
print(a)        # [1, 2, 3, 4] 😱

c = a.copy()    # còpia de veritat (o a[:] o list(a))
c.append(5)
print(a)        # [1, 2, 3, 4]
```

Per a llistes o diccionaris niats, `copy.deepcopy(x)`.
