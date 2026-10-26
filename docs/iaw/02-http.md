# UT1 · 2. HTTP: peticions, respostes i diagnòstic

## Què viatja per la xarxa

HTTP defineix com un client demana una acció i com un servidor contesta. HTTPS protegeix eixa comunicació amb TLS. Una petició inclou un mètode, una ruta, capçaleres i, de vegades, un cos. La resposta inclou un estat, capçaleres i, habitualment, un cos.

Exemple didàctic d'una API de préstec de material audiovisual:

```http
GET /api/prestecs/73 HTTP/1.1
Host: material.example
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{"codi":73,"material":"Projector","estat":"reservat"}
```

`GET` és l'acció, `/api/prestecs/73` és el recurs i `Accept` indica què accepta el client. `Content-Type` descriu el contingut que realment retorna el servidor. La línia en blanc separa capçaleres i cos. `.example` s'usa ací com a domini fictici; aquesta resposta és il·lustrativa.

## Quin mètode trie?

| Mètode | Intenció habitual | Exemple del magatzem |
| --- | --- | --- |
| GET | Consultar sense modificar l'estat del servidor | Veure un préstec |
| POST | Enviar dades per a processar-les o crear un recurs | Demanar un préstec |
| PUT | Substituir la representació d'un recurs | Canviar una fitxa completa |
| PATCH | Modificar alguns camps | Canviar només la data de retorn |
| DELETE | Eliminar un recurs | Eliminar una reserva |

POST no xifra les dades: la protecció en trànsit depén d'HTTPS. GET posa els paràmetres d'un formulari en la URL; POST els envia habitualment al cos. Les capçaleres `Cookie`, `Authorization` i `Content-Type` tenen funcions diferents: estat del navegador, autenticació i format de dades, respectivament.

## Cas resolt: la petició arriba, però què falla?

**Situació:** una consulta al servei de préstecs retorna `404`; una altra petició a PHP retorna `502`.

1. Un `404` és una resposta HTTP: has contactat amb un servidor. Revisa la ruta, el fitxer, l'identificador i la configuració que resol les rutes.
2. Un `502` de Nginx apunta a un problema en la comunicació amb el servei que té darrere. Revisa si PHP-FPM està actiu i si `fastcgi_pass` usa el nom i el port correctes. No demostra per si sol que el codi PHP siga incorrecte.
3. Si `curl` diu que no es pot connectar, encara no hi ha resposta HTTP: revisa servei, port publicat i adreça.

En el laboratori del tema següent pots observar les respostes amb:

```bash
curl -i http://localhost:8092/
curl -I http://localhost:8092/
```

`-i` mostra capçaleres i cos. `-I` demana només capçaleres amb HEAD; una aplicació pot tractar HEAD de manera diferent. Amb F12 → Xarxa → recarregar, el navegador permet inspeccionar també mètodes, redireccions i recursos secundaris.

## Els estats que necessites reconéixer

| Estat | Lectura útil |
| --- | --- |
| 200 / 201 | Operació correcta / recurs creat |
| 301 / 302 / 303 | Redirecció; mira `Location` |
| 400 | Petició que l'aplicació considera incorrecta |
| 401 | Cal autenticar-se correctament |
| 403 | Accés rebutjat |
| 404 | Recurs no trobat |
| 500 | Fallada interna; revisa els logs |
| 502 / 503 | Problema amb el servei posterior / servei no disponible |

!!! success "Per a repassar"
    Separa mètode, ruta, capçaleres, cos i estat. Un codi HTTP orienta el diagnòstic, però cal contrastar-lo amb la petició i els logs.

---

Font del temari: [apunts originals de UT1](https://victoria-nr.github.io/iaw-alumnos/UT1/apuntes/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
