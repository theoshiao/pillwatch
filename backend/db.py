from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import * 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://amyxjhuang:{POSTGRESQL_PASSWORD}@localhost/pillwatch'
db = SQLAlchemy(app)
# db.init_app(app)