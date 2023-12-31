from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import * 
from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = AZURE_POSTGRESQL_CONNECTIONSTRING
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
