input_name = input('Enter your name: ')

list_input_name = list(input_name)

for i in list_input_name:

      print('{0} : {1}'.format(i, list_input_name.index(i)))

'''
      
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9))
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)

print(dt) # 2015-01-01 12:00:00+09:00
print(dt.tzname()) # UTC+09:00

'''
'''
import itertools
import sys, time

done = False

def animate():
      for c in itertools.cycle(['....','.......','..........','............']):
            if done:
                  break
            sys.stdout.write('\rCHECKING IP ADDRESS AND NOT USED PORT '+c)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\r -----SERVER STARTED. WAITING FOR CLIENT-----\n') 

animate()
'''

      
