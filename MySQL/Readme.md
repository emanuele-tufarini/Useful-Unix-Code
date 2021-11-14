## Connettersi al DB con MySQL

Eseguire il login con MySQL

	  mysql -u root -p

Eseguire il login con MySQL specificando host e password

	mysql -h <ServerIP> -u <User> -P <Port> -p

## Procedure di backup

Effettuare il backup di un DB specifico con MySQL

	mysqldump -u root -p <DBname> > DB-backup.sql
 
Effettuare il backup delle tabelle con MySQL

	mysqldump -u root -p <DBname> <Table1> <Table2> > <BackupName>.sql
  
Effettuare il backup compresso (GZ) di un DB specifico con MySQL

	mysqldump -u <User> -p <DBname> | gzip > <BackupName>.sql.gz

Effettuare il backup da un host remoto di un DB specifico con MySQL

	mysqldump -P <Port> -h <ServerIP> -u <User> -p <DBname> > <BackupName>.sql
  
Effettuare il backup di tutti i DB con MySQL

	mysqldump --all-databases -u <User> -p<Password> > <BackupName>-$(date +%F).sql
  
Effettuare il backup di un DB MySQL in un container Docker

	docker exec <ContainerID> sh -c 'exec mysqldump --all-databases -u<User> -p<Password>' > <BackupName>.sql

## Procedure di Restore

Effettuare il restore di tutti i DB MySQL

	mysql --all-databases -u root -pPASSWORD < DB-full-backup.sql

Effettuare il restore delle tabelle con MySQL

	mysqldump -u -p <DBname> <TableName> < <BackupName>.sql

Effettuare il restore di uno specifico DB MySQL in un container Docker

	docker exec <ContainerID> sh -c 'exec mysql --all-databases -uroot -pPASSWORD' < DB-full-backup.sql

## Comandi MySQL

Visualizzare tutti i DB

	SHOW DATABASES;

Creare un DB

	CREATE DATABASE <DBname>;

Utilizzare un DB

	USE <DBname>;
  
Creare una tabella (prima colonna chiave primaria AUTO_INCREMENT)

	CREATE TABLE <TableName> {

	<PRIMARYColumn> int(3) NOT NULL AUTO_INCREMENT,

	<Column2> VARCHAR(255),

	<Column3> VARCHAR(255),

	PRIMARY KEY (<PRIMARYColumn>)

	};

Ottenere la descrizione della tabella

	DESCRIBE TABLE <TableName>;
  
Inserire i dati in una tabella (1 metodo)

	INSERT INTO table_name (<Column1>, <Column2>, <Column3>) VALUES (<Value1>, <Value2>, <Value3>);
  
Inserire i dati in una tabella (2 metodo)

	INSERT INTO table SET <Column1>=<Value1>, <Column2>=<Value2>, <Column3>=<Value3>;
  
Mostrare il contenuto di una tabella

	SELECT * FROM <TableName>;
  
SELECT con condizione WHERE

	SELECT <Column1>, <Column2> FROM <TableName> WHERE column3 = <Condizione>;
  
Aggiornare i campi di una tabella

	UPDATE <TableName> SET <Column1> = <Variable> WHERE <Column2> = <Condizione>;
  
UPDATE di una colonna di una tabella (calcolata a partire dalle altre colonne se una condizione è soddisfatta)

	UPDATE `DB`.`TABELLA` SET <Column1> = <Column2> - <Column3> WHERE <Column4> > <Condizione>;
  
Cancellare un DB

	DROP DATABASE <DBname>;
  
Cancellare una tabella

	DROP TABLE <TableName>;
  
Tipi di chiavi

	UNIQUE KEY

	PRIMARY KEY

	FOREIGN KEY
  
Creare una tabella relazionale (in questo caso la tabella relazionale è nominata <RelationalTable>)

	CREATE TABLE <Table1> {

	<Table1Column1> VARCHAR(255) NOT NULL,

	PRIMARY KEY (<Table1Column1>)

	};

	CREATE TABLE <Table2> {

	<Table2Column1> VARCHAR(255) NOT NULL,

	PRIMARY KEY (<Table2Column1>)

	};

	CREATE TABLE <RelationalTable> {

	ID int(4) AUTO_INCREMENT,

	<Table1Column1> VARCHAR(255) NOT NULL,

	<Table2Column1> VARCHAR(255) NOT NULL,

	PRIMARY KEY (<ID>),

	FOREIGN KEY (<Table1Column1>) REFERENCE tabella1 (<Table1Column1>),

	FOREIGN KEY (<Table2Column1>) REFERENCE tabella2 (<Table2Column1>),

	};
  
Queries con JOIN

	SELECT * FROM <Table1>

	JOIN <RelationalTable> on <Table1>.<Table1Column1> = <RelationalTable>.<Table1Column1>

	WHERE <RelationalTable>.<Table1Column1> = <Condizione>;
  
## Creare procedure MySQL con phpMyAdmin

- Selezionare il DB

- Procedure

- Aggiungi una routine

- (Parametri: Elimina, tipo di accesso dati SQL: CONTAINS SQL) Inserire il nome della routine e inserire il codice SQL in Definizione.

La procedura deve essere inclusa tra BEGIN e END.
  
ESEMPIO

Imposta l’AUTO_INCREMENT della tabella = 1, poi esegui l’INSERT della differenza tra le due tabelle

	BEGIN

	ALTER TABLE <Table2> AUTO_INCREMENT = 1;

	INSERT INTO <Database2>.<Table2> (<Column1>,<Column2>,<Column3>)

	SELECT <Column1>,<Column2>,<Column3> FROM <Table1>

	EXCEPT

	SELECT <Column1>,<Column2>,<Column3> FROM <Table2>

	END

Operatori utili EXCEPT (differenza), INTERSECTION (intersezione), UNION (unione)

CURRENT_DATE (2021-07-07) e NOW() (2021-07-07 08:53:26)

	SELECT CURRENT_DATE 

	SELECT NOW()

SELECT colonna1, colonna2, count ALL dove la colonna1 corrisponde alla data di oggi

	SELECT <Column1>, <Column2> , count(*) FROM <Table> WHERE <Column1> LIKE CURRENT_DATE GROUP BY <Column1>, <Column2>;
