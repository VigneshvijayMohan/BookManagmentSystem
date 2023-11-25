from flask import Flask, jsonify, request
from forms import LoginForm, RegistrationForm
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8a3de1d0597330cdc49e6496aa7b33fe'
csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Book(db.Model):
    id = id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), unique = True, nullable = False)
    author = db.Column(db.String(20), unique = True, nullable = False)
    isdn = db.Column(db.Integer, unique = True, nullable = False)
    publidate = db.Column(db.DateTime, nullable = False)
    
    
    def __repr__(self):
        return f"User('{self.title}', '{self.author}', '{self.isdn}', '{self.publidate}')"




@app.route("/list")
def list_books():
    return jsonify('list of books')

@app.route("/register", methods =['POST'])
def register():
    data = request.form
    form = RegistrationForm(data = data)
    if form.validate():
        
        # somwrhin
        return jsonify({"message":"Registration Complete"}), 200
    else: 
        errors = form.errors
        return jsonify({"Errors":errors}), 400


@app.route("/login", methods =['POST'])
def login():
    data = request.form
    form = LoginForm(data = data)
    if form.validate():
        # somwrhin
        return jsonify({"message":"Login Complete"}), 200
    else: 
        errors = form.errors
        return jsonify({"Errors":errors}), 400

if __name__ == "__main__":
    app.run(debug=True)