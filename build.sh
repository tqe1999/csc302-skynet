#!/bin/sh

docker-compose up --build || (
  echo "docker-compose not present, try running install-env.sh first"
  return 1
)