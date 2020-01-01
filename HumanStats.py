from GameStats import GameStats

class HumanStats(GameStats):

  def __init__(self):
    super(HumanStats, self).__init__(health=10, attack=5)
    self.magic = 10
    self.defense = 3
    self.dark_magic = 0
    self.speed = 1
    self.dark_points = 0
    self.light_magic = 0
    self.light_points = 0

  def print_stats(self):
    print(f"Health: {self.health}, Magic: {self.magic}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}, Dark Magic: {self.dark_magic}, Light Magic: {self.light_magic}")
