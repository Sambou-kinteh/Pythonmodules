from turtle import *

class Car:
    'class of moving cars'

    def __init__(self, wheels, body, speed):
        self.wheels = Wheels
        self.body = Body
        self.speed = Speed
        self.windscreen = WindScreen




def Wheels(radius, radius2, plate_color, tyre_color):
    begin_fill()
    fillcolor(tyre_color)
    width(2)
    circle(radius)
    end_fill()
    up()
    left(90)
    fd(radius)
    down()
    begin_fill()
    fillcolor(plate_color)
    circle(radius2)
    end_fill()


def Door(door_color, door_length, door_height):
    begin_fill()
    fillcolor(door_color)
    left(90)
    fd(door_height)
    left(90)
    fd(door_length)  # (radius*2) + 10)
    left(90)
    fd(12)

    fd(20)
    left(90)
    left(90)
    end_fill()
    # handle


def Door_two(door_color, door_length, door_height):
    begin_fill()
    fillcolor(door_color)
    left(90)
    # handle
    fd(30)

    right(90)
    fd(door_length)
    right(90)
    fd(door_height)
    right(180)
    circle(10, 180)
    end_fill()


def Body(body_color):
    shape('turtle')
    width(2)
    forward(75)
    right(45)
    forward(40)
    begin_fill()
    fillcolor(body_color)
    forward(-40)
    right(-45)
    forward(-75)
    right(135)
    fd(30)
    right(45)
    fd(50)
    left(90)
    fd(30)
    left(90)
    fd(50)
    fd(30)
    # first door
    end_fill()
    Door('red', 30, 30)  # (door_color, door_length, door_height, handle_color)
    left(180)
    Wheels(10, 5, 'orange', 'black')  # (radius, radius2, plate_color)
    fd(10)
    begin_fill()
    fillcolor(body_color)
    fd(50)
    Door_two('red', 30, 30)  # (door_color, door_length, door_height, handle_color)
    # right(100)
    Wheels(10, 5, 'orange', 'black')  # (radius, radius2, plate_color)
    fd(25)
    right(90)
    left(90)
    fd(10)
    left(90)
    fd(30)
    end_fill()


class Ferrari(Car):
    '''func1 = Wheels(10, 5, 'orange', 'black')
    func2 = Body('brown')
    ferrari = Car(func2, func1)'''
    Body('orange')
    color('teal')
    write('Ferrari      ', move=True)
    '''Speed = 2
    Door('red', 30, 30, 'green')
    Wheels(10, 5, 'orange', 'black')    
    Door_two('red', 30, 30, 'green')
    Wheels(10, 5, 'orange', 'black')'''


clear()



class Nissan(Car):
    right(90)
    Body('teal')
    color('teal')
    write('Nissan      ', move=True)
    '''Door('green', 30, 30)
    Wheels(10, 5, 'black', 'orange')    
    Door_two('green', 30, 30)
    Wheels(10, 5, 'black', 'orange')'''


if __name__ == '__Ferrari__':
    Ferrari()
    mainloop()
