from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import  LoginManager
# from flask_login import LoginManager
# login_manager = LoginManager()

db = SQLAlchemy(app)
encode = Bcrypt(app)
loginm = LoginManager(app)
loginm.login_view = 'login'
loginm.login_message_category = 'info'

def create_app():
	app = Flask(__name__)
	#Protect Against Cookie Modification
	app.config['SECRET_KEY'] = 'f9a2fd8f07fae783cf24ae35997a2a7c'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///slisff.db'
	#from the app package/folder, importing the routes.py
	from app import routes

	return app