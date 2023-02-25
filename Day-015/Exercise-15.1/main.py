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
    ordered_item = ""
    while (ordered_item != "espresso") and (ordered_item != "latte") \
            and (ordered_item != "cappuccino") and (ordered_item != "off"):
        ordered_item = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return ordered_item


def check_resources():
    print()


def payment():
    print("Please insert coins.")


item = ""
while item != "off":
    # take order
    item = order()
    if item != "off":
        # process coins
        payment()
        # check resources
        check_resources()

print("Goodbye.")
