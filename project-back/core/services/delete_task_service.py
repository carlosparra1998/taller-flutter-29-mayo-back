from flask import jsonify, abort
from flask_jwt_extended import get_jwt_identity
from ..classes.task import Task
from ..init import Session

def delete_task_service(uuidTask):
    try:
        session = Session()
        task = session.query(Task).filter_by(uuidtask=uuidTask).first()
        if task is None or task.username != get_jwt_identity():
            session.close()
            abort(404)
        session.delete(task)
        session.commit()
        return {"msg" : "OK", "data" : {}}, 200
    except:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400 
    finally:
        session.close()