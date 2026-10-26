# Git y GitHub

Tema independiente y transversal a IAW, ASO y Python. Cubre la introducción de UT0 de ASO: guardar, revisar y compartir cambios.

## ¿Qué guarda cada herramienta?

Git es el programa que conserva el historial en tu equipo. GitHub aloja una copia remota y ofrece colaboración. Puedes hacer commits sin conexión; para enviarlos al remoto necesitas red y permisos.

```mermaid
flowchart LR
    A[Archivos editados] -->|git add| B[Preparación]
    B -->|git commit| C[Historial local]
    C -->|git push| D[Remoto]
```

`git add` selecciona el contenido que entrará en el próximo commit. Si después vuelves a editar el archivo, la nueva edición todavía no está preparada. `git pull` obtiene e integra cambios remotos; puede producir conflictos que debes revisar.

## Caso resuelto: corregir un inventario de cables

**Objetivo propio:** registrar que el stock real es de 8 cables. Crea una carpeta de laboratorio que no esté dentro de otro repositorio. Este ejemplo es local y no crea ni envía nada a GitHub.

```bash
mkdir inventario-lab
cd inventario-lab
git init
git config user.name "Estudiante de pruebas"
git config user.email "estudiante@example.com"
printf 'Cables: 7\n' > inventario.txt
git add inventario.txt
git commit -m "Registra el inventario inicial"
printf 'Cables: 8\n' > inventario.txt
git diff
git add inventario.txt
git diff --cached
git commit -m "Corrige el recuento de cables"
git status --short
git log --oneline
```

### ¿Qué compruebas en cada paso?

1. `init` crea el historial vacío. `clone URL` sería la alternativa para un proyecto existente; no debes hacer `init` dentro de un clon.
2. La configuración sin `--global` se aplica solo al laboratorio. Nombre y correo identifican al autor; no autentican el acceso a GitHub.
3. El primer commit guarda 7. Después, `diff` muestra una línea eliminada con 7 y otra añadida con 8.
4. `diff --cached` permite revisar exactamente el cambio preparado.
5. Después del segundo commit, `status --short` no muestra cambios pendientes. `log` muestra dos commits, con identificadores variables.

**Para los trabajos:** revisa `status` y el diff antes del commit. Un mensaje como «Valida campos vacíos del formulario» explica mejor el cambio que «cosas».

## Conexión con GitHub y SSH

En un repositorio con remoto y rama configurados, `git push` envía commits y `git pull` integra los del remoto. `git remote -v` permite comprobar a qué repositorio apuntas. Si la primera subida lo requiere, `git push -u origin NOMBRE_RAMA` vincula la rama local con la remota; sustituye el nombre por el real.

Una clave SSH tiene una parte pública y otra privada. GitHub recibe la **pública**, terminada en `.pub`. La privada se queda en tu equipo. `ssh -T git@github.com` comprueba la autenticación SSH; un mensaje de autenticación correcta puede ir acompañado de un código de salida distinto de cero porque GitHub no ofrece una shell interactiva.

## Errores típicos

| Síntoma | Causa probable |
| --- | --- |
| `nothing to commit` | No hay cambios preparados o no hay cambios nuevos. |
| Veo el commit local, pero no en GitHub | Falta `push`, ha fallado o miras otra rama. |
| `Permission denied (publickey)` | Clave, agente SSH o cuenta sin acceso. |
| Rechazo porque el remoto ha avanzado | Revisa e integra los cambios remotos antes de enviar. |

!!! success "Para repasar"
    Editar, preparar, guardar localmente y enviar son cuatro pasos diferentes. Explica en qué estado está tu cambio antes de repetir comandos.

---

Fuente del temario: [apuntes originales de ASO](https://angelabserrano.github.io/aso/git/introduccion/). Explicación y casos didácticos propios. Consulta: 26/10/2026.
