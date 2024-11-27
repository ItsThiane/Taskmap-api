from fastapi import APIRouter, HTTPException
from typing import List
from models import TaskCreate, TaskUpdate, TaskResponse
from services import add_task, update_task, delete_task

router = APIRouter()

@router.post("/tasks", response_model=TaskResponse)
async def add_new_task(task: TaskCreate):
    try:
        return await add_task(task)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.get("/users/{user_id}/tasks", response_model=List[TaskResponse])
async def get_user_tasks(user_id: int):
    try:
        return await get_user_tasks(user_id)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task_status(task_id: int, task: TaskUpdate):
    try:
        return await update_task(task_id, task)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.delete("/tasks/{task_id}")
async def delete_task_by_id(task_id: int):
    try:
        return await delete_task(task_id)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))
