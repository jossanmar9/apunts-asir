# Apuntes ASIR

Apuntes desarrollados en **castellano** de los apuntes de clase de **IAW, ASO, Python y Sostenibilidad**, organizados por módulo, unidad y tema, con explicaciones desde cero y ejemplos propios resueltos paso a paso. **Git y GitHub tiene una sección independiente.** Sirven para preparar los exámenes y como guía mientras haces ejercicios. Las tablas y el repaso complementan la explicación; no la sustituyen.

🌐 **[Web de Apuntes ASIR](https://jossanmar9.github.io/apunts-asir/)**

## Estudiar desde el repositorio

| Sección | Contenido | Apuntes |
| --- | --- | --- |
| IAW · Implantación de aplicaciones web | UT1: entorno web · UT2: programación PHP | [Índice de IAW](docs/iaw/index.md) |
| ASO · Administración de sistemas operativos | UT1: Bash | [Índice de ASO](docs/aso/index.md) |
| Introducción a Python | UT1: entorno y datos · UT2: objetos y cadenas · UT3: control y bibliotecas | [Índice de Python](docs/python-classe/index.md) |
| Git y GitHub | Tema independiente: repositorios, commits, remoto y SSH | [Git y GitHub](docs/git-github/index.md) |
| Sostenibilidad aplicada al sistema productivo | Seis unidades del PDF: ASG, retos, ODS, economía circular, huellas y plan | [Índice de Sostenibilidad](docs/sostenibilidad/index.md) |
| Cómo estudiar | Método de estudio y consejos para aprender | [Cómo estudiar](docs/estudiar/index.md) |

Cada tema incluye explicaciones desde cero, instrucciones comentadas, problemas fáciles resueltos paso a paso, seguimiento de variables, resultados esperados y errores habituales. Cada tema tiene además tres ejercicios de práctica con pistas y soluciones plegadas. El vocabulario y el repaso quedan al final como consulta. Los casos didácticos **no son los ejercicios de clase para practicar o entregar**, ni versiones con solo los nombres o los datos cambiados.

## Resúmenes de Sostenibilidad

Se han añadido las seis unidades de *Sostenibilidad aplicada al sistema productivo* (Juan Jesús García Navarro y Antonio Ramón Álvarez Sánchez, Editex, edición 2024), a partir del PDF facilitado por el estudiante. Incluyen explicaciones en castellano, ejemplos nuevos paso a paso, vocabulario y **18 ejercicios nuevos** con pistas y soluciones plegadas. El PDF permanece como consulta local; el repositorio contiene los resúmenes, no una copia del libro. Consulta el [índice y alcance](docs/sostenibilidad/index.md).

## Material integrado

Las tablas, explicaciones y técnicas de los apuntes anteriores se han incorporado dentro de IAW, ASO, Python y Git y GitHub. No hay una sección pública de complementos ni un glosario separado: los términos se definen en su contexto. Consulta el [mapa de integración](archivo/INTEGRACION.md) para localizar los originales conservados.

## Criterio de redacción

En ASO se utiliza Bash con la cabecera `#!/bin/bash`, siguiendo el formato de clase. Mantén esta cabecera en los scripts y soluciones nuevos. Para mostrar mensajes se utiliza `echo`, como en clase; conserva también este criterio en los ejemplos y ejercicios.

- Desarrolla la explicación para un estudiante que empieza: qué significa cada concepto, cómo funciona y por qué se utiliza.
- Incorpora el desarrollo útil del material anterior; no lo reduzcas a una tabla o a una mención.
- Utiliza problemas sencillos y explícalos paso a paso, con la salida y el motivo de cada operación. Evita las etiquetas «problema propio» o «con datos conocidos».
- Mantén enunciados distintos de los ejercicios de práctica o entrega de clase.
- Sitúa vocabulario, tablas y repaso como apoyo a la explicación, sin sustituirla.
- Incluye tres ejercicios sencillos de práctica en cada tema, distintos de las demostraciones de teoría y de las tareas de clase. Mantén pistas y soluciones paso a paso plegadas; comprueba las soluciones ejecutables.

## Fuentes y criterio de actualización

- [IAW — victoria-nr](https://victoria-nr.github.io/iaw-alumnos/)
- [ASO — angelabserrano](https://angelabserrano.github.io/aso/)
- [Introducción a Python — victoria-nr](https://victoria-nr.github.io/python-intro-alumnos/)

Última consulta: **26/10/2026**. Traducción al castellano: **27/10/2026**. Consulta la [cobertura por unidades](docs/classe.md). Los apuntes y ejemplos son de redacción propia; las fuentes de teoría se enlazan en cada tema.

**Actualización manual, cuando lo solicite el estudiante.** Cuando se anuncien materiales nuevos:

1. Revisa la teoría y los enunciados nuevos para identificar conceptos y evitar resolver los ejercicios asignados.
2. Actualiza el módulo y la unidad correspondientes con explicaciones claras en castellano y casos didácticos diferentes, no simples cambios de nombres o datos.
3. Explica entrada, pasos, resultado y errores. Distingue lo publicado de lo que solo está planificado.
4. Comprueba los ejemplos ejecutables y la compilación; actualiza fuentes, fecha y cobertura.

No hay sincronización automática con las webs de clase. El material anterior que amplía los temas publicados se ha integrado en ellos, en castellano. Cada tema incluye sus palabras clave y definiciones. Los originales y los contenidos para unidades aún no publicadas se conservan en `archivo/`, fuera de `docs/`: no se generan en la web ni se indexan en su buscador.

## Estructura

```text
docs/
├── index.md          portada por módulos y temas independientes
├── iaw/              UT1 y UT2, con 8 temas
├── aso/              UT1 Bash, con 5 temas
├── git-github/       tema independiente de Git y GitHub
├── python-classe/    UT1 a UT3, con 8 temas
├── sostenibilidad/   seis unidades del PDF, con resúmenes y ejercicios
├── estudiar/         método y consejos de estudio en castellano
├── classe.md         fuentes y cobertura del temario
└── assets/           estilos de la web
archivo/              originales anteriores, fuera de la web
└── INTEGRACION.md    correspondencia entre materiales y temas actuales
mkdocs.yml            configuración y menú de la web
```

La antigua página de Git en ASO conserva un enlace a la nueva sección para que los enlaces publicados sigan siendo útiles.

## Trabajar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Abre `http://127.0.0.1:8000`. Para comprobar la compilación: `mkdocs build --strict`.

## Revisar los ejemplos

Con Python 3, Bash, PHP, Git y `bc` instalados:

```bash
mkdocs build --strict --site-dir /tmp/asir-revision-web
python3 scripts/revisar_apuntes.py --site-dir /tmp/asir-revision-web
```

El comprobador revisa sintaxis, ejecuta ejemplos en carpetas temporales y comprueba enlaces, tablas y ejercicios desplegables de la web generada. Las comprobaciones adicionales `--http` y `--docker` prueban los formularios mediante un servidor local y el entorno Nginx/PHP en un proyecto Docker temporal independiente; necesitan permisos para abrir puertos locales y acceder a Docker. Estas pruebas comprueban los casos incluidos, pero no sustituyen la revisión de las explicaciones.

## Publicar cambios

Edita los `.md` dentro de `docs/` y registra cualquier página nueva en `nav:` de `mkdocs.yml`. Después de revisar y probar, un commit enviado a `main` activa la Action que publica la web en GitHub Pages.
