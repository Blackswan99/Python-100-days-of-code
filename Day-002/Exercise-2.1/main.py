# Don't change the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

####################################
#Write your code below this line

digit1_string = two_digit_number[0]
digit2_string = two_digit_number[1]

digit1 = int(digit1_string)
digit2 = int(digit2_string)

result = digit1 + digit2
result_string = str(result)

print(result_string)
