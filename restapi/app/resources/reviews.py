from app import db
from flask_restful import Resource, reqparse

from app.models.dmv import DMVModel
from app.models.reviews import ReviewModel
from flask_jwt_extended import get_jwt_identity,jwt_required
from app.models.user import UserModel

_rev_parser = reqparse.RequestParser()

_rev_parser.add_argument('_id',
				type=int,
				required=True,
				help="This field cannot be blank."
				)

def check_duplicate(dmvid,ident):
	if len(ReviewModel.query.filter_by(user_id=ident, dmv_id=dmvid).all()) > 1:
		return True
	return False


class ReviewList(Resource):

	def get(self):


		
		
		data = _rev_parser.parse_args()

		reviews = DMVModel.query.get(data['_id']).reviews

		resultlist = dict()

		for i in range(len(reviews)):
			curr_revs = reviews[i]
			resultlist["instructor" + str(i+1)] = {"comment":curr_revs.comment, "upvotes":curr_revs.upvotes, "downvotes":curr_revs.downvotes,
			"time":curr_revs.timestamp, "dmv_id" :curr_revs.dmv_id, "author" :curr_revs.author}

		return resultlist
	
		return {"message": "Invalid Id!"}, 404

	@jwt_required
	def post(self):
		_rev_parser.add_argument('comment',
				required=True,
				help="This field cannot be blank."
				)

		data = _rev_parser.parse_args()

		ident = get_jwt_identity()

		if check_duplicate(data['_id'], ident):
			return {"message": "Error: Attempted to place a review twice"}, 403

		review = ReviewModel()
		review.upvotes = 1
		review.downvotes = 0
		review.user_id = ident
		review.author = UserModel.query.get(ident).username
		review.comment = data['comment']
		review.dmv_id = data['_id']

		db.session.add(review)
		db.session.commit()

		return {"message": "Review created successfully."}, 201


		


