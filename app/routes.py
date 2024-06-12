from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Book

api = Blueprint('api', __name__)


@api.route('/books', methods=['POST'])
def add_book():

    data = request.get_json()
    
    book = Book.query.filter_by(serial_number=data['serial_number']).first()
    if book:
        return jsonify({'message': 'Serial number already exists'}), 400
        
    new_book = Book(
        serial_number=data['serial_number'],
        title=data['title'],
        author=data['author'],
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 200


@api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    db.session.commit()
    return jsonify([{
        'serial_number': book.serial_number,
        'title': book.title,
        'author': book.author,
        'is_borrowed': book.is_borrowed,
        'borrowed_by': book.borrowed_by,
        'borrowed_on': book.borrowed_on
    } for book in books])


@api.route('/books/<serial_number>', methods=['DELETE'])
def delete_book(serial_number):
    book = Book.query.filter_by(serial_number=serial_number).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404


@api.route('/books/<serial_number>', methods=['PATCH'])
def update_status(serial_number):
    data = request.get_json()
    book = Book.query.filter_by(serial_number=serial_number).first()
    if book:
        book.is_borrowed = data['is_borrowed']
        book.borrowed_by = data.get('borrowed_by') if data['is_borrowed'] else None
        book.borrowed_on = datetime.now() if data['is_borrowed'] else None
            
        db.session.commit()
        return jsonify({'message': 'Book status updated'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404
