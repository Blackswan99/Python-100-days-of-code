# Don't change the code below
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# Don't change the code above

#Write your code below this line
lower_name1 = name1.lower()
lower_name2 = name2.lower()
score_true_name1 = 0
score_true_name2 = 0
score_love_name1 = 0
score_love_name2 = 0

score_true_name1 += lower_name1.count('t')
score_true_name1 += lower_name1.count('r')
score_true_name1 += lower_name1.count('u')
score_true_name1 += lower_name1.count('e')

score_love_name1 += lower_name1.count('l')
score_love_name1 += lower_name1.count('o')
score_love_name1 += lower_name1.count('v')
score_love_name1 += lower_name1.count('e')

score_true_name2 += lower_name2.count('t')
score_true_name2 += lower_name2.count('r')
score_true_name2 += lower_name2.count('u')
score_true_name2 += lower_name2.count('e')

score_love_name2 += lower_name2.count('l')
score_love_name2 += lower_name2.count('o')
score_love_name2 += lower_name2.count('v')
score_love_name2 += lower_name2.count('e')

score_true = score_true_name1+score_true_name2
score_love = score_love_name1+score_love_name2

score_as_int = score_true * 10 + score_love

if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score_as_int}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50:
    print(f"Your score is {score_as_int}, you are alright together.")
else:
    print(f"Your score is {score_as_int}.")
