def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def division(num1,num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Division by zero is not allowed.")

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the lines above: ")
function = operations[operation_symbol]
result = function(num1,num2) 
print(f"{num1} {operation_symbol} {num2} = {result}")
