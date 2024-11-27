from pydantic import BaseModel
from typing import List




# Modèles Pydantic pour valider les données d'entrée

class TaskCreate(BaseModel):
    description: str
    user_id: int

class TaskUpdate(BaseModel):
    status: str

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

class TaskResponse(BaseModel):
    id: int
    description: str
    user_id: int
    status: str
