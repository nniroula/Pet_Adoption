from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

# class AddNames(FlaskForm):
#     first_name = StringField("First Name")
#     last_name = StringField("Last Name")

class AddPetForm(FlaskForm):
    pet_name = StringField("Pet Name")
    pet_species = StringField("Species type")
    pet_photo_url = StringField("Image URL")
    pet_age = IntegerField("Age")
    pet_notes = StringField("Notes")


"""
# Step 3: Create Add Pet Form
Create a form for adding pets. This should use Flask-WTF, and should have the following fields:

Pet name
Species
Photo URL
Age
Notes
This should be at the URL path /add. Add a link to this from the homepage.

"""