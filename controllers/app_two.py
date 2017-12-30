import flask

# this is flask frame output app , entry file import this
app_two = flask.Blueprint('app_two',__name__,url_prefix='/app_two')

@app_two.route("/")
def index():
	return "app_two blueprint"

@app_two.route("/one")
def two_one():
	print 'this is app_two /one'
	return flask.render_template("app_two/index.html",data={"title":"app_two:one"})

@app_two.route("/two")
def two_two():
	print 'this is app_two /two'
	return flask.render_template("app_two/index.html",data={"title":"app_two:two"})