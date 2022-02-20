from fastapi import FastAPI
from sqlalchemy import false
from databases.schemas import TodoRequest
from databases.models import Todo
from databases.dababase import Base,engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

Base.metadata.create_all(engine)



app = FastAPI()


#for react 
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

#our urls 

@app.post('/api/todos/')
async def create_todo(todo : TodoRequest):

    session = Session(bind=engine,expire_on_commit=false)
    todo_post = Todo(title = todo.title,description = todo.description ,completed = todo.completed)
    session.add(todo_post)
    session.commit()
    return f"todo name : {todo.title}"

@app.get('/api/todos/')
async def get_todo():
    session = Session(bind=engine,expire_on_commit=false)
    todo = session.query(Todo).all()
    session.close()
    return todo

@app.put('/api/todos/{id}/')
async def update_todo(id:int,name:str,description:str,completed:bool):
    session = Session(bind=engine,expire_on_commit=false)
    todo = session.query(Todo).get(id)
    if todo : 
        todo.title = name
        todo.description = description
        todo.completed = completed
        session.commit()
        session.close
        return f"todo name : {todo.title}"
    else :
        return f"Error we did not find todo with id {id}"

@app.delete('/api/todos/{id}/')
async def delete_todo(id:int):
    session = Session(bind=engine,expire_on_commit=false)
    todo = session.query(Todo).get(id)
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
        return "todo was successfully deleted"
    else : 
        return f"Error we did not find todo with id {id}"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
