from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3  # Import Python's built-in SQLite module
from priority_queue import add_patient, get_next_patient, get_sorted_queue

app = Flask(__name__)
CORS(app)

DB_FILE = "smartqueue.db"

# NEW: Function to create the database table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            priority INTEGER NOT NULL,
            served INTEGER DEFAULT 0  -- 0 means waiting, 1 means served/removed
        )
    ''')
    conn.commit()
    conn.close()

# Initialize the database right away
init_db()

@app.route('/')
def home():
    return "SmartQueue Backend Running!"