import flask

# this is flask frame output app , entry file import this
 '''
	@ blueprint_name : self define 
	@ module name : always be __name__
	@ define which document in the application(app_one) is the static folder :/app_one/statics
	@ define which document in the application(app_one) is the template folder :/app_one/tpls
	@ define the url user interview like here : /app_one/one
 '''
#app_one would export to the entry file
app_one = flask.Blueprint('app_one',
							__name__,
							static_folder='statics',
							template_folder='tpls',
							url_prefix='/app_one'
						)

@app_one.route("/")
def index():
	return "app_one blueprint"

@app_one.route("/one")
def one():
	# here data could be replaced by other variable , It is not changeless
	return flask.render_template("index.html",data={"title":"app_one:one"})

@app_one.route("/two")
def two():
	return flask.render_template("index.html",data={"title":"app_one:two"})