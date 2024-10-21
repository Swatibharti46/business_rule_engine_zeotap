# app.py
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# This will hold the rules in memory for simplicity
rules = []

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string):
    # Basic implementation to parse rule_string into an AST
    # You need to implement the parsing logic here
    # For simplicity, let's return a simple Node
    return Node(type="operator", left=Node(type="operand", value="age"), right=Node(type="operand", value="30"))

def combine_rules(rule_strings):
    # Combine rules into a single AST
    return Node(type="operator", left=create_rule(rule_strings[0]), right=create_rule(rule_strings[1]))

def evaluate_rule(ast, data):
    # Evaluate the rule against the provided data
    # You need to implement the logic for evaluating the AST
    return data["age"] > 30  # Placeholder logic

@app.route('/create_rule', methods=['POST'])
def handle_create_rule():
    data = request.json
    rule_string = data.get('rule_string')
    ast = create_rule(rule_string)
    rules.append(ast)
    return jsonify({"message": "Rule created", "ast": ast.__dict__})

@app.route('/combine_rules', methods=['POST'])
def handle_combine_rules():
    data = request.json
    rule_strings = data.get('rule_strings')
    combined_ast = combine_rules(rule_strings)
    return jsonify({"message": "Rules combined", "ast": combined_ast.__dict__})

@app.route('/evaluate_rule', methods=['POST'])
def handle_evaluate_rule():
    data = request.json
    ast = data.get('ast')
    user_data = data.get('user_data')
    result = evaluate_rule(ast, user_data)
    return jsonify({"is_eligible": result})

if __name__ == '__main__':
    app.run(debug=True)
