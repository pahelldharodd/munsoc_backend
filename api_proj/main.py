from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Dummy database
urls_db: Dict[str, str] = {
    "github": "https://github.com",
    "google": "https://www.google.com",
}

# Pydantic model for input validation
class URLModel(BaseModel):
    name: str
    url: str

@app.get("/urls")
def get_urls():
    return urls_db

@app.post("/urls")
def create_url(url_data: URLModel):
    urls_db[url_data.name] = url_data.url
    return {"message": "URL added", "data": url_data}

@app.put("/urls/{name}")
def update_url(name: str, url_data: URLModel):
    urls_db[name] = url_data.url
    return {"message": "URL updated", "data": url_data}

@app.delete("/urls/{name}")
def delete_url(name: str):
    urls_db.pop(name, None)
    return {"message": "URL deleted"}
