from flask import Flask, render_template
from models import db
from forms import SignupForm
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mam:27Cucumbers@localhost/lovers"
db.init_app(app)

app.secret_key = "development-key"

# class User(db.Model):
# 	id = db.Column(db.Integer, primary_key = True)
# 	username = db.Column(db.String(80), unique=True)
# 	email = db.Column(db.string(120), unique=True)
	
# 	def __init__(self, username, email):
# 		self.username = username
# 		self.email = email
		
# 	def __repr__(self):
# 		return '<User %r>' % self.username

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/signup")
def signup():
	form = SignupForm()
	return render_template("signup.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)