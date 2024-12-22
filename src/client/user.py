import bcrypt
from src.db.db import Database

class User:
    def __init__(self, db: Database):
        self.db = db

    def user_exists(self, username, email):
        return self.db.fetch_one(
            "SELECT id FROM users WHERE username = ? OR email = ?", 
            (username, email)
        ) is not None

    def register_user(self, username, password, email):
        if self.user_exists(username, email):
            print(f"Ошибка: пользователь с username {username} или email {email} уже существует.")
            return False

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return self.db.execute(
            "INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
            (username, hashed_password, email)
        )

    def check_password(self, username, password):
        user = self.db.fetch_one(
            "SELECT password FROM users WHERE username = ?",
            (username,)
        )
        if user is None:
            print("User is not found")
            return False
        return bcrypt.checkpw(password.encode(), user[0])
