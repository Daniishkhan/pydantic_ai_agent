import sqlite3

def get_db_connection():
    conn = sqlite3.connect('bank_database.db')
    conn.row_factory = sqlite3.Row
    return conn
    

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS customers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        '''
    )
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    init_db()