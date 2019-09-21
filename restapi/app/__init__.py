from flask import Flask, jsonify

from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app.resources.home import Home



from flask_restful import Api
from flask_jwt_extended import JWTManager

from app.blacklist import BLACKLIST


app = Flask(__name__)
app.secret_key = 'dan'

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

api = Api(app)
jwt = JWTManager(app)


from app.resources.user import UserRegister, UserLogin, UserLogout, TokenRefresh
from app.resources.dmv import DMVbasicinfo
from app.resources.instructors import InstructorsList
from app.models.user import UserModel #has to be after db decalred since using it
from app.models.dmv import DMVModel
from app.models.instructors import InstructorModel
from app.models.reviews import ReviewModel

"""
`claims` are data we choose to attach to each jwt payload
and for each jwt protected endpoint, we can retrieve these claims via `get_jwt_claims()`
one possible use case for claims are access level control, which is shown below.
"""
@jwt.user_claims_loader
def add_claims_to_jwt(identity):  # Remember identity is what we define when creating the access token
    if identity == 1:   # instead of hard-coding, we should read from a config file or database to get a list of admins instead
        return {'is_admin': True}
    return {'is_admin': False}


# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST  # Here we blacklist particular JWTs that have been created in the past.


# The following callbacks are used for customizing jwt response/error messages.
# The original ones may not be in a very pretty format (opinionated)
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'message': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):  # we have to keep the argument here, since it's passed in by the caller internally
    return jsonify({
        'message': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        "description": "Request does not contain an access token.",
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        "description": "The token is not fresh.",
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        "description": "The token has been revoked.",
        'error': 'token_revoked'
    }), 401


api.add_resource(Home,'/home')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout,'/logout')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(DMVbasicinfo, '/DMVinfo')
api.add_resource(InstructorsList, '/Instructors')



if __name__ == '__main__':
  app.run(port=5000, debug=True)