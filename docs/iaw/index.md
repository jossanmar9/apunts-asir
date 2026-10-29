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

Además de los problemas explicados dentro de los apuntes, hay un banco separado de ejercicios **sin solución** para practicar de forma autónoma. Los enunciados son diferentes de las prácticas de clase y mantienen el mismo nivel y contenidos.

- **UT1:** 60 ejercicios de arquitectura, HTTP, Docker, Compose, Nginx, PHP-FPM, MariaDB, variables, logs y diagnóstico.
- **UT2:** 50 ejercicios de PHP, control de flujo, arrays, funciones, formularios, validación, sesiones y depuración.

Consulta la sección **Ejercicios → IAW** de la web.

## Material pendiente

UT3 (acceso a bases de datos) y las unidades posteriores se incorporarán cuando dispongamos del material de clase correspondiente, para no adelantar contenidos que no sean los que se trabajan en el curso.

## Cómo estudiar estos apuntes

Lee primero la guía de repaso. Después entra en cada tema e intenta explicar con tus propias palabras qué hace cada componente o instrucción. En programación, predice el resultado antes de ejecutar. En Docker, intenta identificar primero **qué servicio falla y qué evidencia lo demostraría** antes de cambiar configuraciones.
