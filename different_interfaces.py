import tkinter
from tkinter import*
root = Tk()
root.geometry('250x250+50+50')
root.title('interface')

tk = tkinter.Tk()


def page_one():
        b = Button(root, text='go to_1', command=page_two)
        b.pack()

def page_two():
        root1 = Tk()
        root1.geometry('250x250+50+50')
        root1.title('interface  001')
        Button(root1, text='go to_2',width=10, command=page_three).pack()

def page_three():
        root2 = Tk()
        root2.geometry('250x250+50+50')
        root2.title('interface  002')
        Button(root2, text='go to_1', command=page_one).pack()
        

if __name__ == '__main__':
    page_one()
    mainloop()
