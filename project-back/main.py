from flask import request
from flask_jwt_extended import jwt_required
from core.services.register_service import register_service
from core.services.login_service import login_service
from core.services.refresh_service import refresh_service
from core.services.get_tasks_service import get_tasks_service
from core.services.create_task_service import create_task_service
from core.services.update_task_service import update_task_service
from core.services.delete_task_service import delete_task_service
import json
from flask import Flask
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

app = Flask(__name__)
config_path = os.path.abspath('config.json')
config = open(config_path)
config = json.load(config)
app.config['JWT_SECRET_KEY'] = config["jwt"]
jwt = JWTManager(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/api/v1/register', methods=['POST'])
def register(): 
    return register_service(request)

@app.route('/api/v1/login', methods=['POST'])
def login(): 
    return login_service(request)

@app.route('/api/v1/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh(): 
    return refresh_service()

@app.route('/api/v1/tasks', methods=['GET'])
@jwt_required()
def get_tasks(): 
    return get_tasks_service()

@app.route('/api/v1/tasks', methods=['POST'])
@jwt_required()
def create_task(): 
    return create_task_service(request)

@app.route('/api/v1/tasks/<uuid:uuidTask>', methods=['PUT'])
@jwt_required()
def update_task(uuidTask): 
    return update_task_service(request, uuidTask)

@app.route('/api/v1/tasks/<uuid:uuidTask>', methods=['DELETE'])
@jwt_required()
def delete_task(uuidTask): 
    return delete_task_service(uuidTask)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)