import tkinter, math
from tkinter import*
from tkinter import messagebox

#-------------------------------------Scientific Calculator------------------------------------#
root = Tk()
root.geometry('323x375+100+25')
root.title('Calculator')
root.minsize(width = 323, height = 350)
root.maxsize(width = 323, height = 375)

text_input = StringVar()
operator = ""

#-----------------------------------------Functionality Block-----------------------------------------------------#

#FUNC FOR BRINGING Quad
def Go_To_Quad():
    import tkinter_quadratic_eq
    if Go_To_Quad:
        root.destroy()
        return

#FUNC FOR EXITING THE PROGRAM    
def Q_exit():
    qExit = messagebox.askyesno('Exiting Calculator', 'Do you want to quit from Sam.tk')
    if qExit > 0:
        root.destroy()
        return

#FUNC FOR BRINGING BIO
def Go_To_Bio():
    import tkinter_f_math_bionomial
    if Go_To_Bio:
        root.destroy()
        return
    
#FUNC FOR BRINGING AUTO
def Go_To_Auto():
    import Calculator_part_two2
    if Go_To_Auto:
        root.destroy()
        return

#FUNC FOR BRINGING HERON
def Go_To_Hrn():
    import tkinter_f_math_herons
    if Go_To_Hrn:
        root.destroy()
        return    

#FUNC FOR BRINGING SCIENTIFIC CALCULATOR
def Go_To_Sci():
    import tkinter_ai_calc
    if Go_To_Sci:
        root.destroy()
        return

#FUNC FOR BRINGING THE MATRICE
def Go_To_Mat():
    import tkinter_matrice
    if Go_To_Mat:
        root.destroy()
        return     

#setting an icon for our Tk()
root.iconbitmap(bitmap = 'questhead')

#CREATING A DROP DOWN FUNCTIONALITY
My_Menu = Menu(root)
root.config(menu = My_Menu)
#sub_menu 1
S_Menu = Menu(My_Menu)
My_Menu.add_cascade(label = 'Other Functions', menu = S_Menu)

ss_menu = Menu(S_Menu)
S_Menu.add_cascade(label = 'Further Math Functions', menu = ss_menu)
qua = ss_menu.add_command(label = 'Quadratic Equation      ax\u00b2+bx+c', command = Go_To_Quad)
bio = ss_menu.add_command(label = 'Bionomial Theorem       (a+n)\u00b11', command = Go_To_Bio)
Heron = ss_menu.add_command(label = 'Area(Heron\'s Formula   A(x1,y1), B(x2,y2), C(x3,y3))', command = Go_To_Hrn)
mat = ss_menu.add_command(label = 'Matrice(3x3) Solver   ', command = Go_To_Mat)

S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...', command = Q_exit)

#sub_menu2
sub2 = Menu(My_Menu)
My_Menu.add_cascade(label = 'Edit', menu = sub2)
calc_form_2 = sub2.add_command(label = 'Auto Answering Format', command = Go_To_Auto)
sci_calc = sub2.add_command(label = 'Scientific Calculator', command = Go_To_Sci)

#DISPLAY AREA
txtDisplay = Entry(root,font=('arial',20,'bold'), textvariable=text_input,
                   insertwidth=4, bg='steel blue', justify='right',fg='powder blue')
txtDisplay.grid(columnspan=4,padx=10,pady=10)

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

#---------------------------------------------------------BTN's------------------------------------------------------#
 
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
#-------------------------------------------------------------------------------------------------------------------------#
if __name__ == '__main__':
    mainloop()

              
