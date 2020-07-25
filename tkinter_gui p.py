import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
title = tk.title('ECHAT')
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

label1 = tkinter.Label(frame, text='Welcome to Echat',bg='teal')
label1.pack(side=TOP)#.grid(column=0,row=1,pady=4,bg='blue')
frame2 = tkinter.Frame(tk, relief=RIDGE, borderwidth=1)
frame2.pack(fill=BOTH,expand=10)
label2 = tkinter.Label(frame2, text='Fill the form to signup',bg='teal')
label2.grid(column=1,row=3)

label3 = tkinter.Label(frame2, text='First Name:')
label3.grid(column=1,row=4)
fname = tkinter.Entry(frame2)
fname.grid(column=2,row=4)

label4 = tkinter.Label(frame2, text='Last Name:')
label4.grid(column=1,row=6)
lname = tkinter.Entry(frame2)
lname.grid(column=2,row=6)

label5 = tkinter.Label(frame2, text='Username:')
label5.grid(column=1,row=8)
uname = tkinter.Entry(frame2)
uname.grid(column=2,row=8)

label6 = tkinter.Label(frame2, text='Password:')
label6.grid(column=1,row=10)
pword = tkinter.Entry(frame2,state=NORMAL)
pword.grid(column=2,row=10)

submit = tkinter.Button(frame2, text='SIGNUP', bg='teal',command=tk.destroy)
submit.grid(padx=5,pady=3, column=1,row=18)

label9 = tkinter.Label(frame2, text='Male ')
label9.grid(column=1,row=14)
male = tkinter.Radiobutton(frame2, value=1)
male.grid(column=2,row=14)

label10 = tkinter.Label(frame2, text='Female ')
label10.grid(column=1,row=16)
female = tkinter.Radiobutton(frame2, value=2)
female.grid(column=2,row=16)

label7 = tkinter.Label(frame, text='Username: ')
label7.pack()#grid(column=4,row=2)
login_uname = tkinter.Entry(frame)
login_uname.pack()#grid(column=5,row=2)

label8 = tkinter.Label(frame, text='Password: ')
label8.pack()#grid(column=6,row=2)
login_pass = tkinter.Entry(frame)
login_pass.pack()#grid(column=7,row=2)

login = tkinter.Button(frame, text='LOGIN', bg='teal',command=tk.destroy)
login.pack()#grid(column=4,row=3)
tkinter.image_types()
tkinter.Image(frame, imgtype=JPG, name='sam.jpg')

tk.mainloop()


