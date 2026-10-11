# Glossari

Paraules que apareixen en els apunts, explicades amb paraules senzilles.

## Sistema i terminal

**Terminal**
:   La finestra on escrius ordres de text. També es diu *consola*.

**Shell**
:   El programa que entén les ordres que escrius en el terminal i les executa. El més habitual en Linux és **Bash**.

**Ordre** (o comandament)
:   Una instrucció que escrius en el terminal: `ls`, `cd`, `mkdir`...

**Script**
:   Un fitxer de text amb diverses ordres que s'executen una darrere l'altra.

**Shebang**
:   La primera línia d'un script, que comença per `#!` i diu quin programa l'ha d'executar. Exemple: `#!/bin/bash`.

**Ruta** (path)
:   L'adreça d'un fitxer o carpeta. **Absoluta** si comença per `/` (`/home/ana/notes.txt`), **relativa** si parteix de la carpeta on estàs (`notes.txt`, `../fotos`).

**Directori**
:   Una carpeta.

**`.` i `..`**
:   `.` és la carpeta actual. `..` és la carpeta de dalt (la que la conté).

**`~`**
:   La teua carpeta personal (`/home/el_teu_usuari`).

**Permisos**
:   Què es pot fer amb un fitxer: **r** (llegir), **w** (escriure) i **x** (executar). Es canvien amb `chmod`.

**root**
:   L'usuari administrador de Linux, que ho pot fer tot. Amb `sudo` executes una ordre com a root.

**Procés**
:   Un programa que s'està executant. Cada procés té un número únic: el **PID**.

**Senyal**
:   Un avís que s'envia a un procés per a parar-lo, matar-lo, etc. Es fa amb `kill`.

**Variable d'entorn**
:   Una variable que el sistema ja té creada i que poden llegir tots els programes: `$HOME`, `$USER`, `$PATH`...

**PATH**
:   La llista de carpetes on el sistema busca les ordres quan les escrius.

## Entrada i eixida

**Argument** (o paràmetre)
:   Una dada que passes a un script o una ordre en executar-la, darrere del nom. En `./copia.sh fitxer.txt /tmp`, els arguments són `fitxer.txt` i `/tmp`.

**Opció**
:   Un argument especial que comença per `-` i modifica el comportament: `ls -l`, `grep -i`.

**stdin, stdout, stderr**
:   Els tres canals d'un programa: **entrada** (normalment el teclat), **eixida** (la pantalla) i **errors** (també la pantalla).

**Redirecció**
:   Enviar l'eixida d'una ordre a un fitxer (`>`, `>>`) o llegir l'entrada d'un fitxer (`<`).

**Tuberia** (pipe)
:   El símbol `|`, que passa l'eixida d'una ordre com a entrada de la següent.

**Codi d'eixida**
:   El número que deixa una ordre en acabar: **0 si ha anat bé**, un altre si ha fallat. En Bash es veu amb `$?`.

**`/dev/null`**
:   Un fitxer especial que ho descarta tot. S'usa per a amagar eixides.

## Programació

**Variable**
:   Un nom on guardes un valor per a usar-lo després.

**Tipus de dada**
:   La classe de valor: número enter, decimal, text, verdader/fals...

**Cadena** (string)
:   Un text: `"hola"`.

**Booleà**
:   Un valor que només pot ser **cert** (`True`) o **fals** (`False`).

**Condició**
:   Una pregunta que dona cert o fals: `edat >= 18`.

**Condicional**
:   Codi que només s'executa si es complix una condició (`if`).

**Bucle**
:   Codi que es repetix diverses vegades (`for`, `while`).

**Iteració** (o volta)
:   Cada repetició d'un bucle.

**Bucle infinit**
:   Un bucle que no acaba mai perquè la condició sempre és certa. Es para amb ++ctrl+c++.

**Indentació**
:   Els espais al principi de la línia que marquen què està dins d'un bloc. En Python és obligatòria.

**Funció**
:   Un tros de codi amb nom que fa una tasca i es pot usar moltes vegades.

**Cridar una funció**
:   Executar-la, escrivint el seu nom.

**Retornar** (return)
:   El que fa una funció quan torna un resultat a qui l'ha cridada.

**Variable local**
:   Una variable que només existix dins d'una funció.

**Array / Llista**
:   Una variable que guarda molts valors, cadascun en una posició numerada **començant per 0**.

**Índex**
:   La posició d'un element en una llista o un text. El primer és el **0**.

**Diccionari / Array associatiu**
:   Una col·lecció de parelles **clau → valor**, on busques per nom en compte de per posició.

**Expressió regular** (regex)
:   Una manera de descriure "formes" de text per a buscar-les: `^[0-9]+$` vol dir "només dígits".

**Mòdul / Llibreria**
:   Un fitxer amb funcions ja fetes que pots importar i usar.

**Excepció**
:   Un error que es produïx mentre el programa s'executa (dividir per zero, fitxer que no existix...).

**Depurar** (debug)
:   Buscar i corregir errors en el codi.

**Sintaxi**
:   Les regles d'escriptura d'un llenguatge. Un *error de sintaxi* vol dir que alguna cosa està mal escrita.

**Cmdlet**
:   Una ordre de PowerShell. Sempre té la forma *Verb-Nom*: `Get-Process`, `New-Item`...

**Propietat**
:   Una dada d'un objecte. Per exemple, un fitxer té les propietats `Name`, `Length` (mida)... Es llig amb un punt: `$fitxer.Length`.

**Mètode**
:   Una acció d'un objecte. Es crida amb un punt i parèntesis: `$text.ToUpper()`.

**Política d'execució**
:   La configuració de Windows que diu si es poden executar scripts de PowerShell. Es canvia amb `Set-ExecutionPolicy`.

**Directori Actiu** (Active Directory)
:   El servei de Windows Server que guarda els usuaris, grups i equips d'una organització en un sol lloc.

**Contenidor**
:   Una aplicació aïllada amb tot el que necessita per a funcionar, creada a partir d'una imatge de Docker. Comparteix el kernel de l'equip (no és una màquina virtual).

**Imatge** (Docker)
:   La plantilla de només lectura a partir de la qual es creen els contenidors. Es descarreguen de Docker Hub.

**Volum**
:   Un espai on Docker guarda dades fora del contenidor, perquè no es perden quan l'esborres.

**Port publicat**
:   Un port del teu equip connectat amb un port del contenidor (`-p 8080:80`), perquè es puga accedir des de fora.

**YAML**
:   Un format de text per a fitxers de configuració on l'estructura es marca amb espais. El usa Docker Compose (`compose.yaml`).

**Repositori** (Git)
:   Una carpeta amb l'historial de canvis guardat per Git (en la carpeta oculta `.git`).

**Commit**
:   Una "foto" guardada del projecte, amb un missatge que explica què ha canviat.

**Branca** (branch)
:   Una línia de treball independent dins d'un repositori. La principal es diu `main`.

**Remot** (remote)
:   Una còpia del repositori en un altre lloc, com GitHub. Normalment es diu `origin`.

**Push / Pull**
:   Pujar els teus commits al remot / baixar els del remot.

**Merge**
:   Ajuntar els canvis d'una branca amb una altra.

**Conflicte**
:   Quan dues branques han canviat la mateixa línia i Git no sap quina triar: ho has de decidir tu.

**Pull Request** (PR)
:   Una petició en GitHub per a revisar i ajuntar una branca amb una altra.

**Classe / Objecte**
:   Una classe és un motle; un objecte és una cosa concreta creada amb eixe motle.
