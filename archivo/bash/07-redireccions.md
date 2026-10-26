# 7. Redireccions i tuberies

## Les tres "vies" de cada programa

Tot programa té tres canals de comunicació:

| Número | Nom | Per a què | Normalment va a... |
| ------ | --- | --------- | ------------------ |
| 0 | **entrada** (stdin) | el que rep el programa | el teclat |
| 1 | **eixida** (stdout) | el resultat normal | la pantalla |
| 2 | **errors** (stderr) | els missatges d'error | la pantalla |

Per això, quan executes una ordre, veus en pantalla tant el resultat com els errors: tots dos van a la pantalla per defecte. Però **els pots enviar a altres llocs**. Això és una **redirecció**.

## Guardar l'eixida en un fitxer

| S'escriu | Què fa |
| -------- | ------ |
| `ordre > fitxer` | guarda l'eixida en el fitxer. **Si ja existia, l'esborra i el torna a escriure** |
| `ordre >> fitxer` | **afig** l'eixida al final del fitxer, sense esborrar el que hi havia |

```bash
date > registre.txt         # registre.txt només té la data
date >> registre.txt        # ara té dues dates, una davall de l'altra
ls -l /etc > llista.txt     # guarda el llistat en un fitxer en compte de mostrar-lo
```

!!! danger "`>` esborra el fitxer"
    Si fas `echo "hola" > notes.txt` i `notes.txt` tenia coses, **les perds**. Si vols afegir, usa `>>`.

## Guardar o amagar els errors

```bash
ls /no_existix 2> errors.txt        # els errors van al fitxer, no a la pantalla
```

El `2` davant de `>` vol dir "el canal 2" (errors).

### `/dev/null`: la paperera

`/dev/null` és un fitxer especial: tot el que s'hi envia desapareix. S'usa per a **amagar** coses:

```bash
find / -name "*.conf" 2> /dev/null      # amaga els errors "Permission denied"
ping -c1 google.com > /dev/null         # amaga l'eixida normal
ping -c1 google.com &> /dev/null        # amaga-ho tot (eixida i errors)
```

### Tot al mateix fitxer

```bash
./backup.sh > registre.log 2>&1         # eixida i errors al mateix fitxer
./backup.sh &> registre.log             # forma curta del mateix
```

`2>&1` vol dir "envia els errors (2) al mateix lloc que l'eixida (1)".

### Escriure un missatge d'error des de l'script

```bash
echo "Error: el fitxer no existix" >&2
```

`>&2` envia el missatge pel canal d'errors. És el correcte per als missatges d'error dels teus scripts.

## Llegir d'un fitxer

```bash
wc -l < /etc/passwd        # wc llig del fitxer: mostra només el número de línies
```

## Tuberies: `|`

La **tuberia** (`|`, la barra vertical, ++altgr+1++) agafa **l'eixida d'una ordre** i la passa com a **entrada de la següent**. Així pots encadenar ordres senzilles per a fer coses complexes.

```bash
ls /etc | wc -l
```

1. `ls /etc` fa la llista de fitxers de `/etc`.
2. En compte de mostrar-la, la passa a `wc -l`.
3. `wc -l` compta les línies → resultat: quants fitxers hi ha en `/etc`.

Més exemples:

```bash
cat /etc/passwd | grep "bash"                  # només les línies que tenen "bash"
ps aux | grep nginx                            # busca el procés nginx
cut -d: -f7 /etc/passwd | sort | uniq -c       # quants usuaris usen cada shell
history | tail -5                              # les 5 últimes ordres
```

Es llig d'esquerra a dreta, com una cadena de muntatge: cada ordre fa una feina i passa el resultat a la següent.

## `tee`: veure i guardar alhora

`tee` mostra per pantalla **i** guarda en un fitxer:

```bash
ls -l | tee llista.txt        # ho veus i a més queda guardat
ls -l | tee -a llista.txt     # -a: afig en compte d'esborrar
```

També s'usa per a escriure en fitxers del sistema com a root:

```bash
echo "nameserver 1.1.1.1" | sudo tee -a /etc/resolv.conf
```

(`sudo echo ... > /etc/fitxer` **no funciona**, perquè la redirecció la fa el teu usuari, no root.)

## Escriure diverses línies en un fitxer (here-document)

```bash
cat > config.txt << FI
servidor=web01
port=80
usuari=$USER
FI
```

Tot el que hi ha entre `<< FI` i la paraula `FI` es guarda en el fitxer. La paraula pot ser qualsevol (`EOF` és la més habitual). Les variables (`$USER`) es canvien pel seu valor.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| He perdut el contingut d'un fitxer | Has usat `>` en compte de `>>` | `>>` per a afegir |
| Els errors continuen eixint en pantalla | Has redirigit només l'eixida (`>`) | Afig `2> /dev/null` o usa `&>` |
| `sudo echo x > /etc/f` → `Permission denied` | La redirecció no la fa root | <code>echo x &#124; sudo tee /etc/f</code> |
| `ordre 2>&1 > f` no guarda els errors | L'ordre importa | `ordre > f 2>&1` |

!!! success "Per a l'examen"
    | Vull... | S'escriu |
    | ------- | -------- |
    | guardar l'eixida (esborrant) | `ordre > f` |
    | afegir l'eixida | `ordre >> f` |
    | guardar els errors | `ordre 2> f` |
    | amagar els errors | `ordre 2> /dev/null` |
    | amagar-ho tot | `ordre &> /dev/null` |
    | tot al mateix fitxer | `ordre > f 2>&1` |
    | missatge d'error | `echo "..." >&2` |
    | passar l'eixida a una altra ordre | <code>ordre1 &#124; ordre2</code> |
    | veure i guardar | <code>ordre &#124; tee f</code> |
