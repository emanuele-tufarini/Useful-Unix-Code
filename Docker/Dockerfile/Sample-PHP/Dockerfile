# Creare nella directory del Dockerfile un file index.php

FROM php:7.4-cli
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
CMD [ "php", "./index.php" ]

# docker build -t <ImageName> .
# docker run -it --rm --name <ContainerName> <ImageName>
