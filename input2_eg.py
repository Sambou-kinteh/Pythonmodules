#this will ask for user input
import sys
import turtle
import tkinter, random
from tkinter import *


root = Tk()
root.geometry('450x675+50+25')
root.title('Chatbot')

##If woken up
rand_rep = random.choice(seq=('Hi', 'Hello!', 'Sup?', 'Waker!', 'Morning!'))
################Variables##################################
m_text = StringVar()

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue',width=90).grid(column = 5, row = 1)


hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=60).grid(column = 5, row = 2)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=55).grid(column = 5, row = 3)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=50).grid(column = 5, row = 4)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=45).grid(column = 5, row = 5)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=40).grid(column = 5, row = 6)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=35).grid(column = 5, row = 7)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=60).grid(column = 5, row = 8)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=60).grid(column = 5, row = 9)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue', width=60).grid(column = 5, row = 10)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=60).grid(column = 5, row = 11)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=60).grid(column = 5, row = 12)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=60).grid(column = 5, row = 13)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=35).grid(column = 5, row = 14)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=40).grid(column = 5, row =15)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=45).grid(column = 5, row = 16)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=50).grid(column = 5, row =17)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=55).grid(column = 5, row =18)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=60).grid(column = 5, row =19)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='left',fg='powder blue', width=90).grid(column = 5, row =20)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =21)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =22)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row = 23)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =24)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =25)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =26)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =27)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =28)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =29)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =30)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =31)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =32)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =33)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =34)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =35)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =36)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =37)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =38)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =39)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =40)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =41)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =42)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =43)

hi = Entry(root,font=('arial',20,'bold'),
                   insertwidth=4, bg='steel blue',textvariable = m_text, justify='right',fg='powder blue').grid(column = 5, row =44)

      
