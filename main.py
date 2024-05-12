#main.py
from utils.user_manager import UserManager
from utils.dice_game import DiceGame

def main_menu():
    user_manager = UserManager()
    user_manager.load_users()
    dice_game = DiceGame(user_manager)

    while True:
        print("\nWelcome to Dice Roll Game!")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice, or leave blank to cancel: ")
        if not choice:
            return
        if choice == "1":
            user_manager.register()
        elif choice == "2":
            current_user = user_manager.login()
            if current_user:
                logged_in_menu(dice_game, current_user)
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please try again.")

def logged_in_menu(self, current_user):
    self.current_user = current_user

    while True:
        print(f"\nWelcome, {current_user.username}!")
        print("Menu:")
        print("1. Start game")
        print("2. Show top scores")
        print("3. Log out")
        choice = input("\nEnter your choice, or leave blank to cancel: ")
        if not choice:
            return
        if choice == "1":
            self.play_game(current_user.username)
        elif choice == "2":
            self.show_top_scores()
        elif choice == "3":
            self.logout(current_user)
            return
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()