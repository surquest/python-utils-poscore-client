from __future__ import annotations
from pydantic import BaseModel
import uuid


class Blob(BaseModel):
    id: uuid.UUID
    file_name: str
    content_type: str
    content: bytes
