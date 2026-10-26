# UT1 · 3. Llegir dades i mostrar resultats

## `input()` sempre retorna text

Si l'usuari escriu `12`, `input()` retorna `"12"`. Per a calcular has de convertir-lo amb `int()` o `float()`. Convertir no és el mateix que validar totes les regles del problema: un enter negatiu continua sent un enter, però pot ser inadmissible com a quantitat de mostres.

`print()` pot separar arguments amb `sep` i triar el final amb `end`. Les f-strings insereixen expressions entre claus. Un `\n` representa un salt de línia i `\t` una tabulació. Les cometes triples permeten text de diverses línies.

## Exemple resolt: consum d'una impressora 3D

**Problema nou:** estimar quants metres de filament consumeix una sessió segons hores i metres per hora. Suposem entrades positives i decimals amb punt; la validació s'introdueix en UT3.

```python
hores = float(input("Hores de treball: "))
metres_hora = float(input("Metres de filament per hora: "))
consum = hores * metres_hora
print(f"Filament estimat: {consum:.2f} m")
print("Unitat", "metres", sep=": ")
```

### Prova amb dades conegudes

Escriu `2.5` i `1.2`.

1. Les dues entrades són inicialment text.
2. `float` les converteix a valors decimals.
3. `2.5 * 1.2` és 3.0 metres.
4. `:.2f` mostra dues xifres decimals: `Filament estimat: 3.00 m`.
5. El segon `print` mostra `Unitat: metres`.

Si escrius `dues`, la conversió produeix `ValueError`. Si escrius `2,5`, també falla amb aquest programa: el separador decimal que espera `float` és el punt. No anuncies que el programa accepta qualsevol entrada si encara no la valides.

## Una altra prova de tipus

```python
text = "6"
print(text * 3)       # 666
print(int(text) * 3)  # 18
print(str(18) + " m") # 18 m
```

La mateixa sintaxi `*` té significats diferents segons els tipus. `"6" + 3` falla perquè no hi ha una concatenació automàtica de cadena i enter. Una f-string com `f"{3} m"` resol la presentació sense alterar el tipus de la variable original.

## Com estudiar un programa d'entrada i eixida

Fes una taula amb el text introduït, el tipus després de la conversió, la fórmula i l'eixida. Després prova un valor simple que pugues calcular mentalment. Si un càlcul de consum amb zero hores dona una quantitat positiva, hi ha un error de lògica encara que Python no mostre cap excepció.

| Símptoma | Causa habitual |
| --- | --- |
| `TypeError` en sumar | S'estan barrejant text i números. |
| Es veuen `{consum}` literalment | Falta la `f` abans de les cometes. |
| Apareixen massa decimals | Aplica un format de presentació; no és una validació. |

!!! success "Per a repassar"
    Llig text, converteix quan cal i mostra amb un format comprensible. Identifica en quin pas pot fallar cada entrada.

---

Fonts del temari: [05-cadenas-entrada-salida](https://victoria-nr.github.io/python-intro-alumnos/unidades/u01-introduccion-python/teoria/05-cadenas-entrada-salida/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
