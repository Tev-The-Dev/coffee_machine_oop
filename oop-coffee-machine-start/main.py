from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

making_coffee = True

menu = Menu()

while making_coffee:
    print (f"What would you like? {menu.get_items()}: ")
    choice = str(input())
    if choice not in menu.get_items():
        making_coffee = False

