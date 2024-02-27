# welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# display map
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

# display first choice
print("You're at a cross road. Where do you want to go? ")
choice1 = input('Type "left" or "right"\n').lower()

# check if user input was "right"
if choice1 == "right":
   # display next choice
   print("You come to a lake. There is an island in the middle of the lake. ")
   choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()

   # check if user input was "wait"
   if choice2 == "wait":
      # display next choice
      print("You arrive at the island unharmed. There is a house with 3 doors.")
      choice3 = input("One red, one yellow, and one blue. Which colour do you choose?\n").lower()
      
      # check if user input was "yellow"
      if choice3 == "yellow":
         # display win
         print("You Win!\n")

      # else, check if user input was "Blue"
      elif choice3 == "blue":
         # display game over
         print("You were eaten by beasts. Game Over.\n")

      # else, check if user input was "Red"
      elif choice3 == "red":
         # display game over
         print("You were burned by fire. Game over.\n")

      # else, game over
      else:
         print("You chose a door that doesn't exist. Game Over.\n")
      
   # else, display game over 
   else:
      print("You were attacked by a troute. Game Over.\n")


# else, display game over
else:
   print("You fell into a hole. Game Over.\n")
