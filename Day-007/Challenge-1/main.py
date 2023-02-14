import random
#Step 1 
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
rnd_idx = random.randint(0,2)
chosen_word = word_list[rnd_idx]
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = (input("Guess a letter: ")).lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for c in chosen_word:
    if c == guess:
        print("Right")
    else:
        print("Wrong")
