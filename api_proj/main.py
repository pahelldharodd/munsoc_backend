from fastapi import FastAPI
from typing import Dict
from .models import URLModel  # Import the model from models.py

app = FastAPI()

# Dummy database
urls_db: Dict[str, str] = {
    "github": "https://github.com",
    "google": "https://www.google.com",
}

@app.get("/", summary="Root endpoint", description="Welcome to the URL API!")
def root():

    return {"message": "Welcome to the URL API!"}   

@app.get("/urls", summary="Get all URLs", description="Retrieve all URLs stored in the database.")
def get_urls():

    return urls_db

@app.post("/urls", summary="Create a new URL", description="Add a new URL to the database.")
def create_url(url_data: URLModel):

    urls_db[url_data.name] = url_data.url
    return {"message": "URL added", "data": url_data}

@app.put("/urls/{name}", summary="Update an existing URL", description="Update the URL for a given name.")
def update_url(name: str, url_data: URLModel):

    urls_db[name] = url_data.url
    return {"message": "URL updated", "data": url_data}

@app.delete("/urls/{name}", summary="Delete a URL", description="Remove a URL from the database by its name.")
def delete_url(name: str):

    urls_db.pop(name, None)
    return {"message": "URL deleted"}
