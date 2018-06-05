import unittest

from flask_validator.rulespliter import ruleSpliter


class TestRuleSplitter(unittest.TestCase):

    def testRuleOnly(self):
        rule = 'max'
        result = ruleSpliter(rule)
        print(result)
        self.assertEqual(result['rule'], 'max')
        self.assertEqual(len(result['data']), 0)
    
    def testRuleWithSingleData(self):
        rule = 'min:12'
        result = ruleSpliter(rule)
        print(result)
        self.assertEqual(result['rule'], 'min')
        self.assertEqual(len(result['data']), 1)
    
    def testRuleWithDoubleData(self):
        rule = 'exists:users,id'
        result = ruleSpliter(rule)
        print(result)
        self.assertEqual(result['rule'], 'exists')
        self.assertEqual(len(result['data']), 2)
