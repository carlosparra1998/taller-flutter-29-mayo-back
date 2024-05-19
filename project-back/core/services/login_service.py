from flask import jsonify, abort
from ..classes.user import User
from flask_jwt_extended import create_access_token, create_refresh_token
from ..init import Session

def login_service(request):
    try:
        session = Session()
        if not request.json or not 'userName' in request.json or not 'password' in request.json:
            abort(400)
        userName = request.json['userName']
        password = request.json['password']
        user = session.query(User).filter_by(username=userName).first()
        if not user or user.password != password:
            return {"msg": "Credenciales incorrectas"}, 401
        access_token = create_access_token(identity=userName)
        refresh_token = create_refresh_token(identity=userName)
        return {"msg": "OK", "data" : {"access_token" : access_token, "refresh_token" : refresh_token}}, 200
    except Exception:
        session.rollback()
        return {"msg": "Ha fallado el proceso"}, 400   
    finally:
        session.close()          
