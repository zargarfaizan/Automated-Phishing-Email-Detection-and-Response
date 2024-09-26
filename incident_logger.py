import sqlite3
from datetime import datetime

# Create the SQLite database for logging incidents
def init_db():
    conn = sqlite3.connect('incidents.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY, subject TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

# Log phishing incident
def log_incident(subject):
    conn = sqlite3.connect('incidents.db')
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO incidents (subject, timestamp) VALUES (?, ?)", (subject, timestamp))
    conn.commit()
    conn.close()
