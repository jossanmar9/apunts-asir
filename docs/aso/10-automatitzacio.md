# UT2 · 4. Automatización: cron y at

## Cuándo usar cada herramienta

- **cron** → tareas que se repiten periódicamente.
- **at** → una tarea que debe ejecutarse **una sola vez** en un momento futuro.

## `cron`

`cron` es un demonio que revisa periódicamente los *crontabs* buscando trabajos programados.

Editar el crontab del usuario:

```bash
crontab -e
```

Listarlo:

```bash
crontab -l
```

Una línea de cron tiene cinco campos temporales antes de la orden:

```text
minuto hora dia_mes mes dia_semana orden
```

Ejemplo: ejecutar una copia cada día a las 02:30:

```cron
30 2 * * * /home/alumno/copia.sh
```

Ejemplo: cada lunes a las 08:00:

```cron
0 8 * * 1 /home/alumno/informe.sh
```

Ejemplo: cada 15 minutos:

```cron
*/15 * * * * /home/alumno/comprobar.sh
```

## Cómo leer una expresión cron

```cron
0 23 * * 5 /home/alumno/backup.sh
```

Léela de izquierda a derecha:

1. minuto `0`
2. hora `23`
3. cualquier día del mes
4. cualquier mes
5. día de la semana `5`

→ viernes a las 23:00.

!!! warning "Error típico"
    En `cron` es mejor usar **rutas absolutas**. El entorno no es necesariamente el mismo que tienes en la terminal interactiva.

Para guardar salida y errores:

```cron
0 2 * * * /home/alumno/copia.sh >> /home/alumno/copia.log 2>&1
```

## `at`: una sola ejecución

Ejemplo interactivo:

```bash
at 18:30
```

Después escribes la orden y finalizas la entrada.

También puedes enviar una orden por pipe:

```bash
echo "/home/alumno/copia.sh" | at 18:30
```

Listar tareas pendientes:

```bash
atq
```

Eliminar la tarea 14:

```bash
atrm 14
```

## ¿Cron o at?

| Necesidad | Herramienta |
|---|---|
| copia cada noche | `cron` |
| informe cada lunes | `cron` |
| apagar una vez esta noche | `at` |
| ejecutar un script dentro de una hora | `at` |

## Ejemplo de administración

Script:

```bash
#!/bin/bash
ahora=$(date '+%F %T')
echo "$ahora - copia ejecutada" >> /home/alumno/backup.log
```

Crontab:

```cron
0 3 * * * /home/alumno/backup.sh
```

Esto combina Bash con automatización real: el script realiza la tarea y `cron` decide **cuándo** se ejecuta.