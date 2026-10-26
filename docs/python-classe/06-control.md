# UT3 · 1. Condicionals i bucles amb seguiment de valors

## Decidir amb `if`

Un bloc comença amb `:` i es delimita amb sagnat coherent. `if/elif/else` prova les condicions en ordre i executa el primer bloc que correspon. No és el mateix que diversos `if` independents, que poden executar més d'un bloc.

## Exemple resolt: estat d'una cua d'impressió

**Problema nou:** amb 0 documents la cua està buida; d'1 a 4, és curta; a partir de 5, és llarga. Una quantitat negativa és incoherent.

```python
documents = 4
if documents < 0:
    estat = "Dada incorrecta"
elif documents == 0:
    estat = "Buida"
elif documents <= 4:
    estat = "Curta"
else:
    estat = "Llarga"
print(estat)
```

**Resultat:** `Curta`. Prova -1, 0, 1, 4 i 5 per a cobrir errors i límits. En arribar a `documents <= 4`, ja saps que no és negatiu ni zero: les condicions anteriors també aporten informació.

## Repetir amb `while`: exemple resolt de tallar una cinta

Tenim 17 cm i volem fragments complets de 5 cm:

```python
restant = 17
fragments = 0
while restant >= 5:
    restant -= 5
    fragments += 1
print(f"Fragments: {fragments}; restant: {restant} cm")
```

| Volta | Restant abans | Restant després | Fragments |
| --- | --- | --- | --- |
| 1 | 17 | 12 | 1 |
| 2 | 12 | 7 | 2 |
| 3 | 7 | 2 | 3 |

La quarta comprovació és falsa; l'eixida és `Fragments: 3; restant: 2 cm`. La variable que controla la parada canvia en cada volta.

Un `while` també pot repetir una entrada fins que siga vàlida. Per a un catàleg de dues opcions:

```python
opcio = input("Material: paper o tela? ").strip().lower()
while opcio not in ("paper", "tela"):
    opcio = input("Escriu paper o tela: ").strip().lower()
print(f"Material triat: {opcio}")
```

## Repetir amb `for` i `range`

`for` recorre un iterable. `range(inici, fi, pas)` exclou `fi`; el pas no pot ser zero. `range` no crea una llista sencera: pots convertir-lo amb `list()` si la necessites.

```python
for pagina in range(2, 9, 3):
    print(pagina)  # 2, 5, 8 en línies separades
for compte in range(3, 0, -1):
    print(compte)  # 3, 2, 1
```

Per a numerar elements, `enumerate` evita gestionar un índex manual:

```python
for posicio, color in enumerate(["ocre", "blau", "gris"], start=1):
    print(posicio, color)
```

Mostra `1 ocre`, `2 blau` i `3 gris`. Usa `_` com a nom de variable per conveni quan només vols repetir i no necessites el valor, com en `for _ in range(2): print("marca")`.

## `break`, `continue` i `else` d'un bucle

Exemple nou: buscar una etiqueta urgent entre notes:

```python
notes = ["pendent", "urgent", "resolt"]
for nota in notes:
    if nota == "resolt":
        continue
    if nota == "urgent":
        print("Hi ha una nota urgent")
        break
else:
    print("No hi ha notes urgents")
```

`break` acaba el bucle i evita el seu `else`. Si elimines `urgent` de les dades, el recorregut acaba normalment i executa l'`else`. En un `while`, la regla és la mateixa: `else` s'executa quan acaba sense `break`, fins i tot si no ha entrat mai al cos.

Els bucles anidats multipliquen recorreguts: dos colors per tres mides produeixen sis combinacions. Abans d'anidar, calcula quantes voltes faràs.

!!! success "Per a repassar"
    Escriu la condició, què canvia i quan acaba. En un recorregut, separa «ometre aquest element» de «deixar de buscar».

---

Fonts del temari: [01-condicionales](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/01-condicionales/), [02-while](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/02-while/), [03-for-range](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/03-for-range/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
