from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
     return render_template('ben.html')

@app.route('/harry')
def harry():
     return render_template('harry.html')

# Create a Flask app that passes list of names to a template and within the template iterates through the list and only shows the names that contain the letter "b".
# ["ben", "harry", "bob", "jay", "matt", "bill"]
# search all indexes in list names for character 'b'

# first attempt error @app.route('/bnames')
#def bnames():
    #names = ["ben", "harry", "bob", "jay", "matt", "bill"]
   # bnames = names.query.all('b')
   # return render_template('bnames.html')

if __name__ == "__main__":
     app.run(debug=True, host='0.0.0.0')