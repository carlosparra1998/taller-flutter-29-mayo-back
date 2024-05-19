from flask import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

def refresh_service():
    try:
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        refresh_token = create_refresh_token(identity=current_user)
        return {"msg": "OK", "data" : {"access_token" : access_token, "refresh_token" : refresh_token}}, 200
    except Exception:
        return {"msg": "Ha fallado el proceso"}, 400             