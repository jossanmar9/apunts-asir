# Com estudiar i aprendre més ràpid

Programar (Bash, PowerShell, Python, PHP) i usar eines com Git o Docker **no s'aprén llegint**: s'aprén **fent**. Esta pàgina és un mètode senzill per a estudiar menys hores i recordar més.

## 1. Fes, no llegisques

Llegir uns apunts dona la sensació que ho entens. Però fins que no ho escrius tu, no ho saps.

| ❌ Estudiar «passiu» | ✅ Estudiar «actiu» |
| -------------------- | ------------------- |
| Rellegir els apunts tres vegades | Llegir **un** exemple i escriure'l tu en el terminal |
| Subratllar | Canviar l'exemple i veure què passa |
| Veure vídeos un darrere l'altre | Fer un exercici **sense mirar** la solució |
| Copiar la solució | Intentar-ho 15 minuts, i només després mirar-la |

!!! tip "La regla dels 15 minuts"
    Quan comences un tema, els primers 15 minuts han de ser **fent** alguna cosa que funcione (un `hola.sh`, un `docker run hello-world`), no llegint teoria. Si funciona prompte, et quedes amb ganes de continuar.

**La trampa dels tutorials**: veure tutorial rere tutorial sense fer res teu és procrastinar disfressat d'estudiar. Després de cada tutorial, fes **alguna cosa diferent** amb el que has vist.

## 2. Una sessió d'estudi de 50 minuts

```text
 5 min   Recordar SENSE mirar: què vaig fer l'última vegada? (escriu-ho en un paper)
25 min   Fer: llegir un apartat i provar CADA exemple en el terminal
 5 min   Descans (lluny de la pantalla)
10 min   Un exercici sense mirar la solució
 5 min   Apuntar en la teua xuleta el que has après i els errors que t'han eixit
```

- **Màquina virtual** per a practicar: si la trenques, no passa res. Fes una **instantània** abans de provar coses perilloses.
- **El mòbil fora** de la taula. Cada interrupció costa uns minuts de tornar a concentrar-se.

## 3. Recordar, no rellegir (*active recall*)

El cervell aprén quan ha de **traure** la informació, no quan la torna a veure.

- Abans d'obrir els apunts, pregunta't: *«Com era el bucle `for` en Bash?»* Intenta escriure'l. Després comprova-ho.
- Tapa la solució dels exercicis i fes-los de nou uns dies després.
- Fes-te **targetes** (paper o una app com Anki): per davant la pregunta, per darrere la resposta.

| Davant | Darrere |
| ------ | ------- |
| Bash: comprovar si existix un fitxer | `if [[ -f "$fitxer" ]]; then ...` |
| Git: desfer l'últim commit sense perdre els canvis | `git reset --soft HEAD~1` |
| Docker: veure els contenidors parats | `docker ps -a` |
| PHP: evitar XSS | `htmlspecialchars($x)` |

## 4. Repetir espaiat

Repassar **poc i sovint** és molt millor que molt el dia abans de l'examen.

```text
Dia 0: aprens el tema      Dia 1: repàs ràpid (10 min)      Dia 3: repàs
Dia 7: repàs               Dia 15: exercici del tema sense mirar
```

Cada vegada costa menys. Si una cosa ja la saps, l'espaies més; si l'has oblidada, tornes a començar.

## 5. Explica-ho amb paraules senzilles (tècnica Feynman)

Si no ho saps explicar de manera senzilla, encara no ho entens del tot.

1. Tria un concepte: *«Què és un volum de Docker?»*
2. Explica-ho en veu alta (o per escrit) com si parlares amb algú que no sap res d'informàtica.
3. On t'entrebanques o necessites paraules tècniques, **ahí hi ha el forat**.
4. Torna als apunts per a eixe trosset i tornar-ho a explicar.

Explicar-ho a un company (o fer-li les preguntes) és el millor repàs que hi ha.

## 6. Els errors són la millor classe

Quan alguna cosa falla:

1. **Llig el missatge d'error sencer**, sense por. Quasi sempre diu què passa i on (la línia).
2. **Reprodueix-lo**: fes que torne a fallar de la mateixa manera. Si «a vegades falla», encara no saps per què.
3. **Divideix**: comenta la meitat del codi o prova cada ordre per separat fins a trobar la que falla.
4. **Busca** el missatge exacte (entre cometes) en el buscador.
5. **Apunta'l** en la teua xuleta: error → causa → solució. Cada tema d'estos apunts acaba amb una taula d'**errors típics** per això.

| Eina | Per a què |
| ---- | --------- |
| `bash -x script.sh` | veure cada línia que s'executa |
| [ShellCheck](https://www.shellcheck.net/) | trobar errors en scripts de Bash |
| `print()` / `echo` / `Write-Host` | veure el valor de les variables en un punt |
| `php -l fitxer.php` | comprovar la sintaxi de PHP |
| `git status` | saber en quin estat està el repositori **sempre** |
| `docker logs nom` | per què ha fallat un contenidor |

## 7. Problemes grans → problemes menuts

Un exercici difícil és només un grapat d'exercicis fàcils que encara no has separat.

!!! example "«Fes un script que faça una còpia de seguretat de /home cada nit i esborre les de més de 7 dies»"
    1. Fer un `tar` de `/home` a mà, en el terminal. ✔️
    2. Posar-li la data en el nom (`$(date +%F)`). ✔️
    3. Ficar-ho en un script i executar-lo. ✔️
    4. Esborrar les còpies velles amb `find -mtime +7 -delete` (provant-ho primer **sense** `-delete`). ✔️
    5. Programar-lo amb `cron`. ✔️

    Cada pas es prova abans de passar al següent. Vegeu el [mètode per a resoldre problemes](../bash/metode.md).

## 8. La teua xuleta

Fes una xuleta **pròpia** de cada llenguatge, d'una o dues pàgines, i ves-la completant. Escriure-la ja és estudiar. Les [xuletes d'esta web](../xuletes/index.md) són un punt de partida.

Un truc: tin un repositori de Git amb els teus exercicis i scripts. Fes **commits** amb missatges clars cada vegada que acabes un exercici. Al final del curs tindràs tot el que has fet, i practicaràs Git sense adonar-te'n.

## 9. Pregunta (i pregunta bé)

No hi ha preguntes tontes. Però sí preguntes **concretes**, que tenen resposta:

| ❌ Pregunta vaga | ✅ Pregunta concreta |
| ---------------- | -------------------- |
| «No em va Docker» | «`docker run -p 80:80 nginx` dona `port is already allocated`. Què vol dir?» |
| «Com funciona Git?» | «Què passa exactament quan faig `git commit`? On es guarda?» |
| «El meu script no funciona» | «Este `if` sempre entra per l'`else` encara que el fitxer existix. Ací està el codi i l'eixida.» |

Quan preguntes, posa: **què vols fer**, **què has fet** (el codi o l'ordre), **què esperaves** i **què ha passat** (l'error exacte). Moltes vegades, en escriure-ho, ja trobes la solució tu.

## 10. Usar la IA sense que t'impedisca aprendre

La IA (ChatGPT, Claude, Copilot...) és una gran ajuda, però si fa ella els exercicis, tu no aprens, i en l'examen no la tindràs.

- ✅ Demana-li que t'**explique** un error o una ordre, o que et pose **exercicis** nous.
- ✅ Fes l'exercici tu i després demana-li que te'l **revise**.
- ❌ No copies codi que no entens: llig-lo línia a línia. Si no saps explicar què fa cada línia, no l'has entés.
- ⚠️ La IA s'equivoca, i sovint genera codi **insegur** que «funciona»: SQL concatenat (injecció SQL), HTML sense escapar (XSS), contrasenyes escrites dins del codi. **Revisa-ho sempre**, i prova-ho.

## 11. Prepara l'examen pràctic

- Fes els exercicis **en el temps** de l'examen i **sense** mirar res.
- Fes-los en una **màquina neta**, com la de l'examen.
- Aprén a usar l'**ajuda** que sí que tindràs: `man ordre`, `ordre --help`, `Get-Help`, `help()` en Python, `docker ... --help`, `git help`.
- El dia d'abans: repàs ràpid de les xuletes i **dormir**. Dormir és quan el cervell guarda el que has après.

## 12. Automatitza el que repetixes

Si fas una cosa **tres vegades** a mà, fes un script. És la millor manera de practicar Bash, PowerShell o Python: amb problemes **teus** (organitzar les fotos, fer còpies, crear usuaris de prova en la màquina virtual).

## 13. Cuida't

Estudiar moltes hores seguides, de nit i sense descans, cansa i s'aprén menys. Millor **una hora cada dia** que set hores el diumenge. Si un dia no et funciona res, deixa-ho i torna-hi demà: moltes vegades la solució apareix sola després de descansar.

!!! success "En resum"
    1. **Fes**, no llegisques. 2. **Recorda** sense mirar. 3. Repassa **poc i sovint**. 4. **Explica-ho** senzill. 5. Els **errors** s'apunten. 6. Problemes grans en **trossos**. 7. Una **xuleta** pròpia i un **repositori** amb els teus exercicis.

Més idees sobre com escriure bon codi: [Consells de programadors](consells.md).
