#!/bin/sh

docker-compose build test &&
docker-compose up test || (
  echo "docker-compose not present, try running install-env.sh first"
  return 1
)
