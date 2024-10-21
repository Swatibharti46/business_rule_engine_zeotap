from flask import Blueprint, request, jsonify
from ast import literal_eval
from .ast import create_ast, evaluate_ast, combine_asts  
from .database import insert_rule, get_last_rule, get_all_rules

api = Blueprint('api', __name__)

@api.route('/api/rules', methods=['POST'])
def create_rule():
    data = request.get_json()
    rule_string = data.get('rule')
    try:
        ast = create_ast(rule_string)
        insert_rule(str(ast))  # Store AST in database 
        return jsonify({'message': 'Rule created successfully!', 'ast': ast}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@api.route('/api/rules/combine', methods=['POST'])
def combine_rules_route():
    try:
        all_rules = get_all_rules()
        # Convert string representations back to dictionaries
        asts = [literal_eval(rule[0]) for rule in all_rules]  
        combined_ast = combine_asts(asts)
        if combined_ast:
            return jsonify({'message': 'Rules combined', 'ast': combined_ast}), 200
        else:
            return jsonify({'message': 'No rules to combine'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/rules/evaluate', methods=['POST'])
def evaluate_rule():
    data = request.get_json()
    user_data = data.get('data')
    try:
        # Get the last created rule 
        last_rule = get_last_rule()
        if last_rule:
            ast = literal_eval(last_rule[0]) # Convert string representation back to dict
            result = evaluate_ast(ast, user_data)
            return jsonify({'result': result}), 200
        else:
            return jsonify({'error': 'No rules found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
