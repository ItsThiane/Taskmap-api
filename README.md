Taskmap - Application de Gestion de Tâches




Taskmap est une API Flask qui permet de gérer des utilisateurs et leurs tâches. L'application utilise MySQL comme base de données relationnelle et est entièrement containerisée avec Docker et Docker Compose.



Fonctionnalités principales
Ajouter des utilisateurs à la base de données.
Créer, mettre à jour, supprimer et récupérer des tâches associées à un utilisateur.
Les tâches sont stockées dans une table distincte liée à celle des utilisateurs via une relation.
Connexion à la base de données via MySQL Connector.


Prérequis
-Docker
-Docker Compose


Structure du projet
DockerLab/
├── python-api/                 # Contient l'API Flask
│   ├── app.py                  # Point d'entrée principal
│   ├── database.py             # Connexion à la base de données MySQL
│   ├── task_manager.py         # Gestion des tâches (endpoints API)
│   ├── user_manager.py         # Gestion des utilisateurs (endpoints API)
│   ├── requirements.txt        # Dépendances Python
│   └── Dockerfile              # Dockerfile pour l'API
├── docker-compose.yml          # Configuration Docker Compose
└── README.md                   # Documentation du projet


Instructions pour déployer l'application
1. Préparer la base de données
Assurez-vous que la base de données MySQL sera correctement initialisée. Voici les étapes à suivre :

Les identifiants de connexion et le nom de la base de données utilisés par l'API sont définis dans le fichier docker-compose.yml.
Une fois les conteneurs démarrés, vous devez créer manuellement les tables nécessaires.

Pour creer et démarrer les conteneurs

```bash
docker-compose up 

API Flask : accessible sur http://localhost:5000
MySQL : accessible sur le port 3306.