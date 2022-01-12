- [Disattivare HiperV su Windows 11](#disattivare-hiperv-su-windows-11)
- [Installare Multipass](#installare-multipass)
- [Creare una VM con multipass per utilizzare i software Linux](#creare-una-vm-con-multipass-per-utilizzare-i-software-linux)
- [Aggiornare la VM](#aggiornare-la-vm)
- [Rimuovere la VM](#rimuovere-la-vm)

## Disattivare HiperV su Windows 11

Virtualbox potrebbe non funzionare su Windows 11 se HyperV è abilitato (Multipass richiede HyperV attivato per funzionare)

Disattivare HyperV

	bcdedit /set hypervisorlaunchtype off

Attivare HyperV

	bcdedit /set hypervisorlaunchtype auto

Se il computer monta la versione di Windows Home installare [Virtualbox](https://www.virtualbox.org/wiki/Downloads "Virtualbox") ed abilitare i driver di Multipass su Virtualbox

	multipass set local.driver=virtualbox

## Installare Multipass
Installare [multipass](http://romanysoft.ghttps://multipass.run/ithub.io/MarkdownD/ "Multipass") per creare VM istantanee (disponibile per Linux, MacOS e Windows) tramite il file di installazione fornito sul sito.
In alternativa si può utilizzare VirtualBox, un container Docker o altre tipologie di virtualizzazione o containerizzazione.

## Creare una VM con multipass per utilizzare i software Linux
Una volta installato multipass avviare a seconda dell'OS utilizzato:
- il terminale di Linux
- il terminale di MacOS
- la powershell di Windows

Mostrare tutte le versioni di Ubuntu disponibili

	multipass find


Creare e lanciare una VM (se la versione viene omessa verrà utilizzata l'ultima versione di Ubuntu Server LTS)

	multipass launch --name <VMname> <Version>

Modificare le caratteristiche della VM

	--cpus=CPUS        Number of CPUs to allocate. Minimum: 1, default: 1.

	--size=SIZE        Disk space to allocate. Positive integers, in bytes, or with K, M, G suffix. Minimum: 512M, default: 5G.

	--mem=MEMORY       Amount of memory to allocate. Positive integers, in bytes, or with K, M, G suffix. Minimum: 128M, default: 1G.

Montare una cartella contenente i file nella VM

	multipass mount /path/myFolder <VMname>

Smontare una cartella contenente i file nella VM

	multipass umount <VMname>:/path/myFolder
	
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
