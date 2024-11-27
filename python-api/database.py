import mysql.connector
from mysql.connector import Error



def get_db_connection():
    """
    Crée une connexion à la base de données et la retourne.
    """
    try:
        connection = mysql.connector.connect(
            host="database",  
            user="root",      
            password="TDroot@5",  
            database="taskmap_db"  
        )
        if connection.is_connected():
            print("Connexion réussie à la base de données MySQL !")
        return connection
    except Error as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None
