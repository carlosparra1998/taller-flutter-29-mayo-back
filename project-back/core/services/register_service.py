from flask import jsonify, abort
from ..classes.user import User
from sqlalchemy.exc import IntegrityError
from ..init import Session

def register_service(request):
    try:
        session = Session()
        if not request.json or not 'userName' in request.json or not 'password' in request.json:
            abort(400)
        userName = request.json['userName']
        password = request.json['password']
        user = User(username=userName, password=password)
        session.add(user)
        session.commit()
        return {"msg": "OK", "data" : {}}, 200
    except IntegrityError:
        session.rollback()
        return {"msg": "El usuario ya existe"}, 400
    except Exception:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400             
    finally:
        session.close()
