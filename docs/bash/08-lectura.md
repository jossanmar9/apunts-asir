# 8. Llegir dades

## `read`

```bash
read -p "Nom: " nom
echo "Hola $nom"
```

| Opció | Què fa |
| ----- | ------ |
| `-p "text"` | mostra un missatge abans |
| `-r` | no interpreta `\` (posa-la sempre) |
| `-s` | no mostra el que escrius (contrasenyes) |
| `-n N` | acaba després de N caràcters (sense Intro) |
| `-t N` | temps màxim en segons; si s'esgota, torna error |
| `-a arr` | guarda les paraules en un array |
| `-d ':'` | llig fins a `:` en compte de fins a Intro |

```bash
read -rsp "Contrasenya: " pass; echo
read -rn1 -p "Continuar? (s/n) " r; echo
read -rt 10 -p "Tens 10 s: " resp || echo "Temps esgotat"
read -ra parts <<< "192 168 1 10"; echo "${parts[2]}"   # 1
```

Si li dones diverses variables, reparteix les paraules i l'última es queda la resta:

```bash
read -r nom cognoms <<< "Jose Vicente Sanjuan"
echo "$cognoms"     # Vicente Sanjuan
```

## Argument o `read`?

!!! tip "Llig bé l'enunciat"
    Si diu "**com a argument**" o "**per paràmetre**", usa `$1`, `$2`... i **no** `read`. Si diu "**demana a l'usuari**" o "**per teclat**", usa `read`.

Un patró habitual: usar l'argument si existix i, si no, preguntar.

```bash
dir=$1
[ -z "$dir" ] && read -rp "Directori: " dir
```

## Validar el que escriu l'usuari

```bash
while true; do
    read -rp "Edat: " edat
    [[ $edat =~ ^[0-9]+$ ]] && (( edat <= 120 )) && break
    echo "Valor no vàlid, torna-ho a provar"
done
```

## Menús amb `select`

`select` genera un menú numerat automàticament:

```bash
PS3="Tria una opció: "
select op in "Espai en disc" "Memòria" "Usuaris connectats" "Eixir"; do
    case $REPLY in
        1) df -h ;;
        2) free -h ;;
        3) who ;;
        4) break ;;
        *) echo "Opció no vàlida" ;;
    esac
done
```

`$REPLY` és el número triat i `$op` el text.

## Finestres gràfiques: `zenity`

En un escriptori gràfic es poden fer diàlegs senzills:

```bash
nom=$(zenity --entry --title="Alta" --text="Nom de l'usuari:")
zenity --question --text="Crear $nom?" && echo "Sí"
zenity --info --text="Fet"
opcio=$(zenity --list --column="Opció" "Processos" "Disc" "Eixir")
```

`zenity` torna 0 si l'usuari prem *Acceptar* i 1 si prem *Cancel·lar*.
