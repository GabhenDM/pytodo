from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Setup our redis connection for storing the blacklisted tokens
revoked_store = redis.StrictRedis(host='redis', port=6379, db=0,decode_responses=True,password=app.config['REDIS_PASS'])

from .models import users
from .routes import routes

if __name__ == "__main__":
    app.run()