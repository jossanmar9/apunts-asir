# UT2 · 1. Objectes, mètodes i tractament de cadenes

## Funció i mètode

Una funció es crida com `len(text)`. Un mètode es crida sobre l'objecte: `text.upper()`. Els parèntesis executen l'operació; `text.upper` només obté una referència al mètode. Les cadenes són immutables: has de conservar el valor retornat si vols continuar usant la transformació.

## Exemple resolt: interpretar una etiqueta d'arxiu sonor

**Problema nou:** de l'etiqueta `"  jazz:directe:flac  "`, obtindre l'estil, el tipus de gravació i el format. Els dos separadors estan garantits en aquest primer exemple.

```python
original = "  jazz:directe:flac  "
etiqueta = original.strip()
primer = etiqueta.find(":")
ultim = etiqueta.rfind(":")
estil = etiqueta[:primer]
gravacio = etiqueta[primer + 1:ultim]
format_audio = etiqueta[ultim + 1:]
print(estil.title(), gravacio, format_audio.upper(), sep=" | ")
print(etiqueta.count(":"))
print(etiqueta.startswith("jazz:"), etiqueta.endswith(":flac"))
```

**Resultat esperat:** `Jazz | directe | FLAC`, després `2` i `True True`.

### Segueix els índexs

La cadena neta és `jazz:directe:flac`. El primer `:` està en la posició 4 i l'últim en la 12. `[:4]` pren les posicions 0 a 3. `[5:12]` pren `directe`. `[13:]` pren fins al final. El límit dret del tall queda exclòs.

`find()` retorna -1 quan no troba la subcadena; `index()` llança `ValueError`. Si els separadors no estan garantits, comprova'ls abans d'extraure: un tall amb -1 podria donar un resultat aparentment correcte però equivocat.

## Operacions que convé tindre a mà

| Operació | Exemple i lectura |
| --- | --- |
| `strip`, `lstrip`, `rstrip` | Llevar espais dels dos extrems, esquerra o dreta |
| `lower`, `upper` | Passar a minúscules o majúscules |
| `capitalize`, `title` | Primera lletra de la frase o inicis de paraula |
| `replace('a', 'b', 1)` | Substituir només la primera coincidència |
| `count(':')` | Comptar aparicions |
| `isalpha`, `isalnum` | Només lletres / lletres o nombres |
| `isdigit`, `isupper`, `islower` | Comprovar el contingut o les lletres amb cas |

`isdigit()` inclou determinats caràcters Unicode que no admet `int()`; no és un validador universal de nombres. Tampoc accepta signe negatiu o punt decimal. Per a una entrada ASCII restringida pots comprovar explícitament els caràcters admesos.

```python
so = "violi"
print(so[0], so[-1])  # v i
print(so[::2])       # vii
print(so[::-1])      # iloiv
print("ol" in so)    # True
print("-" * 4)       # ----
```

Accedir a `so[99]` produeix `IndexError`, però un tall com `so[:99]` s'ajusta al final disponible. `strip()` no lleva espais interns. `replace()` no valida si el significat del resultat és correcte.

## Funcions de biblioteca i aleatorietat

`string.ascii_letters` i `string.digits` proporcionen alfabets útils. `random.choice(sequencia)` selecciona un element i `random.randint(a, b)` inclou tots dos extrems. Per a demostrar una selecció de mostra pots fer `random.choice("ABC")`; el resultat varia. Les contrasenyes o tokens reals necessiten una font adequada com `secrets`, no l'aleatorietat de simulació de `random`.

!!! success "Per a repassar"
    Escriu els índexs sota la cadena abans de tallar-la. Comprova sempre què passa si falta el separador que esperes.

---

Fonts del temari: [01-objetos-predefinidos](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/01-objetos-predefinidos/), [02-metodos-cadenas](https://victoria-nr.github.io/python-intro-alumnos/unidades/u02-objetos-cadenas/teoria/02-metodos-cadenas/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
