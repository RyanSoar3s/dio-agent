import sqlite3
from typing import Literal

def login_db(user: str, passw: str) -> Literal["access allowed", "access denied"]:
    connect = sqlite3.connect("database.db")
    cursor = connect.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{passw}'"
    
    cursor.execute(query)
    res = cursor.fetchone()
    
    connect.close()
    
    return "access allowed" if res else "access denied"
    
