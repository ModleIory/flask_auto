#! -*- coding:utf-8 -*-
import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
'''
# must install pymysql[mysql-python is not available] or show error:ImportError: No module named MySQLdb 
# and change "mysql://root:root@localhost:3306/sqlalchemy" to "mysql+pymysql://root:root@localhost:3306/sqlalchemy"
'''
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/sqlalchemy"

db=SQLAlchemy(app)

'''
#here,increate automantic
'''
class User(db.Model):

	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True)
	password=db.Column(db.String(20),unique=True)
	email = db.Column(db.String(120), unique=True)
	gender = db.Column(db.Integer)
	saying = db.Column(db.String(200))
	#when init must give value , not null
	def __init__(self, username=None, email=None):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username






