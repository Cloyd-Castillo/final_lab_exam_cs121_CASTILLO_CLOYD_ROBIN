# dice_game.py
import random
from utils.user_manager import UserManager
from utils.score import Score
from utils.user import User
import os

class DiceGame:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.scores = []
        self.current_user = None
        self.load_scores()

    def load_scores(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/rankings.txt"):
            with open("data/rankings.txt", "w"):
                pass
        else:
            with open("data/rankings.txt", "r") as f:
                for line in f:
                    username, game_id, points, wins = line.strip().split(",")
                    self.scores.append(Score(username, int(points), int(wins)))

    def save_scores(self):
        with open("data/rankings.txt", "w") as f:
            for score in self.scores:
                f.write(f"{score.username},{score.game_id}, {score.points}, {score.wins}\n")

    def play_game(self, username):
        user = self.user_manager.users.get(username, None)
        if user is None:
            print("User not found.")
            return

        stage = 1
        user_points = 0
        user_wins = 0

        while True:
            print(f"Starting stage {stage} for {username}.")
            user_score, cpu_score = self.play_stage()

            if user_score > cpu_score:
                print(f"You won this stage {username}!")
                user_wins += 1
                user_points += 3 * stage
            elif user_score < cpu_score:
                print(f"You lost this stage {username}.")
                break
            else:
                print("It's a tie!")
                

            print(f"\n{username} Total Points: {user_points}, Stages Won: {user_wins}")

            if user_wins < 2:
                continue_choice = input("Do you want to continue to the next stage? (1 for Yes, any other key for No): ").strip()
                if continue_choice != "1":
                    break
            else:
                print("You have already won the maximum number of stages.")
                break

            stage += 1

        if user_wins == 0:
            print("Game over. You didn't win any stages.")
        else:
            self.save_score(username, user_points, user_wins)
            print(f"Game over. You won {user_wins} stage(s) with a total of {user_points} points.")

    def play_stage(self):
        user_score = 0
        cpu_score = 0

        for _ in range(3):
            user_roll = random.randint(1, 6)
            cpu_roll = random.randint(1, 6)

            print(f"\n{self.current_user} rolled: {user_roll}")
            print(f"CPU rolled: {cpu_roll}")

            if user_roll > cpu_roll:
                print(f"You won this round!")
                user_score += 1
            elif user_roll < cpu_roll:
                print("You lost this round!")
                cpu_score += 1
            else:
                print("It's a tie!")

        return user_score, cpu_score

    def save_score(self, username, points, wins):
        score = Score(username, points, wins)
        self.scores.append(score)
        self.save_scores()

    def show_top_scores(self):
        sorted_scores = sorted(self.scores, key=lambda x: (-x.points, -x.wins))
        print("Top Scores:")
        for i, score in enumerate(sorted_scores[:10], start=1):
            print(f"{i}. {score.username}: Points {score.points}, Wins {score.wins}")

    def logout(self, username):
        self.current_user = None
        print(f"Goodbye {username}! You logged out successfully.")

    def register(self):
        username = self.user_manager.get_valid_username()
        if username:
            password = self.user_manager.get_valid_password()
            if password:
                user = User(username, password)
                self.user_manager.register(user)
                print(f"User {username} registered successfully.")

    def login(self):
        username = input("Enter username, or leave blank to cancel: ").strip()
        if username:
            password = input("Enter password, or leave blank to cancel: ").strip()
            if password:
                if self.user_manager.login(username, password):
                    self.current_user = username
                    return username
                else:
                    print("Invalid username or password.")
        return None
