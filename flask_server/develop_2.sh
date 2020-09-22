#!/bin/bash
docker build \
--file=flask_server_2.Dockerfile \
--tag="flask_server_2:0.1" \
.

docker create \
--interactive \
--tty \
--rm \
--name=flask_server \
--publish-all \
--mount type=bind,source="$(pwd)/src",target=/home/flask_server_user/src \
--workdir /home/flask_server_user/src \
flask_server:0.1