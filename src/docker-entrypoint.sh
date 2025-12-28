#!/bin/bash
set -ex

rm -rf **/__pycache__

pip install -r requirements.txt

# Run with uvicorn externally (no import in app.py)
find . |entr -c -r -s "python ./app.py"