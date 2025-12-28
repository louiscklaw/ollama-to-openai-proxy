"""
Pydantic models for request/response schemas.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for chat completions endpoint."""

    model: str = Field(..., description="Model name to use for generation")
    messages: List[dict] = Field(..., description="List of chat messages")
    stream: bool = Field(default=False, description="Whether to stream the response")
    temperature: float = Field(default=0.7, description="Sampling temperature")
    max_tokens: int = Field(default=512, description="Maximum tokens to generate")


class GenerateRequest(BaseModel):
    """Request model for text generation endpoint."""

    model: str = Field(..., description="Model name to use for generation")
    prompt: str = Field(..., description="Text prompt for generation")
    stream: bool = Field(default=False, description="Whether to stream the response")
    temperature: float = Field(default=0.7, description="Sampling temperature")
    max_tokens: int = Field(default=512, description="Maximum tokens to generate")
