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
class Book(db.Model):

	id=db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer)
	begin_time = db.Column(db.Date)
	end_time = db.Column(db.Date)
	name = db.Column(db.String(20))
	description = db.Column(db.String(50),default="No more description")
	#when init must give value , not null
	def __init__(self):
		pass

	def __repr__(self):
		return '<Book %r>' % self.name






