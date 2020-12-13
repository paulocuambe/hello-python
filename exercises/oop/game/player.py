class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team
        self.games = []

    def __str__(self):
        return f"{self.name} | {self.team}"