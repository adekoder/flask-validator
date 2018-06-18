import unittest

from flask_validator.rulesplitter import ruleSplitter


class TestRuleSplitter(unittest.TestCase):

    def testRuleOnly(self):
        rule = 'max'
        result = ruleSplitter(rule)
        print(result)
        self.assertEqual(result['name'], 'max')
        self.assertEqual(len(result['args']), 0)
    
    def testRuleWithSingleData(self):
        rule = 'min:12'
        result = ruleSplitter(rule)
        print(result)
        self.assertEqual(result['name'], 'min')
        self.assertEqual(len(result['args']), 1)
    
    def testRuleWithDoubleData(self):
        rule = 'exists:users,id'
        result = ruleSplitter(rule)
        self.assertEqual(result['name'], 'exists')
        self.assertEqual(len(result['args']), 2)
