import Tkinter
from Tkconstants import*
tk = Tkinter.Tk()

frame = Tkinter.Frame(tk, relief=RIDGE, borderwidth=3)
frame.pack(fill=BOTH, expand=500)
frame_1 = Tkinter.Frame(tk, relief=RIDGE, borderwidth=4)
frame_1.pack(fill=X,side=LEFT, expand=250)
fn = Tkinter.Message(frame, text="FirstName:")
fn.pack(fill=BOTH,side=LEFT, expand=500)
fn = Tkinter.Canvas()

tk.mainloop()
