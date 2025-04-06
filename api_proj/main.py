from fastapi import FastAPI, HTTPException
from . import models  # Import from models.py

app = FastAPI()
todos = []

@app.get("/Todo", response_model=list[models.Todo], tags=["Read"])
async def send_todos():
    return todos

@app.post("/Todo", response_model=models.Todo, tags=["Create"])
async def create(todo: models.Todo):
    if any(t.name == todo.name for t in todos):
        raise HTTPException(status_code=400, detail=f"Todo with name '{todo.name}' already exists")
    todos.append(todo)
    return todo

@app.put(
    "/Todo/{name}", 
    response_model=models.Todo, 
    tags=["Update"],
    summary="Update a Todo",
    description="Update the content of a todo by its name.",
    responses={
        200: {"description": "Todo updated successfully."},
        404: {"description": "Todo not found with the given name."}
    }
)
async def update_todo(name: str, updated_todo: models.Todo):
    for i, todo in enumerate(todos):
        if todo.name == name:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail=f"Todo with name '{name}' not found")

@app.delete(
    "/Todo/{name}", 
    tags=["Delete"],
    summary="Delete a Todo",
    description="Delete a todo by its name.",
    responses={
        200: {"description": "Todo deleted successfully."},
        404: {"description": "Todo not found with the given name."}
    }
)
async def delete_todo(name: str):
    for i, todo in enumerate(todos):
        if todo.name == name:
            deleted = todos.pop(i)
            return {
                "message": f"Todo '{name}' deleted successfully",
                "deleted": deleted
            }
    raise HTTPException(status_code=404, detail=f"Todo with name '{name}' not found")