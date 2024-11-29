from fastapi import APIRouter, HTTPException
from typing import List
from models import UserCreate, UserResponse
from services import create_user
from database import get_db_connection

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def add_user(user: UserCreate):
    try:
        return create_user(user)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.get("/users", response_model=List[UserResponse])
async def get_users():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users
