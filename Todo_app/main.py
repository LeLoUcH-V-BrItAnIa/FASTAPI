from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool
# CREATE DATAS 
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "Message":"Tast Added !",
        "Data":todo
    }
# GET DATAS 
@app.get("/todos")
def get_todo():
    return todos

# GET SPECIFIC DATA 
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error":"Todo Not Found !"}
# UPDATE 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,Updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = Updated_todo
        return{"Message":"Data updated!",
               "Data":Updated_todo}
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index,todo in enumerate(todos):
            if todo.id == todo_id:
                todos.pop(index)
                return {"Message":"Data Deleted !"}
            