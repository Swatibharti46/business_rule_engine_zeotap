import ast

def create_ast(rule_string):
    """Creates an AST from a rule string.
    
    For simplicity, this example directly converts the rule string 
    into a dictionary. In a real-world application, you'd use 
    a parser (like `ast.parse`) and implement a proper AST structure. 
    """
    try:
        # Attempt to evaluate the rule string to check for basic syntax errors.
        ast.literal_eval(rule_string)  
    except (SyntaxError, ValueError) as e:
        raise ValueError(f"Invalid rule syntax: {e}") 
    return {'rule': rule_string}

def combine_asts(asts):
    """Combines multiple ASTs into one.

    This is a placeholder. You'll need to implement your logic here.
    For this example, it combines rules using "AND".
    """
    if not asts:
        return None
    combined_rule = " and ".join([ast['rule'] for ast in asts])  
    return {'rule': combined_rule} 

def evaluate_ast(ast, data):
    """Evaluates an AST against user data.

    This is a simplified evaluation using `eval()`. 
    Do NOT use `eval()` with user-provided input in production 
    due to security risks. 
    """
    rule = ast['rule']
    # Simple rule evaluation (replace with robust and secure logic):
    for key, value in data.items():
        if isinstance(value, str):
            rule = rule.replace(f"{key}", f"'{value}'") 
        else:
            rule = rule.replace(f"{key}", str(value))
    try:
        result = eval(rule)
        return result
    except Exception as e:
        raise ValueError(f"Error evaluating rule: {e}")