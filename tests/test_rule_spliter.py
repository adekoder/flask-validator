import unittest
from flask_validator.validator_engine import ValidatorEngine


class TestRuleSplitter(unittest.TestCase):
        
    def testRuleOnly(self):
        result = ValidatorEngine().ruleSplitter('max')
        self.assertEqual(result[0], 'max')
        self.assertEqual(len(result[1]), 0)

    def testRuleWithSingleData(self):
        result = ValidatorEngine().ruleSplitter('min:12')
        self.assertEqual(result[0], 'min')
        self.assertEqual(len(result[1]), 1)

    def testRuleWithDoubleData(self):
        result = ValidatorEngine().ruleSplitter('exists:users,id')
        self.assertEqual(result[0], 'exists')
        self.assertEqual(len(result[1]), 2)
