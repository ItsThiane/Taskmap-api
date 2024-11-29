import mysql.connector
from database import get_db_connection
from models import TaskCreate, TaskUpdate, UserCreate

# Services pour les tâches
def add_task(task: TaskCreate):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO tasks (title, description, user_id) VALUES (%s, %s, %s)",
            (task.title, task.description, task.user_id)
        )
        db.commit()
        return {"id": cursor.lastrowid, "title": task.title, "description": task.description, "user_id": task.user_id, "status": "TO DO"}
    except mysql.connector.Error as err:
        raise Exception(f"Error: {str(err)}")
    finally:
        cursor.close()

def update_task(task_id: int, task: TaskUpdate):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("UPDATE tasks SET status = %s WHERE id = %s", (task.status, task_id))
        db.commit()
        return {"id": task_id, "status": task.status}
    except mysql.connector.Error as err:
        raise Exception(f"Error: {str(err)}")
    finally:
        cursor.close()

def delete_task(task_id: int):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        db.commit()
        return {"message": "Task deleted successfully"}
    except mysql.connector.Error as err:
        raise Exception(f"Error: {str(err)}")
    finally:
        cursor.close()

# Services pour les utilisateurs
def create_user(user: UserCreate):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (user.username, user.email, user.password))
        db.commit()
        return {"id": cursor.lastrowid, "username": user.username, "email": user.email}
    except mysql.connector.Error as err:
        raise Exception(f"Error: {str(err)}")
    finally:
        cursor.close()
