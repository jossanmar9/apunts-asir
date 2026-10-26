# UT2 · 1. PHP, variables i generació d'HTML

## On s'executa cada cosa

PHP s'executa al servidor. El resultat pot ser HTML, JSON o text. El navegador no executa el PHP original. Obrir un `.php` com a fitxer local no equival a demanar-lo a un servidor PHP.

Per a aquests exemples pots usar la carpeta `public` del laboratori d'UT1. Si tens l'intèrpret PHP instal·lat, també pots provar només PHP amb `php -S 127.0.0.1:8093 -t public`. Eixe servidor és per a desenvolupament local i no reprodueix el stack complet de Nginx i MariaDB.

## Les regles bàsiques

Les variables comencen per `$` i distingeixen majúscules. `=` assigna; `===` compara valor i tipus. Les instruccions solen acabar en `;`. El punt `.` concatena text i `echo` escriu en la resposta. `<?= expressio ?>` equival a imprimir eixa expressió.

| Tipus | Exemple | Per a què serveix |
| --- | --- | --- |
| int | `24` | Recompte enter |
| float | `2.75` | Quantitat decimal |
| string | `'Sala violeta'` | Text |
| bool | `true` | Una condició |
| array | `['A', 'B']` | Una col·lecció |
| null | `null` | Absència de valor |

Les cometes dobles poden interpolar variables; les simples conserven el text literal. `//` i `/* ... */` són comentaris PHP. Un comentari HTML pot arribar al navegador; un comentari PHP no forma part de la resposta.

## Exemple resolt: places d'un taller de ceràmica

**Objectiu:** mostrar les places que queden. No hi ha formulari ni dades de classe: els valors estan fixats per a seguir el càlcul.

Desa `taller.php`:

```php
<?php
$capacitat = 18;
$reserves = 11;
$lliures = $capacitat - $reserves;
$nom = 'Ceràmica & color';
$complet = $lliures === 0;
?>
<h1><?= htmlspecialchars($nom, ENT_QUOTES, 'UTF-8') ?></h1>
<p>Places lliures: <?= $lliures ?></p>
<p><?= $complet ? 'Sense places' : 'Inscripció oberta' ?></p>
```

### Raonament pas a pas

1. PHP associa 18 i 11 a dues variables enteres.
2. Resta les reserves de la capacitat: `18 - 11 = 7`.
3. La comparació `7 === 0` és falsa; `$complet` val `false`.
4. El ternari `condicio ? valor_si : valor_no` tria el text «Inscripció oberta».
5. `htmlspecialchars` transforma els caràcters especials per a inserir text en HTML. L'ampersand es codifica en el codi font i el navegador mostra `&`.

**Resultat visible:** «Ceràmica & color», «Places lliures: 7» i «Inscripció oberta». Si reserves 18 places, veuràs 0 i «Sense places». Si poses 20 reserves, apareix un nombre negatiu: el programa necessita una regla de validació; la resta, tota sola, no garanteix dades coherents.

## Operadors que faràs servir

`+`, `-`, `*`, `/` i `%` calculen. `&&`, `||` i `!` combinen o neguen condicions. `??` aporta un valor alternatiu quan una dada no existeix o és `null`, com en `$_GET['sala'] ?? ''`. No valida que la dada siga correcta.

Un array indexat usa posicions: `$sales = ['Blava', 'Verda'];` i `$sales[0]` dona `Blava`. Un array associatiu usa claus: `$sala = ['nom' => 'Blava', 'capacitat' => 18];`. Accedeixes amb `$sala['capacitat']`. Si la clau no existeix, comprova-la o usa `??`.

| Error | Causa i solució |
| --- | --- |
| `Undefined variable` | Revisa nom i assignació abans d'usar-la. |
| `Parse error` | Mira `;`, cometes i claus, també en la línia anterior. |
| Es mostra codi PHP | Estàs obrint el fitxer directament o el servidor no el processa. |
| Text d'usuari es converteix en HTML | Escapa'l en el punt on generes HTML. |

!!! success "Per a repassar"
    Primer es calculen les dades; després es genera la resposta. Validar dades i escapar HTML són operacions diferents.

---

Font del temari: [apunts originals de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
