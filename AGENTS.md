# AGENTS.md

This file contains guidelines and commands for agentic coding agents working on this Ollama to OpenAI Proxy repository.

## Build/Lint/Test Commands

### Development Setup
```bash
# Install dependencies
pip install -r src/requirements.txt

# Install development tools
pip install ruff black mypy pytest

# Run development server with auto-reload
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload

# Alternative: run from src directory
cd src && python app.py
```

### Docker Development
```bash
# Start with docker-compose
cd docker && docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Quick start script
./docker/dc_up.sh
```

### Code Quality
```bash
# Lint with ruff
ruff check src/
ruff format src/

# Format with black
black src/

# Type checking
mypy src/

# Self-check script
./scripts/ai_selfcheck.sh

# Reset environment
./scripts/ai_reset_env.sh
```

### Testing
```bash
# Run tests (when available)
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_specific.py -v
```

## Code Style Guidelines

### Project Structure
- **Main app**: `src/app.py` - FastAPI application entry point
- **Configuration**: `src/config/settings.py` - All configuration variables
- **Models**: `src/models/schemas.py` - Pydantic request/response models
- **Routes**: `src/routes/` - API endpoint handlers
  - `proxy.py` - Route aggregator
  - `api/` - Individual endpoint implementations
- **Docker**: `docker/` - Container configuration and scripts

### Import Style
```python
# Standard library imports first
import logging
from typing import Dict, List, Optional

# Third-party imports next
import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

# Local imports last
from config.settings import API_HEADERS, CHAT_COMPLETIONS_URL
from models.schemas import ChatRequest
```

### Code Formatting
- **Indentation**: 4 spaces
- **Line length**: Maximum 88 characters (Black default)
- **String quotes**: Double quotes for consistency
- **Docstrings**: Triple quotes with description and purpose details

### Naming Conventions
- **Variables**: `snake_case`
- **Functions**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Files**: `snake_case.py`
- **Routers**: `router` variable name

### Error Handling
```python
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    response_json = response.json()
    return transformed_response
except requests.exceptions.RequestException as e:
    logging.error(f"❌ Request failed: {str(e)}")
    raise HTTPException(status_code=500, detail=f"Request failed: {str(e)}")
```

### Logging Patterns
- Use structured logging with emoji indicators
- **🟢** for successful operations
- **📡** for request/response logging
- **❌** for errors
- **🔄** for transformations

```python
logging.info("🟢 Processing request for /api/endpoint")
logging.error(f"❌ Operation failed: {error_message}")
```

### API Endpoint Patterns
- Use FastAPI `APIRouter` for modular routing
- Include comprehensive docstrings with purpose, input/output APIs
- Follow the documented pattern in existing routes
- Always include request/response transformation logic

```python
@router.post("/api/endpoint")
async def endpoint_handler(request: RequestModel):
    """
    Convert between API formats.
    
    Purpose:
    - Receive input format: [URL documentation]
    - Query backend: [URL documentation]
    - Return output format: [URL documentation]
    """
    logging.info("🟢 Processing request for /api/endpoint")
    
    try:
        # Transform request and call backend
        # Transform response and return
        pass
    except Exception as e:
        logging.error(f"❌ Request failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
```

### Pydantic Models
- Use `Field` for descriptions and defaults
- Include type hints for all fields
- Add comprehensive docstrings

```python
class ChatRequest(BaseModel):
    """Request model for chat completions endpoint."""
    
    model: str = Field(..., description="Model name to use for generation")
    messages: List[dict] = Field(..., description="List of chat messages")
    stream: bool = Field(default=False, description="Whether to stream the response")
```

### Configuration Management
- All configuration in `src/config/settings.py`
- Use environment variables for sensitive data
- Group related settings together
- Include type hints

### Docker Development
- Use volume mounts for live code reloading
- Set `PYTHONUNBUFFERED=1` and `PYTHONDONTWRITEBYTECODE=1`
- Expose port 8000 internally, map to 11434 externally

## Architecture Notes

This is a proxy service that translates between Ollama API format and LM Studio/OpenAI API format. Key patterns:

1. **Request Transformation**: Convert incoming Ollama requests to LM Studio format
2. **Backend Communication**: Use `requests` library with configured headers
3. **Response Transformation**: Convert LM Studio responses back to Ollama format
4. **Error Handling**: Consistent HTTP exceptions with logging

## Development Workflow

1. Make changes to source code in `src/`
2. Run linting commands to ensure code quality
3. Test using docker-compose for full integration
4. Check logs for emoji-indicated status messages
5. Verify API compatibility with both Ollama and LM Studio formats

## Port Configuration

- **Internal**: FastAPI runs on port 8000
- **External**: Docker maps to port 11434 (Ollama-compatible)
- **Backend**: LM Studio API typically on 192.168.10.1:8400

Always ensure these port mappings are maintained in docker-compose.yml.