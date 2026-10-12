# PHP (Implantació d'aplicacions web)

Com funciona una aplicació web per dins, amb **PHP** i una base de dades **PostgreSQL**, i com es posa en marxa en un servidor. No cal saber programar molt: l'objectiu és entendre-les, adaptar-les i **desplegar-les**.

## Ordre recomanat

| Tema | Què aprens |
| ---- | ---------- |
| [1. Què és PHP](01-introduccio.md) | com s'executa, el primer script, el servidor de proves |
| [2. El llenguatge](02-llenguatge.md) | variables, condicions, bucles, arrays, funcions, `include` |
| [3. Formularis](03-formularis.md) | `$_GET`, `$_POST`, validar, evitar XSS |
| [4. Sessions i usuaris](04-sessions.md) | `$_SESSION`, galetes, *login* amb contrasenyes segures |
| [5. Bases de dades amb PDO](05-pdo.md) | connectar amb PostgreSQL, consultes preparades, injecció SQL |
| [6. Una aplicació CRUD](06-crud.md) | llistar, afegir, editar i esborrar alumnes |
| [7. Desplegar aplicacions](07-desplegament.md) | posar-la en un servidor, permisos, Docker, WordPress |

Després: [exercicis resolts](exercicis.md). Resum d'una pàgina: [xuleta de PHP](../xuletes/php.md).

**El codi complet** dels exemples, provat: [:material-download: crud-alumnes.zip](../assets/fitxers/php/crud-alumnes.zip) · [:material-download: login.zip](../assets/fitxers/php/login.zip)

## La base de dades d'exemple

Els temes 5 i 6 usen una base de dades d'un **institut** amb cinc taules:

| Taula | Columnes |
| ----- | -------- |
| `cicles` | `codi` (clau), `nom`, `grau` |
| `professors` | `id`, `nom`, `cognoms`, `correu`, `data_alta` |
| `alumnes` | `id`, `nom`, `cognoms`, `data_naix`, `poblacio`, `cicle` (→ `cicles`) |
| `moduls` | `codi`, `nom`, `hores`, `curs`, `cicle` (→ `cicles`), `professor` (→ `professors`) |
| `matricules` | `alumne` (→ `alumnes`), `modul` (→ `moduls`), `nota` |

[:material-download: Descarrega institut.sql](../assets/fitxers/institut.sql) i carrega-la:

```bash
sudo apt install postgresql
sudo -u postgres createdb institut
sudo -u postgres psql -d institut -f institut.sql
sudo -u postgres psql -d institut -c "SELECT nom, cognoms, cicle FROM alumnes;"
```

### El SQL que cal saber per a PHP

```sql
SELECT nom, cognoms FROM alumnes WHERE cicle = 'ASIR' ORDER BY cognoms;   -- llegir
INSERT INTO alumnes (nom, cognoms, cicle) VALUES ('Joan', 'Albà', 'ASIR'); -- afegir
UPDATE alumnes SET poblacio = 'Onda' WHERE id = 3;                         -- modificar
DELETE FROM alumnes WHERE id = 3;                                          -- esborrar
```

!!! danger "`UPDATE` i `DELETE` sempre amb `WHERE`"
    Sense `WHERE`, es modifiquen o s'esborren **totes** les files.
