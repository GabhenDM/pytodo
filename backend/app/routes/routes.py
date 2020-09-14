from app import app
from flask import jsonify
from ..views import users


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hello World"})


@app.route("/users",methods=['POST'])
def create_user():
    return users.create_user()
