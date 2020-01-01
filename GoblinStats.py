import random

from GameStats import GameStats

class GoblinStats(GameStats):

  def __init__(self, number_goblins):
    self.goblin_list = [GameStats(health=random.randint(1, 10), attack=3) for _ in range(number_goblins)]
    self.attack = 3
    self.number_goblins = number_goblins
    self.enemy_type = "goblins"

  def print_stats(self):
      for i in range(self.number_goblins):
        print(f"Goblin {i} health: {self.goblin_list[i].health}")
  
  def get_live_goblins(self):
    live_guys = [i for i in range(self.number_goblins) if self.goblin_list[i].health > 0]
    return live_guys

  def dead(self):
    deadness = True
    for goblin in self.goblin_list:
      if goblin.health > 0:
        deadness = False
    return deadness

  def be_attacked(self, attack_strength):
      live_goblins = self.get_live_goblins()
      goblin_hit = random.randint(0, len(live_goblins)-1)
      self.goblin_list[live_goblins[goblin_hit]].health = max(self.goblin_list[live_goblins[goblin_hit]].health - attack_strength, 0)


  