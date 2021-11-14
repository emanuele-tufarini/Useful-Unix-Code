FROM ubuntu:<Version>
MAINTAINER <Name> <Surname> <EMAIL>
RUN mkdir work
WORKDIR work
RUN apt-get update 
RUN apt-get install -y --no-install-recommends tzdata
RUN apt-get install -y python3-pip 
RUN apt-get install -y jupyter-notebook 
RUN apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install mysqlclient 
COPY ./<Folder> .
RUN jupyter notebook --generate-config
CMD ["jupyter-notebook","--no-browser","--ip=0.0.0.0","--port=<ExposedPort>","--NotebookApp.token='<Token>'","--allow-root"]
EXPOSE <ExposedPort>

# docker build -t <ImageName> .
# docker run -p <HostPort>:<ExposedPort> --name <ContainerName> <ImageName>

