from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()



options = menu.get_items()

is_on = True

while is_on :
    order = input(f"What wuold you like to drink ? {options} :").lower()
    if order == 'off' :
        is_on = False
    elif order == 'report' :
        maker.report()
        money.report()
    else :
        drink = menu.find_drink(order)
        if drink is not None and maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            maker.make_coffee(drink)


