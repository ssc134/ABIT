#!/bin/bash
docker build \
--file=flask_server.Dockerfile \
--tag="flask_server:0.1" \
.

docker create \
--interactive \
--tty \
#--rm \
--name=flask_server \
--publish-all \
--mount type=bind,source="$(pwd)",target=/home/flask_server_user/src \
--workdir /home/flask_server_user/src \
flask_server:0.1

docker start flask_server
docker port flask_server
docker attach flask_server

