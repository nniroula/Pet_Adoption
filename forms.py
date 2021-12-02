from flask_wtf import FlaskForm
from wtforms import StringField

class AddNames(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    