from flask import jsonify, abort
from ..classes.task import Task
from flask_jwt_extended import get_jwt_identity
from ..init import Session

def update_task_service(request, uuidTask):
    try:
        session = Session()
        if not request.json:
            abort(400)
        session = Session()
        task = session.query(Task).filter_by(uuidtask=uuidTask).first()
        if task is None or task.username != get_jwt_identity():
            session.close()
            abort(404)
        task.title = request.json.get('title', task.title)
        task.description = request.json.get('description', task.description)
        task.color = request.json.get('color', task.color)
        task.active = request.json.get('active', task.active)
        task.preference = request.json.get('preference', task.preference)
        session.commit()
        return {"msg" : "OK", "data" : task.to_dict()}, 200
    except:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400     
    finally:
        session.close()        
