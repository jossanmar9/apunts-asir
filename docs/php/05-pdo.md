# 5. Bases de dades amb PDO

**PDO** (*PHP Data Objects*) és la manera de connectar PHP amb una base de dades. La mateixa forma de treballar serveix per a **PostgreSQL**, MySQL/MariaDB, SQLite...: només canvia la cadena de connexió.

```bash
sudo apt install php-pgsql          # PostgreSQL (php-mysql per a MariaDB/MySQL, php-sqlite3 per a SQLite)
php -m | grep -i pdo                # PDO, pdo_pgsql...
```

Els exemples usen la [base de dades `institut`](index.md#la-base-de-dades-dexemple) i un usuari `app` amb permisos només per a llegir i modificar dades:

```sql
CREATE ROLE app LOGIN PASSWORD 'canvia-la';
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app;
GRANT USAGE ON ALL SEQUENCES IN SCHEMA public TO app;
```

!!! danger "Mai l'usuari `postgres` (o `root`) en una aplicació"
    Si hi ha una injecció SQL, l'atacant tindria permisos per a fer **qualsevol cosa** (esborrar bases de dades, llegir-ho tot). Un usuari propi amb el **mínim** de permisos.

## Connectar

```php
$dsn = "pgsql:host=127.0.0.1;port=5432;dbname=institut";
try {
    $pdo = new PDO($dsn, "app", "canvia-la", [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,   // els errors llancen excepcions
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,         // files com a arrays associatius
    ]);
} catch (PDOException $e) {
    exit("No s'ha pogut connectar: " . $e->getMessage());
}
```

| SGBD | DSN |
| ---- | --- |
| PostgreSQL | `pgsql:host=127.0.0.1;port=5432;dbname=institut` |
| MySQL / MariaDB | `mysql:host=127.0.0.1;dbname=institut;charset=utf8mb4` |
| SQLite | `sqlite:/var/www/dades/app.db` (un fitxer, sense usuari ni contrasenya) |

!!! warning "No mostres l'error de connexió a l'usuari en producció"
    `$e->getMessage()` pot mostrar el servidor, l'usuari... En producció, guarda'l en el registre (`error_log($e->getMessage())`) i mostra un missatge genèric.

## Consultar

Un exemple complet (resultats reals):

```php title="pdo.php"
// 1. Una consulta sense dades de l'usuari
$files = $pdo->query("SELECT nom, cognoms, cicle FROM alumnes ORDER BY cognoms")->fetchAll();
foreach ($files as $f) {
    echo "{$f['cognoms']}, {$f['nom']} ({$f['cicle']})\n";
}

// 2. Amb dades de l'usuari: SEMPRE consulta preparada
$cicle = "ASIR";                                   // imagina que ve de $_GET["cicle"]
$stmt = $pdo->prepare("SELECT COUNT(*) FROM alumnes WHERE cicle = :cicle");
$stmt->execute(["cicle" => $cicle]);
echo "Alumnes de $cicle: " . $stmt->fetchColumn() . "\n";

// 3. Una fila
$stmt = $pdo->prepare("SELECT * FROM alumnes WHERE id = ?");
$stmt->execute([3]);
$alumne = $stmt->fetch();                          // false si no n'hi ha
print_r($alumne);

// 4. Inserir i saber l'id
$stmt = $pdo->prepare("INSERT INTO alumnes (nom, cognoms, poblacio, cicle) VALUES (?, ?, ?, ?) RETURNING id");
$stmt->execute(["Joan", "Albà Ros", "Onda", "ASIR"]);
echo "Nou alumne amb id " . $stmt->fetchColumn() . "\n";

// 5. Modificar: quantes files han canviat
$stmt = $pdo->prepare("UPDATE alumnes SET poblacio = ? WHERE nom = ?");
$stmt->execute(["Castelló", "Joan"]);
echo "Files modificades: " . $stmt->rowCount() . "\n";
```

```console
$ php pdo.php
Beltran Ros, Sara ()
Climent Mas, Núria (SMX)
Gil Amat, Toni (DAW)
Pons Ferrer, Laura (ASIR)
Puig Vidal, Ana (ASIR)
Roig Serra, Pep (ASIR)
Sales Bou, Marc (DAW)
Alumnes de ASIR: 3
Array
(
    [id] => 3
    [nom] => Laura
    [cognoms] => Pons Ferrer
    [data_naix] => 2005-06-25
    [poblacio] => Castelló
    [cicle] => ASIR
)
Nou alumne amb id 8
Files modificades: 1
```

| Mètode | Torna |
| ------ | ----- |
| `$pdo->query($sql)` | executa una consulta **sense paràmetres** |
| `$pdo->prepare($sql)` + `$stmt->execute([...])` | consulta **preparada** ⭐ |
| `->fetchAll()` | **totes** les files (un array d'arrays) |
| `->fetch()` | **la següent** fila (o `false` si no n'hi ha més) |
| `->fetchColumn()` | el valor de la **primera columna** de la fila següent (per a `COUNT(*)`, un id...) |
| `->rowCount()` | quantes files ha afectat un `INSERT`, `UPDATE` o `DELETE` |
| `$pdo->lastInsertId()` | l'últim id inserit (en PostgreSQL és millor `RETURNING id`) |

### Paràmetres: `?` o `:nom`

```php
$stmt = $pdo->prepare("SELECT * FROM alumnes WHERE cicle = ? AND poblacio = ?");
$stmt->execute(["ASIR", "Castelló"]);                                   // en ordre

$stmt = $pdo->prepare("SELECT * FROM alumnes WHERE cicle = :cicle AND poblacio = :pob");
$stmt->execute(["cicle" => "ASIR", "pob" => "Castelló"]);              // per nom
```

## Injecció SQL ⭐

Si es **concatena** el que escriu l'usuari dins del SQL, pot canviar la consulta. És l'atac **injecció SQL** (*SQL injection*), un dels més perillosos: permet llegir tota la base de dades, saltar-se un *login* o esborrar dades.

```php title="injeccio.php"
$entrada = "x' OR '1'='1";              // el que escriu un atacant en el formulari

// ❌ MALAMENT: concatenar
$sql = "SELECT COUNT(*) FROM alumnes WHERE cognoms = '$entrada'";
echo "$sql\n→ " . $pdo->query($sql)->fetchColumn() . " files\n";

// ✅ BÉ: consulta preparada
$stmt = $pdo->prepare("SELECT COUNT(*) FROM alumnes WHERE cognoms = ?");
$stmt->execute([$entrada]);
echo "Preparada → " . $stmt->fetchColumn() . " files\n";
```

```console
$ php injeccio.php
SELECT COUNT(*) FROM alumnes WHERE cognoms = 'x' OR '1'='1'
→ 8 files
Preparada → 0 files
```

Amb la concatenació, la condició `OR '1'='1'` és **sempre certa**: torna **totes** les files. En un *login* (`WHERE usuari = '...' AND clau = '...'`), l'atacant entraria sense contrasenya. Amb la consulta preparada, el valor s'envia **separat** del SQL: es busca literalment un cognom que es diga `x' OR '1'='1`.

!!! danger "La regla"
    Qualsevol dada que vinga de fora (`$_GET`, `$_POST`, `$_COOKIE`, un fitxer, una API) va **sempre** com a **paràmetre** d'una consulta preparada. **Mai** concatenada.

    Els paràmetres només serveixen per a **valors**. Si un **nom de columna** ha de dependre de l'usuari (per exemple, l'ordre: `ORDER BY $camp`), comprova'l amb una llista de valors permesos:
    ```php
    $camp = in_array($_GET["ordre"] ?? "", ["nom", "cognoms", "poblacio"], true) ? $_GET["ordre"] : "cognoms";
    ```

## Transaccions

```php
try {
    $pdo->beginTransaction();
    $pdo->prepare("DELETE FROM matricules WHERE alumne = ?")->execute([$id]);
    $pdo->prepare("DELETE FROM alumnes WHERE id = ?")->execute([$id]);
    $pdo->commit();
} catch (PDOException $e) {
    $pdo->rollBack();          // si alguna falla, es desfan les dues
    throw $e;
}
```

Si alguna de les ordres falla, el `rollBack()` desfà les altres: o es fa tot o no es fa res.

## On posar les dades de connexió

```php title="config.php"
<?php
// Dades de connexió. En producció, fora del DocumentRoot o en variables d'entorn.
return [
    "dsn"   => "pgsql:host=127.0.0.1;port=5433;dbname=institut",
    "user"  => "app",
    "clau"  => "canvia-la",
];
```

```php
$c = require __DIR__ . "/config.php";
$pdo = new PDO($c["dsn"], $c["user"], $c["clau"], [...]);
```

O amb **variables d'entorn** (el que es fa amb Docker):

```php
$pdo = new PDO(getenv("DB_DSN"), getenv("DB_USER"), getenv("DB_PASS"));
```

!!! warning "No pugues contrasenyes a Git"
    Afig `config.php` al `.gitignore` i deixa un `config.example.php` sense les dades reals.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `could not find driver` | Falta l'extensió de PDO per a eixe SGBD | `sudo apt install php-pgsql` i reiniciar Apache / PHP-FPM |
| `SQLSTATE[08006] ... Connection refused` | PostgreSQL no està en marxa, o host/port incorrecte | `systemctl status postgresql`; revisa el DSN |
| `SQLSTATE[08006] ... password authentication failed for user "app"` | Usuari o contrasenya incorrectes (o el `pg_hba.conf` no deixa) | Revisa-ho; el fitxer `pg_hba.conf` de PostgreSQL diu qui es pot connectar |
| `SQLSTATE[42501]: Insufficient privilege: permission denied for table x` | L'usuari de l'aplicació no té permís | `GRANT` |
| `SQLSTATE[42P01]: Undefined table` | La taula no existix (o una altra base de dades) | Revisa el `dbname` |
| `SQLSTATE[HY093]: Invalid parameter number` | El nombre de `?` o de `:noms` no coincidix amb l'`execute` | Compta'ls |
| Els errors no ixen: la consulta simplement no fa res | Sense `ERRMODE_EXCEPTION` (en PHP < 8 era el per defecte) | Posa'l sempre |
| `permission denied for sequence alumnes_id_seq` en un `INSERT` | Falta permís sobre la seqüència del `SERIAL` | `GRANT USAGE ON ALL SEQUENCES ...` |

!!! success "Per a l'examen"
    ```php
    $pdo = new PDO("pgsql:host=127.0.0.1;dbname=bd", "usuari", "clau",
                   [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]);
    $files = $pdo->query("SELECT ...")->fetchAll();
    $stmt = $pdo->prepare("SELECT * FROM t WHERE id = ?");  $stmt->execute([$id]);  $fila = $stmt->fetch();
    $stmt = $pdo->prepare("INSERT INTO t (a, b) VALUES (:a, :b)");  $stmt->execute(["a" => $a, "b" => $b]);
    $stmt->rowCount();  $stmt->fetchColumn();
    $pdo->beginTransaction(); ... $pdo->commit(); / $pdo->rollBack();
    ```
    - **Consultes preparades** sempre que hi haja dades de fora → evita la **injecció SQL**
    - Un usuari de BD propi amb el **mínim** de permisos · dades de connexió fora del codi públic i de Git
