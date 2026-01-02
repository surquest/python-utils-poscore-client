from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class InstallationResponse(BaseModel):
    """Represents an individual photo or note response for a specific row."""
    type: int
    photoId: str
    photoName: str
    note: Optional[str] = None
