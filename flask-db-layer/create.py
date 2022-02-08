from app import db, Users, Accounts

db.drop_all()
db.create_all()

# Extra: this section populates the table with an example entry
#Here we are importing the SQLAlchemy object db and the Users class defined in app.py
testuser = Users(first_name='Grooty ',last_name='Toot')
testaccounts = Accounts(member_status='Yes', email_address='hello@email.com')
db.session.add(testuser)
db.session.add(testaccounts)
db.session.commit()