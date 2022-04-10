from turtle import Turtle, Screen
from prettytable import PrettyTable



# djoko = Turtle()
# print(djoko)
# djoko.shape("turtle")
# djoko.color("aquamarine")
# djoko.pencolor("red")
# def begin_fill():
#     while True:
#         djoko.forward(200)
#         djoko.left(250)
# begin_fill()
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Character", ["Gosho", "Peshkko", "Simo"])
table.add_column("Skills", ["Qdene", "Piene", "Mnogo piene"])
table.align = "r"

print(table)