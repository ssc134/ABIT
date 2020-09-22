#!/bin/bash
docker build \
--file=flask_server.Dockerfile \
--tag="flask_server:0.1" \
.