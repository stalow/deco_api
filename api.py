import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Route pour obtenir les valeurs des tâches
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)
        return jsonify(tasks_data)
    except FileNotFoundError:
        return jsonify({})

# Définition de la route
@app.route('/hello', methods=['GET'])
def hello():
    return 'hello'


# Route pour recevoir les données via POST
@app.route('/tasks', methods=['POST'])
def receive_tasks():
    try:
        tasks_data = request.json
        with open("tasks.json", "w") as file:
            json.dump(tasks_data, file)
        return jsonify({"message": "Data received and stored successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=8000)
