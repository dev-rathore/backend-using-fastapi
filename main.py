from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import Todo

app = FastAPI()

origins = [
  "http://localhost:3000",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

todos = []

@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/api/todos")
async def get_todos():
  return todos

@app.get("/api/todos/{todo_id}")
async def get_todo(todo_id: int):
  try:
    for todo in todos:
      if todo.id == todo_id:
        return todo
  except IndexError:
    raise HTTPException(status_code=404, message="Todo not found")

@app.post("/api/todos")
async def create_todo(todo: Todo):
  todos.append(todo)
  return todos

@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int):
  try:
    for todo in todos:
      if todo.id == todo_id:
        todos.remove(todo)
        return todos
  except IndexError:
    raise HTTPException(status_code=404, message="Todo not found")

@app.put("/api/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
  try:
    for t in todos:
      if t.id == todo_id:
        t.item = todo.item
        return todos
  except IndexError:
    raise HTTPException(status_code=404, message="Todo not found")
