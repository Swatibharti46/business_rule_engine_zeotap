import sqlite3

def create_database():
    """Creates the database table if it doesn't exist."""
    conn = sqlite3.connect('rules.db')  
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ast TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_rule(ast_string):
    """Inserts a rule into the database."""
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (ast) VALUES (?)", (ast_string,))
    conn.commit()
    conn.close()

def get_last_rule():
    """Retrieves the last inserted rule."""
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ast FROM rules ORDER BY id DESC LIMIT 1")
    last_rule = cursor.fetchone()
    conn.close()
    return last_rule

def get_all_rules():
    """Retrieves all rules."""
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ast FROM rules")
    all_rules = cursor.fetchall()
    conn.close()
    return all_rules