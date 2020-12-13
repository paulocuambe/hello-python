import random


class Game:
    def __init__(self, player1, player2, date):
        self.player1 = player1
        self.player2 = player2
        self.date = date
        self.result = None

    def play(self):
        if self.result is None:
            self.result = random.choice([self.player1, self.player2
                                         ]).name + " won the game."
        else:
            return Exception("This game has been played.")

    def __repr__(self):
        return f"{self.player1.name} vs {self.player2.name} - {self.date}"