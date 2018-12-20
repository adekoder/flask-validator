import unittest
from flask_validator.validators.date import Date

class TestDateRegexBuild(unittest.TestCase):

    def test_build_regex_with_slash(self):
        date = Date()
        result = date._build_regex('d/m/y h:i:s')
        self.assertEqual(result, '[1-31]{1,2}[/][1-12]{1,2}[/]\\d{2} [00-23]{2}[:][00-59]{2}[:][00-59]{2}')
    
    def test_build_regex_with_hyphen(self):
        date = Date()
        result = date._build_regex('d-m-y h:i:s')
        self.assertEqual(result, '[1-31]{1,2}[-][1-12]{1,2}[-]\\d{2} [00-23]{2}[:][00-59]{2}[:][00-59]{2}')
    
    def test_build_regex_with_date_of_double_digits(self):
        date = Date()
        result = date._build_regex('D/M/Y h:i:s')
        self.assertEqual(result, '[01-31]{1,2}[/][01-12]{1,2}[/]\\d{4} [00-23]{2}[:][00-59]{2}[:][00-59]{2}')

    def test_build_date_regex_throw_key_error(self):
        date = Date()
        self.assertRaises(KeyError, date._date_regex_string, 'd/y\\m')
    
    def test_build_time_regex_throw_key_error(self):
        date = Date()
        self.assertRaises(KeyError, date._time_regex_string, 'h-i-s')
            