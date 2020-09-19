from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema
import sys


def get_users():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        for user in result:
            print(user)
        return jsonify({'message':'Successfully fetched users','data':result}),200

def get_user(id):
    user = Users.query.get(id)
    if not user:
        result = user_schema.dump(user)
        return jsonify({'message':'Successfully fetched user','data':result}),200
    else:
        return jsonify({'message': 'No such user','data':{}}),404


def get_user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except Exception as e:
        print(e)
        return None


def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'No such user','data':{}}),404
    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message':'Successfully deleted user','data':result}),200     
    except Exception as e:
        message = list(e.orig.args)[1]
        db.session.rollback()
        return jsonify({'message':'Error deleting user','desc':message}), 500
    
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

def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(id)
    if not user:
        return jsonify({'message':"User doesn't exist",'data':{}}),404
    
    pass_hash = generate_password_hash(password)
    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        result = user_schema.dump(user)
        result.pop("password",None)
        return jsonify({'message':'User updated succesfully','data':result}),201
    except Exception as e:
        message = list(e.orig.args)[1]
        db.session.rollback()
        return jsonify({'message':'Error updating user','desc':message}), 500