FROM python:3.11-slim-bullseye

WORKDIR /app

# Install system dependencies including entr
RUN apt-get update && apt-get install -qqy entr curl wget

# # Copy requirements and install Python dependencies
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# # Copy application code
# COPY src/ ./src/

# # Make docker-entrypoint.sh executable
# RUN chmod +x src/docker-entrypoint.sh

# Expose port
EXPOSE 8000

