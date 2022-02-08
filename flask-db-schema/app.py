from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object
# Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

#create new tables
class Accounts(db.Model):
    member_status = db.Column(db.Boolean, default=False)
    email_address = db.Column(db.String, primary_key=True)
    mobile_number = db.Column(db.String(14), nullable=False)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')