from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

#flask app init
app = Flask(__name__)


# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)