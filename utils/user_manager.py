# user_manager.py
from utils.user import User
import os

class UserManager:
    def __init__(self):
        self.users = {}

    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if os.path.exists("data/users.txt"):
            with open("data/users.txt", "r") as f:
                for line in f:
                    username, password = line.strip().split(",")
                    self.users[username] = User(username, password)

    def save_users(self):
        with open("data/users.txt", "w") as f:
            for user in self.users.values():
                f.write(f"{user.username},{user.password}\n")

    def validate_username(self, username):
        return len(username) >= 4

    def validate_password(self, password):
        return len(password) >= 8

    def register(self):
        while True:
            username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
            if not username:
                return None
            if not self.validate_username(username):
                print("Username must be at least 4 characters long.")
                continue
            if username in self.users:
                print("Username already exists.")
                continue
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if not password:
                return None
            if not self.validate_password(password):
                print("Password must be at least 8 characters long.")
                continue
            user = User(username, password)
            self.users[username] = user
            self.save_users()
            print("Registration successful.")
            return user

    def login(self):
        while True:
            username = input("Enter username, or leave blank to cancel: ")
            if not username:
                return None
            if username not in self.users:
                print("Invalid username or password.")
                continue
            password = input("Enter password, or leave blank to cancel: ")
            if not password:
                return None
            user = self.users[username]
            if user.password == password:
                print(f"Login successful. Welcome, {username}!")
                return user
            else:
                print("Invalid username or password.")