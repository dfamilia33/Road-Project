from app import db
from flask_restful import Resource, reqparse

from app.models.dmv import DMVModel
from app.models.reviews import ReviewModel

_rev_parser = reqparse.RequestParser()
_rev_parser.add_argument('_id',
                          type=int,
                          required=True,
                          help="This field cannot be blank."
                          )


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

