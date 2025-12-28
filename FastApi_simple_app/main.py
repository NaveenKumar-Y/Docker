from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import os

app = FastAPI()

version = os.environ.get("APP_VERSION", "v1.0.0")

@app.get("/")
def read_root():
    return {"message": "hello from fastapi", "version": version}


@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/readyz")
def readiness_check():
    return {"status": "ready"}

@app.get("/tasks")
def list_tasks():
    items = ["cheese", "pepper", "bread"]
    return {"items": items}

class Task(BaseModel):
    name: str
    price: float

@app.post("/tasks")
def create_task(task: Task):
    # FastAPI handles validation automatically before this line is reached
    # try:
    #     Task(**task)
    # except ValidationError as e:
    #     raise HTTPException(status_code=400, detail=str(e))
    
    if not task:
        raise HTTPException(status_code=404, detail="Task is missing")
    return {"task_created": task}
