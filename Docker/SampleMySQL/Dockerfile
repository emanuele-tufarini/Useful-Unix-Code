# Sample of MySQL Dockerfile
FROM mysql
ENV MYSQL_DATABASE <DBname>
# Creare una cartella <SqlScript> nella stessa directory del Dockerfile
# La cartella <SqlScript> deve contenere gli script sql
COPY ./<SqlScript>/ /docker-entrypoint-initdb.d/

# COMANDI PER AVVIARE IL CONTAINER UTILIZZARLO E COLLEGARLO A PHPMYADMIN
# docker build -t <ImageName> . 
# docker run -d -p <HostPort ex 3306>:3306 --name <ContainerName> -e MYSQL_ROOT_PASSWORD=<Password <ImageName>
# docker exec -it <ContainerName> bash 
# mysql -u root -p # password : miqualat2020
# docker run --name miqualat-phpmyadmin-container -d --link miqualat-mysql-container:db -p <HostPort ex 8080>:80 phpmyadmin
