import unittest
from ast import create_ast, evaluate_ast

class TestRuleEngine(unittest.TestCase):

    def test_create_ast(self):
        rule_string = "(age > 30) and (department == 'Sales')"
        ast = create_ast(rule_string)
        self.assertEqual(ast['rule'], rule_string)

    def test_evaluate_ast(self):
        rule_string = "(age > 30) and (department == 'Sales')"
        ast = create_ast(rule_string)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_ast(ast, data)
        self.assertTrue(result)


if __name__ == '__main__':