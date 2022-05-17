from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '9aad4163fdb903e924e956c2152ef40a1d44'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import main






























# # import bcrypt
# from flask import Flask
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_bcrypt import Bcrypt
# # from flask_login import LoginManager
# # import os
# # from os import path
# app = Flask(__name__)

# # app.config['SECRET_KEY'] = '9aad4163fdb903e924e956c2152ef40a1d44'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['MAIL_SERVER']='smtp.gmail.com'
# # app.config['MAIL_PORT'] = 465
# # app.config['MAIL_USERNAME'] = 'abigail.nyawira22@gmail.com'
# # app.config['MAIL_PASSWORD'] = 'WaChIrA07!' 
# # app.config['MAIL_USE_TLS'] = False
# # app.config['MAIL_USE_SSL'] = True
# # db = SQLAlchemy(app)
# # bcrypt = Bcrypt(app)
# # login_manager = LoginManager(app)
# # login_manager.login_view = 'login'
# # login_manager.login_message_category = 'info'



# # def create_database(app):
# #     if not path.exists("app/" + "page.db"):
# #         db.create_all(app=app)
# #         print("Created database!")

# from app import main

