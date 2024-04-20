# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"






print(table)

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Console", ["Steam Deck", "Aya Neo", "Onex Player", "Nintendo Switch"])
table.add_column("Price", ["$600", "$700", "$1000", "$400"])
table.add_column("Ranking", ["Mid Range", "Expensive", "Expensive", "Budget Range"])
table.align = "l"

print(table)