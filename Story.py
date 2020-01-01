class Story():

  def __init__(self, human_stats):
    self.human_stats = human_stats

  def print_intro(self):
    print ("Welcome to D&D. You are going on a adventure to find a mystical gem hidden in the depths of a abandoned mine shaft. Good luck.")
    print ("You are currently at the center of Mombassa, which is the center of the computer map.")
    print("You can move 1 in every direction apart from diagonal.")

  def mystical_serum(self):
    print("You travel to the outskirts and find a mystic serum.You drink it and feel tankier.")

  def magic_trident(self):
    print("You end up going for a swim in the ocean and find at the floor a magic trident.")

  def mystical_sword(self):
    print("You find a abandoned shop with a mystical gem,sadly this is not the win gem but you make a mystical sword out of it")
  
  def diamond_armor(self):
    print("You managed to buy diamond armor from the shopkeeper")

  def iron_boots(self):
    print("You found iron boots on the ground!")

  def Suknana(self):
    print('You arrive in Suknana,a major city of this reigon.You are gifted magic armor,gold sword and a dark staff by a "dark lord"')

  def ruby_armor(self):
    print("You arrive in a village.You are gifted ruby armor by a rich man.")

  def win(self):
    print("You won! You found the gem!")
    print("You would later make this gem into amazing things and sell/keep them")
    print ("Sell or Keep?")
    userinput = str(input())
    if userinput== "Keep":
      print ("You keep the stuff and go on to face many more lands and defeat many more foes.")
      print("How would you end up?")
      userinput = str(input())
      if userinput == "Hero":
        print("What is your hero name")
        userinput = str(input())
        if userinput == "Luke Skywalker":
          print("bum bumbum bum")
    if userinput== "Sell":
      print ("You go on to become rich off the gem stuff and become well respected in society.")
      print ("How would you use the money")
      print("Make a worldwide banking system or become a 1% of population")
      userinput = str(input())
      if userinput == "Banking System":
        print("What is your bank called")
        userinput = str(input())
        if userinput == "American Express":
          print("Hey! You found a easter egg!")
  


  def dark_win(self):
    if self.human_stats.dark_points >0:
      print("You got the dark ending!")
      print("You end up meeting up with the 'dark lord' back in Suknana.You learn darkness from him and kill him and become more powerful in dark magic")
      print("What would you do:Destroy the Cities of Harmony(Capital of Swarelia and major cities) or Become ruler of the nation and rename the Cities of Harmony to Cities of Darkness")
      userinput = str(input())
      if userinput == "Destroy the cities":
        print("You destory the Cities and create your lair over the wreakage.")
      if userinput == "Become Ruler":
        print("You become ruler and rename the cities. You are the ultimate ruler and the people are your slaves")

  def Saffron(self):
    print("You arrive in Saffron, a major city of Swarelia.Its a famous holy city filled with churches.You are given holy armor and a holy sword")

  def Ashardon(self):
    print("You arrive in Ashardon, a Dark city.It's controlled by a dark lord who trains apprentice's.You become a dark master, 1 below lord.")

  def Temple_of_light(self):
    print("You arrive to a Temple of harmony.The populus take you in and you become great at light magic.")
  
  def light_win(self):
    if self.human_stats.light_points >0:
      print("You got the light ending!")
      print("You become a master of light magic and are invited to take the current king's place when he die's")
      print("Do you take the offer or become a amazing light master healer")
      userinput = str(input())
      if userinput == "Accept the offer":
        print("You take the king's place and become a kind and harmonic leader.")
      if userinput == "Reject the offer":
        ("You reject the offer,displeasing the populus.You become the country docter though.")