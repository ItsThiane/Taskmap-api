Taskmap - Application de Gestion de Tâches




Taskmap est une API Flask qui permet de gérer des utilisateurs et leurs tâches. L'application utilise MySQL comme base de données relationnelle et est entièrement containerisée avec Docker et Docker Compose.



  Fonctionnalités principales

-  Ajouter des utilisateurs à la base de données.
-  Créer, mettre à jour, supprimer et récupérer des tâches associées à un utilisateur.



## Prérequis
-  Minikube 
-  Kubectl 



Instructions pour déployer l'application



# Kubernetes 


## Étapes
1. Démarrer Minikube avec 3 nœuds :
   ```bash
   minikube start --nodes 3 --driver=docker

2. Appliquer les manifestes
```bash
kubectl apply -f k8s/

3. Verifier les pods:
Kubectl get pods

4. Acceder au service backend
minicube service backend 


