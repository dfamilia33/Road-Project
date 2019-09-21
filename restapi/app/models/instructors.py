from app import db


class InstructorModel(db.Model):
	__tablename__ = 'instructors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	rating = db.Column(db.Integer)