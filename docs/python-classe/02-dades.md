# UT1 · 2. Variables, tipus i operadors

## Un nom apunta a un objecte

En `mostres = 12`, Python avalua primer el costat dret i associa el nom `mostres` amb el resultat. El tipus pertany a l'objecte: `type(mostres)` indica `int`. Un objecte té tipus, valor i identitat; `id()` permet consultar-ne un identificador durant la seua vida, no un número estable que hages de memoritzar.

| Tipus | Exemple | Operacions habituals |
| --- | --- | --- |
| int | `12` | Comptar, dividir amb quocient i residu |
| float | `1.75` | Càlculs aproximats amb decimals |
| str | `"etiqueta"` | Concatenar, extraure, buscar |
| bool | `True` | Condicions |
| complex | `2 + 3j` | Càlculs amb part real i imaginària |

Usa noms com `mostres_per_caixa`, sense espais ni guions. No poden començar per xifra ni ser paraules reservades. Evita ocultar funcions amb noms com `str` o `input`. Les constants en majúscules, com `CAPACITAT = 8`, són una convenció, no una prohibició de canviar el valor.

## Exemple resolt: empaquetar mostres de ceràmica

**Problema nou:** tenim 29 mostres i cada estoig n'admet 8. Quants estoigs plens podem fer, quantes mostres queden i quants estoigs necessitem en total?

```python
mostres = 29
capacitat = 8
plens = mostres // capacitat
sobrants = mostres % capacitat
necessaris = (mostres + capacitat - 1) // capacitat
print(f"Plens: {plens}; sobrants: {sobrants}; necessaris: {necessaris}")
```

**Resultat esperat:** `Plens: 3; sobrants: 5; necessaris: 4`.

1. `29 // 8` dona 3: tres estoigs complets.
2. `29 % 8` dona 5: mostres que no caben en eixos tres.
3. La fórmula `(n + capacitat - 1) // capacitat` arrodoneix cap amunt per a enters no negatius i capacitat positiva. El quart estoig conté cinc mostres.

No uses aquesta fórmula sense comprovar les seues condicions quan l'entrada vinga de l'usuari.

## Operadors i representació de nombres

`/` fa divisió i retorna habitualment `float`; `//` arrodoneix el quocient cap a menys infinit; `%` dona el residu; `**` és la potència. Els parèntesis fan explícita la prioritat: `(2 + 3) * 4` dona 20, mentre que `2 + 3 * 4` dona 14.

`==`, `!=`, `<`, `<=`, `>` i `>=` comparen. `and`, `or` i `not` combinen condicions. `=` assigna. En context numèric els booleans es comporten com 1 i 0, però una condició clara és millor que un truc difícil de llegir.

```python
print(0b1100, 0o14, 0xC)  # 12 12 12
print(1.5e3)              # 1500.0
print(0.1 + 0.2 == 0.3)   # False
```

Les bases canvien la notació, no el valor. Molts decimals no tenen representació binària exacta; mostrar dos decimals no elimina l'aproximació interna. Per a diners amb requisits exactes, usa cèntims enters o eines decimals adequades.

## Mutabilitat: canviar un objecte o canviar de referència

```python
etiquetes = ["roig"]
altra_referencia = etiquetes
altra_referencia.append("blau")
print(etiquetes)  # ['roig', 'blau']

text = "roig"
text_nou = text.upper()
print(text, text_nou)  # roig ROIG
```

La llista és mutable i els dos noms apunten a la mateixa llista. La cadena és immutable: `upper()` crea un resultat nou. `is` compara identitat i `==` compara igualtat de valors; per a comparar textos usa `==`. Pots explorar operacions amb `help(str)`.

!!! success "Per a repassar"
    Abans d'una operació, identifica els tipus. El text `"8"` i l'enter `8` tenen significats diferents encara que s'assemblen en pantalla.

---

Fonts del temari: [03-datos-variables](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/03-datos-variables/), [04-numeros-operadores](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/04-numeros-operadores/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
