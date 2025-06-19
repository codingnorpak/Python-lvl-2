class FootballPlayer:
  def __init__(self, name, aftername):
    self.name = name
    self.aftername = aftername

  def move(self):
    print("Scoring a goal!")

class BasketballPlayer:
  def __init__(self, name, aftername):
    self.name = name
    self.aftername = aftername

  def move(self):
    print("Shooting into the net!")

footballplayer1 = FootballPlayer("Cristano", "Ronaldo")
basketballplayer1 = BasketballPlayer("Lebron", "James")

for x in (footballplayer1, basketballplayer1):
  x.move()