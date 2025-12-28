"""
Configuration settings for the proxy service.
"""

from typing import Dict, Any

# LM Studio API Configuration
LM_STUDIO_API = "http://192.168.10.1:8400/api/v1"

# API Headers
API_HEADERS = {
    "Authorization": "Bearer your_local_access_key_here",
    "Content-Type": "application/json",
}

# Model Configuration
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 512

# API Endpoints
CHAT_COMPLETIONS_URL = f"{LM_STUDIO_API}/chat/completions"
MODELS_URL = f"{LM_STUDIO_API}/models"
