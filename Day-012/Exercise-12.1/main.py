#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import os

logo = '''
 ▄▄ • ▄• ▄▌▄▄▄ ..▄▄ · .▄▄ ·     ▄▄▄▄▄ ▄ .▄▄▄▄ .     ▐ ▄ ▄• ▄▌• ▌ ▄ ·. ▄▄▄▄· ▄▄▄ .▄▄▄  
▐█ ▀ ▪█▪██▌▀▄.▀·▐█ ▀. ▐█ ▀.     •██  ██▪▐█▀▄.▀·    •█▌▐██▪██▌·██ ▐███▪▐█ ▀█▪▀▄.▀·▀▄ █·
▄█ ▀█▄█▌▐█▌▐▀▀▪▄▄▀▀▀█▄▄▀▀▀█▄     ▐█.▪██▀▐█▐▀▀▪▄    ▐█▐▐▌█▌▐█▌▐█ ▌▐▌▐█·▐█▀▀█▄▐▀▀▪▄▐▀▀▄ 
▐█▄▪▐█▐█▄█▌▐█▄▄▌▐█▄▪▐█▐█▄▪▐█     ▐█▌·██▌▐▀▐█▄▄▌    ██▐█▌▐█▄█▌██ ██▌▐█▌██▄▪▐█▐█▄▄▌▐█•█▌
·▀▀▀▀  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀▀      ▀▀▀ ▀▀▀ · ▀▀▀     ▀▀ █▪ ▀▀▀ ▀▀  █▪▀▀▀·▀▀▀▀  ▀▀▀ .▀  ▀'''

print(logo)
chose = input("Do you want to [e]nter a guess or have a [r]andom one?(e/r) ")
if chose.lower() == "r":
    number_to_guess = random.randint(1,100)
else:
    number_to_guess = int(input("Please enter a number to guess: "))

os.system('clear')

print(logo)
print("Welcome to the number guessing game!")
print("You have to guess a number between 1 and 100.")
