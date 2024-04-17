# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /appDe

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers de l'application dans le conteneur
COPY api.py .

# Exposer le port 8080 pour l'application Flask
EXPOSE 8080

# Commande pour exécuter l'application Flask
CMD ["python", "api.py"]
