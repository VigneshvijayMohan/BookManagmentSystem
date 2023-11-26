from book_management import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    books = db.relationship('Book', backref = 'editor', lazy = True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
class Book(db.Model):
    id = id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), unique = True, nullable = False)
    author = db.Column(db.String(200), nullable = False)
    isdn = db.Column(db.Integer, unique = True, nullable = False)
    publidate = db.Column(db.DateTime, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    
    def __repr__(self):
        return f"User('{self.title}', '{self.author}', '{self.isdn}', '{self.publidate}')"