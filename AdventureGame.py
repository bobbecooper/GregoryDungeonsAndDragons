
import random

from GameMap import GameMap, directions
from HumanStats import HumanStats
from GoblinStats import GoblinStats
from DragonStats import DragonStats
from Story import Story

class AdventureGame():
  def __init__(self):
    self.human_stats = HumanStats()
    self.story = Story(self.human_stats)
    self.game_map = GameMap(self.human_stats, self.story)
    self.game_ended = False
    self.is_defended = False
    self.story.print_intro()
  
  def take_turn(self):
    self.print_situation()
    user_input = self.get_input()
    self.update_situation(user_input)
    return self.game_ended

  def print_situation(self):
    self.human_stats.print_stats()
    self.game_map.print_position()
    
  def get_input(self):
    direction = ""
    while direction not in directions + ["Q"]:
      print("Direction?")
      direction = str(input())
    return direction

  def update_situation(self, user_input):
    self.game_map.move(user_input)
    if "Q" in user_input:
      self.game_ended = True
    if self.game_ended == False:
      hit_dragon = self.game_map.check_map()
      if hit_dragon:
        self.enemy = DragonStats()
        self.game_ended = self.combat()
        if self.game_ended == False:
          if self.human_stats.dark_points >0:
            print(f"Dark points: {self.human_stats.dark_points}")
            self.story.dark_win()

          elif self.human_stats.light_points >0:
            print(f"Light points: {self.human_stats.light_points}")
            self.story.light_win()
            
          else:
            self.story.win()
            self.game_ended = True
        if self.game_ended == False:
          self.check_for_goblins()

  def check_for_goblins(self):
    goblin_chance = random.randint(1,16)
    if goblin_chance == 1:
      print ("Oh no! Goblins!")
      self.enemy = GoblinStats(number_goblins=3)
      self.game_ended = self.combat()
    
  def combat(self):
    print(f"You have run into trouble: {self.enemy.enemy_type}")
    combat_ended = False
    while not combat_ended:
      (combat_ended, game_ended) = self.enemy.do_combat(self.human_stats)
    return game_ended

  


    
  


















































