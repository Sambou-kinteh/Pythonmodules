#creating a square of 50mm's in a for loop

import turtle

sam = turtle.Turtle()

for i in [0, 1, 2, 3]:
    sam.forward(50)
    sam.right(90)
    sam.forward(60)
    sam.left(100)
    sam.forward(60)
    sam.left(30)
