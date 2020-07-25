import tkinter
from tkinter.constants import *
from tkinter import *
from tkinter import _cnfmerge
tk1 = Tk()
DIALOG_ICON = 'questhead'
frame = tkinter.Frame(tk1, relief=GROOVE, borderwidth=2)


class Dialog(Widget):
    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(
                self.tk.call(
                      'tk_dialog', self._w,
                      cnf['title'], cnf['text'],
                      cnf['bitmap'], cnf['default'],
                       cnf['buttons']))
        try: Widget.destroy(self)
        except TclError: pass
    def destroy(self): pass

def _test():
    player_name = name1.get()
    d = Dialog(None, {'title': 'Question',
                      'text':
                      'What do you want me to do for you',
                      'bitmap': DIALOG_ICON,
                      'default': '0',
                      'buttons':'click to go to next frame'})
    if __name__ == '__main__':
        add = Button(None, text='Add', command=_add).pack()
        mul = Button(None, text='Multiply').pack()
    '''sub = Button(None, text='Substract').pack()
    drw = Button(None, text='Draw').pack() '''
    tk1.event_delete(_add)


                      
    
def _add():
    a = Dialog(None, {'title': 'Add',
                      'text':'Enter you values below',
                       'bitmap': DIALOG_ICON,
                      'default': '0',
                      'buttons':'()'})
    Entry(None).pack()
    Entry(None).pack()
    Button(None, text='=')


    

    

tk = tkinter.Tk()

tk.title('KIDS APP')

frame = tkinter.Frame(tk, relief=GROOVE, borderwidth=2)
frame.pack(fill=BOTH, expand=1 , pady=100, padx=185)

label = tkinter.Label(frame, text='Hello Kid!', bg='red', highlightcolor='blue')
label.pack(side=TOP)
name = tkinter.Label(frame, text = 'What\'s your name:', bg='pink')
name.pack(side=TOP)

name1 = tkinter.Entry(frame)
name1.pack(side=TOP)

if __name__ == '__main__':
    next = tkinter.Button(frame, text='Next', bg='teal', highlightcolor='green',command=_test)
    next.pack(side=TOP)

'''create interfaces and asq for 1 to 5, if any do that thing(inter 2)'''



tk.mainloop()
