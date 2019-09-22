from flask_restful import Resource, reqparse
from app import db


from app.models.dmv import DMVModel
from app.models.instructors import InstructorModel
from app.models.reviews import ReviewModel


"""_dmv_parser = reqparse.RequestParser()
_dmv_parser.add_argument('_id',
                          type=int,
                          required=True,
                          help="This field cannot be blank."
                          )"""




class DMVbasicinfo(Resource):

	def get(self,_id):
		

		try:
			qdmv = DMVModel.query.get(_id)
			return {"name": qdmv.name, "rating":qdmv.rating, "id" :qdmv.id}
		except:
			return {"message": "Invalid Id!"}, 404
