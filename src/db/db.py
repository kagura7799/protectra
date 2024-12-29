import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        try:
            load_dotenv() 
            self.conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_DATABASE")
            )
            if self.conn.is_connected():
                print("Connected to MySQL database")
                self.cursor = self.conn.cursor()

        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None

    def execute(self, query, params=()):
        if self.conn and self.cursor:
            try:
                self.cursor.execute(query, params)
                self.conn.commit()
                return True
            except Error as e:
                print(f"Database error: {e}")
                return False
        else:
            print("Connection or cursor is not initialized")
            return False
        
    def fetch_one(self, query, params=()):
        if self.conn and self.cursor:
            try:
                self.cursor.execute(query, params)
                return self.cursor.fetchone()
            except Error as e:
                print(f"Database error: {e}")
                return None
        else:
            print("Connection or cursor is not initialized")
            return None

    def fetch_all(self, query, params=()):
        if self.conn and self.cursor:
            try:
                self.cursor.execute(query, params)
                return self.cursor.fetchall()
            except Error as e:
                print(f"Database error: {e}")
                return []
        else:
            print("Connection or cursor is not initialized")
            return []

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
