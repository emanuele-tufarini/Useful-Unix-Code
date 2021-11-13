## Utilizzare il comando SCP

Copiare una cartella in remoto in una macchina locale

	scp -r user@yourServerIp:/path/to/remote /home/to/local/

Copiare una cartella locale in una macchina remota

	scp -r /path/to/local username@yourServerIp:/path/to/remote

## Installare docker su Ubuntu

	sudo apt install docker-ce

	sudo apt install docker-compose

## Installare docker su Fedora

	sudo dnf -y install dnf-plugins-core

	sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo

	sudo dnf install docker-ce docker-ce-cli containerd.io

	sudo systemctl start docker

	sudo systemctl enable docker

## Aggiungere $USER al gruppo docker

Aggiungendo $USER al gruppo docker l'utente non dovrà inserire ogni volta il comando sudo

	sudo groupadd docker

	sudo gpasswd -a $USER docker

## Comandi utili per i container docker

Installare un immagine da [Docker Hub](https://hub.docker.com/ "Docker Hub")

	docker pull [IMAGE_NAME]

Elencare i processi docker-compose (nella cartella con il file compose)

	docker-compose ps

Elencare tutti i processi attivi

	docker ps

Elencare tutti i processi

	docker ps -a

Avviare un servizio con compose (nella cartella con il file compose)

	docker-compose up

Avviare un servizio docker compose senza sovrascriverlo se già avviato

	docker-compose up --no-recreate

Fermare un container

	docker stop [container-id]

Eliminare un container

	docker rm [container-id]

Avviare un processo

	docker start [container-id]

Riavviare un processo

	docker restart [container-id]

Creare un immagine docker (nella cartella con il Dockerfile)

	docker build -t [image-name] .

Avviare il container accedendo alla shell (la seconda volta è necessario entrare con exec per non resettarlo)

	docker run -ti --name [container-name] [image-id] /bin/bash

Entrare in un container docker accedendo alla shell (il container deve essere in up)

	docker exec -ti --name [container-name] [container-id] /bin/bash

Copiare un file in un container

	docker cp myFile [container-id]:/work

Copiare un file del container nella macchina host

	docker cp [container-id]:/path/to/container/myFile /path/to/local

## Comandi per il backup dei container Docker

Salvare l'immagine del container docker

	docker save [container-name] > [image-name].tar

Caricare l'immagine docker

	docker load /path/to/[image-name].tar [image-name]

Esportare il container docker in un file TAR

	docker export [container-name] > [image-name].tar

Importare il container docker in un file TAR (precedentemente esportato)

	docker import /path/to/[image-name].tar [image-name]

## Comandi per mostrare i log dei container docker

Mostrare i log del container docker

	docker logs [container-id]

Mostrare i primi log del container docker

	docker logs [container-id] | head

Mostrare gli ultimi log del container docker

	docker logs [container-id] | tail


## Ricreare un servizio docker compose

	docker-compose up --build --force-recreate --no-deps -d [service_name]

## Eseguire un backup completo del database mysql dentro a un container docker

	docker exec [container-id] sh -c 'exec mysqldump --all-databases -uroot -pPASSWORD' >  /HostPath/DATABASE_FULL_backup_$(date +"%d%m%Y_%H%M").sql
