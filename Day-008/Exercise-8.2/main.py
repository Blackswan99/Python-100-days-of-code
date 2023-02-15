#Write your code below this line
def prime_checker(number):
    prime = True
    if number == 1:
        print("It's a prime number.")
    else:
        for num in range(1,number+1):
            if number % num == 0 and num != 1 and num != number:
                prime = False
                print(f"Number is dividable by {num}.")
        if prime == True:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
