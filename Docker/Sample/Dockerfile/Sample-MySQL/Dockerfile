# Creare nella directory del Dockerfile una cartella chiamata <sql-script> contenente tutti gli script SQL

FROM mysql
ENV MYSQL_DATABASE <DBname>
COPY ./sql-script/ /docker-entrypoint-initdb.d/

# docker build -t <ImageName> . 
# docker run -d -p <HostPort>:3306 --name <ContainerName> -e MYSQL_ROOT_PASSWORD=<Password <ImageName>
# docker exec -it <ContainerName> bash 
# mysql -u root -p
# docker run --name <ContainerName> -d --link <ContainerName>:db -p <HostPort>:80 phpmyadmin
