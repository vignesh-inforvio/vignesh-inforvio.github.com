import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Fetching raw user input
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # VULNERABLE: Direct string formatting allows SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return "Login successful!"
        else:
            return "Invalid credentials."
    except Exception as e:
        return f"Database error: {e}"
