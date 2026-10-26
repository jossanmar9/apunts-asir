# UT3 · 2. Llegir errors i depurar amb mètode

## Tres problemes diferents

Un error de **sintaxi** impedeix interpretar el programa. Una excepció **durant l'execució** apareix quan una operació no es pot completar. Un error **lògic** produeix una resposta equivocada sense que Python ho detecte.

| Exemple | Tipus de problema |
| --- | --- |
| `if pendent > 0` sense `:` | Sintaxi |
| `int("quatre")` | Excepció `ValueError` |
| Multiplicar per unitats equivocades | Lògica |

## Cas resolt: un recompte que sembla funcionar

**Objectiu nou:** saber quants sobres calen per a 19 targetes, amb 6 targetes per sobre. El codi inicial usa `sobres = 19 // 6` i mostra 3.

1. Calcula manualment: tres sobres guarden 18 targetes i queda una targeta fora.
2. Inspecciona `targetes`, `capacitat` i el residu amb un breakpoint o impressions.
3. El problema és l'arrodoniment: la divisió entera compta només sobres complets.
4. Per a aquests enters positius, usa `(targetes + capacitat - 1) // capacitat`.
5. Comprova també 0, 6, 7 i 18 targetes.

```python
targetes = 19
capacitat = 6
sobres = (targetes + capacitat - 1) // capacitat
print(f"{targetes=}, {capacitat=}, {sobres=}")
```

**Resultat:** `targetes=19, capacitat=6, sobres=4`. No hi havia un missatge d'error que llegir: has necessitat contrastar la resposta amb el significat del problema.

## Llegir una traça de crides

Mira l'última línia per a reconéixer el tipus i el missatge; després localitza la línia del teu fitxer indicada just abans. Si hi ha diverses crides, segueix com s'ha arribat a l'operació que falla.

- `NameError`: nom absent o mal escrit.
- `TypeError`: operació incompatible amb els tipus.
- `ValueError`: tipus d'entrada esperat, però contingut no convertible o inadmissible.
- `IndexError`: posició fora de la seqüència.
- `FileNotFoundError`: ruta que no es pot trobar.

## Excepcions: reconéixer les eines

La teoria les presenta com a ampliació; no són necessàries per a resoldre tots els exercicis d'iniciació. Exemple didàctic separat:

```python
text = "moltes"
try:
    peces = int(text)
except ValueError:
    print("No es pot interpretar com un enter")
else:
    print(f"Peces llegides: {peces}")
```

**Resultat:** s'executa `except`, perquè `int` falla. Captura l'error concret que esperes, no qualsevol excepció per a continuar sense saber què ha passat. El `else` s'executaria si la conversió acabara sense excepció.

`raise ValueError("capacitat incorrecta")` llança una excepció. `assert condicio` comprova una hipòtesi interna durant desenvolupament; no ha de ser l'única validació d'entrada d'un programa, perquè les assercions es poden desactivar.

## Guia mentre treballes

Reprodueix el cas menut que falla, anota què esperaves i observa els valors abans de la línia. Canvia una causa concreta i repeteix el cas original i els límits. A VS Code, una variable que encara no apareix pot simplement no haver-se assignat en el punt on estàs parat.

!!! success "Per a repassar"
    Que el programa acabe sense excepcions no demostra que siga correcte. Necessites dades de prova amb un resultat que pugues justificar.

---

Fonts del temari: [04-depuracion-excepciones](https://victoria-nr.github.io/python-intro-alumnos/unidades/u03-control-flujo-sysadmin/teoria/04-depuracion-excepciones/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
