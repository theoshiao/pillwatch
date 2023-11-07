from db import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from bcrypt import checkpw, gensalt, hashpw
from config import *

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        # Hash the password and store it in the user object
        self.password = hashpw(password.encode('utf-8'), gensalt())

    def check_password(self, password):
        # Compare the provided password with the stored hashed password
        return checkpw(password.encode('utf-8'), self.password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pill(db.Model): 
    __tablename__ = 'pills'
    pill_id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=False) 
    generic_name = db.Column(db.String(100), nullable=False) 
    description = db.Column(db.Text)
