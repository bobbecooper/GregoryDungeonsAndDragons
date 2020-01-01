
import random

directions = ["E", "W", "N", "S"]

class GameMap():
  
  def __init__(self, stats, story):
    self.x_position = 5
    self.y_position = 5
    self.gem = (7, 8)
    self.iron_boots = (6, 7)
    self.ruby_armor = (8, 6)
    self.diamond_armor = (8, 3)
    self.mystical_sword = (5, 3)
    self.magic_trident = (9, 9)
    self.mystical_serum = (6, 1)
    self.Suknana = (7, 2)
    self.Saffron = (2, 10)
    self.Ashardon = (4, 10)
    self.Temple_of_light = (3, 6)
    self.stats = stats
    self.story = story

  def print_position(self):
    print(f"You are at position ({self.x_position}, {self.y_position})")
    print("Here are the directions you can go:")
    print(self.available_directions())
  
  def available_directions(self):
    available = ""
    if self.x_position < 10:
      available = available + "E"
    if self.x_position > 1:
      available = available + "W"
    if self.y_position > 1:
      available = available + "S"
    if self.y_position < 10:
      available = available + "N"
    return available

  def check_map(self):
      self.cities()
      if (self.x_position, self.y_position) == self.mystical_serum:
        self.story.mystical_serum()
        self.stats.health = self.stats.health + 10
        self.mystical_serum = (100, 100)
      if (self.x_position, self.y_position) == self.magic_trident:
        self.story.magic_trident()
        self.stats.magic = self.stats.magic + 10
        self.magic_trident = (100, 100)
      if (self.x_position, self.y_position) == self.mystical_sword:
        self.story.mystical_sword()
        self.stats.attack = self.stats.attack + 10
        self.mystical_sword = (100, 100)
      if (self.x_position, self.y_position) == self.diamond_armor:
        self.story.diamond_armor()
        self.stats.defense = self.stats.defense + 3
        self.diamond_armor = (100, 100)
      if (self.x_position, self.y_position) == self.iron_boots:
        self.story.iron_boots()
        self.stats.speed = self.stats.speed + 2
        self.iron_boots = (100, 100)
      if (self.x_position, self.y_position) == self.ruby_armor:
        self.story.ruby_armor()
        self.stats.defense = self.stats.defense + 10
      if (self.x_position, self.y_position) == self.gem:
        return True
      return False
      
  def cities(self):
      if (self.x_position, self.y_position) == self.Suknana:
        self.story.Suknana()
        self.stats.defense = self.stats.defense + 6
        self.stats.attack = self.stats.attack +5
        self.stats.dark_magic = self.stats.dark_magic + 30
        self.stats.dark_points = self.stats.dark_points + 15
        self.Suknana = (100, 100)
      if (self.x_position, self.y_position) == self.Saffron:
        self.story.Saffron()
        self.stats.defense = self.stats.defense + 10
        self.stats.attack = self.stats.attack +10
        self.stats.dark_points = self.stats.dark_points - 15
        self.Saffron =(100, 100)
      if (self.x_position, self.y_position) == self.Ashardon:
        self.story.Ashardon()
        self.stats.defense = self.stats.defense + 15
        self.stats.attack = self.stats.attack +15
        self.stats.dark_magic = self.stats.dark_magic + 30
        self.stats.dark_points = self.stats.dark_points + 30
        self.Ashardon = (100, 100)
      if (self.x_position, self.y_position) ==    self.Temple_of_light:
        self.story.Temple_of_light()
        self.stats.light_magic = self.stats.light_magic + 30
        self.stats.defense = self.stats.defense + 15
        self.stats.light_points = self.stats.light_points + 50
        self.Temple_of_light = (100, 100)
      

  def move(self, user_input):
      available = self.available_directions()
      speed = random.randint(1, self.stats.speed)
      if "N" in user_input and "N" in available:
        self.y_position = self.y_position +  speed
      if "S" in user_input and "S" in available:
        self.y_position = self.y_position - speed
      if "E" in user_input and "E" in available:
        self.x_position = self.x_position + speed
      if "W" in user_input and "W" in available:
        self.x_position = self.x_position - speed
