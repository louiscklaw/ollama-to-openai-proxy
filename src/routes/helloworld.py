"""
Helloworld endpoint for testing purposes.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/helloworld")
async def helloworld():
    """Simple helloworld endpoint for testing."""
    return "fine, how are you"
