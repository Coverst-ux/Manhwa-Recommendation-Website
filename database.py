import sqlite3
import uuid
from datetime import datetime

con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("PRAGMA foreign_keys = ON")

cur.execute('''CREATE TABLE IF NOT EXISTS sessions(id TEXT PRIMARY KEY, 
            created_at TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS manhwa_list(
            id INTEGER PRIMARY KEY,
            session_id TEXT,
            slug TEXT,
            title TEXT,
            genres TEXT,
            status TEXT,
            demographic TEXT,
            added_at TEXT,
            FOREIGN KEY (session_id) REFERENCES sessions(id)
            
    ) ''')

def create_session():
        session_uuid =  uuid.uuid4()
        time_stamp = datetime.now().isoformat()
        cur.execute('''INSERT INTO sessions 
                    ("id", "created_at") VALUES
                    (?, ?)
                    ''', (str(session_uuid), time_stamp))
        con.commit()
        return session_uuid

def add_manhwa(session_uuid, hid, slug, title, genres, status, demographic, cover_url, added_at):
        cur.execute('''
                    INSERT INTO manhwa_list
                    ("session_id", "hid", "slug", "title", "genres", "status", "demographic", "cover_url", "added_at") VALUES
                    (?,?,?,?,?,?,?,?,?)
                    ''', (str(session_uuid), hid, slug, title, genres, status, demographic, cover_url, added_at))
        con.commit()
        return cur.lastrowid
        