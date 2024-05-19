from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity
from ..classes.task import Task
from ..init import Session

def create_task_service(request):
    try:
        current_user = get_jwt_identity()
        session = Session()
        if not request.json or not 'title' in request.json:
            abort(400)

        new_task = Task(
            username=current_user,
            title=request.json['title'],
            description=request.json.get('description', ""),
            color=request.json.get('color', "#FFFFFF"),
            active=True,
            preference=request.json.get('preference', 1),
        )
        session.add(new_task)
        session.commit()
        return {"msg" : "OK", "data" : new_task.to_dict()}, 200
    except Exception:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400   
    finally:
        session.close()          