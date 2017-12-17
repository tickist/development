#!/usr/bin/env bash

docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
docker-compose  up   --no-deps --build --force-recreate frontend