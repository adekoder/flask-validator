import unittest
from flask import json
from app import app
from flask_validator.validator import ValidatorAttributeError
class TestValidator(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_validator_with_wrong_json_data(self):
        response = self.client.post('/index', data=json.dumps({}),
         headers={
             'content-type': 'application/json'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertIn('errors', data)
