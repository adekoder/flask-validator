import unittest

from flask_validator.validators import  validators
from flask_validator.exceptions import ValidationArgumentError

class TestDateValidators(unittest.TestCase):

    def test_date_with_correct_format(self):
        result = validators['date']('2017/02/21 12:02:23', '%Y/%m/%d %H:%M:%S')
        self.assertTrue(result['status'])
    
    def test_date_with_wrong_format(self):
        result = validators['date']('1/21/2017 31:01:23', '%Y/%m/%d %H:%M:%S')
        self.assertFalse(result['status'])

    def test_date_equal_with_correct_data(self):
        result = validators['date']('2017/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2017/03/02 00:01:23'))
        self.assertTrue(result['status'])
    
    def test_date_equal_with_wrong_data(self):
        result = validators['date']('2017/02/01 00:01:23', *('%Y/%m/%d %H:%M:%S', '2018/02/01 00:01:23'))
        self.assertFalse(result['status'])

    def test_date_after_with_correct_date(self):
        result = validators['date_after']('2018/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2017/03/02 00:01:23'))
        self.assertTrue(result['status'])
    
    def test_date_after_with_wrong_date(self):
        result = validators['date_after']('2018/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2019/03/02 00:01:23'))
        self.assertFalse(result['status'])
    
    def test_date_after_raise_error(self):
        self.assertRaises(ValidationArgumentError, validators['date_after'], '2018/03/02 00:01:23', *('2019/03/02 00:01:23'))
    
    def test_date_after_or_equal_with_correct_date(self):
        result = validators['date_after_or_equal']('2018/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2017/03/02 00:01:23'))
        self.assertTrue(result['status'])
    
    def test_date_after_or_equal_with_wrong_date(self):
        result = validators['date_after_or_equal']('2018/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2019/03/02 00:01:23'))
        self.assertFalse(result['status'])
    
    def test_date_after_or_equal_raise_error(self):
        self.assertRaises(ValidationArgumentError, validators['date_after_or_equal'], '2018/03/02 00:01:23', *('2019/03/02 00:01:23'))

    def test_date_before_with_correct_date(self):
        result = validators['date_before']('2017/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2018/03/02 00:01:23'))
        self.assertTrue(result['status'])
    
    def test_date_before_with_wrong_date(self):
        result = validators['date_before']('2019/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2018/03/02 00:01:23'))
        self.assertFalse(result['status'])
    
    def test_date_before_raise_error(self):
        self.assertRaises(ValidationArgumentError, validators['date_before'], '2018/03/02 00:01:23', *('2019/03/02 00:01:23'))
    
    def test_date_before_or_equal_with_correct_date(self):
        result = validators['date_before_or_equal']('2019/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2019/03/02 00:01:23'))
        self.assertTrue(result['status'])
    
    def test_date_before_or_equal_with_wrong_date(self):
        result = validators['date_before_or_equal']('2019/03/02 00:01:23', *('%Y/%m/%d %H:%M:%S', '2016/03/02 00:01:23'))
        self.assertFalse(result['status'])
    
    def test_date_before_or_equal_raise_error(self):
        self.assertRaises(ValidationArgumentError, validators['date_before_or_equal'], '2018/03/02 00:01:23', *('2019/03/02 00:01:23'))

