## Attivare HiperV su Windows 11

Se avete installato Virtualbox e disabilitato HyperV dovete riattivarlo

Attivare HyperV

	bcdedit /set hypervisorlaunchtype on
	
Disattivare HyperV

	bcdedit /set hypervisorlaunchtype off

## Installare Multipass
Installare [multipass](http://romanysoft.ghttps://multipass.run/ithub.io/MarkdownD/ "Multipass") per creare VM istantanee (disponibile per Linux, MacOS e Windows) tramite il file di installazione fornito sul sito.
In alternativa si può utilizzare VirtualBox, un container Docker o altre tipologie di virtualizzazione o containerizzazione.

## Creare una VM con multipass per utilizzare i software Linux
Una volta installato multipass avviare a seconda dell'OS utilizzato:
- il terminale di Linux
- il terminale di MacOS
- la powershell di Windows

Creare e lanciare una VM (basata sull'ultima versione di Ubuntu Server LTS)

	multipass launch --name <VMname>

Modificare le caratteristiche della VM

	--cpus=CPUS        Number of CPUs to allocate. Minimum: 1, default: 1.

	--size=SIZE        Disk space to allocate. Positive integers, in bytes, or with K, M, G suffix. Minimum: 512M, default: 5G.

	--mem=MEMORY       Amount of memory to allocate. Positive integers, in bytes, or with K, M, G suffix. Minimum: 128M, default: 1G.

Montare una cartella contenente i file nella VM

	multipass mount /path/myFolder <VMname>

Visualizzare il percorso di mount della cartella

	multipass info <VMname>

Accedere alla Shell della VM

	multipass shell <VMname>

Uscire dalla VM

	exit

## Aggiornare la VM

Impostare la password dell'utente ubuntu

	sudo passwd ubuntu

Aggiornare la VM

	sudo apt update && sudo apt upgrade

## Rimuovere la VM

Rimuovere la VM

	multipass delete <VMname>

Recuperare la VM

	multipass recover <VMname>
	
Rimuovere definitivamente la VM (rimuoverà tutte le VM in delete)

	multipass purge

Controllare la lista delle VM

	multipass list

Stoppare la VM

	multipass stop <VMname>

Avviare la VM

	multipass start <VMname>
