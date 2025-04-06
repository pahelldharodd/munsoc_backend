from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    """
    Pydantic model for URL data.
    This model is used to validate the input data for creating or updating URLs.
    """
    # id:int
    name: str  # The name/key for the URL
    url: str   # The actual URL