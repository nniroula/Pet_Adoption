from flask import Flask

app = Flask(__name__)

@app.route('/wtforms')
def check_flask_setup():
    return "<h3> FLASK, SQLALCHEMY, AND WTFORMS ARE QUIT HARD TO LEARN </h1>"
    