## Creare una VM (headless)

Visualizzare gli ostype (i sistemi operativi che Virtualbox è in grado di emulare)

	vboxmanage list ostypes

Virtualbox si compone di un'interfaccia grafica GUI e di un'interfaccia headless che può essere controllata tramite il terminale di Linux. Questa modalità permette di creare ed accedere alle VM senza accedere all'interfaccia GUI. Inoltre tramite il protocollo RDP è possibile streammare l'interfaccia GUI di Virtualbox da un server headless a una macchina host in modo da poter configurare le VM con la componente grafica del programma (consiglio di utilizzare Remmina per accedere alla porta RDP configurata)

	vboxmanage createvm --name "nome_macchina_virtuale" --ostype "Linux_64" --register --basefolder $PWD

Impostare memoria e network

	vboxmanage modifyvm "nome_macchina_virtuale" --ioapic on

	vboxmanage modifyvm "nome_macchina_virtuale" --memory 1024 --vram 128

Opzioni di networking --nic<1-N> none | null | nat | natnetwork | bridged | intnet | hostonly | generic

	vboxmanage modifyvm "nome_macchina_virtuale"  --nic1 nat

Crea il disco rigido su cui verrà installata la macchina virtuale

	vboxmanage createhd --filename $PWD/nome_macchina_virtuale/nome_macchina_virtuale_DISK.vdi --size 80000 --format VDI

Collega il controller SATA alla macchina virtuale

	vboxmanage storagectl "nome_macchina_virtuale" --name "SATA Controller" --add sata --controller IntelAhci

Collega l’immagine VDI al sata controller 

	vboxmanage storageattach "nome_macchina_virtuale" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium  $PWD/nome_macchina_virtuale/nome_macchina_virtuale_DISK.vdi

Collega il controller IDE alla macchina virtuale

	vboxmanage storagectl "nome_macchina_virtuale" --name "IDE Controller" --add ide --controller PIIX4

Collega l’ISO all’IDE controller (optical drive)

	vboxmanage storageattach "nome_macchina_virtuale" --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --``medium $PWD/sistema_operativo.iso

Imposta il boot dall’IDE controller (optical drive)

	vboxmanage modifyvm "nome_macchina_virtuale" --boot1 dvd --boot2 disk --boot3 none --boot4 none

Impostare l'accesso RDP e avviare la VM

	vboxmanage modifyvm "nome_macchina_virtuale" --vrde on

	vboxmanage modifyvm "nome_macchina_virtuale" --vrdemulticon on --vrdeport 10001

	vboxheadless --startvm "nome_macchina_virtuale"

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

	vboxmanage clonevm "nome_macchina_virtuale" --name "nuovo_nome_macchina_virtuale" --register

Creare uno snapshot

	vboxmanage snapshot "nome_macchina_virtuale" take "nome_snapshot"

Mostrare gli snapshot

	vboxmanage showvminfo "nome_macchina_virtuale" | grep "Name:"

Cancellare uno snapshot

	vboxmanage snapshot "nome_macchina_virtuale" delete "nome_snapshot"

Ripristinare uno snapshot

	vboxmanage snapshot "nome_macchina_virtuale" restore "nome_snapshot"

Esportare una VM formato OVA

	vboxmanage export <name or UUID>  -o image.ova

Importare una VM formato OVA

	vboxmanage import image.ova

## Definire le regole di port forwarding

Aggiungere regole di port forwarding

	vboxmanage modifyvm "nome_macchina_virtuale" --natpf1 "ssh,tcp,,11000,,22"

Mostrare le regole di port forwarding della VM

	vboxmanage showvminfo "nome_macchina_virtuale" | grep "Rule("

	vboxmanage modifyvm "nome_macchina_virtuale" --natpf1 "nome_regola"

## Abilitare protocollo RDP (screen streaming per server headless)

Per effettuare uno streaming di Virtualbox devo installare Remmina (protocollo RDP)

	vboxmanage modifyvm $MACHINENAME --vrde on

	vboxmanage modifyvm $MACHINENAME --vrdemulticon on --vrdeport 10001

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
