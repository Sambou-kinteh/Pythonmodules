import re, tkinter, math
from tkinter.constants import*
from tkinter import*
from tkinter import messagebox

#<----------Factors\\\Dont forget----------->
tk = tkinter.Tk()
tk.title('MATRICE(3x3) SOLVER')

tk.maxsize(width = 585, height = 300)
tk.minsize(width = 475, height = 215)

frame = tkinter.Frame(tk, relief = FLAT, borderwidth= 8, bg='orange')
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text='This interface is for solving matrices(3x3)', fg='teal', underline= True)
label.pack(side=TOP)

frame2 = tkinter.Frame(tk, relief = FLAT, borderwidth= 10, bg='powder blue' )
frame2.pack(fill=BOTH, expand=1)


ans_display = StringVar()
ans_display1 = StringVar()
ans_display2 = StringVar()
eq_a = StringVar()
eq_b = StringVar()
eq_c = StringVar()
#error = StringVar()

#FUNC FOR EXITING THE PROGRAM
def Exit():
    Exit = messagebox.askyesno('Exiting System', 'Do you want to exit from SAMSKI')
    if Exit > 0:
        tk.destroy()
        return

#FUNC FOR BRINGING THE CALCULATOR
def Go_To_Calc():
    import Calculator_part_two
    if Go_To_Calc:
        tk.destroy()
        return   

#FUNC FOR BRINGING THE BIONOMAIL
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

#FUNC FOR BRINGING THE QUADRATIC
def Go_To_Quad():
    import tkinter_quadratic_eq
    if Go_To_Quad:
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
Quad = ss_menu.add_command(label = 'Quadratic Equations      ax\u00b2 + bx + c', command = Go_To_Quad)

S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...', command = Exit)

#--------------------------------EXCEPTIION HANDLING BLOCK------------------------------------#
try:
    #a
    eqa = tkinter.Label(frame2, text='Equation A : ', fg= 'teal', relief=FLAT)
    eqa.grid(column=1, row=2)

    a_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= eq_a)
    a_entry.grid(column=3, row=2)

    #b
    eqb = tkinter.Label(frame2, text='Equation B : ', fg= 'teal', relief=FLAT)
    eqb.grid(column=1, row=3)

    b_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= eq_b)
    b_entry.grid(column=3, row=3)

    #c
    eqc = tkinter.Label(frame2, text='Equation C : ', fg= 'teal', relief=FLAT)
    eqc.grid(column=1, row=4)

    c_entry = tkinter.Entry(frame2, relief=FLAT, textvariable= eq_c)
    c_entry.grid(column=3, row=4)
    
    def matrices():
        global a_entry
        global b_entry
        global c_entry

        eqA = str(a_entry.get())
        eqB = str(b_entry.get())
        eqC = str(c_entry.get())
        
        #PATTERNS TO MATCH
        pattern1 = r'(?P<num1_1>\d*)(?P<letter1_1>\w).\+.(?P<num1_2>\d*)(?P<letter1_2>\w).\+.(?P<num1_3>\d*)(?P<letter1_3>\w).\=.(?P<num1_4>\d*)'
        pattern2 = r'(?P<num2_1>\d*)(?P<letter2_1>\w).\+.(?P<num2_2>\d*)(?P<letter2_2>\w).\+.(?P<num2_3>\d*)(?P<letter2_3>\w).\=.(?P<num2_4>\d*)'
        pattern3 = r'(?P<num3_1>\d*)(?P<letter3_1>\w).\+.(?P<num3_2>\d*)(?P<letter3_2>\w).\+.(?P<num3_3>\d*)(?P<letter3_3>\w).\=.(?P<num3_4>\d*)'

        #SEARCHES
        search1 = re.search(pattern1, eqA, re.S)
        search2 = re.search(pattern2, eqB, re.S)
        search3 = re.search(pattern3, eqC, re.S)

        #VARIABLES
        '''#<------For Eq1------>
        var1_1 = search1.group('letter1_1')
        var1_2 = search1.group('letter1_2')
        var1_3 = search1.group('letter1_3')

        #<------For Eq2------>
        var2_1 = search2.group('letter2_1')
        var2_2 = search2.group('letter2_2')
        var2_3 = search2.group('letter2_3')

        #<------For Eq3------>
        var3_1 = search3.group('letter3_1')
        var3_2 = search3.group('letter3_2')
        var3_3 = search3.group('letter3_3')'''
        #if search1:
        #print('a= %s, b= %s, c= %s' % (search1.group('num1_1'), search1.group('num1_2'), search1.group('num1_3')))
        A = int(search1.group('num1_1'))
        B = int(search1.group('num1_2'))
        C = int(search1.group('num1_3'))
        AEquals = eq1 = int(search1.group('num1_4'))

        #if search2:
        #print('x= %s, y= %s, z= %s' % (search2.group('num2_1'), search2.group('num2_2'), search2.group('num2_3')))
        D = int(search2.group('num2_1'))
        E = int(search2.group('num2_2'))
        F = int(search2.group('num2_3'))
        BEquals = eq2 = int(search2.group('num2_4'))

        #if search3:
            #print('p= %s, q= %s, r= %s' % (search3.group('num3_1'), search3.group('num3_2'), search3.group('num3_3')))
        G = int(search3.group('num3_1'))
        H = int(search3.group('num3_2'))
        I = int(search3.group('num3_3'))
        CEquals = eq3 = int(search3.group('num3_4'))


        #Get our True Matrice First
        a1 = int(E*I)-(H*F)
        b1 = int(D*I)-(G*F)
        c1 = int(D*H)-(G*E)
        a2 = int(A*a1)
        b2 = int(B*b1)
        c2 = int(C*c1)
        DetOfTrueMat = a2 - b2 + c2

        #Find our Ax

        a3 = int(E*I)-(H*F)
        b3 = int(eq2*I)-(eq3*F)
        c3 = int(eq2*H)-(eq3*E)
        a4 = int(eq1*a3)
        b4 = int(B*b3)
        c4 = int(C*c3)
        DetOfAxMat = a4 - b4 + c4

        #Find our Ay

        a5 = int(eq2*I)-(eq3*F)
        b5 = int(D*I)-(G*F)
        c5 = int(D*eq3)-(eq2*G)
        a6 = int(A*a5)
        b6 = int(eq1*b5)
        c6 = int(C*c5)
        DetOfAyMat = a6 - b6 + c6

        #Find our Az

        a7 = int(E*eq3)-(H*eq2)
        b7 = int(D*eq3)-(eq2*G)
        c7 = int(D*H)-(G*E)
        a8 = int(A*a7)
        b8 = int(B*b7)
        c8 = int(eq1*c7)
        DetOfAzMat = a8 - b8 + c8
     
        x_value = round(DetOfAxMat/DetOfTrueMat, 3)
        y_value = round(DetOfAyMat/DetOfTrueMat, 3)
        z_value = round(DetOfAzMat/DetOfTrueMat, 3)

        return (ans_display.set('%s   or   %s/%s' % (x_value, DetOfAxMat, DetOfTrueMat)),
                ans_display1.set('%s   or   %s/%s' % (y_value, DetOfAyMat, DetOfTrueMat)),
                 ans_display2.set('%s   or   %s/%s' % (z_value, DetOfAzMat, DetOfTrueMat)))
        
    '''class final():
        matrices()
        
        def x_func():
            x_value = DetOfAxMat/DetOfTrueMat
            return x_value

        def y_func():
            y_value = DetOfAyMat/DetOfTrueMat
            return y_value

        def z_func():
            z_value = DetOfAzMat/DetOfTrueMat
            return z_value'''
            
        

    def clear():
        ans_display.set('')
        ans_display1.set('')
        ans_display2.set('')
        eq_a.set('')
        eq_b.set('')
        eq_c.set('')
    #------------------------------X1-----------------------------------#
    x1 = tkinter.Label(frame2, text='X = ', fg='steel blue', bg='powder blue')
    x1.grid(sticky=W, column=7, row=8)
    x1_ent = tkinter.Entry(frame2, relief=FLAT, bg = 'powder blue', fg = 'black', textvariable= ans_display)
    x1_ent.grid(sticky=W, column= 8, row=8)
    #------------------------------X2-------------------------------#    
    x2 = tkinter.Label(frame2, text='Y = ', fg='steel blue', bg='powder blue')
    x2.grid(sticky=W, column=7, row=10)
    x2_ent = tkinter.Entry(frame2, relief=FLAT, bg = 'powder blue', fg = 'black', textvariable= ans_display1)
    x2_ent.grid(sticky=W, column=8, row=10)
    #------------------------------X3-------------------------------#    
    x3 = tkinter.Label(frame2, text='Z = ', fg='steel blue', bg='powder blue')
    x3.grid(sticky=W, column=7, row=12)
    x3_ent = tkinter.Entry(frame2, relief=FLAT, bg = 'powder blue', fg = 'black', textvariable= ans_display2)
    x3_ent.grid(sticky=W, column=8, row=12)
    #-------------------------------------IF ERROR----------------------------------------------------------#
    #error_box = tkinter.Entry(frame2, relief=FLAT, state='readonly', textvariable= error)          #
    #error_box.grid(sticky=W, column=2, row=11)                                                     #
    #-----------------------------------------------------------------------------------------------#

    

    #answer buootn
    ans = tkinter.Button(frame2, text='SEE ANSWER', fg='teal', bg = 'black', relief= FLAT, command=matrices,
                         activebackground = 'aqua', activeforeground = 'black')
    ans.grid(sticky=E, column = 0, row = 11)
    #ans.bind("<Key-Up>", quadratic,quadratic1)

    clear = tkinter.Button(frame2, text='CLEAR', fg='black', bg = 'teal', relief= FLAT, command=clear,
                           activebackground = 'red', activeforeground = 'aqua')
    clear.grid(sticky=E, column=1, row=11)

    #exit btn
    exit = tkinter.Button(frame2, text='EXIT', fg='black', bg = 'red', relief= FLAT, command=Exit,
                          activebackground = 'black', activeforeground = 'red')
    exit.grid(sticky=E, column=2, row=11)

    

    
except ValueError:
    raise ValueError("Mistaken us........")
    #print('Error while solving')
    m = messagebox.askretrycancel('Quadratic Error', 'An error occurred while solving.\nInput a valid Quadratic Equation')
    '''if m != 'Retry':
        tk.destroy()'''
#-------------------------------------------------------#

if  __name__  == '__main__':
    mainloop()


