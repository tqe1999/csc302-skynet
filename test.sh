#!/bin/sh

sudo docker compose build test &&
sudo docker compose up test || (
  echo "docker-compose not present, try running install-env.sh first"
  return 1
)
