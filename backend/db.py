from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import * 
from flask_login import LoginManager
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = AZURE_POSTGRESQL_CONNECTIONSTRING
db = SQLAlchemy()
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
