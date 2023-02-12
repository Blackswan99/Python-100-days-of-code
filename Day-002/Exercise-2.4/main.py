#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill_as_float = float(input("What was the total bill? $"))
tip_as_int = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_as_int = int(input("How many people to split the bill? "))

splitted_bill_as_float = round((total_bill_as_float / people_as_int) * (tip_as_int / 100 + 1), 2)

print(f"Each person should pay: ${splitted_bill_as_float}")
