# UT2 · 3. Servicios y systemd

## ¿Qué es un servicio?

Un **servicio** es un proceso que se ejecuta en segundo plano y proporciona una funcionalidad al sistema o a los usuarios. Ejemplos habituales: Apache/Nginx, MySQL/PostgreSQL o SSH.

Linux ha tenido diferentes sistemas de inicio, como SysVinit y Upstart. El tema se centra en **systemd**, que organiza servicios mediante unidades (*units*).

Las unidades se encuentran habitualmente en rutas como:

```text
/etc/systemd/system
/lib/systemd/system
```

## `systemctl`

Órdenes que debes dominar:

```bash
systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
sudo systemctl enable ssh
sudo systemctl disable ssh
```

No confundas **start** y **enable**:

- `start` → inicia el servicio **ahora**.
- `enable` → configura que se inicie durante el arranque.

Para hacer las dos cosas:

```bash
sudo systemctl enable --now ssh
```

Y para deshabilitar y detener:

```bash
sudo systemctl disable --now ssh
```

## Listar servicios

```bash
systemctl list-units --type=service
```

## Flujo de diagnóstico sencillo

Si un servicio no funciona:

```bash
systemctl status ssh
```

Mira si está activo, si ha fallado y los mensajes que aparecen. Después puedes consultar el journal:

```bash
journalctl -u ssh
```

Para ver mensajes recientes:

```bash
journalctl -u ssh -n 50
```

## Ejemplo mental de examen

**Pregunta:** «Quiero que SSH se inicie ahora y también automáticamente después de reiniciar.»

```bash
sudo systemctl enable --now ssh
```

**Pregunta:** «Quiero reiniciar el servicio porque he cambiado la configuración.»

```bash
sudo systemctl restart ssh
```

**Pregunta:** «Solo quiero saber qué le pasa.»

```bash
systemctl status ssh
```

!!! tip
    Antes de memorizar órdenes, diferencia tres ideas: **estado actual**, **acción ahora** y **comportamiento en el arranque**.