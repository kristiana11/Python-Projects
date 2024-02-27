import random

# rock (0)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# paper (1)
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# scissors (2)
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# game images
game_images = [rock, paper, scissors]

# get user input
choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# display uer choice
print(game_images[choice])

# generate random choice
computer_choice = random.randint(0,2)

# display computer choice
print("Computer chose:")
print(game_images[computer_choice])

# check who wins
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!") 
elif choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and choice == 2:
  print("You lose")
elif computer_choice > choice:
  print("You lose")
elif choice > computer_choice:
  print("You win!")
elif computer_choice == choice:
  print("It's a draw")
