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




@app.route("/health/ready")
async def readiness():
    return jsonify({"status": "ready"}), 200

@app.route("/health/live")
async def liveness():
    return jsonify({"status": "alive"}), 200





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

