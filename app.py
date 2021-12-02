from flask import Flask, render_template
from flask.scaffold import F
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

# from forms import AddNames

app = Flask(__name__)

app.config['SECRET_KEY'] = "ohnoboy"
debug = DebugToolbarExtension(app)

SQLALCHEMY_DATABASE_URI = "postgresql:///Pet_Adoption_db"  # your database name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # set to False and sqlalchemy won't yell at you
app.config['SQLALCHEMY_ECHO'] = True # this shows sql statements in terminal

connect_db(app)
# db.drop_all()  # at first all existing tables if there is any and then create one
db.create_all()

# @app.route('/wtforms')
# def check_flask_setup():
#     return render_template('home.html')

# chekc the wtforms is working properly
# @app.route('/names')
# def add_names():
#     form = AddNames()  # this a form object
#     return render_template("home.html", form = form)

# check that models.py works fine
# @app.route('/modlecheck')
# def check_modleclass():
#     first_pet = Pet.query.all()
#     return render_template("home.html", first_pet = first_pet)

@app.route("/")
def show_all_pets():
    pets = Pet.query.all()
    # pets = db.session.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add')
def add_pet():
    # Create a form for adding pets. This should use Flask-WTF, and should have the following fields:
    # This should be at the URL path /add. Add a link to this from the homepage.
    form = AddPetForm()
    return render_template("add_pet.html", form = form)


"""
Step 2: Make Homepage Listing Pets
The homepage (at route /) should list the pets:

name
show photo, if present
display “Available” in bold if the pet is available for adoption
"""






