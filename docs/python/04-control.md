# 4. Control de flux

## `if`, `elif`, `else`

```python
us = 85
if us < 70:
    print("OK")
elif us < 90:
    print("AVÍS")
else:
    print("CRÍTIC")
```

Expressió condicional en una línia:

```python
estat = "actiu" if codi == 0 else "error"
```

Comprovar si un valor està en una llista:

```python
if resposta.lower() in ("s", "si", "sí", "y"):
    print("Continuem")
```

## `match` (Python 3.10+)

Equivalent al `case` de Bash:

```python
match ordre:
    case "start":
        arrancar()
    case "stop" | "halt":
        parar()
    case _:
        print("Ordre desconeguda")
```

`_` és "qualsevol altre valor".

## `while`

```python
intents = 3
while intents > 0:
    clau = input("Contrasenya: ")
    if clau == "secret":
        print("Benvingut")
        break
    intents -= 1
    print(f"Incorrecta. Et queden {intents}")
else:
    print("Compte bloquejat")   # només si el bucle acaba SENSE break
```

## `for`

`for` recorre qualsevol col·lecció: llista, cadena, fitxer, diccionari...

```python
for servei in ["ssh", "nginx", "cron"]:
    print(servei)

for lletra in "hola":
    print(lletra)
```

### `range`

```python
range(5)          # 0 1 2 3 4
range(1, 6)       # 1 2 3 4 5   (el final no s'inclou)
range(0, 20, 5)   # 0 5 10 15
range(10, 0, -1)  # 10 9 ... 1
```

```python
for i in range(1, 11):
    print(f"7 x {i:2} = {7 * i}")
```

### `enumerate` i `zip`

```python
for num, linia in enumerate(linies, start=1):   # índex + valor
    print(f"{num}: {linia}")

noms = ["ana", "pep"]
notes = [8, 6]
for nom, nota in zip(noms, notes):              # dues llistes en paral·lel
    print(nom, nota)
```

## `break`, `continue`, `pass`

```python
for linia in open("/etc/ssh/sshd_config"):
    linia = linia.strip()
    if not linia or linia.startswith("#"):
        continue                 # salta comentaris i buides
    if linia.startswith("Port"):
        print(linia)
        break                    # ja l'hem trobat
```

`pass` no fa res: serveix per a deixar un bloc buit mentre escrius.

## Bucles niats

```python
for fila in range(1, 4):
    for col in range(1, 4):
        print(f"{fila * col:3}", end="")
    print()
```

## Operador morsa `:=`

Assigna i compara alhora. Útil en bucles que demanen dades:

```python
while (ordre := input("> ")) != "eixir":
    print(f"Has escrit {ordre}")
```

## Validar una entrada (patró habitual)

```python
while True:
    text = input("Port (1-65535): ")
    if text.isdigit() and 1 <= int(text) <= 65535:
        port = int(text)
        break
    print("Valor no vàlid")
```
