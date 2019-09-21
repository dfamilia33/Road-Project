from flask_restful import Resource
from flask_jwt_extended import jwt_required



class Home(Resource):
	@jwt_required
	def get(self):
		return {'message':'The home endpoint has been accessed. Add more resources to build this api!'}

