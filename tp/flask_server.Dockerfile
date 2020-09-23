FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y nano
RUN apt-get install -y python3.8
RUN apt-get install python3-pip -y
RUN pip3 install Flask
RUN pip3 install Flask-RESTful
RUN apt-get install -y sudo
RUN useradd flask_server_user -p 'temporary' -u 1001 -m
RUN passwd -d flask_server_user
RUN usermod -aG sudo flask_server_user
USER flask_server_user
WORKDIR /home/flask_server_user/src
ENV PORT=8888
EXPOSE 8888