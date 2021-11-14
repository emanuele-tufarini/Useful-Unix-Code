FROM ubuntu:latest
RUN apt update && apt install  openssh-server sudo -y
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1000 <User> 
RUN  echo '<User> :<User> ' | chpasswd
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]

# docker build -t <ImageName> .
# docker run -dit --name <ContainerName> -p <HostPort>:22 <ImageName>
# ssh <User>@<ContainerIP> -p <HostPort>
# user <User>  password <User> 
