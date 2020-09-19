from dotenv import load_dotenv
load_dotenv()
import os
import random
import string
from datetime import timedelta

basedir = os.path.dirname(os.path.realpath(__file__))

# Configurações iniciais
user = os.getenv("MYSQL_USER")
passwd = os.getenv("MYSQL_PASS")
database = os.getenv("MYSQL_DB")
host = os.getenv("MYSQL_HOST")
port = int(os.getenv("MYSQL_PORT"))
gen = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(gen) for i in range(12))
REDIS_PASS = os.getenv("REDIS_PASS")
# Definições do banco de dados e app
# Gera uma chave aleatória para aplicação a cada execução do servidor

SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{passwd}@{host}:{port}/{database}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
DEBUG = True

# Definições Redis
ACCESS_EXPIRES = timedelta(hours=12)
