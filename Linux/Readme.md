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
