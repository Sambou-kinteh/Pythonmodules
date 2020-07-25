import tkinter
from tkinter import*
import math
from tkinter import messagebox

root = Tk()
root.geometry('650x300+50+50')
root.title('Area(Herons Formula)')

#---------------------------------FUTURE PROGRESS- (A+X)(X+Y)(1+X)(CALCULUS)----------------------#
root.minsize(width = 600, height = 250)
root.maxsize(width = 625, height = 300)


frame = tkinter.Frame(root, relief = FLAT, borderwidth= 8, bg='orange')
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text='This interface is for solving Area\nIn Coodinate Geometry In the Form\nA(X1+Y1), B(X2+Y2) and C(X3+Y3)', fg='teal', underline= True)
label.pack(side=TOP)

frame2 = tkinter.Frame(root, relief = FLAT, borderwidth= 10, bg='powder blue' )
frame2.pack(fill=BOTH, expand=1)


#MY WORD VARIABLES
ans_display = StringVar()
text_x1 = StringVar()
text_y1 = StringVar()
text_x2 = StringVar()
text_y2 = StringVar()
text_x3 = StringVar()
text_y3 = StringVar()
#error = StringVar()

#FUNC FOR EXITING THE PROGRAM
def Exit():
    Exit = messagebox.askyesno('Exiting System', 'Do you want to exit from SAMSKI')
    if Exit > 0:
        root.destroy()
        return

#FUNC FOR BRINGING CALCULATOR
def Go_To_Calc():
    import Calculator_part_two
    if Go_To_Calc:
        root.destroy()
        return   

#FUNC FOR BRINGING QUADRATIC
def Go_To_Quad():
    import tkinter_quadratic_eq
    if Go_To_Quad:
        root.destroy()
        return

#FUNC FOR BRINGING BIONOMIAL
def Go_To_Bio():
    import tkinter_f_math_bionomial
    if Go_To_Bio:
        root.destroy()
        return

#FUNC FOR BRINGING MATRICE
def Go_To_Mat():
    import tkinter_matrice
    if Go_To_Mat:
        root.destroy()
        return    

#CREATING A DROP DOWN FUNCTIONALITY
My_Menu = Menu(root)
root.config(menu = My_Menu)

S_Menu = Menu(My_Menu)
My_Menu.add_cascade(label = 'Other Functions', menu = S_Menu)
cal = S_Menu.add_command(label = 'Calculator', command = Go_To_Calc)

ss_menu = Menu(S_Menu)
S_Menu.add_cascade(label = 'Further Math Functions', menu = ss_menu)
qua = ss_menu.add_command(label = 'Quadratic Equation      ax\u00b2+bx+c', command = Go_To_Quad)
bio = ss_menu.add_command(label = 'Bionomial Theorem       (a+n)\u00b11', command = Go_To_Bio)
mat = ss_menu.add_command(label = 'Matrice(3x3) Solver      ', command = Go_To_Mat)


S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...', command = Exit)

#--------------------------------EXCEPTIION HANDLING BLOCK------------------------------------#
try:

    def Area():
        #----MY GLOBAL VARIABLES----#
        global x1
        global y1
        global x2
        global y2
        global x3
        global y3
        
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        x3 = int(x3_entry.get())
        y3 = int(y3_entry.get())

        #Calc for A
        a = math.sqrt((int(y2) - int(y1))**2 + (int(x2) - int(x1))**2)
        #Calc for B
        b = math.sqrt((int(y3) - int(y2))**2 + (int(x3) - int(x2))**2)
        #Calc for C
        c = math.sqrt((int(y3) - int(y1))**2 + (int(x3) - int(x1))**2)
        #Calc for S
        s = ((int(a)+int(b)+int(c)))/2

        return math.sqrt(int(s) * ((int(s) - int(a)) * (int(s) - int(b)) * (int(s) - int(c))))
        
            

    def final():
        ans_display.set(Area())

    def clear():
        ans_display.set('')
        text_x1.set('')
        text_y1.set('')
        text_x2.set('')
        text_y2.set('')
        text_x3.set('')
        text_y3.set('')
    #------------------------------AREA-----------------------------------#
    area_int = tkinter.Label(frame2, text='Area = ', fg='steel blue', bg='powder blue')
    area_int.grid(sticky=W, column=7, row=8)
    area_ent = tkinter.Entry(frame2, font = ('arial', 10, 'bold') , relief='flat', textvariable= ans_display, width = 25, bg = 'powder blue',
                            fg = 'black')
    area_ent.grid(sticky=W, column= 8, row=8)
    #-------------------------------------IF ERROR----------------------------------------------------------#
    #error_box = tkinter.Entry(frame2, relief=FLAT, state='readonly', textvariable= error)          #
    #error_box.grid(sticky=W, column=2, row=11)                                                     #
    #-----------------------------------------------------------------------------------------------#

    #a
    a_lbl = tkinter.Label(frame2, text='A : ', fg= 'teal', relief=FLAT)
    a_lbl.grid(column=1, row=2)
    #x1
    x1_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_x1, text = 'X1')
    x1_entry.grid(column=3, row=2)
    #y1
    y1_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_y1)
    y1_entry.grid(column=4, row=2)

    #b
    b_lbl = tkinter.Label(frame2, text='B : ', fg= 'teal', relief=FLAT)
    b_lbl.grid(column=1, row=3)
    #x2
    x2_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_x2)
    x2_entry.grid(column=3, row=3)
    #y2
    y2_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_y2)
    y2_entry.grid(column=4, row=3)

    #c
    c_lbl = tkinter.Label(frame2, text='C : ', fg= 'teal', relief=FLAT)
    c_lbl.grid(column=1, row=4)
    #x3
    x3_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_x3)
    x3_entry.grid(column=3, row=4)
    #y3
    y3_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_y3)
    y3_entry.grid(column=4, row=4)

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

    
except ValueError:
    print('Error while solving')
    m = messagebox.askretrycancel('Quadratic Error', 'An error occurred while solving.\nInput a valid Quadratic Equation')
    '''if m != 'Retry':
        tk.destroy()'''
#-------------------------------------------------------#

if  __name__ == '__main__':
    mainloop()

