# 1. Instal·lació

Docker té dues formes de presentar-se:

| | Docker Engine | Docker Desktop |
| - | ------------- | -------------- |
| Què és | el motor, des del terminal | una aplicació amb finestra que porta el motor dins |
| On | Linux (servidors i escriptori) | Windows, Mac i Linux |
| Ús típic | servidors, pràctiques en Linux | equips Windows |

## Linux (Debian / Ubuntu): Docker Engine

La forma recomanada és afegir el repositori oficial de Docker. En Ubuntu:

```bash
# 1. Preparar el sistema i la clau del repositori
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# 2. Afegir el repositori de Docker
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 3. Instal·lar Docker i Docker Compose
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

En **Debian**, canvia `ubuntu` per `debian` en les dues URL.

!!! tip "La manera ràpida (per a proves)"
    ```bash
    curl -fsSL https://get.docker.com | sudo sh
    ```
    Fa tots els passos anteriors automàticament.

### Usar Docker sense `sudo`

Per defecte, cada ordre de Docker necessita `sudo`. Per a evitar-ho, afig el teu usuari al grup `docker`:

```bash
sudo usermod -aG docker $USER
```

**Tanca la sessió i torna a entrar** perquè faça efecte (o executa `newgrp docker`).

!!! warning "Seguretat"
    Estar en el grup `docker` és pràcticament com ser root: es pot muntar qualsevol carpeta del sistema dins d'un contenidor. En un servidor real, dona este permís només a qui ho necessite.

### Comprovar que funciona

```bash
docker --version             # versió de Docker
docker compose version       # versió de Docker Compose
docker run hello-world       # el "Hola món" de Docker
```

Si `hello-world` mostra *Hello from Docker!*, tot està correcte. Este és el que ha passat:

1. Docker ha buscat la imatge `hello-world` en l'equip i no l'ha trobat.
2. L'ha descarregada de Docker Hub.
3. Ha creat un contenidor, que ha mostrat el missatge i ha acabat.

## Windows: Docker Desktop

1. Activa **WSL 2** (el subsistema de Linux per a Windows). En PowerShell com a administrador:
    ```powershell
    wsl --install
    ```
    i reinicia.
2. Descarrega **Docker Desktop** de [docker.com](https://www.docker.com/products/docker-desktop/) i instal·la'l.
3. Obri Docker Desktop i espera que diga *Engine running*.
4. Ja pots usar `docker` des de PowerShell o des del terminal de WSL.

## Errors típics

| Error | Per què | Solució |
| ----- | ------- | ------- |
| `permission denied while trying to connect to the Docker daemon socket` | El teu usuari no està en el grup `docker` | `sudo usermod -aG docker $USER` i torna a entrar |
| `Cannot connect to the Docker daemon` | El servei de Docker no està arrancat | `sudo systemctl start docker` (Linux) o obri Docker Desktop |
| `docker-compose: command not found` | Ara s'escriu amb espai, és un plugin | `docker compose` (sense guió) |
| Docker Desktop no arranca en Windows | Falta WSL 2 o la virtualització està desactivada | `wsl --install`; activa la virtualització en la BIOS |

!!! success "Per a l'examen"
    - **Imatge** = plantilla · **Contenidor** = imatge en execució · **Registre** = d'on es descarreguen (Docker Hub)
    - Contenidor ≠ màquina virtual: comparteix el kernel de l'amfitrió
    - Instal·lar ràpid en Linux: `curl -fsSL https://get.docker.com | sudo sh`
    - Sense sudo: `sudo usermod -aG docker $USER` (i tornar a entrar)
    - Provar: `docker run hello-world`
    - Compose: `docker compose` (amb espai)
