# Installare Multipass
Installare [multipass](http://romanysoft.ghttps://multipass.run/ithub.io/MarkdownD/ "Multipass") per creare VM istantanee (disponibile per Linux, MacOS e Windows) tramite il file di installazione fornito sul sito.
In alternativa si può utilizzare VirtualBox, un container Docker o altre tipologie di virtualizzazione o containerizzazione.
Gromacs è disponibile inoltre per ambienti Unix.

# Creare una VM con multipass per utilizzare i software Linux
Una volta installato multipass avviare a seconda dell'OS utilizzato:
- il terminale di Linux
- il terminale di MacOS
- La powershell di Windows

Creare e lanciare una VM (basata sull'ultima versione di Ubuntu Server LTS)

`multipass launch --name MultipassGromacs`

Montare una cartella contenente i file nella VM

`multipass mount /path/myFolder MultipassGromacs`

Visualizzare il percorso di mount della cartella

`multipass info MultipassGromacs`

Accedere alla Shell della VM

`multipass shell MultipassUbuntu`

# Aggiornare la VM
Aggiornare la VM

`sudo apt update && sudo apt upgrade`

# Rimuovere la VM

Rimuovere la VM

`multipass delete MultipassUbuntu`

Rimuovere definitivamente la VM (rimuoverà tutte le VM in delete)

`multipass purge`

Controllare la lista delle VM

`multipass list`

Stoppare la VM

`multipass stop MultipassUbuntu`

Avviare la VM

`multipass start MultipassUbuntu`
