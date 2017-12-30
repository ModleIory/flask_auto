import flask
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
# must install pymysql[mysql-python is not available] or show error:ImportError: No module named MySQLdb 
# and change "mysql://root:root@localhost:3306/sqlalchemy" to "mysql+pymysql://root:root@localhost:3306/sqlalchemy"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/sqlalchemy"

db=SQLAlchemy(app)

class User(db.Model):
	#here ， increate automantic
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(20),unique=True)
	passwork=db.Column(db.String(20),unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username
		return '<User %r>' % self.username






