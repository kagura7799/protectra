from src.db.db import Database
from src.client.user import User

def main():
    with Database() as db:
        user_service = User(db)

        if user_service.register_user("new_user", "secure_password", "new_user@example.com"):
            print("Reistration sucessfull!")

        if user_service.check_password("new_user", "secure_password"):
            print("Password is valid")
        else:
            print("Password is invalid")

if __name__ == "__main__":
    main()