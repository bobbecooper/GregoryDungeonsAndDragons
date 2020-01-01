import random

from Combat import Combat

class GameStats():

  def __init__(self, health, attack):
    self.health = health # human is 10
    self.attack = attack # human is 5
      
  def do_combat(self, human_stats):
    human_stats.print_stats()
    self.print_stats()
    self.combat_event = Combat(human_stats, self)
    userinput = self.combat_event.getcombatinput()
    (combat_ended, game_ended) = self.combat_event.updatecombatsituation(userinput)
    return (combat_ended, game_ended)

  def enemy_attack(self, human_stats):
    attack_strength = random.randint(0, self.attack)
    print(f"You are being attacked by {self.enemy_type} with damage {attack_strength}")
    human_stats.be_attacked(attack_strength)
  
  def defend(self, human_stats):
    if human_stats.defense > 0:
      self.do_attack(human_stats)
      human_stats.defense = human_stats.defense - 1
      return True
    else:
      print("You're out of defenses!")
      return False
    
  def do_attack(self, human_stats):
    attack_strength = random.randint(0, human_stats.attack)
    print(f"You attack the {self.enemy_type} with damage {attack_strength}")
    self.be_attacked(attack_strength)

  def spell(self, human_stats):
    miss_chance = random.randint(1,4)
    if miss_chance== 1:
      print ("You missed!")
      return
    attack_strength = random.randint(1, human_stats.magic)
    self.be_attacked(attack_strength)

  def do_dark_magic(self, human_stats):
      attack_strength = random.randint (1, human_stats.dark_points)
      self.be_attacked(attack_strength)
      
  def dead(self):
    return self.health <= 0

  def be_attacked(self, attack_strength):
    self.health = self.health - attack_strength

  def light_spell(self, human_stats):
    attack_strength = random.randint(1, human_stats.light_magic)
    self.be_attacked(attack_strength)