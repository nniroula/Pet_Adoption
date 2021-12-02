from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from forms import AddNames

app = Flask(__name__)

app.config['SECRET_KEY'] = "ohnoboy"
debug = DebugToolbarExtension(app)

db = SQLAlchemy()
db.app = app
db.init_app(app) 


@app.route('/wtforms')
def check_flask_setup():
    return render_template('home.html')

# chekc the wtforms is working properly
@app.route('/names')
def add_names():
    form = AddNames()  # this a form object
    return render_template("home.html", form = form)
