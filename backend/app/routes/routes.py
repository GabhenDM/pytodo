from app import app
from flask import jsonify
from ..views import users, auth


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hello World"})


@app.route("/users",methods=['GET'])
def get_users():
    return users.get_users()

@app.route("/users/<id>",methods=['GET'])
def get_user(id):
    return users.get_user(id)

@app.route("/users",methods=['POST'])
def create_user():
    return users.create_user()

@app.route("/users/<id>",methods=['PUT'])
def update_user(id):
    return users.update_user(id)

@app.route("/users/<id>",methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)

@app.route('/auth',methods=['POST'])
def authenticate():
    return auth.auth()