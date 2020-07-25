from turtle import*
import turtle
#screen = turtle
speed(50)
def tree():
    begin_fill()
    fillcolor('red')
    turtle.setworldcoordinates(-10,-0.5,50,1.5)
    right(45)
    for _ in range(8):
        left(90)
        forward(0.5)
    end_fill()
    return tree



tree()
up()
left(45)
forward(5)
fd(5)
down()

tree()
up()
left(45)
fd(5)
down()

tree()
up()
left(45)
fd(5)
down()

tree()
up()
left(45)
fd(5)
down()

tree()
up()
left(45)
fd(5)
down()

tree()
up()
left(45)
fd(5)
down()

tree()
left(90)
tree()
left(30)
tree()
left(30)
tree()
left(30)
