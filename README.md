# Ollama to OpenAI Proxy

A FastAPI-based proxy service that seamlessly translates requests between Ollama API format and OpenAI-compatible API format (specifically for LM Studio). This proxy enables you to use Ollama-compatible clients with LM Studio backend services.

## 🚀 Features

- **API Translation**: Converts between Ollama and OpenAI/LM Studio API formats
- **Multiple Endpoints**: Supports model listing, text generation, and chat completions
- **FastAPI Based**: Built with modern async Python framework
- **Docker Ready**: Complete containerization with docker-compose
- **Structured Logging**: Comprehensive logging with emoji indicators for easy debugging
- **Type Safety**: Full type hints and Pydantic models for request/response validation

## 📋 Supported Endpoints

| Ollama Endpoint | Description | OpenAI Equivalent |
|-----------------|-------------|-------------------|
| `GET /api/tags` | List available models | `GET /v1/models` |
| `POST /api/generate` | Text generation | `POST /v1/completions` |
| `POST /api/chat` | Chat completions | `POST /v1/chat/completions` |

## 🏗️ Architecture

```mermaid
graph LR
    subgraph "Client Layer"
        O1[Ollama Client]
        O2[OpenAI Client]
    end

    subgraph "Proxy Service"
        R[FastAPI Router]
        T[Request Transformer]
        L[Response Transformer]
    end

    subgraph "Backend Layer"
        LM[LM Studio API]
    end

    %% Request Flow
    O1 -->|/api/chat<br/>/api/generate<br/>/api/tags| R
    O2 -->|/v1/chat/completions<br/>/v1/completions<br/>/v1/models| R
    R --> T
    T -->|Translate Request| LM
    LM -->|LM Studio Response| L
    L -->|Translate Response| R
    R --> O1
    R --> O2

    %% Styling
    classDef client fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef proxy fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef backend fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px

    class O1,O2 client
    class R,T,L proxy
    class LM backend
```

The proxy acts as a translation layer, allowing clients that expect Ollama API responses to work seamlessly with LM Studio backends.

## 🛠️ Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd docker

# Start the service
docker-compose up -d

# The service will be available at http://localhost:11434
```

### Option 2: Local Development

```bash
# Navigate to the source directory
cd src

# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
# or
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Option 3: Quick Start Script

```bash
# From project directory
./docker/dc_up.sh
```

## ⚙️ Configuration

The proxy service can be configured by modifying `src/config/settings.py`:

```python
# LM Studio API Configuration
LM_STUDIO_API = "http://192.168.10.1:8400/api/v1"

# API Headers (add your authentication if needed)
API_HEADERS = {
    "Authorization": "Bearer your_access_key_here",
    "Content-Type": "application/json",
}
```

## 📖 Usage Examples

### List Models (Ollama Format)

```bash
curl -X GET http://localhost:11434/api/tags
```

Response:
```json
{
  "models": [
    {
      "name": "llama2",
      "modified_at": "2023-08-01T00:00:00.000000000-00:00",
      "size": 3792359401,
      "digest": "a2af6cc3eb7fa8be8504abaf9b04e88f17a119ec3f04a3addf55f55f92841195f5a",
      "details": {
        "format": "ggml",
        "family": "llama",
        "families": ["llama"],
        "parameter_size": "7B",
        "quantization_level": "q4_0"
      }
    }
  ],
  "status": "tags endpoint working"
}
```

### Generate Text

```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama2",
    "prompt": "Why is the sky blue?",
    "stream": false
  }'
```

### Chat Completions

```bash
curl -X POST http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama2",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ],
    "stream": false
  }'
```

## 🐳 Docker Deployment

The service includes comprehensive Docker support:

### Docker Compose
- **Service Name**: `ollama_to_openai_proxy`
- **Port Mapping**: `11434:8000` (Ollama-compatible port)
- **Auto-restart**: `unless-stopped`
- **Volume Mount**: Local source code for development

### Build and Run Manually
```bash
# Build the image
docker build -t ollama-proxy -f docker/Dockerfile .

# Run the container
docker run -p 11434:8000 ollama-proxy
```

## 🔧 Development

### Project Structure
```
<repo>/
├── src/
│   ├── app.py                 # Main FastAPI application
│   ├── config/
│   │   └── settings.py         # Configuration settings
│   ├── models/
│   │   └── schemas.py         # Pydantic request/response models
│   └── routes/
│       ├── api/
│       │   ├── chat.py         # Chat completions endpoint
│       │   ├── generate.py     # Text generation endpoint
│       │   └── tags.py         # Model listing endpoint
│       └── proxy.py            # Route aggregator
└── docker/
    ├── docker-compose.yml      # Docker Compose configuration
    ├── Dockerfile              # Container build definition
    └── dc_up.sh               # Quick start script
```

### Development Commands

```bash
# Install dependencies
pip install -r src/requirements.txt

# Run with auto-reload
uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload

# Linting and formatting
pip install ruff black mypy
ruff check src/
ruff format src/
black src/
mypy src/

# Testing (when available)
python -m pytest tests/ -v
```

## 📝 API Reference

### Core Endpoints

- **GET /api/tags**: Lists available models
- **POST /api/generate**: Generates text completion
- **POST /api/chat**: Handles chat completions

### Request/Response Format

All endpoints follow Ollama API specification and translate to/from LM Studio internally. See the usage examples above for detailed request/response formats.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following standard Python and FastAPI best practices
4. Run linting and type checking
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**: Change the port mapping in docker-compose.yml
2. **Connection Refused**: Check LM Studio backend configuration
3. **Authentication Errors**: Verify API headers in settings.py

### Logging

The service provides structured logging with emoji indicators:
- 🟢 Successful operations
- 📡 Request/response logging
- ❌ Errors
- 🔄 Transformations/conversions

Check container logs with:
```bash
docker-compose logs -f
```

## 📞 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the code documentation
3. Open an issue in the repository

## application

- this work best with `logseq` `ollama` plugin.
![](./documentation/Logseq_SwGONorEnH.png)

- setting of the ollama endpoint
![](./documentation/Logseq_2b0jz60xPK.png)

---

**Note**: This proxy service is designed to work specifically with LM Studio backends. For other AI service providers, you may need to modify the translation logic in the route handlers.
