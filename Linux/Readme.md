## Utilizzare il comando SSH

Connettersi ad un server con il protocollo SSH

	ssh <User>@<ServerIP>

Specificare una porta
	
	ssh <User>@<ServerIP> -p 2255

## Utilizzare il comando SCP

Copiare una cartella in remoto in una macchina locale

	scp -r <User>@<ServerIP>:/path/to/remote /home/to/local/

Copiare una cartella locale in una macchina remota

	scp -r /path/to/local <User>@<ServerIP>:/path/to/remote

## Impostare i permessi

	chmod <a, u, g, o> <+, -> <r, w, x> <File>

	a = all
	u = you have to add <User>
	g = you have to add <Group>
	o = other

	+ = add permission
	- = remove permission

	r = read
	w = write
	x = execute
	
## Lavorare con gli utenti e mostrare l'hostname

Mostrare l’hostname

	hostname -I
	
Mostrare quale utente sono
	
	whoami

Cambiare User
	
	su <User>

## Lavorare con i file e le cartelle

Mostrare il contenuto della directory

	ls
	
	ls -lsh

Mostrare il percorso della directory in cui mi trovo

	pwd

Cambiare cartella

	cd </path/to/folder>

Creare una cartella
	
	mkdir <myFolder>
	
Rimuovere una cartella
	
	rm -r <myFolder>
	
	rmdir <myFolder>

Rinominare un file o una cartella
	
	mv <Name> <newName>
	
Spostare un file o una cartella
	
	mv <path> <newPath>

Stampare il contenuto di <myFile>

	cat <myFile>

Ordinare le righe di un file

	sort <myFile1>

Scaricare un file con wget

	wget <myURL>

	wget <myURL> -o <myFile>

## Manipolare i file


Creare un file vuoto

	touch <myFile>

Cancellare un file

	rm <myFile>
	
Cerca una determinata parola in <myFile>

	cat <myFile> | grep <String>

Esegui la differenza di <myFile1> e <myFile2> inserisci la differenza in <myFile3>

	grep -v -Ff <myFile1> <myFile2>.txt > <myFile3>
	
## Lavorare con i dischi

Mostrare i dischi

	df

Mostrare i dischi (for human)

	df -h

Montare o rimuovere un disco (in una cartella

	mount /DiskName /Folder

	umount /DiskName
	
## Eseguire un file SH o Python
	
	./<myFile.sh>
	
	python <myFile.py>
	
	python3 <myFile.py>
	
## Aggiungere una schedule (attività) nel Crontab

	crontab -e

	# min(0-59) h(0-23) d(1-31) m(1-12) d(0-7)
	
	* * * * * /path/<Command>
	
	* * * * * /path/<myFile.sh>

## Mostrare la data

	date

	date +"%d-%m-%Y"
	
## Lavorare con la cronologia

Mostrare la cronologia

	history

Cancellare la cronologia

	history -c

Scrivere la cronologia

	history -w

## Antivirus ClamAV

Installare ClamAV

	sudo apt install clamav

Aggiornare ClamAV

	freshclam

Scansionare tutti i file

	clamscan -r /

Mostrare solo i file infetti

	clamscan -r -i /

Non effettuare una scansione degli archivi

	clamscan -r --scan-archive=no /

Scansionare una cartella specifica

	clamscan -r /home/USER

Spostare tutti i file infetti in una seconda cartella

	clamscan -r --move=/home/USER/VIRUS /home/USER

Rimuovere tutti i file infetti presenti in una cartella

	clamscan -r --remove /home/USER

Mostrare tutte le opzioni (help)

	clamscan –-help
