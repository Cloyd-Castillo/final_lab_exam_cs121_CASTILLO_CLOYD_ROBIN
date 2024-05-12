# user.py
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.points = 0
        self.stages_won = 0

    def __str__(self):
        return self.username