from pydantic import BaseModel

class URLModel(BaseModel):
    """
    Pydantic model for URL data.
    This model is used to validate the input data for creating or updating URLs.
    """
    name: str  # The name/key for the URL
    url: str   # The actual URL