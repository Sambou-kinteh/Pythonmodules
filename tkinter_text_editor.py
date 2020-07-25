#<-------------------------------------GUI EDITOR--------------------------------->

import tkinter, os
from tkinter.constants import*
from tkinter import*


tk = tkinter.Tk()
tk.geometry('815x370+60+30')
tk.title('SAMSKI EDITOR')

tk.minsize(height = 270, width = 550)


def Text_save():
     tk1 = tkinter.Tk()
     tk1.geometry('40x55+50+25')
     tk1.title('Save as...')

     save_frame = tkinter.Frame(tk1, relief = 'flat')
     save_frame.pack(anchor = N, fill = BOTH)
     global save_dir

     save_dir = tkinter.Entry(save_frame)
     save_dir.pack(anchor = W, fill = BOTH)
     
     
     My_Menu = Menu(tk1)
     tk1.config(menu = My_Menu)

     S_Menu = Menu(My_Menu)
     My_Menu.add_cascade(label = 'File', menu = S_Menu)
     CALC = S_Menu.add_command(label = 'Save          ', command = save_as)
     

def save_as():
     global value
     global save_dir
     
     s_dir = save_dir.get()
     value = listBox.get()

     words = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
     punc = '''\|,<.>/?:;@'#~[{]}-_=+)(*&^%$£"!¬`'''
     nums = '''0123456789'''

     let_them = 0
     punc_them = 0
     num_them = 0
     
     for letter in value:
          if letter in words:
               let_them += 1
     for punx in value:
          if punx in punc:
               punc_them += 1
     for nun in value:
          if nun in nums:
               num_them += 1
                    

     if (s_dir.endswith('*')):
          with open(os.path.join(s_dir, '.txt'), 'a') as dirr:
               dirr.write(value)
               dirr.write('\n\n\n\n\n\n\n\n\n\n\nChar: {0}\nLetters: {1}\nNums: {2}\n'.format(punc_them, let_them, num_them))
               dirr.close()
               print('File Saved and pasted at:  %s' % (s_dir))


     else:
          with open(os.path.join(s_dir + '.txt'), 'a') as dirr:
               dirr.write(value)
               dirr.write('\n\n\n\n\n\n\n\n\n\n\nChar: {0}\nLetters: {1}\nNums: {2}\n'.format(punc_them, let_them, num_them))
               dirr.close()
               print('File Saved and pasted at:  %s' % (s_dir))
          

main_frame = tkinter.Frame(tk, relief = 'sunken', bg = 'light grey', width = 700, height = 395)
main_frame.pack(anchor = N, side = 'bottom', fill = BOTH)

bottom_frame = tkinter.Frame(main_frame, relief = 'flat', bg = 'light grey', width = 700, height = 20)
bottom_frame.pack(anchor = S, side = 'bottom', fill = X)

scrollBar = Scrollbar(main_frame)
scrollBar.pack(side = 'right', fill = BOTH)

listBox = tkinter.Entry(main_frame, bg = 'white', width = 1000)
listBox.pack(side = 'left', fill = BOTH)
scrollBar.config( command = scrollBar.get())

mm = tkinter.Message(main_frame, bg = 'black')
mm.pack(anchor = N, fill = BOTH)

words = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'''
nums = '''1234567890'''

l = listBox.get()


for char in l:
               if char in words:
                    global length
                    length = (len(list(char)))

                    textt = tkinter.Label(bottom_frame, text = 'Words: %s' % (length))
                    textt.pack(anchor = E)               


#listBox.insert(0, tkinter.Entry(listBox))

#CREATING A DROP DOWN FUNCTIONALITY
My_Menu = Menu(tk)
tk.config(menu = My_Menu)

S_Menu = Menu(My_Menu)
My_Menu.add_cascade(label = 'File', menu = S_Menu)
CALC = S_Menu.add_command(label = 'New File          ')#, command = )
open1 = S_Menu.add_command(label = 'Open...          ')
save = S_Menu.add_command(label = 'Save as            ', command = Text_save)

'''ss_menu = Menu(S_Menu)
S_Menu.add_cascade(label = 'Further Math Functions', menu = ss_menu)

bio = ss_menu.add_command(label = 'Bionomial Theorem         (a+x)\u00b11')#, command = Go_To_Bio)
Heron = ss_menu.add_command(label = 'Area(Heron\'s Formula   A(x1,y1), B(x2,y2), C(x3,y3))')#, command = Go_To_Hrn)
mat = ss_menu.add_command(label = 'Matrice(3x3) Solver   ')#, command = Go_To_Mat)'''

S_Menu.add_separator()
exit = S_Menu.add_command(label = 'Exit...')#, command = Exit)

