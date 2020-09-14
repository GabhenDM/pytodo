from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
import sys

def create_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    pass_hash = generate_password_hash(password)
    user = Users(username,pass_hash,name,email)
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        result.pop("password",None)
        return jsonify({'message':'User registered succesfully','data':result}),201
    except Exception as e:
        message = list(e.orig.args)[1]
        db.session.rollback()
        return jsonify({'message':'Error creating user','desc':message}), 500