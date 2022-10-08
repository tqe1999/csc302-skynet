#!/bin/sh

sudo docker compose build || (
  echo "docker-compose not present, try running install-env.sh first"
  return 1
)