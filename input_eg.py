#this will ask for user input
import sys
import turtle
import tkinter, random
from tkinter import *


root = Tk()
root.geometry('610x675+50+25')
root.title('Chatbot')


##############################SCROOLING EFFECT###################################################
 

def up_event(self, event):
    index = self.listbox.index("active")
    if self.listbox.selection_includes(index):
        index = index - 1
    else:
        index = self.listbox.size() - 1
    if index < 0:
        self.listbox.bell()
    else:
        self.select(index)
        self.on_select(index)
    return "break"

def down_event(self):
    index = self.listbox.index("active")
    if self.listbox.selection_includes(index):
        index = index + 1
    else:
        index = 0
    if index >= self.listbox.size():
        self.listbox.bell()
    else:
        self.select(index)
        self.on_select(index)
        return "break"
    
##################################SCROLL BAR################################################
   

#################################################################################################
##If woken up
rand_rep = random.choice(seq=('Hi', 'Hello!', 'Sup?', 'Waker!', 'Morning!'))
################Variables##################################
m_text = StringVar()

def v():
    global l
    
    sb = Scrollbar(root)
    sb.pack(side = 'right' , fill = Y)
    root.bbox(row=20, column=20)
        
    l = Listbox(root, yscrollcommand = sb.get(), height=675, width = 610)
    l.bind("<Key-Up>", up_event)
    l.bind("<Key-Down>", down_event)
    hi = Entry(l,font=('arial',20,'bold'),
                  insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)
    
    l.insert(0, 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?'
             , 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Sup?', 'Hello!', 'Hello!', 'Hello!', 'Hello!'
             , 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!'
             , 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!', 'Hello!'
             , 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!', 'Morning!'
             , 'Morning!', 'Morning!')
    
    l.pack(side='left', fill=BOTH)
    sb.configure(command= l.yview)
v()    
 
#####################################INPUTS#######################################################




'''
hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=E)

hi = Entry(l,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').pack(fill=Y, anchor=W)'''
##################################################################################################

if __name__ == '__main__':
    mainloop()
