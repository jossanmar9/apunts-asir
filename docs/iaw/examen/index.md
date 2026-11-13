# Preparación del examen · UT1 + UT2

**Fecha del examen:** 3 de diciembre de 2026.

Esta sección reúne todo lo necesario para preparar el examen de IAW: cómo es la prueba, qué hay que entender, un plan de estudio día a día y preguntas tipo examen con solución.

[:material-pencil: **Ir a las preguntas tipo examen**](preguntas.md){ .md-button .md-button--primary }

---

## Cómo es el examen

- Es **escrito**. No se usa VS Code ni se ejecuta código.
- Cada pregunta presenta un **caso**: un enunciado, un fragmento de `compose.yaml`, de configuración de Nginx o de PHP, o un síntoma de error.
- Cada caso tiene normalmente **tres apartados**:

| Apartado | Qué se pide normalmente |
| --- | --- |
| **a)** | Explicar **qué ocurre** y por qué |
| **b)** | Proponer **qué cambiarías** (se puede explicar con palabras; el código exacto no siempre es obligatorio) |
| **c)** | Explicar **cómo lo comprobarías** o qué consecuencia tiene |

!!! tip "Lo que se valora"
    No se busca memorizar comandos ni escribir una práctica desde cero. Se valora **entender el flujo**, saber **qué bloque hay que cambiar** y **justificar** la decisión. No hace falta recordar cada carácter de PHP.

---

## Las 4 ideas que hay que entender

Casi todas las preguntas se pueden razonar con estas cuatro ideas. Si las entiendes, tienes la base del examen.

### Idea 1 · El recorrido de una petición (UT1)

```text
Recurso estático (PDF, imagen, HTML):
Navegador → Nginx → Navegador

Recurso dinámico (.php):
Navegador → Nginx → PHP-FPM → (MariaDB) → PHP-FPM → Nginx → Navegador
```

- **Nginx** recibe la petición. Los ficheros estáticos los devuelve él solo; los `.php` se los pasa a PHP-FPM (`fastcgi_pass php:9000`).
- **PHP-FPM** ejecuta el código y genera HTML.
- **MariaDB** solo interviene si el PHP consulta datos.
- El navegador **nunca recibe el código PHP**, solo el HTML resultante.

**Preguntas que debes saber responder:** si cae MariaDB, ¿qué sigue funcionando? Si el navegador descarga el `.php`, ¿qué pieza falla?

Repaso: [Arquitectura y componentes](../01-arquitectura.md) · [HTTP y diagnóstico](../02-http.md)

### Idea 2 · Cómo se configura el entorno (UT1)

```text
.env  ──►  compose.yaml (${VARIABLE})  ──►  environment del contenedor  ──►  getenv() en PHP
```

- `.env` guarda los valores reales. Compose los usa para rellenar los `${...}`, pero **no llegan al contenedor solos**: hay que declararlos en `environment` (o usar `env_file`).
- `.env` **no se sube** al repositorio (`.gitignore`); `.env.example` es la plantilla sin contraseñas reales.
- **Puertos:** `"8080:80"` → izquierda, el ordenador; derecha, el contenedor.
- **Volúmenes:** `./app:/var/www/html` comparte código; `db_data:/var/lib/mysql` guarda los datos aunque se borren los contenedores.
- `init.sql` solo se ejecuta **la primera vez**, con el volumen vacío (`docker compose down -v` para repetirlo).
- Entre contenedores se usa el **nombre del servicio** (`db`, `php`), nunca `localhost`.
- Ante un fallo: `docker compose ps` y después `docker compose logs <servicio>`.

Repaso: [Docker Compose y entorno reproducible](../03-entorn.md)

### Idea 3 · El flujo de un formulario (UT2 · práctica 1)

```text
1ª visita (GET)   → se muestra el formulario vacío
Envío (POST)      → PHP recoge → valida → errores o resultado → HTML
```

- El `form` necesita `action` (a dónde va), `method="post"` y un `name` en cada campo (PHP lee el `name`, **no** el `id`).
- `if ($_SERVER['REQUEST_METHOD'] === 'POST')` hace que solo se procese cuando se envía.
- Recoger: `trim($_POST['campo'] ?? '')`. Checkbox: `isset($_POST['campo'])` (si no está marcado, no se envía).
- Validar: cada problema se añade a `$errores[]`; se muestran con `foreach`.
- Solo se calcula si no hay errores. Los valores se conservan con `value="..."`, `selected` y `checked`.
- **Siempre se valida en el servidor**, aunque el navegador ayude.

Repaso: [Formularios y validación](../06-formularis.md)

### Idea 4 · Cómo recuerda el servidor quién eres (UT2 · práctica 2)

```text
login.php → autenticar.php → ¿correcto?
                               sí → guarda en $_SESSION → panel.php
                               no → vuelve a login.php con error
panel.php  → si no hay sesión → login.php
logout.php → vacía y destruye la sesión → login.php
```

- **HTTP no tiene memoria:** una variable normal se reinicia en cada petición. Para recordar se usa la **sesión**.
- **Sesión:** los datos están en el **servidor**; el navegador solo guarda un identificador. **Cookie:** el dato se guarda en el **navegador**.
- `session_start()`, `header()` y `setcookie()` van **antes de cualquier salida** (`echo` o HTML).
- Proteger una página = comprobar **en el servidor** `isset($_SESSION['usuario'])`. Esconder un enlace no protege nada.
- Cada navegador (o ventana de incógnito) tiene **su propia sesión**: así se prueba el aislamiento.

Repaso: [Cookies, sesiones y autenticación](../07-estat.md) · [Depuración](../08-depuracio.md)

---

## Cómo responder una pregunta

Usa siempre esta estructura. Aunque no recuerdes la sintaxis exacta, puntúa.

1. **Qué ocurre:** describe el síntoma con tus palabras.
2. **Dónde:** qué servicio, fichero o bloque está implicado (Nginx, `compose.yaml`, la validación, la sesión…).
3. **Por qué:** la causa técnica.
4. **Qué cambiarías:** el cambio mínimo, en palabras o en código.
5. **Cómo lo comprobarías:** qué harías o qué evidencia mirarías (`docker compose ps`, `logs`, el navegador, una prueba con datos correctos e incorrectos, una ventana de incógnito…).

!!! example "Ejemplo de respuesta corta"
    *El navegador descarga el `index.php`.* → **Qué:** el PHP no se ejecuta. **Dónde:** Nginx, en `default.conf`. **Por qué:** falta el bloque `location ~ \.php$` con `fastcgi_pass php:9000`, así que Nginx lo trata como un fichero normal. **Cambio:** añadir ese bloque y reiniciar Nginx. **Comprobación:** recargar la página y revisar `docker compose logs nginx`.

---

## Plan de estudio hasta el 3 de diciembre

Sesiones cortas (30–50 minutos). En cada sesión: leer un poco, explicarlo en voz alta con tus palabras y responder preguntas **sin mirar la solución**.

### Semana 1 · UT1 (14–19 de noviembre)

| Día | Qué hacer |
| --- | --- |
| Vie 14 | Idea 1: recorrido de una petición. Dibujar el camino de un PDF y de un `.php`. |
| Sáb 15 | Idea 1: qué pasa si cae cada servicio. Preguntas tipo examen 1 y 2. |
| Dom 16 | Descanso o repaso ligero. |
| Lun 17 | Idea 2: puertos, volúmenes y `init.sql`. Pregunta tipo examen 3. |
| Mar 18 | Idea 2: `.env`, `environment`, `.env.example` y `.gitignore`. |
| Mié 19 | Repasar el `compose.yaml` y el `default.conf` de la práctica UT1 y explicar cada línea en voz alta. |

### Semana 2 · UT2 (20–26 de noviembre)

| Día | Qué hacer |
| --- | --- |
| Jue 20 | Idea 3: flujo GET/POST de un formulario. Repasar el `index.php` de la práctica 1 bloque a bloque. |
| Vie 21 | Idea 3: validación, `$errores`, `foreach`, conservar valores. Preguntas tipo examen 4 y 5. |
| Sáb 22 | Idea 3: pensar variantes (otro plan, otro mínimo de meses, otro extra) y qué bloque cambiaría. |
| Dom 23 | Descanso o repaso ligero. |
| Lun 24 | Idea 4: variable normal vs sesión vs cookie. Contador con sesión. |
| Mar 25 | Idea 4: login, protección del panel y logout en la práctica 2. Pregunta tipo examen 6. |
| Mié 26 | Idea 4: variantes (nuevo usuario, última hora de acceso, otra preferencia, otra condición de acceso). |

### Semana 3 · Repaso y simulacro (27 de noviembre – 2 de diciembre)

| Día | Qué hacer |
| --- | --- |
| Jue 27 | Repetir todas las preguntas tipo examen **sin mirar** las soluciones. |
| Vie 28 | Repasar solo las que hayan salido mal. |
| Sáb 29 | Simulacro: 4 preguntas seguidas, por escrito, con tiempo. |
| Dom 30 | Descanso. |
| Lun 1 | Repasar las 4 ideas y los errores típicos. |
| Mar 2 | Repaso muy ligero: leer esta página y las chuletas. Dormir bien. |

---

## Checklist antes del examen

- [ ] Sé dibujar el recorrido de una petición estática y de una dinámica.
- [ ] Sé qué servicio falla según el síntoma (descarga del PHP, 502, conexión a BD, tabla inexistente…).
- [ ] Sé explicar `"8080:80"`, los dos tipos de volumen y por qué `init.sql` solo se ejecuta una vez.
- [ ] Sé por qué una variable del `.env` no llega a PHP si no está en `environment`.
- [ ] Sé explicar el flujo GET/POST de un formulario y qué hace `name`, `method` y `action`.
- [ ] Sé cómo se recoge un checkbox y cómo se conservan los valores tras un error.
- [ ] Sé qué bloque cambiar para añadir un plan, un extra o una validación nueva.
- [ ] Sé la diferencia entre variable normal, cookie y sesión.
- [ ] Sé explicar el flujo login → sesión → panel → logout y cómo se protege el panel.
- [ ] Sé cómo comprobar que dos usuarios no comparten la sesión.
