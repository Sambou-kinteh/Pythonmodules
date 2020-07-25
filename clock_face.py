import tkinter, datetime, random
from tkinter import*

choice_color = ('red', 'blue', 'green', 'yellow', 'orange', 'purple', 'aqua',
                'teal', 'powder blue', 'steel blue', 'brown', 'black', 'white', 'pink', 'grey')
choice_color2 = ('teal', 'powder blue', 'aqua', 'grey')
fav_color = input('Will you prefer auto generation or manual(a/m) \n')

root  = Tk()
root.title('Clock & Alarms')
root.geometry('500x500+25+50')
root.minsize(width = 220, height = 65)
#root.maxsize(width = 500, height = 500)
time1 = StringVar()
#root.configure(background = Random_Color(choice_color))
def Manual_Color():
      try:
            manual_color = input('What color would you prefer for your backgorund\n')
            return manual_color
      except Exception as msg:
            print('UnknownColorNameError: [%s]' %(msg))


def Auto_Color(color_tuple):
      rand_color = random.choice(color_tuple)
      return rand_color

def Current_Time():
      try:
            from datetime import datetime as time_obj
            import datetime as date_obj
            import time
            
            seconds_delta = date_obj.timedelta(seconds = 1)
            today = time_obj.now()
            current_period = time_obj(today.year, today.month, today.day, 
                        today.hour, today.minute, today.second)
            while(True):
                  hours = current_period.hour
                  minutes = current_period.minute
                  seconds = current_period.second

                  i = 1
                  i += seconds
                  time.sleep(1)
                  root.update()
                  return ('{0} : {1} : {2}'.format(hours, minutes, i))
                          
      except Exception as msg:
            print('[%s]' %(msg))

def Refresh_Time():
      root.update()
      '''import datetime as date_obj
      from datetime import datetime as time_obj
      import time, itertools
      
      seconds_delta = date_obj.timedelta(seconds = 1)
      today = time_obj.now()
      current_period = time_obj(today.year, today.month, today.day, 
                        today.hour, today.minute, today.second)

      hours = current_period.hour
      minutes = current_period.minute
      seconds = 0#current_period.second
      time1.set('{0} : {1} : {2}'.format(hours, minutes, 13))
      if root.update():
            while (c for c in itertools.cycle(range(0,60, 1))):
                  time.sleep(1)
            time.set('{0} : {1} : {2}'.format(hours, minutes, c))'''

      #hour += hour*60*60

if fav_color == 'm':
      root.configure(background = Manual_Color())
else:
      root.configure(background = Auto_Color(choice_color))


mid_frame = Frame(root, relief = 'flat', height = 400, width = 400,
                  bg =Auto_Color(choice_color2), bd = 0).grid(sticky = N, padx = 1, pady = 1)

time_box = Label(root, font = ('serif', 30, 'bold'), text = Current_Time(),
                   bd = 2, padx = 2, pady = 2, fg ='black', bg = 'white').grid(row=5, column=5) 
'''
refresh_box = Label(mid_frame, font = ('serif', 30, 'bold'), textvariable = time1,
                   bd = 2, padx = 2, pady = 2, fg ='black', bg = 'white').grid(row=5, column=5) 
'''
btnRefresh= Button(root, text='Refresh', padx=2, pady=2, bd=2, fg='black',
                  font=('arial',10,'bold'), width=12, height=1, command=Refresh_Time()).grid(row=3,column=0)



if __name__ == '__main__':
      mainloop()

