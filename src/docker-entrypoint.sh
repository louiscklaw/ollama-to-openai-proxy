#!/bin/bash
set -ex

rm -rf **/__pycache__

pip install -r requirements.txt

# Run with uvicorn externally (no import in app.py)

python ./app.py

while true; do
    sleep 15
    python ./app.py
done
