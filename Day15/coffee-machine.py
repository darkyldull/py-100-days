MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money" : 0.0,
}

value_coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}


def check_resources(user_report):
    if int(resources["coffee"]) < int(MENU[user_report]["ingredients"]["coffee"]) or int(resources["milk"]) < int(MENU[user_report]["ingredients"]["milk"]) or int(resources["water"]) < int(MENU[user_report]["ingredients"]["water"]):
        return True
    else:
        return False

def calculate_money(q, d, n, p):
    total_cost = (q * float(value_coins["quarter"])) + (d * float(value_coins["dime"])) + (n * float(value_coins["nickel"])) + (p * float(value_coins["penny"]))
    total_cost = round(total_cost, 2)
    print(f"Total money given: {total_cost}")
    return total_cost

def check_cost(user_report, user_money):
    if MENU[user_report]["cost"] > user_money:
        print("Sorry, that's NOT enough money. Money Refunded.")
        return True
    else:
        return False


def get_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    return quarters, dimes, nickels, pennies


def update_resources(user_report):
    resources["coffee"] = int(resources["coffee"]) - int(MENU[user_report]["ingredients"]["coffee"])
    resources["milk"] = int(resources["milk"]) - int(MENU[user_report]["ingredients"]["milk"])
    resources["water"] = int(resources["water"]) - int(MENU[user_report]["ingredients"]["water"])
    resources["money"] = float(resources["money"]) + float(MENU[user_report]["cost"])

def give_change(user_report, user_money):
    if MENU[user_report]["cost"] < user_money:
        change = round(user_money - float(MENU[user_report]["cost"]), 2) 
        print(f"Here is your change, {change}!")
    else:
        print("No change!")


user_order = False
while not user_order:
    user_report = input("What would you like? (espresso/latte/cappuccino) or report to check status: ")
    if user_report == 'off':
        break
    if user_report == "report":
        print(resources)
        continue
    if user_report not in MENU:
        print("Invalid Input")
        continue    
    if check_resources(user_report):
        print("Not enough resources!")
        continue
    quarters, dimes, nickels, pennies = get_coins()
    user_money = calculate_money(quarters, dimes, nickels, pennies)

    if check_cost(user_report, user_money):
        continue

    update_resources(user_report)
    give_change(user_report, user_money)
    print(f"Enjoy your {user_report}!")


