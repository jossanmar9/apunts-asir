# UT1 · 1. Bash: scripts, variables, entrada i paràmetres

## Què executa Bash?

Una shell interpreta ordres. Un script guarda ordres en un fitxer perquè pugues repetir el procés. La primera línia `#!/usr/bin/env bash` indica l'intèrpret quan l'executes directament. Amb `bash nom.sh` tries Bash explícitament; amb `./nom.sh` necessites permís d'execució, que pots donar amb `chmod u+x nom.sh`.

En Bash, `nom=valor` assigna i `$nom` expandeix el valor. No poses espais al voltant de `=`. Les cometes dobles conserven els espais d'una dada però expandeixen variables; les simples tracten el contingut literalment. Els comentaris comencen amb `#`.

## Exemple resolt: etiqueta d'una mostra de laboratori

Desa `etiqueta.sh`:

```bash
#!/usr/bin/env bash
if (( $# != 2 )); then
    printf 'Ús: bash etiqueta.sh mostra responsable\n' >&2
    exit 1
fi
mostra=$1
responsable=$2
read -r -p 'Ubicació de la mostra: ' ubicacio
printf 'Mostra: %s\nResponsable: %s\nUbicació: %s\n' \
    "$mostra" "$responsable" "$ubicacio"
```

Executa `bash etiqueta.sh "Roca volcànica" "Laia Ferrer"` i escriu `Armari blau`.

**Resultat esperat:** tres línies amb la mostra, el nom complet i la ubicació. Les cometes fan que cada frase siga un argument. Sense cometes, el nombre d'arguments canviaria i el script mostraria l'ajuda.

### Pas a pas

1. `$#` compta arguments. Si no són dos, el missatge va a l'eixida d'error amb `>&2` i el codi final és 1.
2. `$1` i `$2` són les dades de la crida. `$0` és el nom amb què s'ha invocat el script.
3. `read -r` llig una línia sense tractar les barres invertides com a escapes.
4. `printf` usa un format fix i dades separades. `%s` substitueix text i `\n` salta de línia.

## Variables que convé reconéixer

| Expressió | Significat |
| --- | --- |
| `"$@"` | Tots els arguments, preservant cadascun |
| `$?` | Codi de l'última ordre, que canvia en executar la següent |
| `$$` | Identificador del procés de la shell |
| `${nom:-alternativa}` | Alternativa si no existeix o està buit |
| `$(ordre)` | Captura l'eixida estàndard de l'ordre |

Una variable de shell no passa necessàriament als processos fills. `export COLOR_FITXA=blau` la incorpora a l'entorn dels nous processos. `printenv COLOR_FITXA` la consulta. Usa noms propis del teu script: no sobreescrigues `PATH` amb una ruta de treball, perquè deixaries de localitzar ordres.

## Transformar text i guardar col·leccions

```bash
#!/usr/bin/env bash
fitxer='mostra.versio.txt'
printf '%s\n' "${fitxer%.txt}" "${fitxer:0:6}"
sales=('Sala blau cel' 'Sala grisa')
printf '%s\n' "${sales[0]}" "${#sales[@]}"
```

El primer bloc mostra `mostra.versio` i `mostra`. `%` elimina el sufix que coincideix amb el patró; `${text#patro}` elimina un prefix; les versions dobles `%%` i `##` eliminen la coincidència més llarga. `${text:inici:longitud}` extrau una subcadena. Els arrays indexats comencen en zero i `"${sales[@]}"` conserva cada element.

| Error | Solució |
| --- | --- |
| `nom = valor` | Escriu `nom=valor`. |
| Nom amb espais es parteix | Usa `"$nom"` en passar-lo a una ordre. |
| Arguments buits o desplaçats | Revisa les cometes en la crida i `$#`. |

!!! success "Per a repassar"
    Diferencia una variable, un argument i una entrada per teclat. Segueix sempre com arriben les dades al programa.

---

Font del temari: [apunts originals d’ASO](https://angelabserrano.github.io/aso/linux/bash/). Explicació i casos didàctics propis. Consulta: 26/10/2026.
