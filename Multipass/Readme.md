## Installare Multipass
Installare [multipass](http://romanysoft.ghttps://multipass.run/ithub.io/MarkdownD/ "Multipass") per creare VM istantanee (disponibile per Linux, MacOS e Windows) tramite il file di installazione fornito sul sito.
In alternativa si può utilizzare VirtualBox, un container Docker o altre tipologie di virtualizzazione o containerizzazione.

## Creare una VM con multipass per utilizzare i software Linux
Una volta installato multipass avviare a seconda dell'OS utilizzato:
- il terminale di Linux
- il terminale di MacOS
- la powershell di Windows

Creare e lanciare una VM (basata sull'ultima versione di Ubuntu Server LTS)

	multipass launch --name MultipassVM

Montare una cartella contenente i file nella VM

	multipass mount /path/myFolder MultipassVM

Visualizzare il percorso di mount della cartella

	multipass info MultipassVM

Accedere alla Shell della VM

	multipass shell MultipassVM

## Aggiornare la VM

Aggiornare la VM

	sudo apt update && sudo apt upgrade

## Rimuovere la VM

Rimuovere la VM

	multipass delete MultipassVM

Rimuovere definitivamente la VM (rimuoverà tutte le VM in delete)

	multipass purge

Controllare la lista delle VM

	multipass list

Stoppare la VM

	multipass stop MultipassVM

Avviare la VM

	multipass start MultipassVM
