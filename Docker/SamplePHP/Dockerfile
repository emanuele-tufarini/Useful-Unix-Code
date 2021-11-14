# Sample of PHP Container
FROM php:7.4-cli
# Creare nella directory del Dockerfile un file index.php
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
CMD [ "php", "./index.php" ]

# docker build -t <ImageName> .
# docker run -it --rm --name <ContainerName> <ImageName>
