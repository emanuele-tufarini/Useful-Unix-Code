FROM ubuntu:latest
MAINTAINER <Name> <Surname> <EMAIL>
RUN mkdir work
WORKDIR work
RUN apt update 
RUN apt install -y --no-install-recommends tzdata
RUN apt install -y python3-pip 
RUN apt install -y jupyter-notebook 
RUN apt install -y mysql-server
RUN apt install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip3 install mysqlclient
CMD ["jupyter-notebook","--no-browser","--ip=0.0.0.0","--port=8888","--NotebookApp.token='<Token>'","--allow-root"]
EXPOSE 8888
