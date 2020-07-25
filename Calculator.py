import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter.constants import*
from tkinter import*
import math

root = Tk()
root.geometry('475x425+100+25')
root.title('Calculator')

text_input = StringVar()
operator = ""

root.iconbitmap(bitmap = 'questhead')

#----------------------------------TEXT DISPLAY------------------------------#
txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_input,
                   insertwidth=4, bg='steel blue', justify='right',fg='powder blue')
txtDisplay.grid(columnspan=4,padx=10,pady=10)

#---------------------------------Function Block------------------------------#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clear():
    global operator
    operator = ""
    text_input.set(0)

def equal():
    
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ""
    txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_input,
                   insertwidth=4, bg='steel blue', justify='left',fg='powder blue')
    txtDisplay.grid(columnspan=4,padx=10,pady=10,column=0,row=0)

def qExit():
    qExit = messagebox.askyesno('System Exit', 'Do you want to quit from Sam.tk')
    if qExit > 0:
        root.destroy()
        return    

def Quad():
    import tkinter_quadratic_eq
    if Quad:
        root.destroy()
        return
#-------------------------------------Buttons----------------------------#    
 
btn7 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='7',bg='powder blue',
              command=lambda:btnClick(7), activebackground = 'aqua', activeforeground = 'orange').grid(row=1,column=0)

btn8 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='8',bg='powder blue',
              command=lambda:btnClick(8), activebackground = 'aqua', activeforeground = 'orange').grid(row=1,column=1)

btn9 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='9',bg='powder blue',
              command=lambda:btnClick(9), activebackground = 'aqua', activeforeground = 'orange').grid(row=1,column=2)

add = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='+',bg='powder blue',
              command=lambda:btnClick('+'), activebackground = 'orange', activeforeground = 'aqua').grid(row=1,column=3)

btn4 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='4',bg='powder blue',
              command=lambda:btnClick(4), activebackground = 'aqua', activeforeground = 'orange').grid(row=2,column=0)

btn5 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='5',bg='powder blue',
              command=lambda:btnClick(5), activebackground = 'aqua', activeforeground = 'orange').grid(row=2,column=1)

btn6 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='6',bg='powder blue',
              command=lambda:btnClick(6), activebackground = 'aqua', activeforeground = 'orange').grid(row=2,column=2)

sub = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='-',bg='powder blue',
              command=lambda:btnClick('-'), activebackground = 'orange', activeforeground = 'aqua').grid(row=2,column=3)

btn1 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='1',bg='powder blue',
              command=lambda:btnClick(1), activebackground = 'aqua', activeforeground = 'orange').grid(row=3,column=0)

btn2 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='2',bg='powder blue',
              command=lambda:btnClick(2), activebackground = 'aqua', activeforeground = 'orange').grid(row=3,column=1)

btn3 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='3',bg='powder blue',
              command=lambda:btnClick(3), activebackground = 'aqua', activeforeground = 'orange').grid(row=3,column=2)

mul = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='*',bg='powder blue',
              command=lambda:btnClick('*'), activebackground = 'orange', activeforeground = 'aqua').grid(row=3,column=3)

btn0 = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='0',bg='powder blue',
              command=lambda:btnClick(0), activebackground = 'aqua', activeforeground = 'orange').grid(row=4,column=0)

btnclear = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='C',bg='powder blue',
              command=clear , activebackground = 'red', activeforeground = 'orange').grid(row=4,column=1)

btnequal = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='=',bg='powder blue',
      command=equal , activebackground = 'white', activeforeground = 'orange').grid(row=4,column=2)

div = Button(root,padx=8,pady=8,bd=4,fg='black',font=('arial',15,'bold'),text='/',bg='powder blue',
              command=lambda:btnClick('/'), activebackground = 'orange', activeforeground = 'aqua').grid(row=4,column=3)

quad = Button(root,padx=3,pady=3,bd=0,fg='red',font=('arial',13,'italic'),text='Go To Quadratic',bg='teal',
              command=Quad, activebackground = 'aqua', activeforeground = 'orange').grid(row=8,column=4)

Exit = Button(root,padx=3,pady=2,bd=0,fg='teal',font=('arial',13,'italic'),text='Exit',bg='red',
              command=qExit, activebackground = 'aqua', activeforeground = 'orange').grid(row=9,column=4)
#-----------------------------------------------------------------------------#

if __name__ == 'main':
    mainloop()
              
