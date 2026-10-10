# Python

## Què és Python?

Python és un **llenguatge de programació**: una manera d'escriure instruccions perquè l'ordinador les execute. Es diferencia d'altres llenguatges perquè és molt **fàcil de llegir**: quasi sembla anglés.

```python
for fitxer in fitxers:
    if fitxer.endswith(".log"):
        print(fitxer)
```

Encara que no sàpies programar, segurament endevines què fa: *per a cada fitxer, si acaba en .log, mostra'l*.

## Per què Python si ja sé Bash?

| | Bash | Python |
| - | ---- | ------ |
| Ideal per a | encadenar ordres del sistema | programes amb lògica, càlculs i dades |
| Números decimals | no (cal `bc`) | sí |
| Estructures de dades | limitades | llistes, diccionaris... molt potents |
| Scripts llargs | es fan difícils de llegir | es mantenen clars |
| Funciona en | Linux/Mac | Linux, Mac i Windows |

En administració de sistemes s'usen tots dos: Bash per a coses ràpides, Python quan el script creix.

## Ordre recomanat

Si no has programat mai, segueix-los en ordre.

| Tema | Què aprens |
| ---- | ---------- |
| [1. Entorn de treball](01-entorn.md) | instal·lar, escriure i executar un programa |
| [2. Tipus i variables](02-tipus.md) | guardar dades: números, textos, sí/no |
| [3. Cadenes](03-cadenes.md) | treballar amb text |
| [4. Control de flux](04-control.md) | prendre decisions (`if`) i repetir (`for`, `while`) |
| [5. Estructures de dades](05-estructures.md) | llistes, diccionaris i altres col·leccions |
| [6. Funcions i mòduls](06-funcions.md) | organitzar el codi i usar el d'altres |
| [7. Fitxers, pathlib i glob](07-fitxers.md) | llegir i escriure fitxers, buscar-ne |
| [8. Excepcions](08-excepcions.md) | controlar els errors |
| [9. Python per a sysadmin](09-sysadmin.md) | executar ordres, arguments, logs... |
| [10. Classes i objectes](10-poo.md) | crear els teus propis tipus de dades |

Després: [exercicis resolts](exercicis.md) per a practicar.

Si et trobes una paraula que no entens, mira el [glossari](../glossari.md).

!!! tip "Durant un examen"
    Cada tema acaba amb un requadre verd **«Per a l'examen»** amb el més important. La [xuleta de Python](../xuletes/python.md) ho resumix tot en una pàgina.
