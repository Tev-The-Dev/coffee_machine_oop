# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("aquamarine1")
# timmy.forward(100)
# print(timmy)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasoar"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])
table.align = "l"
print(table.align)

print(table)