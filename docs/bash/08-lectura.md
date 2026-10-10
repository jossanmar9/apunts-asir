# 8. Llegir dades

## Demanar dades a l'usuari: `read`

`read` para l'script i espera que l'usuari escriga alguna cosa i prema ++enter++. El que escriu es guarda en una variable.

```bash
echo "Com et dius?"
read nom
echo "Hola, $nom"
```

Més còmode, amb el missatge en la mateixa línia (`-p` de *prompt*):

```bash
read -p "Com et dius? " nom
echo "Hola, $nom"
```

```console
Com et dius? Ana
Hola, Ana
```

### Opcions útils de `read`

| Opció | Què fa | Exemple |
| ----- | ------ | ------- |
| `-p "text"` | mostra un missatge abans | `read -p "Nom: " nom` |
| `-r` | llig les `\` tal qual (posa-la sempre) | `read -r linia` |
| `-s` | no mostra el que s'escriu (per a contrasenyes) | `read -s -p "Clau: " clau` |
| `-n 1` | llig només 1 caràcter, sense esperar ++enter++ | `read -n 1 -p "s/n: " r` |
| `-t 10` | espera com a màxim 10 segons | `read -t 10 -p "Ràpid: " r` |

```bash
read -s -p "Contrasenya: " clau
echo                           # salt de línia (amb -s no es fa sol)
```

### Llegir diverses dades d'una vegada

Si poses diverses variables, `read` reparteix les paraules:

```bash
read -p "Nom i edat: " nom edat
# si escrius: Ana 30
# nom=Ana, edat=30
```

Si hi ha més paraules que variables, l'última variable es queda amb tota la resta:

```bash
read -r nom cognoms <<< "Laura Pons Ferrer"
echo "$cognoms"     # Pons Ferrer
```

(`<<< "text"` passa el text a `read` com si l'haguera escrit l'usuari.)

## Argument o `read`? Llig bé l'enunciat

Esta és una confusió molt habitual en els exàmens:

| Si l'enunciat diu... | Usa | Exemple d'execució |
| -------------------- | --- | ------------------ |
| "**per argument**", "**per paràmetre**", "**que reba**" | `$1`, `$2`... | `./script.sh 5` |
| "**que demane**", "**per teclat**", "**que pregunte**" | `read` | `./script.sh` i després escrius |

```bash
# Per argument:
numero=$1

# Per teclat:
read -p "Escriu un número: " numero
```

## Validar el que escriu l'usuari

L'usuari pot escriure qualsevol cosa. Per a assegurar-te que és vàlid, torna-li a preguntar fins que ho siga:

```bash
while true; do
    read -p "Escriu la teua edat: " edat
    if [[ $edat =~ ^[0-9]+$ ]]; then    # si és un número...
        break                            # ...ix del bucle
    fi
    echo "Això no és un número. Torna-ho a provar."
done
echo "Tens $edat anys"
```

## Menús automàtics: `select`

`select` crea un menú numerat sense haver de fer-lo a mà:

```bash
PS3="Tria una opció: "
select opcio in "Veure la data" "Veure el disc" "Eixir"; do
    case $REPLY in
        1) date ;;
        2) df -h ;;
        3) break ;;
        *) echo "Opció no vàlida" ;;
    esac
done
```

```console
1) Veure la data
2) Veure el disc
3) Eixir
Tria una opció: 1
dissabte, 10 d’octubre de 2026, 18:15:02 CEST
Tria una opció: 3
```

- `PS3` és el missatge que mostra per a preguntar.
- `$REPLY` és el **número** que ha escrit l'usuari.
- `$opcio` és el **text** de l'opció triada.
- Es repetix sol fins que fas `break`.

## Finestres gràfiques: `zenity`

Si treballes en un escriptori gràfic, `zenity` mostra finestres en compte de preguntar en el terminal:

```bash
nom=$(zenity --entry --text="Com et dius?")       # finestra per a escriure
zenity --info --text="Hola, $nom"                 # finestra d'informació
zenity --question --text="Continuar?" && echo "Ha dit que sí"
```

`zenity` torna 0 si l'usuari prem *Acceptar* i 1 si prem *Cancel·lar*.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| L'script es queda parat | Està esperant en un `read` | Escriu alguna cosa i prem Intro |
| Has usat `read` i l'enunciat deia "per argument" | Confusió | Usa `$1` |
| `read $nom` | `read` vol el **nom** de la variable | `read nom` (sense `$`) |
| Amb `-s` el text següent ix enganxat | No fa salt de línia | Posa un `echo` buit després |

!!! success "Per a l'examen"
    ```bash
    read -p "Missatge: " var        # demanar una dada
    read -s -p "Clau: " clau; echo  # contrasenya
    read -r a b c                   # diverses dades
    ```

    - **"per argument"** → `$1` · **"per teclat"** → `read`
    - `read var`, **sense `$`**
    - Menú: `select op in "A" "B"; do case $REPLY in ...; esac; done`
