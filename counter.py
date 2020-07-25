import tkinter

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief= 'ridge' , borderwidth=3)
frame.pack(fill='both' , side= 'bottom' , expand=200)
frame.config(state = 'writable')

'''file = open('textbox.txt',"w")
file.write('')
textbox = input(Tkinter.Message(frame, text="type in something: "))
textbox = Tkinter.WRITABLE()
textbox.pack(side=BOTTOM)
n = 0
counter = 1
for count in textbox:
    if (chr("") and (count > 0)):
        n += counter

print("counts of characters = ",len(textbox) )'''
#write = Tkinter.Image(imgtype='.jpg', name='samkinteh.jpg', width=2)
#write.pack(side=TOP)
read = tkinter.Message(frame, text="Type in something")
read.pack(side='top')




tk.mainloop()
