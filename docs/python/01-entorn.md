# 1. Entorn de treball

## Instal·lar i comprovar

En Debian/Ubuntu Python 3 ja ve instal·lat:

```bash
python3 --version
sudo apt install python3-pip python3-venv    # pip i entorns virtuals
```

## Mode interactiu

```console
$ python3
>>> 2 + 3
5
>>> nom = "Ana"
>>> nom.upper()
'ANA'
>>> help(str.split)     # ajuda de qualsevol cosa
>>> exit()
```

Ideal per a provar una línia abans de posar-la en un script. `ipython3` és una versió millorada (colors, autocompletat).

## Scripts

```python title="hola.py"
#!/usr/bin/env python3
"""Saluda l'usuari."""

nom = input("Com et dius? ")
print(f"Hola, {nom}!")
```

```bash
python3 hola.py          # opció 1
chmod +x hola.py         # opció 2: com un script de Bash
./hola.py
```

## Les regles bàsiques de la sintaxi

- **La indentació és obligatòria**: els blocs (dins d'un `if`, d'un `for`, d'una funció) es marquen amb 4 espais, no amb claus. Mesclar tabuladors i espais dona error.
- Les línies **no** acaben amb `;`.
- Comentaris amb `#`. Text de documentació entre `"""triples cometes"""`.
- Distingix majúscules: `Nom` i `nom` són variables diferents.
- Els noms de variables i funcions en `minuscules_amb_guions_baixos`.

```python
if edat >= 18:
    print("Major d'edat")     # 4 espais
    print("Pot votar")
print("Açò ja està fora de l'if")
```

## Entorns virtuals i `pip`

Cada projecte hauria de tindre les seues llibreries separades, per no trencar les del sistema:

```bash
python3 -m venv .venv            # crea l'entorn en la carpeta .venv
source .venv/bin/activate        # l'activa (el prompt mostra (.venv))
pip install requests             # instal·la dins de l'entorn
pip freeze > requirements.txt    # guarda la llista de dependències
pip install -r requirements.txt  # les reinstal·la en una altra màquina
deactivate                       # ix de l'entorn
```

!!! warning "error: externally-managed-environment"
    Les distribucions modernes no deixen fer `pip install` fora d'un entorn virtual per protegir el Python del sistema. La solució és crear un `venv`, no usar `--break-system-packages`.

## Editor: VS Code

1. Instal·la l'extensió **Python** de Microsoft.
2. Obri la carpeta del projecte (`code .`).
3. Tria l'intèrpret de l'entorn virtual: ++ctrl+shift+p++ → *Python: Select Interpreter*.
4. ++f5++ executa amb el **depurador**: posa un punt de ruptura fent clic a l'esquerra del número de línia i podràs veure el valor de cada variable pas a pas.

## La filosofia de Python

Escriu `import this` en l'intèrpret. Algunes idees que convé recordar:

- Llegible compta.
- Explícit millor que implícit.
- Simple millor que complex.
- Els errors no haurien de passar en silenci.
