import tkinter
from tkinter import*
import math
from tkinter import messagebox
import webbrowser

root = Tk()
root.geometry('600x200+50+50')
root.title('Bionomial Theorem')

#---------------------------------FUTURE PROGRESS- (A+X)(X+Y)(1+X)(CALCULUS)----------------------#

root.maxsize(width = 650, height = 300)
root.minsize(width = 550, height = 200)

frame = tkinter.Frame(root, relief = FLAT, borderwidth= 8, bg='orange')
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text='This interface is for solving Bionomial Theorem\nIn the form (a+x)\u00b11', fg='teal', underline= True)
label.pack(side=TOP)

frame2 = tkinter.Frame(root, relief = FLAT, borderwidth= 10, bg='powder blue' )
frame2.pack(fill=BOTH, expand=1)

qbio = StringVar()
ans_display = StringVar()
text_a = StringVar()
text_x = StringVar()
text_n = StringVar()
#error = StringVar()

#FUNC FOR EXITING THE PROGRAM
def Exit():
    Exit = messagebox.askyesno('Exiting System', 'Do you want to exit from SAMSKI')
    if Exit > 0:
        root.destroy()
        return

#FUNC FOR BRINGING CALC
def Go_To_Calc():
    import Calculator_part_two
    if Go_To_Calc:
        root.destroy()
        return   

#FUNC FOR BRINGING THE QUADRATIC
def Go_To_Quad():
    import tkinter_quadratic_eq
    if Go_To_Quad:
        root.destroy()
        return

#FUNC FOR BRINGING THE HERON'S
def Go_To_Hrn():
    import tkinter_f_math_herons
    if Go_To_Hrn:
        root.destroy()
        return

#FUNC FOR BRINGING THE MATRICE
def Go_To_Mat():
    import tkinter_matrice
    if Go_To_Mat:
        root.destroy()
        return     

#FUNC FOR BRINGING THE REGISTER PAGE
def Go_To_Bro():
    web = webbrowser.open('file:///C:/Users/Sambou/Desktop/PERSONAL%20WORK/HTML%20PL/STUDENTS%20ENROLMENT%20PAGE1.html')
    return web

#CREATING A DROP DOWN FUNCTIONALITY
My_Menu = Menu(root)
root.config(menu = My_Menu)

S_Menu = Menu(My_Menu)
My_Menu.add_cascade(label = 'Other Functions', menu = S_Menu)
cal = S_Menu.add_command(label = 'Calculator', command = Go_To_Calc)

ss_menu = Menu(S_Menu)
S_Menu.add_cascade(label = 'Further Math Functions', menu = ss_menu)
qua = ss_menu.add_command(label = 'Quadratic Equation        ax\u00b2+bx+c', command = Go_To_Quad)
Heron = ss_menu.add_command(label = 'Area(Heron\'s Formula   A(x1,y1), B(x2,y2), C(x3,y3))', command = Go_To_Hrn)
mat = ss_menu.add_command(label = 'Matrice(3x3) Solver   ', command = Go_To_Mat)

S_Menu.add_separator()
bro = S_Menu.add_command(label = 'Registry                   ', command = Go_To_Bro)

S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...', command = Exit)

#--------------------------------EXCEPTIION HANDLING BLOCK------------------------------------#
try:

    def Bionomial():
        #----MY GLOBAL VARIABLES----#
        global a
        global x
        global n
        
        a = float(a_entry.get())
        x = float(x_entry.get())
        n = float(n_entry.get())
        
        bio1 = int(int(a)**int(n))
        bio2 = int(x*(int(n)*(int(a)**(int(n)-1))))
        bio3 = int(x*(int(n*(int(n)-1)/(math.factorial(2)))*int(a)**(int(n)-2)))
        bio4 = int(x*(int(n*(int(n)-1)*(int(n)-2)/(math.factorial(3)))*int(a)**(int(n)-3)))

        return (str(bio1) + '+' + str(bio2) + 'x +' + str(bio3) + 'x\u00b2 +' + str(bio4) + 'x\u00b3...')
            

    def final():
        ans_display.set(Bionomial())
        form = ('({0} + {1}x)\u00b2'. format(int(a),int(x),int(n)))
        qbio.set(form)

    def clear():
        ans_display.set('')
        text_a.set('')
        text_x.set('')
        text_n.set('')
        qbio.set('')
    #------------------------------BIONOMIAL-----------------------------------#
    bio_int = tkinter.Label(frame2, text='Bionomial = ', fg='steel blue', bg='powder blue')
    bio_int.grid(sticky=W, column=7, row=8)
    bio_ent = tkinter.Entry(frame2, relief='flat', textvariable= ans_display, width = 25, bg = 'powder blue',
                            fg = 'black')
    bio_ent.grid(sticky=W, column= 8, row=8)
    #----------------------------------format---------------------------------------------#
    bio_q = tkinter.Label(frame2, text='Format = ', fg='steel blue', bg='powder blue')
    bio_q.grid(sticky=W, column=7, row=9)
    bio_for = tkinter.Entry(frame2, relief='flat', textvariable= qbio, width = 25, bg = 'powder blue',
                            fg = 'black')
    bio_for.grid(sticky=W, column= 8, row=9)
    #-------------------------------------IF ERROR----------------------------------------------------------#
    #error_box = tkinter.Entry(frame2, relief=FLAT, state='readonly', textvariable= error)          #
    #error_box.grid(sticky=W, column=2, row=11)                                                     #
    #-----------------------------------------------------------------------------------------------#

    #a
    a_lbl = tkinter.Label(frame2, text='A : ', fg= 'teal', relief=FLAT)
    a_lbl.grid(column=1, row=2)

    a_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_a)
    a_entry.grid(column=3, row=2)

    #x
    x_lbl = tkinter.Label(frame2, text='X : ', fg= 'teal', relief=FLAT)
    x_lbl.grid(column=1, row=3)

    x_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_x)
    x_entry.grid(column=3, row=3)

    #n
    n_lbl = tkinter.Label(frame2, text='N : ', fg= 'teal', relief=FLAT)
    n_lbl.grid(column=1, row=4)

    n_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= text_n)
    n_entry.grid(column=3, row=4)

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

