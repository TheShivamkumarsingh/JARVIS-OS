import sqlite3
from pathlib import Path


class Memory:
    def __init__(self):
        # Get project root folder
        BASE_DIR = Path(__file__).resolve().parents[2]

        # Create data folder if it doesn't exist
        data_folder = BASE_DIR / "data"
        data_folder.mkdir(exist_ok=True)

        # Database file
        db_path = data_folder / "jarvis.db"

        # Connect to SQLite
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

        # Create tables
        self.create_conversation_table()
        self.create_profile_table()

    # -------------------------------------------------
    # Conversation Table
    # -------------------------------------------------

    def create_conversation_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_message TEXT,
                assistant_message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

    def remember(self, user_message, assistant_message):
        self.cursor.execute(
            "INSERT INTO conversations(user_message, assistant_message) VALUES(?, ?)",
            (user_message, assistant_message)
        )
        self.connection.commit()

    def get_history(self):
        self.cursor.execute(
            "SELECT user_message FROM conversations ORDER BY id"
        )
        return self.cursor.fetchall()

    # -------------------------------------------------
    # User Profile Table
    # -------------------------------------------------

    def create_profile_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS profile (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        """)
        self.connection.commit()

    def save_profile(self, key, value):
        self.cursor.execute("""
            INSERT OR REPLACE INTO profile(key, value)
            VALUES(?, ?)
        """, (key, value))
        self.connection.commit()

    def get_profile(self, key):
        self.cursor.execute(
            "SELECT value FROM profile WHERE key=?",
            (key,)
        )

        result = self.cursor.fetchone()

        if result:
            return result[0]

        return None

    def get_all_profile(self):
        self.cursor.execute(
            "SELECT key, value FROM profile"
        )

        return self.cursor.fetchall()

    # -------------------------------------------------
    # Close Database
    # -------------------------------------------------

    def close(self):
        self.connection.close()