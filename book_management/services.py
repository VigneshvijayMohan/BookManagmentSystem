from datetime import datetime
from flask import jsonify, request
from book_management import app, db
from book_management.models import Book


class BookService:
    def booklist():
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
    
    def indivi_book( book_id):
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
        
    def adding_books(data):
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
        
        
        
    def editing_book(book_id, data):
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
        
        
    def delete_book(book_id):
        record = Book.query.filter_by(id=book_id).first()
        if record:
            db.session.delete(record)
            db.session.commit()
            return jsonify({"Message":"Book updated Successfully"})
        else:
            return jsonify({"error": "Book not found"}), 404
        
book_management_system = BookService