from app import db

class DMVModel(db.Model):
	__tablename__ = 'dmv'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	rating = db.Column(db.Integer)
	instructors = db.relationship('InstructorModel', backref='dmv', lazy=True)
	reviews = db.relationship('ReviewModel', backref='dmv', lazy=True)