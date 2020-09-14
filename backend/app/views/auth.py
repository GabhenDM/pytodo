from app import app
from functools import wraps
from flask import request, jsonify
import jwt
from werkzeug.security import check_password_hash
from .users import get_user_by_username
import datetime


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message':'could not verify','WWW-Authenticate':'Basic auth="Login required"'}),401

    user = get_user_by_username(auth.username)
    if not user:
        return jsonify({'message':'Wrong username or password','data':{}}),401

    if user and check_password_hash(user.password,auth.password):
        token = jwt.encode({'id':user.id,'username':user.username,'exp':datetime.datetime.now() + datetime.timedelta(hours=12)}, app.config['SECRET_KEY'])
        return jsonify({'message':'Successfully authenticated','token':token.decode('UTF-8'),'exp':datetime.datetime.now() + datetime.timedelta(hours=12)}),200

    return jsonify({'message':'Authentication Failure','WWW-Authenticate':'Basic auth="Login Required'}),401

