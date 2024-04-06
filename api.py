import os
from dotenv import load_dotenv
from flask import Flask, jsonify
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configuration du client MQTT
mqtt_broker = os.getenv("MQTT_BROKER")
mqtt_port = int(os.getenv("MQTT_PORT"))
mqtt_username = os.getenv("MQTT_USERNAME")
mqtt_password = os.getenv("MQTT_PASSWORD")
mqtt_client = mqtt.Client()

# Fonction pour stocker les valeurs de tâche dans un fichier
def store_tasks(tasks_data):
    with open("tasks.json", "w") as file:
        json.dump(tasks_data, file)

# Callback pour la réception des messages MQTT
def on_message(client, userdata, message):
    # Convertir le message reçu en dictionnaire Python
    task_data = json.loads(message.payload)
    # Stocker les valeurs de tâche dans un fichier
    store_tasks(task_data)

# Configurer le client MQTT pour se connecter et s'abonner aux topics des tâches
def setup_mqtt():
    mqtt_client.connect(mqtt_broker, mqtt_port)
    mqtt_client.subscribe("task1")
    mqtt_client.subscribe("task2")
    mqtt_client.subscribe("task3")
    mqtt_client.subscribe("task4")
    mqtt_client.subscribe("task5")
    mqtt_client.on_message = on_message
    mqtt_client.loop_start()

# Route pour obtenir les valeurs des tâches
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)
        return jsonify(tasks_data)
    except FileNotFoundError:
        return jsonify({})

if __name__ == '__main__':
    setup_mqtt()
    app.run(debug=True)