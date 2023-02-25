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
        ordered_item = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    return ordered_item


def check_resources(chosen_item):
    can_offer = True
    if MENU[chosen_item]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water.")
        can_offer = False
    if chosen_item != "espresso":
        if MENU[chosen_item]["ingredients"]["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            can_offer = False
    if MENU[chosen_item]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        can_offer = False
    return can_offer


def payment(chosen_item):
    print("Please insert coins.")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))

    amount_of_money = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if MENU[chosen_item]["cost"] < amount_of_money:
        resources["money"] += MENU[chosen_item]["cost"]
        money_returned = amount_of_money - MENU[chosen_item]["cost"]
        print(f"Here is ${money_returned} in change.")
        print(f"Here is your {chosen_item.title()} ☕️.Enjoy!")
        return money_returned
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return -1


def print_report():
    print("Report:")
    for i in resources:
        if i == "money":
            print(f"{i.title()}: ${resources[i]}")
        else:
            print(f"{i.title()}: {resources[i]} ml")


def provide_coffee(chosen_item):
    resources["water"] -= MENU[chosen_item]["ingredients"]["water"]
    if chosen_item != "espresso":
        resources["milk"] -= MENU[chosen_item]["ingredients"]["milk"]
    resources["coffee"] -= MENU[chosen_item]["ingredients"]["coffee"]


item = ""
while item != "off":
    # take order
    item = order()
    if item == "report":
        print_report()
    elif item != "off" and item != "report":
        # check resources
        if check_resources(item):
            # process coins
            if payment(item) >= 0:
                # provide coffee
                provide_coffee(item)

print("Goodbye.")
