import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True #enables custom error messages
    JWT_BLACKLIST_ENABLED = True  # enable blacklist feature
    JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh'] 