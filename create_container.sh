#!/bin/bash
docker build build_image.Dockerfile\
--file=build_image.Dockerfile \
--tag="flask_server:0.1"
.