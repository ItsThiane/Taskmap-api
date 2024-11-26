--Creation de la base de donnees
CREATE DATABASE IF NOT EXISTS taskmap_db;

--Utiliser la base de donnees
USE taskmap_db;

--Creer la table des utilisateurs
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Creer la table des taches
Create TABLE IF NOT EXISTS tasks (
     id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status ENUM('TO DO', 'DOING', 'DONE') DEFAULT 'TO DO',
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE 
);


