import flask
from models.User import db,User
# this is flask frame output app , entry file import this
'''
	@ blueprint_name : self define 
	@ module name : always be __name__
	@ define which document in the application(app_one) is the static folder :/app_one/statics
	@ define which document in the application(app_one) is the template folder :/app_one/tpls
	@ define the url user interview like here : /app_one/one
'''
#app_one would export to the entry file
app_one = flask.Blueprint('app_one',__name__,url_prefix='/app_one')
req = flask.request

@app_one.route("/")
def index():
	return "app_one blueprint"

@app_one.route("/one")
def one_one():
	print "this is app_one /one"
	# here data could be replaced by other variable , It is not changeless
	return flask.render_template("app_one/index.html",data={"title":"app_one:one"})

@app_one.route("/two")
def one_two():
	print "this is app_one /two"
	return flask.render_template("app_one/index.html",data={"title":"app_one:two"})

@app_one.route("/useradd",methods=['GET'])
def useradd():
	user = req.args.get('user')
	pswd = req.args.get('pswd')
	email = req.args.get('email')
	client = User()
	# print client
	try:
		client.username=user 
		client.password=pswd
		client.gender=0
		client.email=email
		client.saying="Be better !"
		client.nickname="modle jaxure"
		client.other = "I am other"
		db.session.add(client)
		db.session.commit()
	except Exception as e:
		print 'Error below is :'
		print (e)
		return "save Date error!"
	return 'Save Data Ok'

@app_one.route("/usershow",methods=['GET'])
def usershow():
	id=req.args.get('id')
	user = None
	if id:
		user = User.query.filter_by(id=id).all()
	else:
		user = User.query.all()
	print user
	return flask.render_template("app_one/user.html",user=user)

