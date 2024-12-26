from src.db.db import Database
from src.client.user import User
from user_files.crypto import *

def main():
    with Database() as db:
        user_service = User(db)
    
    print(file_encryption("AES", "src/user_files/hello.txt")) # test

if __name__ == "__main__":
    main()