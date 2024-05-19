from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from ..classes.task import Task
from ..init import Session

def get_tasks_service():
    try:
        session = Session()
        current_user = get_jwt_identity()
        user_tasks = [task.to_dict() for task in session.query(Task).filter_by(username=current_user)]
        return {"msg" : "OK", "data" : user_tasks}, 200
    except:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400 
    finally:
        session.close()