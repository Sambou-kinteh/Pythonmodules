import tkinter
from tkinter.constants import*
from tkinter import*
import math
from tkinter import messagebox

#<----------Factors\\\Dont forget----------->
tk = tkinter.Tk()
tk.title('Quadratic Equation')

tk.maxsize(width = 550, height = 275)
tk.minsize(width = 460, height = 200)

frame = tkinter.Frame(tk, relief = FLAT, borderwidth= 8, bg='orange')
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text='This interface is for solving quadradic equation', fg='teal', underline= True)
label.pack(side=TOP)

frame2 = tkinter.Frame(tk, relief = FLAT, borderwidth= 10, bg='powder blue' )
frame2.pack(fill=BOTH, expand=1)


ans_display = StringVar()
ans_display1 = StringVar()
text_a = StringVar()
text_b = StringVar()
text_c = StringVar()
#error = StringVar()

#FUNC FOR EXITING THE PROGRAM
def Exit():
    Exit = messagebox.askyesno('Exiting System', 'Do you want to exit from SAMSKI')
    if Exit > 0:
        tk.destroy()
        return

#FUNC FOR BRINGING THE CALC
def Go_To_Calc():
    import Calculator_part_two
    if Go_To_Calc:
        tk.destroy()
        return   

#FUNC FOR BRINGING THE BIONOMIAL
def Go_To_Bio():
    import tkinter_f_math_bionomial
    if Go_To_Bio:
        tk.destroy()
        return

#FUNC FOR BRINGING THE HERON'S
def Go_To_Hrn():
    import tkinter_f_math_herons
    if Go_To_Hrn:
        tk.destroy()
        return

#FUNC FOR BRINGING THE MATRICE
def Go_To_Mat():
    import tkinter_matrice
    if Go_To_Mat:
        tk.destroy()
        return


#CREATING A DROP DOWN FUNCTIONALITY
My_Menu = Menu(tk)
tk.config(menu = My_Menu)

S_Menu = Menu(My_Menu)
My_Menu.add_cascade(label = 'Other Functions', menu = S_Menu)
CALC = S_Menu.add_command(label = 'Calculator', command = Go_To_Calc)

ss_menu = Menu(S_Menu)
S_Menu.add_cascade(label = 'Further Math Functions', menu = ss_menu)

bio = ss_menu.add_command(label = 'Bionomial Theorem         (a+x)\u00b11', command = Go_To_Bio)
Heron = ss_menu.add_command(label = 'Area(Heron\'s Formula   A(x1,y1), B(x2,y2), C(x3,y3))', command = Go_To_Hrn)
mat = ss_menu.add_command(label = 'Matrice(3x3) Solver   ', command = Go_To_Mat)

S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...', command = Exit)

#--------------------------------EXCEPTIION HANDLING BLOCK------------------------------------#
try:

    def quadratic(a,b,c):
        a = (a_entry.get())
        b = (b_entry.get())
        c = (c_entry.get())
        x1= int(b)**2
        x2= 4*int(a)*int(c)
        x3= 2*int(a) 
        x4= -(-(int(x1)) + (int(x2)))
        x5= math.sqrt(x4)
        return (round((-(int(b)) + (x5)))/x3)


    #for x2
    def quadratic1(a, b, c):
        a = (a_entry.get())
        b = (b_entry.get())
        c = (c_entry.get())
        x6 = int(b)**2
        x7 = 4*int(a)*int(c)
        x8 = 2*int(a)
        x9 = -(-(int(x6)) + (int(x7)))
        x10 = math.sqrt(x9)
        return (round((-(int(b)) - (x10)))/x8)
            

    def final():
        ans_display.set(quadratic(a,b,c))
        ans_display1.set(quadratic1(a,b,c))


    def clear():
        ans_display.set('')
        ans_display1.set('')
        text_a.set('')
        text_b.set('')
        text_c.set('')

except ValueError as msg:
    #raise ValueError("Mistaken us........")
    #print('Error while solving')
    #m = messagebox.askretrycancel('Quadratic Error', 'An error occurred while solving.\nInput a valid Quadratic Equation')
    '''if m != 'Retry':
        tk.destroy()'''
    errorBox = tkinter.Label(frame2, text = msg, fg='black', relief= FLAT)
    errorBox.grid(sticky=E, row = 11, column = 3)
    print('error: %s' % (msg))

try:
    #------------------------------X1-----------------------------------#
    x1 = tkinter.Label(frame2, text='X1 = ', fg='steel blue', bg='powder blue')
    x1.grid(sticky=W, column=7, row=8)
    x1_ent = tkinter.Entry(frame2, relief=FLAT, bg = 'powder blue', fg = 'black', textvariable= ans_display)
    x1_ent.grid(sticky=W, column= 8, row=8)
    #------------------------------X2-------------------------------#    
    x2 = tkinter.Label(frame2, text='X2 = ', fg='steel blue', bg='powder blue')
    x2.grid(sticky=W, column=7, row=10)
    x2_ent = tkinter.Entry(frame2, relief=FLAT, bg = 'powder blue', fg = 'black', textvariable= ans_display1)
    x2_ent.grid(sticky=W, column=8, row=10)
    #-------------------------------------IF ERROR----------------------------------------------------------#
    #error_box = tkinter.Entry(frame2, relief=FLAT, state='readonly', textvariable= error)          #
    #error_box.grid(sticky=W, column=2, row=11)                                                     #
    #-----------------------------------------------------------------------------------------------#

    #a
    a = tkinter.Label(frame2, text='A : ', fg= 'teal', relief=FLAT)
    a.grid(column=1, row=2)

    a_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_a)
    a_entry.grid(column=3, row=2)

    #b
    b = tkinter.Label(frame2, text='B : ', fg= 'teal', relief=FLAT)
    b.grid(column=1, row=3)

    b_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_b)
    b_entry.grid(column=3, row=3)

    #c
    c = tkinter.Label(frame2, text='C : ', fg= 'teal', relief=FLAT)
    c.grid(column=1, row=4)

    c_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_c)
    c_entry.grid(column=3, row=4)

    #answer buootn
    ans = tkinter.Button(frame2, text='SEE ANSWER', fg='teal', bg = 'black', relief= FLAT, command=final,
                         activebackground = 'aqua', activeforeground = 'black')
    ans.grid(sticky=E)
    #ans.bind("<Key-Up>", quadratic,quadratic1)

    clear = tkinter.Button(frame2, text='CLEAR', fg='black', bg = 'teal', relief= FLAT, command=clear,
                           activebackground = 'red', activeforeground = 'aqua')
    clear.grid(sticky=E, column=1, row=11)

    #exit btn
    exit = tkinter.Button(frame2, text='EXIT', fg='black', bg = 'red', relief= FLAT, command=Exit,
                          activebackground = 'black', activeforeground = 'red')
    exit.grid(sticky=E, column=2, row=11)

    
except ValueError as msg:
    #raise ValueError("Mistaken us........")
    #print('Error while solving')
    #m = messagebox.askretrycancel('Quadratic Error', 'An error occurred while solving.\nInput a valid Quadratic Equation')
    '''if m != 'Retry':
        tk.destroy()'''
    errorBox = tkinter.Label(frame2, text = msg, fg='black', relief= FLAT)
    errorBox.grid(sticky=E, row = 11, column = 3)
    print('error: %s' % (msg))
    
#-------------------------------------------------------#

if  __name__  == '__main__':
    mainloop()

