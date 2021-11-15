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
