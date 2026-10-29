# IAW · Implantación de aplicaciones web

Apuntes para estudiar y consultar mientras haces los trabajos, revisados tomando como referencia la teoría, guías y prácticas de clase.

[:material-school: **Empezar por la guía de estudio UT1 + UT2**](00-guia-estudi.md){ .md-button .md-button--primary }

## UT1 · Entorno de implantación web

La unidad gira alrededor de una arquitectura reproducible con **Nginx + PHP-FPM + MariaDB** y Docker Compose. Conviene entender primero el recorrido de una petición y después aprender a diagnosticar cada pieza.

| Tema | Explicación y problemas paso a paso |
| --- | --- |
| 0 | [Guía de estudio y repaso](00-guia-estudi.md) |
| 1 | [Arquitectura y componentes](01-arquitectura.md) |
| 2 | [HTTP y diagnóstico](02-http.md) |
| 3 | [Docker Compose y entorno reproducible](03-entorn.md) |

## UT2 · Programación web en servidor con PHP

La unidad parte del entorno de UT1 y practica el ciclo **petición → PHP → validación/lógica → respuesta HTML**, incluyendo formularios, funciones, arrays, sesiones y depuración.

| Tema | Explicación y problemas paso a paso |
| --- | --- |
| 0 | [Guía de estudio y repaso](00-guia-estudi.md#ut2-php-en-servidor) |
| 1 | [PHP y tipos de datos](04-php.md) |
| 2 | [Control de flujo, arrays y funciones](05-control-funcions.md) |
| 3 | [Formularios y validación](06-formularis.md) |
| 4 | [Cookies, sesiones y autenticación](07-estat.md) |
| 5 | [Depuración y comprobaciones](08-depuracio.md) |

## Ejercicios adicionales

A més dels problemes explicats dins dels apunts, hi ha un banc separat d'exercicis **sense solució** per practicar de manera autònoma. Els enunciats són diferents de les pràctiques de classe i mantenen el mateix nivell i continguts.

- **UT1:** 60 exercicis d'arquitectura, HTTP, Docker, Compose, Nginx, PHP-FPM, MariaDB, variables, logs i diagnòstic.
- **UT2:** 50 exercicis de PHP, control de flux, arrays, funcions, formularis, validació, sessions i depuració.

Consulta la secció **Ejercicios → IAW** de la web.

## Material pendent

UT3 (accés a bases de dades) i les unitats posteriors s'incorporaran quan disposem del material de classe corresponent, per no avançar continguts que no siguen els que treballa el curs.

## Com estudiar aquests apunts

Llig primer la guia de repàs. Després entra en cada tema i intenta explicar amb les teues paraules què fa cada component o instrucció. En programació, prediu el resultat abans d'executar. En Docker, intenta identificar primer **quin servei falla i quina evidència ho demostraria** abans de canviar configuracions.
