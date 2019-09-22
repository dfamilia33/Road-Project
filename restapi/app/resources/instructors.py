from app import db
from flask_restful import Resource, reqparse

from app.models.dmv import DMVModel
from app.models.instructors import InstructorModel



class InstructorsList(Resource):
	def get(self,_id):

		try:
			instructors = DMVModel.query.get(_id).instructors

			resultlist = dict()

			for i in range(len(instructors)):
				currins = instructors[i]
				resultlist["instructor" + str(i+1)] = {"name":currins.name, "rating":currins.rating}

			return resultlist
		except:
			return {"message": "Invalid Id!"}, 404