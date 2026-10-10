# 10. Classes i objectes

Una **classe** és un motle; un **objecte** és una cosa feta amb eixe motle. La classe agrupa dades (**atributs**) i les funcions que treballen amb elles (**mètodes**).

## Definir una classe

```python
class Servidor:
    """Un servidor de la xarxa."""

    def __init__(self, nom, ip, ram_gb=4):     # constructor
        self.nom = nom                           # atributs
        self.ip = ip
        self.ram_gb = ram_gb
        self.serveis = []

    def afig_servei(self, servei):              # mètode
        if servei not in self.serveis:
            self.serveis.append(servei)

    def __str__(self):                           # com es mostra amb print
        return f"{self.nom} ({self.ip}) — {', '.join(self.serveis) or 'sense serveis'}"


web = Servidor("web01", "10.0.0.10", ram_gb=8)    # crear un objecte
web.afig_servei("nginx")
web.afig_servei("php-fpm")
print(web)          # web01 (10.0.0.10) — nginx, php-fpm
print(web.ram_gb)   # 8
```

- `__init__` s'executa en crear l'objecte i hi inicialitza els atributs.
- `self` és l'objecte mateix. Tot mètode el rep com a primer paràmetre (però no el passes en cridar-lo).
- `__str__` defineix el text que mostra `print(objecte)`.

## Atributs de classe

Compartits per tots els objectes:

```python
class Servidor:
    total = 0                # de la classe

    def __init__(self, nom):
        self.nom = nom       # de cada objecte
        Servidor.total += 1
```

## Herència

Una classe filla rep tot el que té la mare i hi pot afegir o canviar coses:

```python
class ServidorBD(Servidor):
    def __init__(self, nom, ip, motor="mariadb"):
        super().__init__(nom, ip)        # crida el constructor de la mare
        self.motor = motor
        self.afig_servei(motor)

    def backup(self):
        print(f"Fent mysqldump de {self.nom}")


db = ServidorBD("db01", "10.0.0.20")
print(db)           # db01 (10.0.0.20) — mariadb  (mètode heretat)
db.backup()
isinstance(db, Servidor)   # True
```

## Propietats

Per a validar en assignar un atribut:

```python
class Usuari:
    def __init__(self, nom, uid):
        self.nom = nom
        self.uid = uid           # passa pel setter de baix

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, valor):
        if valor < 0:
            raise ValueError("L'UID no pot ser negatiu")
        self._uid = valor

    @property
    def es_sistema(self):
        return self.uid < 1000

u = Usuari("jose", 1000)
u.es_sistema        # False (es crida sense parèntesis)
```

## Dataclasses: classes de dades sense escriure tant

```python
from dataclasses import dataclass, field

@dataclass
class Disc:
    punt: str
    total_gb: float
    usat_gb: float

    @property
    def percent(self):
        return self.usat_gb / self.total_gb * 100

d = Disc("/", 50, 41)
print(d)                 # Disc(punt='/', total_gb=50, usat_gb=41)
print(f"{d.percent:.0f} %")
```

`@dataclass` genera automàticament `__init__`, `__repr__` i la comparació `==`.

## Quan usar classes

Per a scripts curts, funcions i diccionaris són suficients. Les classes compensen quan tens diverses "coses" del mateix tipus amb dades i comportament propis (servidors, usuaris, dispositius...) o quan el programa creix i vols organitzar-lo.
