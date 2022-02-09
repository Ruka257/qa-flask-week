# Import everything we need
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" #best practice import os so no db credentials in code # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')