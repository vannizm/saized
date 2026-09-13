import sqlite3

class Memory:
    def __init__(self, db_path="agent_memory.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_input TEXT,
                agent_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save(self, user_input, agent_response):
        self.cursor.execute(
            "INSERT INTO history (user_input, agent_response) VALUES (?, ?)",
            (user_input, agent_response)
        )
        self.conn.commit()

    def get_recent(self, limit=5):
        self.cursor.execute(
            "SELECT user_input, agent_response FROM history ORDER BY id DESC LIMIT ?",
            (limit,)
        )
        return self.cursor.fetchall()