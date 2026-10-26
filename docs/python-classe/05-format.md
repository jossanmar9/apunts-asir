# UT2 · 2. F-strings, formats i Unicode

## El valor i la seua presentació són coses diferents

Una f-string transforma expressions en text. El format `:.2f` mostra dues xifres decimals; `:03d` mostra un enter amb almenys tres xifres i zeros a l'esquerra. El valor numèric original no canvia perquè el mostres amb un format.

## Exemple resolt: targeta d'una mostra mineral

```python
codi = 7
massa = 12.375
mineral = "quars"
print(f"M-{codi:03d} | {mineral.upper()} | {massa:.2f} g")
print(f"{massa=}")
print(f"Etiqueta literal: {{M-{codi:03d}}}")
```

**Eixida esperada:**

```text
M-007 | QUARS | 12.38 g
massa=12.375
Etiqueta literal: {M-007}
```

1. `:03d` no altera el codi 7; crea la representació `007`.
2. `:.2f` arredoneix la representació per a mostrar-la. No converteix `massa` en 12.38.
3. `{massa=}` mostra el nom de l'expressió i el seu valor; és útil en depuració.
4. `{{` i `}}` permeten escriure claus literals dins d'una f-string.

També pots usar `:d` per a enters, `:f` per a decimals i `:s` per a cadenes. Un format incompatible amb el tipus produeix error. `str(codi).zfill(3)` és una alternativa per a obtindre `007` com a text.

## Unicode i comparació

Python representa text amb Unicode. `ord(caracter)` obté el punt de codi i `chr(numero)` fa el recorregut invers:

```python
print(ord("Ω"))        # 937
print(chr(937))        # Ω
print("Z" < "a")       # True
print("Quars" == "quars")  # False
```

La comparació de cadenes és lexicogràfica per punts de codi, no una ordenació alfabètica adaptada a la llengua. Si l'usuari ha d'escriure una ordre independentment de majúscules, normalitza amb `strip().lower()` o `casefold()` segons el cas. Passar a minúscules no elimina accents ni converteix automàticament dos textos Unicode visualment iguals en la mateixa seqüència de caràcters.

## Cas resolt: per què falla un filtre?

**Situació:** esperes `"quars"`, però reps `" Quars "`. La igualtat directa és falsa. Primer neteja els extrems amb `strip()` i després converteix el cas amb `lower()`; el resultat és `"quars"`. Si reps `"quars blau"`, continuarà sent un text diferent: normalitzar no significa ignorar qualsevol diferència.

| Error | Comprovació |
| --- | --- |
| Claus sense substituir | Falta `f` al principi. |
| `ValueError` amb format `d` | El valor no és un enter compatible amb el format. |
| Comparació sorprenent | Mira majúscules, espais i representació amb `repr`. |

!!! success "Per a repassar"
    Separa el càlcul del format. Per a comprovar text, defineix primer quines diferències vols acceptar.

---

Fonts del temari: [03-formateo-fstrings-unicode](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/03-formateo-fstrings-unicode/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
