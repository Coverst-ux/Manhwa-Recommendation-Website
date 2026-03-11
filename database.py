import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute('''CREATE TABLE IF NOT EXISTS sessions(id TEXT PRIMARY KEY, 
            created_at TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS manhwa_list(
            id INTEGER PRIMARY KEY,
            session_id TEXT,
            comick_slug TEXT,
            title TEXT,
            genres TEXT,
            status TEXT,
            demographic TEXT,
            added_at TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
            
    ) ''')