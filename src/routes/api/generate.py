"""
Generate endpoint for LM Studio API integration.
"""

import logging
import requests
from fastapi import APIRouter, HTTPException
from models.schemas import GenerateRequest
from config.settings import API_HEADERS, CHAT_COMPLETIONS_URL

router = APIRouter()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# generate text completion
#
# purpose:
#
# receive an ollama call for text generation
# https://docs.ollama.com/api/generate
#
# query backend to generate text completion
# https://openrouter.ai/docs/api/api-reference/chat
#
# return to caller with ollama api compatible output
# https://docs.ollama.com/api/generate
#
@router.post("/api/generate")
async def generate_text(request: GenerateRequest):
    """
    Convert Ollama-style generate requests to LM Studio-compatible requests.

    Purpose:
    - Receive an Ollama call for text generation: https://docs.ollama.com/api/generate
    - Query backend to generate text completion: https://openrouter.ai/docs/api/api-reference/chat
    - Return to caller with Ollama API compatible output: https://docs.ollama.com/api/generate
    """
    logging.info("🟢 Processing request for /api/generate")

    # Convert Ollama generate request to LM Studio chat completions format
    lm_studio_payload = {
        "model": request.model,
        "messages": [{"role": "user", "content": request.prompt}],
        "temperature": request.temperature,
        "max_tokens": request.max_tokens,
        "stream": request.stream,
    }

    try:
        response = requests.post(
            CHAT_COMPLETIONS_URL, json=lm_studio_payload, headers=API_HEADERS
        )

        response.raise_for_status()
        response_json = response.json()

        # Transform LM Studio response into Ollama-compatible format
        return {
            "model": request.model,
            "created_at": "2023-11-07T05:31:56Z",
            "response": response_json["choices"][0]["message"]["content"],
            "thinking": "",
            "done": True,
            "done_reason": "stop",
            "total_duration": 123456789,
            "load_duration": 12345678,
            "prompt_eval_count": len(request.prompt.split()),  # Rough estimate
            "prompt_eval_duration": 1234567,
            "eval_count": len(
                response_json["choices"][0]["message"]["content"].split()
            ),  # Rough estimate
            "eval_duration": 12345678,
            "logprobs": [],
        }

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ LM Studio request failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"LM Studio request failed: {str(e)}"
        )
