import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
---.__(___)
'''
#Write your code below this line
choose_player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
choose_computer = random.randint(0,2)

if choose_player == 0:
    print(rock)
    print("Computer chose:\n")
    if choose_computer == 0:
        print(rock)
        print("\nDraw.")
    elif choose_computer == 1:
        print(paper)
        print("\nYou lose.")
    else:
        print(scissors)
        print("\nYou win.")       
elif choose_player == 1:
    print(paper)
    print("Computer chose:\n")
    if choose_computer == 0:
        print(rock)
        print("\nYou win.")
    elif choose_computer == 1:
        print(paper)
        print("\nDraw.")
    else:
        print(scissors)
        print("\nYou lose.")  
elif choose_player == 2:
    print(scissors)
    print("Computer chose:\n")
    if choose_computer == 0:
        print(rock)
        print("\nYou lose.")
    elif choose_computer == 1:
        print(paper)
        print("\nYou win.")
    else:
        print(scissors)
        print("\nDraw.") 
else:
    print("Wrong input.")
