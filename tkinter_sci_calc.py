import tkinter
from tkinter import*
import math
import re

#------------------FUTURE PROGRESS- LISTBOXES FOR CONVERSION TYPES AND READABLES----------------#

root = Tk()
root.geometry('1250x575+25+25')
root.title('Scientific Calculator')

root.maxsize(width = 950, height = 550)
root.minsize(width = 385, height = 600)

#--------------------------------Frames-------------------------------------#
#top
top_frame = Frame(root, relief = 'flat', bg = 'white', width = 500, height = 200)
top_frame.pack(anchor = N, side = 'top', fill = Y)

#down
down_frame = Frame(root, relief = 'flat', bg = 'light grey', width = 500, height= 250)
down_frame.pack(anchor = S, side = 'bottom', fill = Y)

#side
side_frame = Frame(root, relief = 'flat', bg = 'black', bd = 2, width = 1000, height= 2)
side_frame.pack(anchor = E, side = 'right', fill = X)

#---------------------------------------FUNCTIONALITY BLOCK-----------------------------------------#
text_pross = StringVar()
text_input = StringVar()
text_disp = StringVar()
text_appro = StringVar()
text_hold = StringVar()
operator = ""
operator1_2_3 = ""

#DISPLAY AREA
ansDisplay = Entry(top_frame,font=('serif',22,'italic'),bg = 'white', relief = 'flat', textvariable=text_input,
                   insertwidth=4, justify='left',fg='black', width = 35)
ansDisplay.grid(columnspan=4,padx=10,pady=10,column=0,row=1)


tDisplay = Entry(top_frame,font=('serif',15,'italic'),bg = 'white', relief = 'flat', textvariable=text_pross,
                   insertwidth=4, justify='left',fg='black', width = 35)
tDisplay.grid(columnspan=4,padx=10,pady=10,column=0,row=0)

#--------------------------------#----------------------------------#----------------------------------#
#2
Display = Entry(top_frame,font=('arial',12), bg = 'white', relief = 'flat', textvariable=text_disp,
                   insertwidth=3, justify='right',fg='black', width = 35)
Display.grid(columnspan=4,padx=10,pady=10, sticky = N)

#2
iDisplay = Entry(top_frame,font=('arial',10), bg = 'white', relief = 'flat', textvariable=text_appro,
                   insertwidth=3, justify='right',fg='black', width = 35)
iDisplay.grid(columnspan=4,padx=10,pady=10, sticky = S)

#If Btn Click
def btnClick(numbers):
    global operator
    global operator1_2_3

    operator = operator + str(numbers)

    operator1_2_3 += str(numbers)
    text_input.set(operator1_2_3)
    '''if Operand:
        text_pross.set(operator)
    else:
        text_pross.set('0')'''


#Clear
def clear():
    global operator1_2_3
    global operator
    operator = ""
    operator1_2_3 = ""
    text_input.set(0)
    text_disp.set('')
    text_appro.set('')
    text_pross.set('')
    text_hold.set('')

#Total
def equal():
    
    global operator
    sumup = float(eval(operator))
    text_input.set(sumup)

    text_disp.set(operator)
    
    app = float(sumup)
    operator8_1_2 = "= {0}".format(round(app, 0))
    text_appro.set(operator8_1_2)

        

#Prevous
def pre():
    global operator
    text_input.set(operator)

#Tan Func
def tan():
    global operator
    global sumup
    x = float(text_input.get())
    tan_1 = math.radians(x)
    tan = math.tan(tan_1)
    
    operator = str(tan)
    text_input.set(operator)
    operator1 = "tan({0}) = {1}".format(x, tan)
    text_disp.set(operator1)
    operator1_1 = "= {0}".format(round(tan, 2))
    text_appro.set(operator1_1)
    '''for i in tan:
        if tan_btn:
            op += "tan({0})".format(x)
            text_disp.set(op)'''
            
    
#Cos Func
def cos():
    global operator
    x = float(text_input.get())
    cos = math.cos(math.radians(x))
    operator = str(cos)
    text_input.set(operator)
    operator_1 = "cos({0}) = {1}".format(x, cos)
    text_disp.set(operator_1)
    operator2_1 = "= {0}".format(round(cos, 2))
    text_appro.set(operator2_1)

#Sin Func
def sin():
    global operator
    x = float(text_input.get())
    sin = math.sin(math.radians(x))
    operator = str(sin)
    text_input.set(operator)
    operator_3 = "sin({0}) = {1}".format(x, sin)
    text_disp.set(operator_3)
    operator3_1 = "= {0}".format(round(sin, 2))
    text_appro.set(operator3_1)

#X2 Func
def X():
    global operator
    x = float(text_input.get())
    x = int(x)
    x2 = int(x**2)
    operator = str(x2)
    text_input.set(operator)
    operator_4 = "{0}\u00b2 = {1}".format(x, x2)
    text_disp.set(operator_4)

#X2 Func
def XY():
    global operator
    x = float(text_input.get())
    x = int(x)
    x2 = int(x**3)
    operator = str(x2)
    text_input.set(operator)
    operator_5 = "{0}\u00b3 = {1}".format(x, x2)
    text_disp.set(operator_5)    

#n! Func
def n_fact():
    global operator
    x = float(text_input.get())
    x = int(x)
    x2 = math.factorial(x)
    operator = str(x2)
    text_input.set(operator)
    operator_5 = "{0}! = {1}".format(x, x2)
    text_disp.set(operator_5)

#Pi Func
def Pi():
    global operator
    x = float(text_input.get())
    x = int(x)

    pi = 22/7
    x2 = pi * x
    operator = str(x2)
    text_input.set(operator)
    operator_5 = "{0} pi = {1}".format(x, x2)
    text_disp.set(operator_5)

    operator4_1 = "= {0}".format(round(x2, 2))
    text_appro.set(operator4_1)
    if x == 0:
        pi = 22/7
        text_input.set(pi)
        operator_6 = "pi = {}".format(pi)
        text_disp.set(operator_6)

        operator6_1 = "= {0}".format(round(pi, 2))
        text_appro.set(operator6_1)
        
#Sqrt Func
def Sqrt():
    global operator
    x = float(text_input.get())
    x = int(x)

    x2 = math.sqrt(x)
    operator = str(x2)
    text_input.set(operator)

    operator_7 = "sqrt({0}) = {1}".format(x, x2)
    text_disp.set(operator_7)

    operator7_1 = "= {0}".format(round(x2, 2))
    text_appro.set(operator7_1)

#Invs Func
def Invs():
    global operator
    x = float(text_input.get())
    x = int(x)

    x2 = 1/x
    operator = str(x2)
    text_input.set(operator)

    operator_8 = "1/{0} = {1}".format(x, x2)
    text_disp.set(operator_8)

    operator8_1 = "= {0}".format(round(x2, 2))
    text_appro.set(operator8_1)

#Plus_Minus Func
def Pls_Mns():
    global operator
    x = float(text_input.get())
    x = int(x)

    x2 = -x
    operator = str(x2)
    text_input.set(operator)

    operator_9 = "negate{0} = {1}".format(x, x2)
    text_disp.set(operator_9)

#Log Func
def Log():
    global operator
    x = float(text_input.get())
    x = int(x)

    x2 = math.log10(x)
    operator = str(x2)
    text_input.set(operator)

    operator_8 = "log {0} = {1}".format(x, x2)
    text_disp.set(operator_8)

    operator8_1 = "= {0}".format(round(x2, 2))
    text_appro.set(operator8_1)
'''
#Mod Func
def Mod(modulus):
    global operator1_2_3
    global operator
    text_input == text_hold

    x = float(text_input.get())
    x = int(x)
    
    if Mod:
        operator = operator + str(modulus)
        text_pross.set(operator)
        text_input.set('0')
        operator1_2_3 = ""

    def mod(Mod):
        y = int(text_input.get())

        xy = x % y
        operator = str(xy)
        if equal:
            text_input.set(operator)

            operator_011 = "{0} Mod {1} = {2}".format(x, y, xy)
            text_disp.set(operator_011)

            operator8_1 = "= {0}".format(round(xy, 2))
            text_appro.set(operator8_1)
    mod(Mod)
'''

#Class of Menu

def MainMenu():
    frame = Frame(root, relief = 'flat', bg = 'light grey', bd = 0, height = 600, width = 250)
    frame.pack(anchor = W, side = 'top')
    
    menu = Menu(frame)
    root.config(menu = menu)
    subMenu = Menu(menu)
    Calc = menu.add_cascade(label = 'Calculator', menu = subMenu)
    

#-----------------------------------#---------------------------------------#-------------------------------#
def Operand(operand):
    global operator1_2_3
    global operator
    global numbers
    Mod = '%'

    operator = operator + str(operand)
    text_pross.set(operator)
    text_input.set(0)
    operator1_2_3 = ""
    if Operand:
        text_input.set('0') 
        if btnClick:
            text_input.set('0')
            text_pross.set(operator)

#------------------------------------------------------ICON FILE---------------------------------------------------------#

#X10 = PhotoImage(file = 'C:\\Users\\Sambou\\Desktop\\PERSONAL WORK\\PYTHON_PL\\10x.png')
#log10 = PhotoImage(file = 'C:\\Users\\Sambou\\Desktop\\PERSONAL WORK\\PYTHON_PL\\log10.png')
#pi_icon = PhotoImage(file = 'C:\\Users\\Sambou\\Desktop\\PERSONAL WORK\\PYTHON_PL\\pi.png')

    
#---------------------------------------------------------BTN's------------------------------------------------------#

#Menu Btn
#menu_btn = Button(top_frame, padx = 20, pady = 5, relief = 'flat', fg = 'black', bg = 'white',
                  #text = '_-_', command = MainMenu).grid(row = 0, column = 0)

#PREVIOUS    
Pre = Button(down_frame,padx=2,pady=2, relief = 'flat',fg='black',font=('arial',8,'italic'),text='Pre', bg='light grey',
              command=pre, activebackground = 'grey', activeforeground = 'black').grid(row=0,column=0)

#CLEAR
btnclear = Button(down_frame,padx=10,pady=10, relief = 'flat',fg='black',font=('arial',12),text='C', bg='light grey',
              command=clear , activebackground = 'grey', activeforeground = 'white').grid(row=0,column=2)
#PLUS/MINUS
pls_mns = Button(down_frame,padx=10,pady=10, relief = 'flat',fg='black',font=('arial',12),text='+-', bg='light grey',
              command=Pls_Mns, activebackground = 'grey', activeforeground = 'black').grid(row=0,column=1)

#PURE MATH FUNC
#Tan
tan_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='tan', bg='light grey',
              command=lambda:tan(), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=4)
#Cos
cos_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='cos', bg='light grey',
              command=lambda:cos(), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=4)
#Sin
sin_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='sin', bg='light grey',
             command=lambda:sin(), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=4)
#X2
X2_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='x\u00b2', bg='light grey',
              command=lambda:X(), activebackground = 'grey', activeforeground = 'black').grid(row=4,column=4)
#X3
X3_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='x\u00b3', bg='light grey',
                command=lambda:XY(), activebackground = 'grey', activeforeground = 'black').grid(row=4,column=5)
#n!
n_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='n!', bg='light grey',
              command=lambda:n_fact(), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=5)
#PI
pi_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='pi', bg='light grey',
              command=lambda:Pi(), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=5)
#op_brk
opn_brk = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='(', bg='light grey',
              command=lambda:btnClick('('), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=5)
#cls_brk
cls_brk = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text=')', bg='light grey',
              command=lambda:btnClick(')'), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=6)
#sqrt_btn
sqrt_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='sqrt', bg='light grey',
              command=lambda:Sqrt(), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=6)
#inverse_btn
ivs_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='1/x', bg='light grey',
              command=lambda:Invs(), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=6)
#log_btn
log_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='log10', bg='light grey',
              command=lambda:Log(), activebackground = 'grey', activeforeground = 'black').grid(row=4,column=6)
#mod_btn
mod_btn = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',12),text='Mod(%)', bg='light grey',
              command=lambda:Operand(' % '), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=7)


#NUMS
 
btn7 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('serif',20,'bold'),text='7', bg='light grey',
              command=lambda:btnClick(7), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=0)

btn8 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='8', bg='light grey',
              command=lambda:btnClick(8), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=1)

btn9 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='9', bg='light grey',
              command=lambda:btnClick(9), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=2)

add = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',23),text='+', bg='light grey',
              command=lambda:Operand('+'), activebackground = 'grey', activeforeground = 'black').grid(row=1,column=3)

btn4 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='4', bg='light grey',
              command=lambda:btnClick(4), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=0)

btn5 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='5', bg='light grey',
              command=lambda:btnClick(5), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=1)

btn6 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='6', bg='light grey',
              command=lambda:btnClick(6), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=2)

sub = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',24),text='-', bg='light grey',
              command=lambda:Operand('-'), activebackground = 'grey', activeforeground = 'black').grid(row=2,column=3)

btn1 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='1', bg='light grey',
              command=lambda:btnClick(1), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=0)

btn2 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='2', bg='light grey',
              command=lambda:btnClick(2), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=1)

btn3 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='3', bg='light grey',
              command=lambda:btnClick(3), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=2)

mul = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',16),text='X', bg='light grey',
              command=lambda:Operand('*'), activebackground = 'grey', activeforeground = 'black').grid(row=3,column=3)

btn0 = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',20,'bold'),text='0', bg='light grey',
              command=lambda:btnClick(0), activebackground = 'grey', activeforeground = 'black').grid(row=4,column=0)

dot = Button(down_frame,padx=20,pady=0, relief = 'flat',fg='black',font=('arial',30),text='.', bg='light grey',
              command=lambda:btnClick('.') , activebackground = 'grey', activeforeground = 'black').grid(row=4,column=1)

btnequal = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',22),text='=', bg='light grey',
      command=equal , activebackground = 'blue', activeforeground = 'white').grid(row=4,column=2)

div = Button(down_frame,padx=30,pady=10, relief = 'flat',fg='black',font=('arial',21),text='/', bg='light grey',
              command=lambda:Operand('/'), activebackground = 'grey', activeforeground = 'black').grid(row=4,column=3)
#-------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    mainloop()
    
