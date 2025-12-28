#!/bin/bash

# dc_up.sh - Start helloworld service

sudo chown 1000:1000 -R ..

echo "Starting helloworld app..."
docker compose up -d
# --build

echo "Service started. Opening shell in container..."
docker compose exec -it app bash

# echo "Following logs..."
# docker compose logs -f