import unittest

from flask_validator.validators import  validators
from flask_validator.exceptions import ValidationArgumentError

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

    def test_alpha_with_wrong_data(self):
        result = validators['alpha']('james_1233')
        self.assertFalse(result['status'])
    
    def test_alpha_with_correct_data(self):
        result = validators['alpha']('james')
        self.assertTrue(result['status'])

    def test_alpha_with_empty_data(self):
        result = validators['alpha']('')
        self.assertFalse(result['status'])
    
    def test_alphanumeric_with_wrong_data(self):
        result = validators['alphanumeric']('james_1233')
        self.assertFalse(result['status'])
    
    def test_alphanumeric_with_correct_data(self):
        result = validators['alphanumeric']('james')
        self.assertTrue(result['status'])

    def test_alphanumeric_with_empty_data(self):
        result = validators['alphanumeric']('')
        self.assertFalse(result['status'])
    
    def test_list_with_wrong_data(self):
        result = validators['list']('james')
        self.assertFalse(result['status'])
    
    def test_list_with_correct_data(self):
        result = validators['list']([1,2,3])
        self.assertTrue(result['status'])
    
    def test_list_plus_limit_with_wrong_data(self):
        result = validators['list']([1,2,3], 2)
        self.assertFalse(result['status'])
        self.assertEqual(result['message'], 'This field must be a list with length of 2')
    
    def test_list_plus_limit_with_corret_data(self):
        result = validators['list']([1,2,3], 3)
        self.assertTrue(result['status'])

    def test_bool_with_correct_data(self):
        result = validators['bool'](True)
        self.assertTrue(result['status'])
    
    def test_bool_with_wrong_data(self):
        result = validators['bool']('hello world')
        self.assertFalse(result['status'])
    
    def test_bool_with_1_and_0_data(self):
        result_1 = validators['bool'](1)
        result_2 = validators['bool'](0)
        self.assertTrue(result_1['status'])
        self.assertTrue(result_2['status'])
        