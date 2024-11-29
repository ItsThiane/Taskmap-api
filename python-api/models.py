from pydantic import BaseModel
from typing import List




# Modèles Pydantic pour valider les données d'entrée

class TaskCreate(BaseModel):
    title: str
    description: str
    user_id: int

class TaskUpdate(BaseModel):
    status: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    user_id: int
    status: str
