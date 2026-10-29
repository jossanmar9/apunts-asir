# UT2 · 4. Automatització: cron i at

## Quan usar cada eina

- **cron** → tasques que es repeteixen periòdicament.
- **at** → una tasca que s'ha d'executar **una sola vegada** en un moment futur.

## `cron`

`cron` és un dimoni que revisa periòdicament els *crontabs* buscant treballs programats.

Editar el crontab de l'usuari:

```bash
crontab -e
```

Llistar-lo:

```bash
crontab -l
```

Una línia de cron té cinc camps temporals abans de l'ordre:

```text
minut hora dia_mes mes dia_setmana ordre
```

Exemple: executar una còpia cada dia a les 02:30:

```cron
30 2 * * * /home/alumne/copia.sh
```

Exemple: cada dilluns a les 08:00:

```cron
0 8 * * 1 /home/alumne/informe.sh
```

Exemple: cada 15 minuts:

```cron
*/15 * * * * /home/alumne/comprovar.sh
```

## Com llegir una expressió cron

```cron
0 23 * * 5 /home/alumne/backup.sh
```

Llig-la d'esquerra a dreta:

1. minut `0`
2. hora `23`
3. qualsevol dia del mes
4. qualsevol mes
5. dia de setmana `5`

→ divendres a les 23:00.

!!! warning "Error típic"
    En `cron` és millor usar **rutes absolutes**. L'entorn no és necessàriament el mateix que tens al terminal interactiu.

Per guardar eixida i errors:

```cron
0 2 * * * /home/alumne/copia.sh >> /home/alumne/copia.log 2>&1
```

## `at`: una sola execució

Exemple interactiu:

```bash
at 18:30
```

Després escrius l'ordre i finalitzes l'entrada.

També pots enviar una ordre per pipe:

```bash
echo "/home/alumne/copia.sh" | at 18:30
```

Llistar tasques pendents:

```bash
atq
```

Eliminar la tasca 14:

```bash
atrm 14
```

## Cron o at?

| Necessitat | Eina |
|---|---|
| còpia cada nit | `cron` |
| informe cada dilluns | `cron` |
| apagar una vegada esta nit | `at` |
| executar un script d'ací a una hora | `at` |

## Exemple d'administració

Script:

```bash
#!/bin/bash
ara=$(date '+%F %T')
echo "$ara - còpia executada" >> /home/alumne/backup.log
```

Crontab:

```cron
0 3 * * * /home/alumne/backup.sh
```

Açò combina Bash amb automatització real: el script fa la tasca i `cron` decideix **quan** s'executa.