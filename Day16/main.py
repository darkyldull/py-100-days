from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_machine =  CoffeeMaker()
coffee_money = MoneyMachine()

user_order = False

while not user_order:
    print(f"The menu is {coffee_menu.get_items()}")
    user_input = input("What would you like? ")
    if not coffee_menu.find_drink(user_input) and user_input != "report":
        continue
    else:
        order = coffee_menu.find_drink(user_input)
    if user_input == "report":
        coffee_machine.report()
        continue
    if not coffee_machine.is_resource_sufficient(order):
        continue
    print(f"The cost is {order.cost}")
    if not coffee_money.make_payment(order.cost):
        continue
    coffee_machine.make_coffee(order)
    print("Enjoy")
