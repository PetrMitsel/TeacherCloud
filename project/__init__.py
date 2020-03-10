from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.sqlite3"
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "postgresql://postgres:Sertdert123!@localhost/TeacherCloud"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = os.environ.get('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

from project import routes
