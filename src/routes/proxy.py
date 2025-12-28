"""
Proxy module that aggregates all proxy-related routers.
"""

from fastapi import APIRouter
from .api.chat import router as chat_router
from .api.tags import router as tags_router
from .api.generate import router as generate_router

# Create main proxy router
router = APIRouter()

# Include individual proxy routers
router.include_router(chat_router)
router.include_router(tags_router)
router.include_router(generate_router)
