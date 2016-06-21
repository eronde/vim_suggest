#!/bin/bash 

echo "REDIS_IP=\"$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' py-word-suggest-redis)\"" > config.py

