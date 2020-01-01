class Combat():

  def __init__(self, human_stats, enemy_stats):
    self.human_stats = human_stats
    self.enemy_stats = enemy_stats
    self.is_defended = False

  def getcombatinput(self):
    user_input = ""
    while user_input not in ["Attack", "Defend", "Spell"]:
      print("Attack,Defend,Spell?") #type these
      user_input = str(input())
    if user_input == "Spell":
      if self.human_stats.dark_magic >0:
        dark_or_light_input = ""
        while dark_or_light_input not in ["Dark", "Light"]:
          print ("Dark or Light?")
          dark_or_light_input = str(input())
        user_input = user_input + dark_or_light_input
    return user_input

  def updatecombatsituation(self, userinput):
    if "Attack" in userinput:
        self.enemy_stats.do_attack(self.human_stats)
    elif "Defend" in userinput:
        self.enemy_stats.defend(self.human_stats)
        self.is_defended = True
    elif "Spell Dark" in userinput:
          self.human_stats.dark_magic = self.human_stats.dark_magic -2
          self.human_stats.dark_points = self.human_stats.dark_points + 1
          self.enemy_stats.do_dark_magic(self.human_stats)
    elif "Spell Light" in userinput:
          self.human_stats.dark_points = self.human_stats.dark_points - 1
          self.human_stats.light_magic - 2
          self.human_stats.light_points + 2
          self.enemy_stats.light_spell(self.human_stats)
    elif "Spell" in userinput:
          self.human_stats.dark_points = self.human_stats.dark_points - 1
          self.human_stats.light_magic - 2
          self.human_stats.light_points + 2
          self.enemy_stats.light_spell(self.human_stats)

    if not self.is_defended:
      self.enemy_stats.enemy_attack(self.human_stats)
    self.is_defended = False
    if self.enemy_stats.dead():
      print(f"Yay! You killed the {self.enemy_stats.enemy_type}!")
      return (True, False) # end battle, don't end game
    elif self.human_stats.dead():
      print(f"Oops, you were killed by the {self.enemy_stats.enemy_type}")
      return (True, True) # end battle, end game
    else:
      return (False, False) # don't end battle, don't end game
