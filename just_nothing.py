import tkinter
from tkinter import*

root = Tk()
root.geometry('250x250+50+50')
root.title('Just Nothing')
'''
l = Label(root, relief = 'raised', width = 10, height = 5, bd = 4, anchor = E , text = ' ')
l.pack()

def call1(val):
    l.configure(text = val)

scrollb = Scale(root, orient = 'vertical' , bg= 'light blue' , activebackground = 'yellow', from_= 0, to = 10, tickinterval = 0.5, sliderlength = 2, command=call1)
scrollb.pack()
'''

sb = Scrollbar(root)
sb.pack(side= 'right' , fill= Y)

l = Listbox(root, yscrollcommand = sb.get)
l.insert(0, 'python', 'java', 'html')
l.pack(side='left', fill=BOTH)
sb.configure(command= l.yview)
