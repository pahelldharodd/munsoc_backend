from fastapi import FastAPI
import models # Import the model from models.py
todos=[]
app = FastAPI()
@app.get("/Todo",response_model=list[models.Todo])
async def send_todos():
    return todos

@app.post("/Todo",response_model=models.Todo)
async def create(todo:models.Todo):
    todos.append(todo)
        
    