import unittest
from flask import json
from . import app

class TestValidator(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_validator_with_bad_json_data(self):
        response = self.client.post('/index', data=json.dumps({'name': 20}),
         headers={
             'content-type': 'application/json'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertIn('errors', data)
    
    def test_validator_with_bad_query_string(self):
        response = self.client.get('/query?name="jamesbond1233"&age=23',
        headers={
            'content-type': 'application/json'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertIn('errors', data)

    def test_validator_with_good_query_string(self):
        response = self.client.get('/query?name=jamesbond&age=23',
        headers={
            'content-type': 'application/json'
        })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
