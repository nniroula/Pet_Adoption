from os import name, supports_effective_ids
from typing import AsyncGenerator
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.fields.simple import BooleanField
from wtforms.validators import  InputRequired, Optional, URL, NumberRange

# class AddNames(FlaskForm):
#     first_name = StringField("First Name")
#     last_name = StringField("Last Name")

class AddPetForm(FlaskForm):
    pet_name = StringField("Pet Name")
    # pet_species = StringField("Species type", validators = [InputRequired(message = "cat, or dog, or porcupine")])
    pet_species = StringField("Species type", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    # cat is actual value, Cat is what a user sees(user interface)
    
    pet_photo_url = StringField("Image URL", validators = [Optional(), URL()])
    pet_age = IntegerField("Age", validators = [Optional(), NumberRange(min=0, max=30)])
    pet_notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """ To edit and existing pet in the database """
    # name = StringField("Edit Name")
    # species = StringField("Edit Species")
    photo_edit = StringField("Edit URL")
    # age  = IntegerField("Edit Age")
    notes_for_edit = TextAreaField("Notes")
    availability_edit = BooleanField("Availability")


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

the species should be either “cat”, “dog”, or “porcupine”
the photo URL must be a URL (but it should still be able to be optional!)
the age should be between 0 and 30, if provided

# Step 3: Create Add Pet Form
Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

Pet name
Species
Photo URL
Age
Notes
This should be at the URL path /add. Add a link to this from the homepage.

"""