import tkinter
from tkinter.constants import*

tk = tkinter.Tk()

class dialog1:
    def __doc__(self):
        """The platform for Table"""

    def __int__(self, master):
        self.master = master
    def win2(self, height, width):
        self.height = height
        self.width = width
        f = tkinter.Frame(tk, relief = RIDGE, borderwidth=2, height = height, width = width)
        f.pack(expand= 1, fill= BOTH)
        menu = tkinter.Menu(f)
        f.config(menu=menu)

        subMenu = tkinter.Menu(menu)
        menu.add_cascade(label="Edit", menu=subMenu)
        subMenu.add_command(label="now what", command=__doc__)
        subMenu.add_separator()


class dialog2:
    def __doc__(self):
        """The platform for layerouts"""

    def __init__(self, master):
        self.master = master
