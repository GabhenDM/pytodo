from app import app,revoked_store
from functools import wraps
from flask import request, jsonify
import jwt
from werkzeug.security import check_password_hash
from .users import get_user_by_username
import datetime
import uuid

def check_if_token_is_revoked(encrypted_token):
    jti = jwt.get_unverified_header(encrypted_token)['jti']
    entry = revoked_store.get(jti)
    if entry is None:
        return True
    return entry == 'true'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.headers.get('Authorization') is None:
            return jsonify({'message':'Authorization is missing','data':{}}),401
        try:
            token = request.headers.get('Authorization').split(" ")[1]
            if check_if_token_is_revoked(token):
                return jsonify({'message':'Token Revoked','data':{}}),401
            data = jwt.decode(token,app.config['SECRET_KEY'])
            current_user = get_user_by_username(username=data['username'])
        except Exception as e:
            return jsonify({'message':'token is invalid or expired','data':{}}),401
        return f(current_user,*args,**kwargs)
    return decorated

def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message':'could not verify','WWW-Authenticate':'Basic auth="Login required"'}),401

    user = get_user_by_username(auth.username)
    if not user:
        return jsonify({'message':'Wrong username or password','data':{}}),401

    if user and check_password_hash(user.password,auth.password):
        jti = uuid.uuid4().hex
        token = jwt.encode({'id':user.id,'username':user.username,'exp':datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'],headers={'jti':jti})
        revoked_store.set(jti, 'false', app.config['ACCESS_EXPIRES'] * 1.2)
        return jsonify({'message':'Successfully authenticated','token':token.decode('UTF-8'),'exp':datetime.datetime.now() + datetime.timedelta(hours=12)}),200

    return jsonify({'message':'Authentication Failure','WWW-Authenticate':'Basic auth="Login Required'}),401

def logout():
    token = request.headers.get('Authorization').split(" ")[1]
    jti =  jwt.get_unverified_header(token)['jti']    
    revoked_store.set(jti, 'true', app.config['ACCESS_EXPIRES'] * 1.2)
    return jsonify({"msg": "Access token revoked"}), 200