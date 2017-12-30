import flask

# this is flask frame output app , entry file import this
app_two = flask.Blueprint('app_two',
							__name__,
							static_folder='statics',
							template_folder='tpls',
							url_prefix='/app_two'
						)

@app_two.route("/")
def index():
	return "app_two blueprint"

@app_two.route("/one")
def one():
	return flask.render_template("index.html",data={"title":"app_two:one"})

@app_two.route("/two")
def two():
	return flask.render_template("index.html",data={"title":"app_two:two"})