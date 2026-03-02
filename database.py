import sqlite3

def get_connection():
    conn = sqlite3.connect('energy_advisor.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS households (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            monthly_bill REAL,
            home_size TEXT,
            bulb_type TEXT,
            has_ac INTEGER,
            appliance_age TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            household_id INTEGER,
            tip TEXT,
            FOREIGN KEY (household_id) REFERENCES households(id)
        )
    ''')
    conn.commit()
    conn.close()