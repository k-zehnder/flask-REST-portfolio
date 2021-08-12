import unittest
from flask_testing import TestCase

from app.main import db
from wsgi import app


class FlaskTestCase(TestCase):
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

    def test_database(self):
        tester = self.app.test_client(self)
        response = tester.get('/', content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)