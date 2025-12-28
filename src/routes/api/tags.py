"""
Model listing endpoint for LM Studio API integration.
"""

import logging
import requests
from fastapi import APIRouter, HTTPException
from config.settings import API_HEADERS, MODELS_URL

router = APIRouter()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# list models
#
# purpose:
#
# receive an ollama call for listing models
# https://docs.ollama.com/api/tags
#
# query the backend to list models
# https://openrouter.ai/docs/api/api-reference/models/get-models
#
# return to the caller with ollama api compatible output
# https://docs.ollama.com/api/tags
#
@router.get("/api/tags")
async def get_tags():
    """
    List models from LM Studio and convert to Ollama-compatible format.

    Purpose:
    - Receive an Ollama call for listing models: https://docs.ollama.com/api/tags
    - Query the backend to list models: https://openrouter.ai/docs/api/api-reference/models/get-models
    - Return to the caller with Ollama API compatible output: https://docs.ollama.com/api/tags
    """
    logging.info("🟢 Processing request for /api/tags")

    try:
        response = requests.get(MODELS_URL, headers=API_HEADERS)
        response.raise_for_status()

        ao_data = response.json()["data"]
        model_ids = []

        for o_data in ao_data:
            model_ids.append(
                {
                    "name": o_data["id"],
                    "modified_at": "2025-01-01T00:00:00.000000000-00:00",
                    "size": 1024,
                    "digest": "a2af6cc3eb7fa8be8504abaf9b04e88f17a119ec3f04a3addf55f92841195f5a",
                    "details": {
                        "format": "N?A",
                        "family": "N?A",
                        "families": ["N/A"],
                        "parameter_size": "N/A",
                        "quantization_level": "N/A",
                    },
                }
            )

        return {"models": model_ids, "status": "tags endpoint working"}

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ Models request failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Models request failed: {str(e)}")
