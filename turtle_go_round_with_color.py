from turtle import *
import turtle
def fan(radius):
    color_circle = input('What\'s your favourite color: ')
    
    begin_fill()
    fillcolor(color_circle)
    speed(100)
    width(3)
    color('blue', color_circle)
    circle(radius/2., 360)
    left(90)
    forward(100)
    end_fill()
    #right(90)

def trace(length1, count, angle):
    while(count<=12):
        shapesize(12,15,3)
        begin_fill()
        fillcolor('yellow')
        up()
        forward(length1)
        forward(-length1)
        down()
        angle_counter = 0
        angle =  angle_counter + 30
        left(angle)
        count = 0
        col = input('Choose another color: ')
        color(col)
        counter = 1
        count += counter
        
        write('Sam Programmer' ,move=False)
        
        back(20)
        end_fill()
        #line += count
        #if (counter == 0):
            #break


def main():
    reset()
    fan(200)
    trace(100, 12, 360)

    while(trace == True):
        break
    
    return 'Am here!'

if __name__ == '__main__':
    main()
    mainloop()
