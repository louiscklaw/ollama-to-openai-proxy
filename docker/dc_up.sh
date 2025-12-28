#!/bin/bash

# dc_up.sh - Start helloworld service

chown 1000:1000 -R ..

cp -r ../src/requirements.txt .

# docker build --network host --no-cache -t ollama_to_openai_proxy .
docker build --network host --no-cache -t ollama_to_openai_proxy_watchdog ./Dockerfile.watchdog

echo "Starting helloworld app..."
docker compose up -d
# --build

echo "Service started. Opening shell in container..."
# docker compose exec -it app bash

# echo "Following logs..."
# docker compose logs -f