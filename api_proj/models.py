from pydantic import BaseModel , HttpUrl

class Todo(BaseModel):
    """
    Pydantic model for URL data.
    This model is used to validate the input data for creating or updating URLs.
    """
    # id:int
    name: str  # The name/key for the URL
    url: HttpUrl  # Ensures it's a valid HTTP/HTTPS URL