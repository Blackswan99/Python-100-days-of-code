MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def order():
    
    while ordered_item != "espresso" or ordered_item != "latte" or ordered_item != "cappuccino":
        ordered_item = input("What would you like? (espresso/latte/cappuccino): ").lower()

def check_resources():
    print()

def payment():
    print("Please insert coins.")
    
#take order
order()
#process coins
payment()
#check resources
check_resources()
