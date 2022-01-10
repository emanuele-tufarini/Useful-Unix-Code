'''
eseguire lo script:

Rscript rScience.R

installare i requisiti dello script:

docker exec -it -u root <rContainer> bash

apt update && apt upgrade

apt install libmariadb-dev

installare il pacchetto RMariaDB (accedere alla shell di R):

install.packages("RMariaDB")
'''

library(DBI)
library(RMariaDB)

# Connect to the MySQL database
con <- dbConnect(RMariaDB::MariaDB(), 
             dbname = "DATABASE", 
             host = "HOSTNAME", 
             port = 3306,
             user = "USER",
             password = "PASSWORD")

df <- dbReadTable(con, "TABLE")

head(df)
