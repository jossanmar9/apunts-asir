# 4. Condicionals

## `if`

```bash
if CONDICIÓ; then
    ordres
elif ALTRA_CONDICIÓ; then
    ordres
else
    ordres
fi
```

La CONDICIÓ és **qualsevol ordre**: si torna 0, és certa. Per això funciona tant amb `[ ]` com amb ordres normals:

```bash
if grep -q "^$usuari:" /etc/passwd; then
    echo "L'usuari $usuari existix"
fi

if ping -c1 -W1 8.8.8.8 &> /dev/null; then
    echo "Hi ha Internet"
fi
```

`grep -q` no mostra res, només torna el codi. És la manera neta de preguntar "conté açò?".

### L'ordre dels `elif` importa

Quan arribes a un `elif`, ja saps que les condicions anteriors eren falses, així que no cal repetir-les:

```bash
if (( us < 70 )); then
    echo "OK"
elif (( us < 90 )); then      # ja sé que us >= 70
    echo "AVÍS"
else                          # ja sé que us >= 90
    echo "CRÍTIC"
fi
```

## `case`

Quan compares **la mateixa variable** amb molts valors, `case` és més clar que una cadena de `elif`:

```bash
case "$1" in
    start)
        systemctl start nginx ;;
    stop)
        systemctl stop nginx ;;
    restart|reload)
        systemctl restart nginx ;;
    *)
        echo "Ús: $0 {start|stop|restart}" >&2
        exit 1 ;;
esac
```

- Cada opció acaba en `;;`.
- `|` separa alternatives.
- `*)` és "qualsevol altra cosa" (com l'`else`).
- Accepta patrons: `*.jpg|*.png)`, `[sS]|[sS][iI])`, `[0-9])`.

```bash
read -p "Vols continuar? (s/n) " resp
case "$resp" in
    [sS]*) echo "Continuem" ;;
    [nN]*) echo "Cancel·lat"; exit 0 ;;
    *)     echo "Resposta no vàlida" ;;
esac
```

## `&&` i `||` com a condicionals curts

```bash
[ -d "$dir" ] || mkdir -p "$dir"          # crea'l si no existix
cd "$dir" && echo "Ara estic en $dir"     # només si cd ha anat bé
[ $# -eq 1 ] || { echo "Ús: $0 fitxer"; exit 1; }
```

!!! warning "`a && b || c` no és un if/else"
    Si `b` falla, també s'executa `c`. Per a lògica de veritat, usa `if`.
