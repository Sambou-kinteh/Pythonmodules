import tkinter
from tkinter import*

root = Tk()
root.geometry('500x500+100+100')
root.title('Canvas')

root.minsize(width = 400, height = 400)
root.maxsize(width = 600, height = 500)

###################DEFINIG A CANVAS#####################

class _Can():
    def __init__(self, bg, master=None):
        self.master = master
        self.bg = bg
        global can_plat
        self.Canvas = can_plat = Canvas(self.bg, self.master, height = 400, width = 400, bg =  'light blue')
        self.Canvas.pack()


def _canv(_Can):
    _canv = _Can(root)
    line = can_plat.create_line(0, 0, 400, 400, width = 5, fill = 'grey')
    line_v = can_plat.create_line(0, 400, 400, 0, width = 5, fill = 'grey')
    
    cir1 = can_plat.create_oval(20, 20, 100, 100, fill='red', width = 0)
    cir2 = can_plat.create_oval(0, 0, 100, 100, fill='steel blue', width = 1)
    cir3 = can_plat.create_oval(20, 20, 100, 0, fill='black', width = 0)
    cir4 = can_plat.create_oval(20, 20, 0, 100, fill='steel blue', width = 1)
    cir5 = can_plat.create_oval(0, 20, 100, 100, fill='teal', width = 0)
    cir6 = can_plat.create_oval(20, 0, 100, 100, fill='steel blue', width = 1)
    cir7 = can_plat.create_oval(100, 50, 300, 300, fill='aqua', width = 0)
    line_h = can_plat.create_line(0, 400, 0, 0, width = 5)
    line_h_1 = can_plat.create_line(0, 400, 400, 400, width = 1)
    line_h_2 = can_plat.create_line(400, 400, 200, 200, width = 50, fill = 'light blue')
    line_h_3 = can_plat.create_line(0, 400, 200, 200, width = 50, fill = 'light blue')
    line_h_4 = can_plat.create_line(200, 0, 200, 200, width = 50, fill = 'light blue')
    line_v_1 = can_plat.create_line(400, 400, 400, 0, width = 1)
    line_v_2 = can_plat.create_line(0, 400, 400, 400, width = 25)
    line_v_3 = can_plat.create_line(0, 0, 400, 0, width = 20)
    line_v_4 = can_plat.create_line(200, 400, 100, 100, width = 5, fill = 'grey')
    line_v_4 = can_plat.create_line(200, 400, 200, 300, width = 5, fill = 'grey')
    line_v_4 = can_plat.create_line(200, 400, 300, 100, width = 5, fill = 'grey')

    
if __name__ == '__main__':
    _canv(_Can)
    mainloop()
        
    
