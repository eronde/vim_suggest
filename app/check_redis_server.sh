#!/bin/bash 

echo "REDIS_IP=\"$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' vim-bigram-suggest-redis-dev)\"" > redis_config.py

