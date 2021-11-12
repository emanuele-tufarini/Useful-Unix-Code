# Table of contents

1. [Utilizzare il comando SCP](#Utilizzare il comando SCP)
2. [Installare docker su Ubuntu](#Installare docker su Ubuntu)
3. [Installare docker su Fedora](#Installare docker su Fedora)
4. [Aggiungere $USER al gruppo docker](#Aggiungere $USER al gruppo docker)
5. [Comandi utili per i container docker](#Comandi utili per i container docker)
6. [Comandi per il backup dei container docker](#Comandi per il backup dei container docker)
7. [Comandi per mostrare i log dei container docker](#Comandi per mostrare i log dei container docker)
8. [Ricreare un servizio docker compose](#Ricreare un servizio docker compose)
8. [Eseguire un backup completo del database mysql dentro a un container docker](#Eseguire un backup completo del database mysql dentro a un container docker)

## Utilizzare il comando SCP

Copiare una cartella in remoto in una macchina locale

`scp -r user@yourServerIp:/path/to/foo /home/user/Desktop/`

Copiare una cartella locale in una macchina remota

`scp -r /path/from/local username@yourServerIp:/path/to/remote`

## Installare docker su Ubuntu

`sudo apt install docker-ce`

`sudo apt install docker-compose`

## Installare docker su Fedora

`sudo dnf -y install dnf-plugins-core`

`sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo`

`sudo dnf install docker-ce docker-ce-cli containerd.io`

`sudo systemctl start docker`

`sudo systemctl enable docker`

## Aggiungere $USER al gruppo docker

Aggiungendo $USER al gruppo docker l'utente non dovrà inserire ogni volta il comando sudo

`sudo groupadd docker `

`sudo gpasswd -a $USER docker `

## Comandi utili per i container docker

Installare un immagine da [Docker Hub](https://hub.docker.com/ "Docker Hub")

`docker pull [IMAGE_NAME]`

Elencare i processi docker-compose (nella cartella con il file compose)

`docker-compose ps`

Elencare tutti i processi attivi

`docker ps`

Elencare tutti i processi

`docker ps -a`

Avviare un servizio con compose (nella cartella con il file compose)

`docker-compose up`

Avviare un servizio docker compose senza sovrascriverlo se già avviato

`docker-compose up --no-recreate`

Fermare un container

`docker stop [container-id]`

Eliminare un container

`docker rm [container-id]`

Avviare un processo

`docker start [container-id]`

Riavviare un processo

`docker restart [container-id]`

Creare un immagine docker (nella cartella con il Dockerfile)

`docker build -t [image-name] .`

Avviare il container accedendo alla shell (la seconda volta è necessario entrare con exec per non resettarlo)

`docker run -ti --name [container-name] [image-id] /bin/bash`

Entrare in un container docker accedendo alla shell (il container deve essere in up)

`docker exec -ti --name [container-name] [container-id] /bin/bash`

Copiare un file in un container

`docker cp example.extension [container-id]:/work`

Copiare un file del container nella macchina host

`docker cp [container-id]:/file/path/within/container /host/path/target`

## Comandi per il backup dei container Docker

Salvare l'immagine del container docker

`docker save [container-name] > [image-name].tar`

Caricare l'immagine docker

`docker load /path/to/[image-name].tar [image-name]`

Esportare il container docker in un file TAR

`docker export [container-name] > [image-name].tar`

Importare il container docker in un file TAR (precedentemente esportato)

`docker import /path/to/[image-name].tar [image-name] `

## Comandi per mostrare i log dei container docker

Mostrare i log del container docker

`docker logs [container-id]`

Mostrare i primi log del container docker

`docker logs [container-id] | head`

Mostrare gli ultimi log del container docker

`docker logs [container-id] | tail`


## Ricreare un servizio docker compose

`docker-compose up --build --force-recreate --no-deps -d [service_name]`

## Eseguire un backup completo del database mysql dentro a un container docker

`docker exec [container-id] sh -c 'exec mysqldump --all-databases -uroot -pPASSWORD' >  /HostPath/DATABASE_FULL_backup_$(date +"%d%m%Y_%H%M").sql`
