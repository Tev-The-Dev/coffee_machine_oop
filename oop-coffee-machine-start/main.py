from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

making_coffee = True
while making_coffee:
    print (f"What would you like? {menu.get_items()}: ")
    choice = str(input())
    if choice == "off":
        in_maintenance_mode = True
        print("Entering maintenance mode")
        while in_maintenance_mode:
            maintain = str(input("What would you like to do?"))
            if maintain == "report":
                coffee_maker.report()
                money_machine.report()
            #TODO: Optional - Add a refill functionality to allow the maintenance team to refill resources
            else:
                print("Going back to regular usage")
                in_maintenance_mode = False
    elif choice in menu.get_items():
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    else:
        print("Thank you for making coffee with us!")
        making_coffee = False