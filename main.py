#lock system test
import time,sys,random
from AdventureGame import AdventureGame 


print("Enter the number code")
guess = int(input())
if guess==5637:
    print("Hi, what do you want to do?")
    print("Message friend,Watch Youtube,Play games?")
    choice = str(input())
if choice== "Message friend":
    print("Bobbe or Justin?")
    friend_choice = str(input())
    if friend_choice== "Bobbe":
        print("What would you like to say?")
        message = str(input())
        print("Message sent")
    if friend_choice== "Justin":
        print("What would you like to say?")
        message = str(input())
        print("Message sent")
if choice== "Watch Youtube":
    print("Preston or DanTDm or Pewdiepie?")
    yt_choice = (input())
    if yt_choice== "Preston":
        print("*fire logo music and animation plays*")
        time.sleep(2)
    if yt_choice== "Pewdiepie":
        print("*its PEWDIEPIE!*")
        time.sleep(2)
    if yt_choice== "DanTDm":
        print("Dan here!")
        time.sleep(2)
    print("Smash dat like and subscribe button for more amazing content!")
if choice== "Play games":
  print ("D&D or Nim?")
  game_choice = str(input())
  if game_choice== "Nim":
    print ("how many toothpicks would you like?")
    toothpick = int(input())
    while toothpick >0:
          print(f"You and your friend have {toothpick} toothpicks,whoever takes the last stick wins,you can take up to 3 sticks a turn, how many do you take?")
          tooth = 0
          while tooth < 1 or tooth > 3:
            tooth = int(input())
          toothpick= toothpick - tooth
          if toothpick== 0:
              print("You won!")
              sys.exit()
          ai = random.randint(1,3)
          toothpick= max(toothpick - ai,0)
          if toothpick== 0:
              print("You lost :(")
              time.sleep(2)
          print(toothpick)
#new game after line 51
if choice== "Play games":
  #stats
  if game_choice== "D&D":
    game = AdventureGame()
    game_ended = False
    while not game_ended:
     game_ended = game.take_turn()


  
























