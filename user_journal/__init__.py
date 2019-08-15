from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'da714fd358e8f3d77b28b041614f4e6c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'

login_manager = LoginManager(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from user_journal.routes import *
