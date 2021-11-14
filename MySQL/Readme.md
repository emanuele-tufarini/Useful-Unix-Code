## Comandi base MySQL

Eseguire il login con MySQL

	  mysql -u root -p

Eseguire il login con MySQL specificando host e password

	mysql -h <ServerIP> -u <User> -P <Port> -p

## Procedure di backup

Effettuare il backup di un database specifico con MySQL

	mysqldump -u root -p <DBname> > DB-backup.sql
 
Effettuare il backup delle tabelle con MySQL

	mysqldump -u root -p <DBname> <Table1> <Table2> > <BackupName>.sql
  
Effettuare il backup compresso (GZ) di un database specifico con MySQL

	mysqldump -u <User> -p <DBname> | gzip > <BackupName>.sql.gz

Effettuare il backup da un host remoto di un database specifico con MySQL

	mysqldump -P <Port> -h <ServerIP> -u <User> -p <DBname> > <BackupName>.sql
  
Effettuare il backup di tutti i database con MySQL

	mysqldump --all-databases -u <User> -p<Password> > <BackupName>-$(date +%F).sql
  
Effettuare il backup di un database MySQL in un container Docker

	docker exec <ContainerID> sh -c 'exec mysqldump --all-databases -u<User> -p<Password>' > <BackupName>.sql

## Procedure di Restore

Effettuare il restore di tutti i database MySQL

	mysql --all-databases -u root -pPASSWORD < DB-full-backup.sql

Effettuare il restore di uno specifico database MySQL in un container Docker

	docker exec [container_id] sh -c 'exec mysql --all-databases -uroot -pPASSWORD' < DB-full-backup.sql

## Comandi MySQL

Visualizzare tutti i database

	SHOW DATABASES;

Creare un database

	CREATE DATABASE [nome_database];

Utilizzare un database

	USE [nome_database];
  
Creare una tabella

	CREATE TABLE [nome_tabella] {

	column1 int(3) NOT NULL AUTO_INCREMENT,

	column2 VARCHAR(255),

	column3 VARCHAR(255),

	PRIMARY KEY (column1)

	};

Ottenere la descrizione della tabella

	DESCRIBE TABLE [nome_tabella];
  
Inserire i dati in una tabella (1 metodo)

	INSERT INTO table_name (column1, column2, column3) VALUES (value1, value2, value3);
  
Inserire i dati in una tabella (2 metodo)

	INSERT INTO table SET column1=value1, column2=value2, column3=value3;
  
Mostrare il contenuto di una tabella

	SELECT * FROM [nome_tabella];
  
SELECT con condizione WHERE

	SELECT column1, column2 FROM [nome_tabella] WHERE column3 = [condizione];
  
Aggiornare i campi di una tabella

	UPDATE [nome_tabella] SET column1 = [variabile] WHERE column3 = [condizione];
  
UPDATE di una colonna di una tabella (calcolata a partire dalle altre colonne se una condizione è soddisfatta)

	UPDATE `DB`.`TABELLA` SET colonna1 = colonna2 - colonna3 WHERE colonna4 > [condizione];
  
Cancellare un database

	DROP DATABASE [nome_database];
  
Cancellare una tabella

	DROP TABLE [nome_tabella];
  
Tipi di chiavi

	UNIQUE KEY

	PRIMARY KEY

	FOREIGN KEY
  
Creare una tabella relazionale (in questo caso la tabella relazionale è nominata tabella_relazionale3)

	CREATE TABLE tabella1 {

	T1colonna1 VARCHAR(255) NOT NULL,

	PRIMARY KEY (T1colonna1)

	};

	CREATE TABLE tabella2 {

	T2colonna1 VARCHAR(255) NOT NULL,

	PRIMARY KEY (T2colonna1)

	};

	CREATE TABLE tabella_relazionale3 {

	id int(4) AUTO_INCREMENT,

	T1colonna1 VARCHAR(255) NOT NULL,

	T2colonna1 VARCHAR(255) NOT NULL,

	PRIMARY KEY (id),

	FOREIGN KEY (T1colonna1) REFERENCE tabella1 (T1colonna1),

	FOREIGN KEY (T2colonna1) REFERENCE tabella2 (T2colonna1),

	};
  
Queries con JOIN

	SELECT * FROM tabella1

	JOIN tabella_relazionale3 on tabella1.T1colonna1 = tabella_relazionale3.T1colonna1

	WHERE tabella_relazionale3.T1colonna1 = <Condizione>;
  
## Creare procedure MySQL con phpMyAdmin

- Selezionare il DB

- Procedure

- Aggiungi una routine

- (Parametri: Elimina, tipo di accesso dati SQL: CONTAINS SQL) Inserire il nome della routine e inserire il codice SQL in Definizione.

La procedura deve essere inclusa tra BEGIN e END.
  
ESEMPIO

Imposta l’AUTO_INCREMENT della tabella = 1, poi esegui l’INSERT della differenza tra le due tabelle

	BEGIN

	ALTER TABLE `Tabella2` AUTO_INCREMENT = 1;

	INSERT INTO `Database2`.`Tabella2` (`Colonna1`,`Colonna2`,`Colonna3`)

	SELECT `Colonna1`,`Colonna2`,`Colonna3` FROM Tabella1

	EXCEPT

	SELECT `Colonna1`,`Colonna2`,`Colonna3` FROM Tabella2

	END

Operatori utili EXCEPT (differenza), INTERSECTION (intersezione), UNION (unione)

CURRENT_DATE (2021-07-07) e NOW() (2021-07-07 08:53:26)

	SELECT CURRENT_DATE 

	SELECT NOW()

SELECT colonna1, colonna2, count ALL dove la colonna1 corrisponde alla data di oggi

	SELECT colonna1, colonna2 , count(*) FROM Tabella WHERE Colonna1 LIKE CURRENT_DATE GROUP BY colonna1, colonna2;
