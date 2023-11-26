from flask import Flask
# from forms import LoginForm, RegistrationForm
# from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# app.config['SECRET_KEY'] = '8a3de1d0597330cdc49e6496aa7b33fe'
# csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from book_management import routes