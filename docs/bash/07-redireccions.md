# 7. Redireccions i tuberies

Tot procés té tres canals:

| Núm. | Nom | Per defecte |
| ---- | --- | ----------- |
| 0 | stdin (entrada) | teclat |
| 1 | stdout (eixida) | pantalla |
| 2 | stderr (errors) | pantalla |

## Redireccions

| Sintaxi | Què fa |
| ------- | ------ |
| `ord > f` | eixida a `f` (el **sobreescriu**) |
| `ord >> f` | eixida al final de `f` (**afig**) |
| `ord 2> f` | errors a `f` |
| `ord > f 2>&1` | eixida i errors al mateix fitxer |
| `ord &> f` | igual que l'anterior (forma curta de Bash) |
| `ord < f` | llig l'entrada de `f` |
| `ord > /dev/null` | descarta l'eixida |
| `ord &> /dev/null` | descarta-ho tot |

```bash
find / -name "*.conf" 2> /dev/null          # sense els "Permission denied"
./backup.sh >> /var/log/backup.log 2>&1     # tot al log
echo "Error: fitxer no trobat" >&2          # escriure un error a stderr
```

!!! warning "L'ordre importa"
    `ord > f 2>&1` → tot a `f` ✅
    `ord 2>&1 > f` → els errors van a la pantalla ❌ (s'apunten on apuntava stdout *abans*).

## Tuberies `|`

L'eixida d'una ordre passa com a entrada de la següent:

```bash
ps aux | grep nginx | grep -v grep
cut -d: -f7 /etc/passwd | sort | uniq -c | sort -rn   # shells més usats
du -sh /var/log/* 2>/dev/null | sort -h | tail -5     # 5 coses més grans
```

Per defecte, el codi d'eixida d'una tuberia és el de **l'última** ordre. Amb `set -o pipefail` falla si qualsevol falla.

## `tee`: veure i guardar alhora

```bash
./instal·la.sh | tee instal·lacio.log       # pantalla + fitxer
echo "nameserver 1.1.1.1" | sudo tee -a /etc/resolv.conf   # escriure com a root
```

`sudo echo x > /etc/f` **no** funciona: la redirecció la fa el teu shell, no root. Per això s'usa `| sudo tee`.

## Here-document: text de diverses línies

```bash
cat > /etc/motd << EOF
Benvingut a $(hostname)
Administrador: $USER
EOF
```

Amb `<< 'EOF'` (entre cometes) no s'expandixen les variables. Amb `<<- EOF` es lleven les tabulacions inicials (útil dins d'un `if`).

Here-string, per a una sola línia:

```bash
read -r a b c <<< "un dos tres"
bc <<< "scale=2; 7/3"
```

## Agrupar ordres

```bash
{ date; uptime; df -h /; } > informe.txt   # mateix shell, eixida conjunta
( cd /tmp && tar czf b.tgz dades )         # subshell: el cd no t'afecta
```

Amb `{ }` cal un espai després de `{` i un `;` abans de `}`.

## Substitució de processos

Tracta l'eixida d'una ordre com si fora un fitxer:

```bash
diff <(ls dir1) <(ls dir2)
while read -r l; do ...; done < <(find . -name "*.sh")   # sense perdre variables
```
