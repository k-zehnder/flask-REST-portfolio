import unittest

from app.main import db
import json
from app.test.base import BaseTestCase


# def register_user(self):
#     return self.client.post(
#         '/user/',
#         data=json.dumps(dict(
#             email='joe@gmail.com',
#             username='username',
#             password='123456'
#         )),
#         content_type='application/json'
#     )


class TestAuthBlueprint(BaseTestCase):
    def test_registration(self):
        """ Test for user registration """
        with self.client:
            response = self.client.get("/", content_type='application/json')
            self.assertEqual(response.status_code, 200)