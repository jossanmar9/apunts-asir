# 10. Classes i objectes

## La idea

Fins ara has guardat dades en variables, llistes i diccionaris, i has fet funcions que treballen amb elles. La **programació orientada a objectes** (POO) ajunta les dues coses: **dades i funcions en un mateix paquet**.

Una analogia:

- Una **classe** és com el **plànol** d'una casa: diu quines parts té i què es pot fer amb ella.
- Un **objecte** és una **casa concreta** construïda amb eixe plànol. Amb el mateix plànol pots fer moltes cases, cada una amb el seu color, la seua adreça...

En informàtica: la classe `Servidor` descriu què té un servidor (nom, IP, memòria) i què pot fer (afegir un servei). Cada servidor concret (`web01`, `db01`) és un objecte.

| Concepte | Què és | Exemple |
| -------- | ------ | ------- |
| **Classe** | el motle, el plànol | `Servidor` |
| **Objecte** | una cosa feta amb el motle | `web01` |
| **Atribut** | una dada de l'objecte | `web01.ip` |
| **Mètode** | una funció de l'objecte | `web01.afig_servei("nginx")` |

## Crear una classe

```python
class Servidor:                              # 1. el nom de la classe, amb majúscula

    def __init__(self, nom, ip):             # 2. es crida en crear un objecte
        self.nom = nom                       #    guarda les dades de l'objecte
        self.ip = ip
        self.serveis = []                    #    llista buida per a començar

    def afig_servei(self, servei):           # 3. un mètode: una funció de la classe
        self.serveis.append(servei)

    def mostra(self):                        # un altre mètode
        print(f"{self.nom} ({self.ip}): {self.serveis}")
```

**Les parts:**

- `class Servidor:` → crea la classe. Per costum, el nom comença per majúscula.
- `__init__` → una funció especial que s'executa **automàticament** cada vegada que crees un objecte. Serveix per a donar-li els valors inicials. (Són dos guions baixos a cada costat.)
- `self` → vol dir "**este objecte**". `self.nom` és "el nom d'este servidor". Tots els mètodes el reben com a primer paràmetre.

## Crear objectes i usar-los

```python
web = Servidor("web01", "10.0.0.10")       # crear un objecte (es crida __init__)
db = Servidor("db01", "10.0.0.20")         # un altre objecte, amb les seues dades

web.afig_servei("nginx")                   # cridar un mètode
web.afig_servei("php")
db.afig_servei("mariadb")

web.mostra()        # web01 (10.0.0.10): ['nginx', 'php']
db.mostra()         # db01 (10.0.0.20): ['mariadb']

print(web.ip)       # 10.0.0.10 → llegir un atribut
```

Fixa't que **no passes `self`** en cridar el mètode: Python el posa sol. `web.afig_servei("nginx")` és com si fera `Servidor.afig_servei(web, "nginx")`.

Cada objecte té **les seues pròpies dades**: afegir un servei a `web` no l'afig a `db`.

## Com es mostra un objecte: `__str__`

Si fas `print(web)`, per defecte ix una cosa lletja com `<__main__.Servidor object at 0x7f...>`. Amb el mètode especial `__str__` decidixes què es mostra:

```python
class Servidor:
    def __init__(self, nom, ip):
        self.nom = nom
        self.ip = ip

    def __str__(self):
        return f"Servidor {self.nom} ({self.ip})"

web = Servidor("web01", "10.0.0.10")
print(web)          # Servidor web01 (10.0.0.10)
```

## Herència: una classe basada en una altra

Una classe pot **heretar** d'una altra: té tot el que té la "mare" i pot afegir coses noves.

```python
class Servidor:
    def __init__(self, nom, ip):
        self.nom = nom
        self.ip = ip

    def __str__(self):
        return f"{self.nom} ({self.ip})"


class ServidorBD(Servidor):                  # ServidorBD hereta de Servidor
    def __init__(self, nom, ip, motor):
        super().__init__(nom, ip)            # crida l'__init__ de la mare
        self.motor = motor                   # i afig una dada nova

    def copia_seguretat(self):               # i un mètode nou
        print(f"Fent còpia de {self.nom} ({self.motor})")


db = ServidorBD("db01", "10.0.0.20", "mariadb")
print(db)                   # db01 (10.0.0.20)  → __str__ heretat de la mare
db.copia_seguretat()        # Fent còpia de db01 (mariadb)
```

- `class ServidorBD(Servidor):` → el nom de la mare entre parèntesis.
- `super().__init__(...)` → aprofita el que ja fa la mare en lloc de repetir-ho.

## Una forma ràpida: `@dataclass`

Si la classe és sobretot per a guardar dades, `@dataclass` t'estalvia escriure l'`__init__`:

```python
from dataclasses import dataclass

@dataclass
class Disc:
    punt: str
    total_gb: float
    usat_gb: float

    def percentatge(self):
        return self.usat_gb / self.total_gb * 100


d = Disc("/", 50, 41)
print(d)                              # Disc(punt='/', total_gb=50, usat_gb=41)
print(f"{d.percentatge():.0f} %")     # 82 %
```

## Quan usar classes?

Per a scripts curts, **no cal**: funcions, llistes i diccionaris són suficients. Les classes valen la pena quan tens moltes "coses" del mateix tipus, cadascuna amb les seues dades i accions (servidors, usuaris, dispositius...).

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `TypeError: __init__() missing 1 required positional argument` | No has passat totes les dades en crear l'objecte | Revisa els paràmetres de `__init__` |
| `NameError: name 'nom' is not defined` dins d'un mètode | T'has oblidat de `self.` | `self.nom` |
| `TypeError: ... takes 1 positional argument but 2 were given` | Falta `self` en la definició del mètode | `def metode(self, ...)` |
| `_init_` no s'executa | Són **dos** guions baixos | `__init__` |

!!! success "Per a l'examen"
    ```python
    class Nom:
        def __init__(self, a, b):     # en crear l'objecte
            self.a = a                # atributs
            self.b = b

        def metode(self, x):          # self sempre el primer
            return self.a + x

        def __str__(self):            # el que mostra print()
            return f"Nom({self.a})"

    obj = Nom(1, 2)                   # crear (sense passar self)
    obj.metode(5)                     # cridar mètode
    obj.a                             # llegir atribut

    class Filla(Nom):                 # herència
        def __init__(self, a, b, c):
            super().__init__(a, b)
            self.c = c
    ```
