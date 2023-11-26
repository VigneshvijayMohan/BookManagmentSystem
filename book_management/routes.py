from flask import request
from book_management import app
from book_management.services import book_management_system



@app.route("/list", methods=['GET'])
def list_books():
    response = book_management_system.booklist()
    return response


@app.route("/list/<book_id>", methods=['GET'])
def list_book_indi(book_id):
    response = book_management_system.indivi_book(book_id)
    return response


@app.route("/books", methods=['POST'])
def add_books():
    data = request.json
    response = book_management_system.adding_books(data)
    return response

@app.route("/books/<book_id>", methods=['PUT'])
def edit_book(book_id):
    data = request.json
    response = book_management_system.editing_book(book_id, data)
    return response



@app.route("/books/<book_id>", methods=['DELETE'])
def delete_book(book_id):
    response = book_management_system.delete_book(book_id)
    return response