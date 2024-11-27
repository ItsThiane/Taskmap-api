import mysql.connector
from database import get_db_connection
from models import TaskCreate, TaskUpdate, UserCreate

# Services pour les tâches
def add_task(task: TaskCreate):
    db = get_db_connection()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO tasks (description, user_id) VALUES (%s, %s)",
            (task.description, task.user_id)
        )
        db.commit()
        return {"id": cursor.lastrowid, "description": task.description, "user_id": task.user_id, "status": "pending"}
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
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
        db.commit()
        return {"id": cursor.lastrowid, "name": user.name, "email": user.email}
    except mysql.connector.Error as err:
        raise Exception(f"Error: {str(err)}")
    finally:
        cursor.close()
