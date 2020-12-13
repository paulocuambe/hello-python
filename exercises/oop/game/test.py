from game import Game
from player import Player

p1 = Player("Lucas", "Kisa")
p2 = Player("Paulo", "Morg")

g1 = Game(p1, p2, "17/12/2020")
g1.play()

print(p1)
print(p2)
print(g1)
print(g1.result)