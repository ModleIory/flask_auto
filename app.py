import flask
# here  importing modules blueprint variable
from controllers.app_one import app_one
from controllers.app_two import app_two

app = flask.Flask(__name__)
# here register the blue map , can scan by user
app.register_blueprint(app_two) 
app.register_blueprint(app_one)

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")	 