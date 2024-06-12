from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(6), unique=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    is_borrowed = db.Column(db.Boolean, default=False)
    borrowed_by = db.Column(db.String(6))
    borrowed_on = db.Column(db.DateTime)
