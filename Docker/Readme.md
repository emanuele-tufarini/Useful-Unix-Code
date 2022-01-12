- [Utilizzare il comando SCP](#utilizzare-il-comando-scp)
- [Installare docker su Ubuntu](#installare-docker-su-ubuntu)
- [Installare docker su Fedora](#installare-docker-su-fedora)
- [Aggiungere $USER al gruppo docker](#aggiungere--user-al-gruppo-docker)
- [Comandi utili per i container docker](#comandi-utili-per-i-container-docker)
- [Comandi per il backup dei container Docker](#comandi-per-il-backup-dei-container-docker)
- [Comandi per mostrare i log dei container docker](#comandi-per-mostrare-i-log-dei-container-docker)
- [Ricreare un servizio docker compose](#ricreare-un-servizio-docker-compose)
- [Eseguire un backup completo del database mysql dentro a un container docker](#eseguire-un-backup-completo-del-database-mysql-dentro-a-un-container-docker)
- [Collegare due container docker (es Spark e MySQL) tramite la network e montare una cartella](#collegare-due-container-docker--es-spark-e-mysql--tramite-la-network-e-montare-una-cartella)

## Utilizzare il comando SCP

Copiare una cartella in remoto in una macchina locale

	scp -r <User>@<ServerIP>:/path/to/remote /home/to/local/

Copiare una cartella locale in una macchina remota

	scp -r /path/to/local <User>@<ServerIP>:/path/to/remote

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

	sudo gpasswd -a <User> docker

## Comandi utili per i container docker

Installare un immagine da [Docker Hub](https://hub.docker.com/ "Docker Hub")

	docker pull <ImageName>

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

	docker stop <ContainerID>

Eliminare un container

	docker rm <ContainerID>

Avviare un processo

	docker start <ContainerID>

Riavviare un processo

	docker restart <ContainerID>

Creare un immagine docker (nella cartella con il Dockerfile)

	docker build -t <ImageName> .

Avviare il container accedendo alla shell (la seconda volta è necessario entrare con exec per non resettarlo)

	docker run -ti --name <ContainerName> [image-id] /bin/bash

Entrare in un container docker accedendo alla shell (il container deve essere in up)

	docker exec -ti --name <ContainerName> [container-id] /bin/bash
	
Entrare in un container docker accedendo alla shell (il container deve essere in up) come root

docker exec -it -u root <containerName> bash

Copiare un file in un container

	docker cp myFile <ContainerID>:/work

Copiare un file del container nella macchina host

	docker cp <ContainerID>:/path/to/container/myFile /path/to/local

## Comandi per il backup dei container Docker

Salvare l'immagine del container docker

	docker save <ContainerName> > <ImageName>.tar

Caricare l'immagine docker

	docker load /path/to/<ImageName>.tar <ImageName>

Esportare il container docker in un file TAR

	docker export <ContainerName> > <ImageName>.tar

Importare il container docker in un file TAR (precedentemente esportato)

	docker import /path/to/<ImageName>.tar <ImageName>

## Comandi per mostrare i log dei container docker

Mostrare i log del container docker

	docker logs <ContainerID>

Mostrare i primi log del container docker

	docker logs <ContainerID> | head

Mostrare gli ultimi log del container docker

	docker logs <ContainerID> | tail

## Ricreare un servizio docker compose

	docker-compose up --build --force-recreate --no-deps -d <ServiceName>

## Eseguire un backup completo del database mysql dentro a un container docker

	docker exec <ContainerID> sh -c 'exec mysqldump --all-databases -uroot -pPASSWORD' >  /HostPath/DATABASE_FULL_backup_$(date +"%d%m%Y_%H%M").sql
	
## Collegare due container docker (es Spark e MySQL) tramite la network e montare una cartella

Mostrare tutte le network presenti in docker

	docker network ls

Identificare la network in cui risiede il container SQL

	docker container inspect <containerName>

Il nome della network è riportato sotto "Networks"

            "Networks": {
                "<networkName>": {
	
Collegare due container docker (es Spark e MySQL) tramite la network
	
	docker run --name <containerName> --net <networkName> <containerImage>

Collegare due container docker (es Spark e MySQL) tramite la network e montare una cartella (eseguire il comando nella cartella da montare)
	
	docker run --name <containerName> --volume $PWD/:/opt/bitnami/spark/work --net <networkName> bitnami/spark
