from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# SQLALCHEMY_DATABASE_URI = 'postgresql:///Pet_Adoption_db'

default_img_url = 'https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554__340.jpg'

# Step 1
class Pet(db.Model):
    """ model class for Pet adoption """
    __tablename__ = "pets"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text)
    photo_url = db.Column(db.Text, default = default_img_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)

def connect_db(app):
    db.app = app
    db.init_app(app) 

"""

# Step 3: Create Add Pet Form
Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

Pet name
Species
Photo URL
Age
Notes
This should be at the URL path /add. Add a link to this from the homepage.


# Step 1: Create Database & Model

Create a Flask and Flask-SQLAlchemy project, “adopt”.

Create a single model, Pet. This models a pet potentially available for adoption:

id: auto-incrementing integer
name: text, required
species: text, required
photo_url: text, optional
age: integer, optional
notes: text, optional
available: true/false, required, should default to available
While setting up the project, add the Debug Toolbar.

"""