"""
Chat completions endpoint for LM Studio API integration.
"""

import logging
import requests
from fastapi import APIRouter, HTTPException
from models.schemas import ChatRequest
from config.settings import API_HEADERS, CHAT_COMPLETIONS_URL

router = APIRouter()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# chat completions
#
# purpose:
#
# receive an ollama call for chat completions
# https://docs.ollama.com/api/chat
#
# query backend to generate chat completions
# https://openrouter.ai/docs/api/api-reference/chat
#
# return to caller with ollama api compatible output
# https://docs.ollama.com/api/chat
#
@router.post("/api/chat")
async def chat_completions(request: ChatRequest):
    """
    Convert OpenAI-style chat completion requests to LM Studio-compatible requests.

    Purpose:
    - Receive an Ollama call for chat completions: https://docs.ollama.com/api/chat
    - Query backend to generate chat completions: https://openrouter.ai/docs/api/api-reference/chat
    - Return to caller with Ollama API compatible output: https://docs.ollama.com/api/chat
    """
    logging.info("🟢 Processing request for /api/chat")

    lm_studio_payload = {"model": request.model, "messages": request.messages}

    try:
        response = requests.post(
            CHAT_COMPLETIONS_URL, json=lm_studio_payload, headers=API_HEADERS
        )

        response.raise_for_status()
        response_json = response.json()

        return {
            "model": response_json["model"],
            "created_at": "2023-11-07T05:31:56Z",
            "message": {
                "role": "assistant",
                "content": response_json["choices"][0]["message"]["content"],
                "thinking": response_json["choices"][0]["message"]["reasoning"],
                "tool_calls": [
                    {
                        "function": {
                            "name": "<string>",
                            "description": "<string>",
                            "arguments": {},
                        }
                    }
                ],
                "images": ["<string>"],
            },
            "done": True,
            "done_reason": response_json["object"],
            "total_duration": 123,
            "load_duration": 123,
            "prompt_eval_count": 123,
            "prompt_eval_duration": 123,
            "eval_count": 123,
            "eval_duration": 123,
            "logprobs": [
                {
                    "token": "<string>",
                    "logprob": 123,
                    "bytes": [123],
                    "top_logprobs": [
                        {"token": "<string>", "logprob": 123, "bytes": [123]}
                    ],
                }
            ],
        }

    except requests.exceptions.RequestException as e:
        logging.error(f"❌ LM Studio request failed: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"LM Studio request failed: {str(e)}"
        )
