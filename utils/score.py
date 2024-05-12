# score.py
import datetime

class Score:
    def __init__(self, username, points=0, wins=0):
        self.username = username
        self.game_id = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.points = points
        self.wins = wins