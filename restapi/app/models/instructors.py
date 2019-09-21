from app import db


class InstructorModel(db.Model):
	__tablename__ = 'instructors'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))
	rating = db.Column(db.Integer)
	dmv_id = db.Column(db.Integer, db.ForeignKey('dmv.id'), nullable=False)

	def __repr__(self):
		return '<Instructor %r>' % self.name