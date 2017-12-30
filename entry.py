import flask
# here  importing modules blueprint variable
from app_one.views import app_one
from app_two.views import app_two

app = flask.Flask(__name__)
# here register the blue map , can scan by user
app.register_blueprint(app_one)
app.register_blueprint(app_two) 

if __name__ == "__main__":
	app.run(debug=True,host="0.0.0.0")	