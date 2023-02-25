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
    "money": 0.0
}


def order():
    ordered_item = ""
    while (ordered_item != "espresso") and (ordered_item != "latte") \
            and (ordered_item != "cappuccino") and (ordered_item != "off") and (ordered_item != "report"):
        ordered_item = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return ordered_item


def check_resources(chosen_item):
    if MENU[chosen_item]["ingredients"]["water"] < resources["water"]:
        print("Sorry there is not enough water.")
        can_offer = False
    elif MENU[chosen_item]["ingredients"]["milk"] < resources["milk"]:
        print("Sorry there is not enough milk.")
        can_offer = False
    elif MENU[chosen_item]["ingredients"]["coffee"] < resources["coffee"]:
        print("Sorry there is not enough coffee.")
        can_offer = False
    else:
        can_offer = True
    return can_offer
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.


def payment():
    print()


def print_report():
    print("Report:")
    for i in resources:
        if i == "money":
            print(f"{i.title()}: ${resources[i]}")
        else:
            print(f"{i.title()}: {resources[i]} ml")


def provide_change():
    print()


def provide_coffee():
    print()


item = ""
while item != "off":
    # take order
    item = order()
    if item == "report":
        print_report()
    elif item != "off" or item != "report":
        # check resources
        if check_resources(item):
            # process coins
            payment()
            # provide coffee
            provide_coffee()
            # provide change
            provide_change()
        
print("Goodbye.")
