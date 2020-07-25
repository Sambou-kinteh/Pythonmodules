import tkinter
from tkinter.constants import*

tk = tkinter.Tk()

frame  = tkinter.Frame(tk, relief = GROOVE, borderwidth = 3)
frame.pack()

photo = tkinter.PhotoImage(file ='C:/Users/Sambou/Desktop/PERSONAL WORK/PYTHON PL/image.py')
image = tkinter.Image(frame, image=photo)
image.pack()

tk.mainloop()

