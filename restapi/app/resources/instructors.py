from app import db
from flask_restful import Resource, reqparse

from app.models.dmv import DMVModel
from app.models.instructors import InstructorModel

_ins_parser = reqparse.RequestParser()
_ins_parser.add_argument('_id',
                          type=int,
                          required=True,
                          help="This field cannot be blank."
                          )

class InstructorsList(Resource):
	def get(self):

		try:
			data = _ins_parser.parse_args()
			instructors = DMVModel.query.get(data['_id']).instructors

			resultlist = dict()

			for i in range(len(instructors)):
				currins = instructors[i]
				resultlist["instructor" + str(i+1)] = {"name":currins.name, "rating":currins.rating}

			return resultlist
		except:
			return {"message": "Invalid Id!"}, 404