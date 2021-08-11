from flask_testing import TestCase

from app.main import db
from app.main import config
from wsgi import app

# class TestingConfig(Config):
#     DEBUG = True
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'fourteener.db')
#     PRESERVE_CONTEXT_ON_EXCEPTION = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app.config.from_object('test')
        return app

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()