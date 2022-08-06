print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n").lower()

if left_right == "left":
  swim_wait = input("'You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.'\n").lower()
  if swim_wait == "wait":
    print("Sadly, a boat never came and you ran out of energy to wait. GG.")
  else:
    which_door = input("\"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\"\n").lower()
    if which_door == "red":
      print("You walk into a large room of hungry lions as the door locks behind you... Looks like you won't be needing treasure anytime soon. GG")
    elif which_door == "yellow":
      print("As soon as you walk in your feet can't touch the ground, there's a large hole and you fall into what seems like a bottomless pit... except it does have a bottom. GG")
    else:
      treasure = input("You made it to the treasure! Open the chest? Y or N?\n")
      if treasure == "Y":
        print("The treasure was actually a mimic and gobbles you up before you have time to react, game over. \nThank you for playing!")
      else:
        print("After coming this far, for some reason you choose not to open the treasure and go on with your life... you win?\nThank you for playing!")
else:
  print("You end up getting hit by a car... Next time watch where you're going. GG")