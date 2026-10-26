# UT2 · 5. Depurar una aplicació sense provar a l'atzar

## Segueix el recorregut de la petició

Quan una pàgina no fa el que esperes, separa tres preguntes: **ha arribat la petició?**, **què ha rebut PHP?** i **quina resposta ha generat?**. Un formulari que no conserva un valor no es diagnostica igual que un contenidor que no arranca.

## Cas resolt: no apareix la duració del torn

**Situació nova:** en un formulari de visita guiada el control diu `name="duracio"`, però el receptor llig `$_POST['temps']`. En enviar 25, el resum apareix buit.

1. En Xarxa del navegador, obri la petició POST. El cos conté `duracio=25`: el navegador envia bé la dada.
2. En desenvolupament local, inspecciona el receptor amb `var_dump($_POST);`. La clau és `duracio`, no `temps`.
3. Corregeix la lectura a `$_POST['duracio'] ?? ''` i valida el resultat abans de calcular.
4. Torna a provar 25, un camp absent i un text no numèric.
5. Retira la impressió de depuració. Si la deixes abans d'un `header()`, pot impedir la redirecció.

**Conclusió del cas:** el problema era el contracte entre el nom del camp i la clau que esperava PHP. Afegir CSS, reiniciar MariaDB o canviar de navegador no corregeix eixe desacord.

## On mirar segons el símptoma

| Símptoma | Comprovació concreta |
| --- | --- |
| No connecta | `docker compose ps`, port i URL |
| Nginx retorna 502 | `docker compose logs --tail=40 motor cartellera` en el laboratori d'UT1 |
| Error de sintaxi PHP | `php -l public/torn.php` si tens PHP local |
| Camp absent | `action`, `method`, `name` i cos del POST |
| `Undefined array key` | Clau real i lectura amb valor alternatiu |
| `headers already sent` | HTML, espais o `echo` anteriors a la capçalera |
| Sessió buida | `session_start()`, cookie i perfil del navegador |
| Resultat numèric incorrecte | Valors d'entrada, tipus i fórmula |

Per a veure errors només en un entorn local de desenvolupament:

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
```

En un servidor publicat, els detalls han d'anar als logs i la resposta a l'usuari ha de ser adequada. No mostres credencials, tokens ni dades personals en les captures de diagnòstic.

## Una comprovació útil abans de donar per acabat un tema

Prepara una taula amb cas normal, límit inferior, límit superior, dada absent i dada incorrecta. Per al telescopi, per exemple, 5 i 40 són vàlids, però 4 i 41 no. Si només proves 15, no has comprovat els límits.

En Git, registra una correcció coherent amb `git add fitxer.php`, `git diff --cached` i `git commit -m "Valida la duració del torn"`. El commit documenta el canvi; no substitueix la prova de funcionament.

!!! success "Per a repassar"
    Reprodueix, observa, explica una causa, corregeix i repeteix el cas que fallava. Canviar moltes coses alhora fa més difícil saber quina resolia el problema.

---

Font del temari: [apunts originals de UT2](https://victoria-nr.github.io/iaw-alumnos/UT2/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
