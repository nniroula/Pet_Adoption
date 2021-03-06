from flask import Flask, render_template, redirect, url_for, flash
from flask.scaffold import F
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

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

@app.route("/")
def show_all_pets():
    pets = Pet.query.all()
    # pets = db.session.query.all()
    return render_template('home.html', pets = pets)

@app.route('/add', methods=["GET", "POST"])  # database does not render table, fix that and this works
def handle_add_pet_form():
    form = AddPetForm()
    if form.validate_on_submit():
        # get data from wtf. They are attributes in forms.py
        nam = form.pet_name   
        specy = form.pet_species  # now pet species has choices as a validator, use it here to work properly
        url = form.pet_photo_url
        ag = form.pet_age 
        noot = form.pet_notes
        # now pass these data to database, which is model class here
        pet_obj = Pet(name = nam, species = specy,  photo_url = url, age = ag, notes = noot)
        db.session.add(pet_obj)
        db.session.commit()
        # return redirect('/')
        return redirect(url_for('show_all_pets')) # url_for takes method name as argument 
    else:
        return render_template("add_pet.html", form = form)

@app.route('/<pet_id_number>')
def details_about_a_pet(pet_id_number):
    
    pet = Pet.query.get_or_404(pet_id_number)
    form  = EditPetForm(obj = pet)

    if form.validate_on_submit():
        # pet.name = form.name.data 
        # pet.species = 
        pet.photo_url = form.photo_edit.data  # comes form edit form class
        pet.notes = form.notes_for_edit.data
        pet.available = form.availability_edit.data
        db.session.commit()
        # flash('update successful')
        return redirect(url_for('show_all_pets'))

    else:
        # if it fails; re-render the edit form
        return render_template("pet_edit_form.html", form=form, pet=pet)


"""


Step 6: Add Display/Edit Form
Make a page that shows some information about the pet:

Name
Species
Photo, if present
Age, if present
It should also show a form that allows us to edit this pet:

Photo URL
Notes
Available
This should be at the URL /[pet-id-number]. Make the homepage link to this.


Step 5: Add Validation
WTForms gives us lots of useful validators; we want to use these for validating our fields more carefully:

the species should be either ???cat???, ???dog???, or ???porcupine???
the photo URL must be a URL (but it should still be able to be optional!)
the age should be between 0 and 30, if provided

Step 4: Create Handler for Add Pet Form
This should validate the form:

if it doesn???t validate, it should re-render the form
if it does validate, it should create the new pet, and redirect to the homepage
This should be a POST request to the URL path /add.

Step 2: Make Homepage Listing Pets
The homepage (at route /) should list the pets:

name
show photo, if present
display ???Available??? in bold if the pet is available for adoption
"""






