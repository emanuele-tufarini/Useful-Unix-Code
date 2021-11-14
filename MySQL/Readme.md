## Comandi base MySQL

Eseguire il login su MySQL

	  mysql -u root -p

Eseguire il login su MySQL specificando host e password

    mysql -h <ServerIP> -u <User> -P <Port> -p

## Procedure di backup

Backup di uno specifico database MySQL

    mysqldump -u root -p nome_db > DB-backup.sql
 
Backup di tabelle MySQL

    mysqldump -u root -p nome_db tabella1 tabella2 > TABLE-backup.sql
  
Backup compresso MySQL

    mysqldump -u <User> -p <DBname> | gzip > <BackupName>.sql.gz

Backup su un host remoto MySQL

    mysqldump -P <Port> -h <ServerIP> -u <User> -p <DBname> > <BackupName>.sql
  
Backup di tutti i database MySQL

    mysqldump --all-databases -u <User> -p<Password> > <BackupName>-$(date +%F).sql
  
Backup di un database MySQL dentro un container Docker

    docker exec <ContainerID> sh -c 'exec mysqldump --all-databases -u<User> -p<Password>' > <BackupName>.sql

## Procedure di Restore

Restore database MySQL

    mysql --all-databases -u root -pPASSWORD < DB-full-backup.sql

Restore di un database MySQL dentro un container Docker

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
  
Sampare il contenuto di una tabella

    SELECT * FROM [nome_tabella];
  
SELECT con condizione WHERE

    SELECT column1, column2 FROM [nome_tabella] WHERE column3 = [condizione];
  
Aggiornare i campi di una tabella

    UPDATE [nome_tabella] SET column1 = [variabile] WHERE column3 = [condizione];
  
UPDATE colonna di una tabella (calcolata a partire dalle altre colonne se una condizione è soddisfatta)

    UPDATE `DB`.`TABELLA` SET colonna1 = colonna2 - colonna3 WHERE colonna4 > [condizione];
  
Cancellare un database

    DROP DATABASE [nome_database];
  
Cancellare una tabella

    DROP TABLE [nome_tabella];
  
Tipi di chiavi

    UNIQUE KEY

    PRIMARY KEY

    FOREIGN KEY
  
Creare una tabella relazionale (tabella_relazionale3, tabella relazionale)

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

    WHERE tabella_relazionale3.T1colonna1 = [condizione];
  
## Creare procedure SQL con phpMyAdmin

Selezionare il DB – Procedure – Aggiungi una routine (Parametri: Elimina, tipo di accesso dati SQL: CONTAINS SQL) Inserire il nome della routine e inserire il codice SQL in Definizione.

La procedura deve essere inclusa tra BEGIN e END.
  
ESEMPIO

Imposta l’AUTO_INCREMENT DELLA TABELLA AD 1, poi esegui l’INSERT della differenza tra le due tabelle

    BEGIN

    ALTER TABLE `Tabella2` AUTO_INCREMENT = 1;

    INSERT INTO `Database2`.`Tabella2` (`Colonna1`,`Colonna2`,`Colonna3`)

    SELECT `Colonna1`,`Colonna2`,`Colonna3` FROM Tabella1

    EXCEPT

    SELECT `Colonna1`,`Colonna2`,`Colonna3` FROM Tabella2

    END

Operatori utili EXCEPT (differenza), INTERSECTION (intersezione), UNION (unione)

Current Date (2021-07-07) e Now (2021-07-07 08:53:26)

    SELECT CURRENT DATE 

    SELECT NOW()

SELECT colonna1, colonna2, count ALL dove la colonna1 corrisponde alla data di oggi

    SELECT colonna1, colonna2 , count(*) FROM Tabella WHERE Colonna1 LIKE CURRENT_DATE GROUP BY colonna1, colonna2;
