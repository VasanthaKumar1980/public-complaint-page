from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    complaint = db.Column(db.String(100))
    email = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.Text)