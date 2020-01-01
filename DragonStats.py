import random

from GameStats import GameStats

class DragonStats(GameStats):

  def __init__(self):
    super(DragonStats, self).__init__(health=50, attack=20)
    self.fire = 25
    self.defense = 10
    self.enemy_type = "dragon"

  def print_stats(self):
    print(f"Dragon Health: {self.health} Dragon Attack: {self.attack} Dragon Fire: {self.fire} Dragon Defense: {self.defense}")