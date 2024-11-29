from fastapi import FastAPI
import uvicorn
from routers import users, tasks





app = FastAPI()



app.include_router(users.router)
app.include_router(tasks.router)


# Route de base
@app.get("/")
async def hello_world():
    return {"message": "Bienvenue sur l'API de gestion des tâches Taskmap!"}








if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

