from flask import Flask
import sqlite3
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# Create a Flask Instance
app = Flask(__name__)
CORS(app)

# Setup homedir path
homedir = os.path.abspath(os.path.dirname(__file__))

# Database config and location
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(homedir, 'db.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Testing API'