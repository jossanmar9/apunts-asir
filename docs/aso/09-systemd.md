# UT2 · 3. Serveis i systemd

## Què és un servei?

Un **servei** és un procés que s'executa en segon pla i proporciona una funcionalitat al sistema o als usuaris. Exemples habituals: Apache/Nginx, MySQL/PostgreSQL o SSH.

Linux ha tingut diferents sistemes d'inici, com SysVinit i Upstart. El tema se centra en **systemd**, que organitza serveis mitjançant unitats (*units*).

Les unitats es troben habitualment en rutes com:

```text
/etc/systemd/system
/lib/systemd/system
```

## `systemctl`

Ordres que has de dominar:

```bash
systemctl status ssh
sudo systemctl start ssh
sudo systemctl stop ssh
sudo systemctl restart ssh
sudo systemctl enable ssh
sudo systemctl disable ssh
```

No confongues **start** i **enable**:

- `start` → inicia el servei **ara**.
- `enable` → configura que s'inicie durant l'arrancada.

Per fer les dues coses:

```bash
sudo systemctl enable --now ssh
```

I per deshabilitar i parar:

```bash
sudo systemctl disable --now ssh
```

## Llistar serveis

```bash
systemctl list-units --type=service
```

## Flux de diagnòstic senzill

Si un servei no funciona:

```bash
systemctl status ssh
```

Mira si està actiu, si ha fallat i els missatges que apareixen. Després pots consultar el journal:

```bash
journalctl -u ssh
```

Per veure missatges recents:

```bash
journalctl -u ssh -n 50
```

## Exemple mental d'examen

**Pregunta:** «Vull que SSH s'inicie ara i també automàticament després de reiniciar.»

```bash
sudo systemctl enable --now ssh
```

**Pregunta:** «Vull reiniciar el servei perquè he canviat la configuració.»

```bash
sudo systemctl restart ssh
```

**Pregunta:** «Només vull saber què li passa.»

```bash
systemctl status ssh
```

!!! tip
    Abans de memoritzar ordres, diferencia tres idees: **estat actual**, **acció ara** i **comportament en l'arrancada**.