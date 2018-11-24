import unittest

from flask_validator.validators import  validators

class TestValidators(unittest.TestCase):
    
    def test_required_with_number(self):
        result = validators['required'](8)
        self.assertTrue(result['status'])
    
    def test_required_with_string(self):
        result = validators['required']('jamesbond')
        self.assertTrue(result['status'])
    
    def test_required_with_empty_data(self):
        result = validators['required']('')
        self.assertFalse(result['status'])

    def test_min_with_bigger_input(self):
        result = validators['min'](100, 9)
        self.assertTrue(result['status'])
    
    def test_min_with_lesser_input(self):
        result = validators['min'](2, 9)
        self.assertFalse(result['status'])
    
    def test_max_with_bigger_input(self):
        result = validators['max'](100, 9)
        self.assertFalse(result['status'])
    
    def test_max_with_lesser_input(self):
        result = validators['max'](2, 9)
        self.assertTrue(result['status'])