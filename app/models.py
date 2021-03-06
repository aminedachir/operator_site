from datetime import datetime
from app import db

class user(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), index = True, unique = True)
	firstname = db.Column(db.String(120))
	lastname = db.Column(db.String(120))
	confirm_email = db.Column(db.String(120))
	password_hash = db.Column(db.String(128))
	confirm_password_hash = db.Column(db.String(128))

	def __repr__(self):
		return f"<user {self.email}>"

