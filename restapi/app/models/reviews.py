from app import db


class ReviewModel(db.Model):
	__tablename__ = 'reviews'

	id = db.Column(db.Integer, primary_key=True)
	comment = db.Column(db.Text(1000))
	upvotes = db.Column(db.Integer)
	downvotes = db.Column(db.Integer)
	timestamp = db.Column(db.String(120))
	dmv_id = db.Column(db.Integer, db.ForeignKey('dmv.id'), nullable=False)
	author = db.Column(db.String(120))
	user_id = db.Column(db.Integer)
	