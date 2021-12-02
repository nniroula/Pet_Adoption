""" This is a seed file to populate database tables as starter data """
from app import app
from models import Pet, db 

# delete all pre-existing tables
db.drop_all()
# create tables
db.create_all()

# create an object of the modle class for data
pet1 = Pet(name = "Woofly", species = "dog", age = 3, notes = "Good one", available = True)

# add new object to db session
db.session.add(pet1)

# Save it to the database
db.session.commit()