# 1. Entorn de treball

## Comprovar que tens Python

En Linux (Ubuntu, Debian...) Python ja ve instal·lat. Obri un terminal i escriu:

```bash
python3 --version
```

Si mostra alguna cosa com `Python 3.12.3`, ja està. Si no, instal·la'l:

```bash
sudo apt install python3 python3-pip python3-venv
```

!!! note "`python3`, no `python`"
    En molts Linux cal escriure `python3`. L'ordre `python` pot no existir o ser una versió antiga.

## Dues maneres d'usar Python

### 1. Mode interactiu: per a provar coses

Escrius `python3` i et deixa escriure instruccions una a una. Cada vegada que prems ++enter++, l'executa i et mostra el resultat:

```console
$ python3
>>> 2 + 3
5
>>> nom = "Ana"
>>> nom.upper()
'ANA'
>>> exit()
```

Els `>>>` indiquen que Python espera que escrigues. Per a eixir: `exit()` o ++ctrl+d++.

És perfecte per a **provar una línia** abans de posar-la en un programa, o per a usar Python com a calculadora.

### 2. Script: un programa guardat en un fitxer

Per a programes de veritat, escrius el codi en un fitxer acabat en `.py`:

```python title="hola.py"
# El meu primer programa
nom = input("Com et dius? ")     # pregunta i guarda la resposta
print("Hola,", nom)              # mostra el missatge
```

I l'executes:

```bash
python3 hola.py
```

```console
Com et dius? Ana
Hola, Ana
```

També el pots executar com un script de Bash si poses una primera línia especial i li dones permís:

```python title="hola.py"
#!/usr/bin/env python3
nom = input("Com et dius? ")
print("Hola,", nom)
```

```bash
chmod +x hola.py
./hola.py
```

## Les regles bàsiques que has de saber

### 1. La indentació (els espais de davant) és obligatòria

En altres llenguatges els blocs es marquen amb claus `{ }`. En Python es marquen amb **4 espais** al principi de la línia. És **obligatori**: si no ho fas bé, dona error.

```python
edat = 20
if edat >= 18:
    print("Major d'edat")       # 4 espais: està DINS de l'if
    print("Pot votar")          # 4 espais: també DINS
print("Fi")                     # 0 espais: ja està FORA de l'if
```

Les línies que acaben en `:` (com `if`, `for`, `def`) obrin un bloc. Les línies de dins van amb 4 espais més.

!!! danger "IndentationError"
    Si veus este error, revisa els espais. No mesclis tabuladors i espais. Els editors com VS Code ho fan automàticament.

### 2. Comentaris

Tot el que va després de `#` Python ho ignora. Serveix per a explicar el codi:

```python
# Açò és un comentari
preu = 100   # també es pot posar al final d'una línia
```

### 3. Majúscules i minúscules importen

`nom`, `Nom` i `NOM` són tres coses diferents. `Print("hola")` dona error perquè la funció es diu `print`.

### 4. Noms de variables

- En minúscules i amb `_` per a separar paraules: `nom_usuari`, `total_bytes`.
- No poden començar per número ni tindre espais.
- Millor noms que expliquen què guarden: `preu` millor que `p`.

## Instal·lar llibreries: entorns virtuals i `pip`

Python porta moltes coses incloses, però de vegades necessites llibreries d'altres persones (per exemple, `requests` per a connectar-se a webs). S'instal·len amb `pip`.

Per a no mesclar les llibreries de diferents projectes, es crea un **entorn virtual** (una carpeta on s'instal·len només per a eixe projecte):

```bash
python3 -m venv .venv            # 1. crear l'entorn (una vegada)
source .venv/bin/activate        # 2. activar-lo (cada vegada que obris el terminal)
pip install requests             # 3. instal·lar el que necessites
deactivate                       # eixir de l'entorn
```

Quan l'entorn està actiu, el terminal mostra `(.venv)` al principi.

!!! warning "error: externally-managed-environment"
    Si fas `pip install` fora d'un entorn virtual, Linux no et deixa (per protegir el Python del sistema). La solució és crear i activar un entorn virtual.

## Editor recomanat: VS Code

1. Instal·la **Visual Studio Code**.
2. Instal·la l'extensió **Python** (de Microsoft).
3. Obri la carpeta del projecte.
4. Prem ++f5++ per a executar el programa.

Té una funció molt útil per a aprendre: el **depurador**. Fes clic a l'esquerra d'un número de línia (apareix un punt roig), prem ++f5++, i el programa es pararà en eixa línia. Podràs veure quant val cada variable i avançar línia a línia.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `python: command not found` | En Linux es diu `python3` | `python3 fitxer.py` |
| `IndentationError` | Espais de davant incorrectes | Revisa que els blocs tinguen 4 espais |
| `SyntaxError` en una línia amb `if` o `for` | Falten els `:` al final | `if x > 5:` |
| `NameError: name 'Print' is not defined` | Majúscules | `print` en minúscules |
| `externally-managed-environment` | `pip` fora d'un entorn virtual | Crea un `venv` |

!!! success "Per a l'examen"
    - Executar: `python3 fitxer.py`
    - Provar coses: `python3` (mode interactiu), `exit()` per a eixir
    - **Indentació obligatòria**: 4 espais dins de cada bloc
    - Les línies `if`, `for`, `while`, `def` **acaben en `:`**
    - Comentaris amb `#`
    - Majúscules importen: `print`, no `Print`
