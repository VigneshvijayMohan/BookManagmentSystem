from flask import Flask, jsonify, request
from forms import LoginForm, RegistrationForm
# from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SECRET_KEY'] = '8a3de1d0597330cdc49e6496aa7b33fe'
# csrf = CSRFProtect(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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




@app.route("/list")
def list_books():
    books = Book.query.all()
    book_list = [
        
        {
            'title':book.title,
            'author':book.author,
            'isdn': book.isdn,
            'publidate': book.publidate
        }
        for book in books
    ]
    return jsonify(books = book_list)


@app.route("/list/<book_id>", methods=['GET'])
def list_book_indi(book_id):
    books = db.session.query(Book).filter(Book.id == book_id).all()
    if books:
        book_list = [
            
            {
                'title':book.title,
                'author':book.author,
                'isdn': book.isdn,
                'publidate': book.publidate
            }
            for book in books
        ]
        return jsonify(books = book_list)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route("/books", methods=['POST'])
def add_books():
    data = request.json
    if data:
        title_new = data['title']
        author_new = data['author']
        isdn_new = data['isdn']
        publidate_new = datetime.strptime(data['publidate'], '%d-%m-%Y')
        user_id_new = data['user_id']
        books = db.session.query(Book).filter(Book.title == title_new).all()
        if books:
            return jsonify({"error": "Book Already exists"}), 404
        else:
            new_book = Book(
                title = title_new, 
                author = author_new,
                isdn = isdn_new,
                publidate = publidate_new,
                user_id = user_id_new
                
            )
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"Message":"Book Added Successfully"})
    else:
        return jsonify({"error": "Missing required fields"}), 404


@app.route("/books/<book_id>", methods=['PUT'])
def edit_book(book_id):
    data = request.json
    record = Book.query.filter_by(id=book_id).first()
    if record:
        record.title = data.get('title', record.title)
        record.author = data.get('author', record.author)
        record.isdn = data.get('isdn', record.isdn)
        publidate_str = data.get('publidate', record.publidate)
        record.publidate = datetime.strptime(publidate_str, '%d-%m-%Y') if publidate_str else record.publidate
        record.user_id = data.get('user_id', record.user_id)
        db.session.commit()
        return jsonify({"Message":"Book updated Successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404




@app.route("/books/<book_id>", methods=['DELETE'])
def delete_book(book_id):
    record = Book.query.filter_by(id=book_id).first()
    if record:
        db.session.delete(record)
        db.session.commit()
        return jsonify({"Message":"Book updated Successfully"})
    else:
        return jsonify({"error": "Book not found"}), 404
        



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)