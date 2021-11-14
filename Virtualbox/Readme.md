## Disattivare HiperV su Windows 11

Virtualbox non funziona su Windows 11 se HyperV è abilitato

Disattivare HyperV

bcdedit /set hypervisorlaunchtype off

Attivare HyperV

bcdedit /set hypervisorlaunchtype on

## Creare una VM (headless)

Visualizzare gli ostype (i sistemi operativi che [Virtualbox](https://www.virtualbox.org/wiki/Downloads "Virtualbox") è in grado di emulare)

	vboxmanage list ostypes

Virtualbox si compone di un'interfaccia grafica GUI e di un'interfaccia headless che può essere controllata tramite il terminale di Linux. Questa modalità permette di creare ed accedere alle VM senza accedere all'interfaccia GUI. Inoltre tramite il protocollo RDP è possibile eseguire lo streaming dell'interfaccia GUI di Virtualbox da un server headless a una macchina host in modo da poter configurare le VM con la componente grafica del programma (consiglio di utilizzare [Remmina](https://remmina.org/ "Remmina") per accedere alla porta RDP configurata)

	vboxmanage createvm --name <VMname> --ostype "Linux_64" --register --basefolder $PWD

Impostare memoria e network

	vboxmanage modifyvm <VMname> --ioapic on

	vboxmanage modifyvm <VMname> --memory 1024 --vram 128

Opzioni di networking --nic<1-N> none | null | nat | natnetwork | bridged | intnet | hostonly | generic

	vboxmanage modifyvm <VMname> --nic1 nat

Crea il disco rigido su cui verrà installata la macchina virtuale

	vboxmanage createhd --filename $PWD/<VMname>/<VMname>_DISK.vdi --size 80000 --format VDI

Collega il controller SATA alla macchina virtuale

	vboxmanage storagectl <VMname> --name "SATA Controller" --add sata --controller IntelAhci

Collega l’immagine VDI al sata controller 

	vboxmanage storageattach <VMname> --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium  $PWD/<VMname>/<VMname>_DISK.vdi

Collega il controller IDE alla macchina virtuale

	vboxmanage storagectl <VMname> --name "IDE Controller" --add ide --controller PIIX4

Collega l’ISO all’IDE controller (optical drive)

	vboxmanage storageattach <VMname> --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --``medium $PWD/<OSname>.iso

Imposta il boot dall’IDE controller (optical drive)

	vboxmanage modifyvm <VMname> --boot1 dvd --boot2 disk --boot3 none --boot4 none

Impostare l'accesso RDP e avviare la VM

	vboxmanage modifyvm <VMname> --vrde on

	vboxmanage modifyvm <VMname> --vrdemulticon on --vrdeport 10001

	vboxheadless --startvm <VMname>

## Avviare una VM

Mostrare la lista delle VM

	vboxmanage list vms

Avviare una VM

	vboxmanage startvm <name or UUID>

Avviare una VM con interfaccia grafica

	vboxmanage startvm <name or UUID> --type gui

Avviare una VM senza interfaccia grafica

	vboxmanage startvm <name or UUID> --type headless

Mostrare tutte le VM avviate

	vboxmanage list runningvms

## Installare le extension pack

	sudo vboxmanage extpack install --replace Oracle_VM_VirtualBox_Extension_Pack-XXX.vbox-extpack

## Eseguire backup e snapshot della VM

Clonare una VM

	vboxmanage clonevm <VMname> --name <newVMName> --register

Creare uno snapshot

	vboxmanage snapshot <VMname> take <SNAPName>

Mostrare gli snapshot

	vboxmanage showvminfo <VMname> | grep "Name:"

Cancellare uno snapshot

	vboxmanage snapshot <VMname> delete <SNAPName>

Ripristinare uno snapshot

	vboxmanage snapshot <VMname> restore <SNAPName>

Esportare una VM formato OVA

	vboxmanage export <name or UUID>  -o image.ova

Importare una VM formato OVA

	vboxmanage import image.ova

## Definire le regole di port forwarding

Aggiungere regole di port forwarding

	vboxmanage modifyvm <VMname> --natpf1 "ssh,tcp,,11000,,22"

Mostrare le regole di port forwarding della VM

	vboxmanage showvminfo <VMname> | grep "Rule("

	vboxmanage modifyvm <VMname> --natpf1 "nome_regola"

## Abilitare protocollo RDP (screen streaming per server headless)

Per effettuare uno streaming di Virtualbox devo installare Remmina (protocollo RDP)

	vboxmanage modifyvm <VMname> --vrde on

	vboxmanage modifyvm <VMname> --vrdemulticon on --vrdeport 10001

## Controllare la macchina virtuale (pause, resume, reset, poweroff e savestate)

	vboxmanage controlvm <name or UUID> <subcommands>

Controllare la macchina virtuale senza interfaccia grafica

	vboxmanage controlvm <name or UUID> <subcommands> --type headless

Cancellare una macchina virtuale e i file (una volta spenta)

	vboxmanage unregister <name or UUID>

Cancellare una macchina virtuale e i file (una volta spenta)

	vboxmanage unregister <name or UUID> --delete

Mostrare le informazioni di una VM

	vboxmanage showvminfo <name or UUID>

Rinominare una VM

	vboxmanage modifyvm <name or UUID> --name <new name>

Cambiare la descrizione di una VM

	vboxmanage modifyvm <name or UUID> --description <new description>

## Cambiare le caratteristiche della VM

Cambiare la ram della VM

	vboxmanage modifyvm <name or UUID> --memory <RAM in MB>

Cambiare il numero dei core della CPU della VM

	vboxmanage modifyvm <name or UUID> --cpus <number>

## Disconnettere e riconnettere la rete ethernet

Disconnettere la rete ethernet

	vboxmanage controlvm <name or UUID> setlinkstate1 off

Riconnettere la rete ethernet

	vboxmanage controlvm <name or UUID> setlinkstate1 on
