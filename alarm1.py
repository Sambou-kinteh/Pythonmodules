import datetime, winsound, time

#alarm_hour = input('HOUR: ')
#alarm_minute = input('MINUTE: ')
#alarm_second = input('SECOND: ')

sound_file = "C:\\Users\\Sambou\\Desktop\\W3SCHOOLS\\gggg\\www.w3schools.com\\jsref\\horse.wav"

def alarm():
      for i in range(0, 10):#while(True):
            
            i = winsound.PlaySound(sound_file , 1)
            return i

def snooze():
      global snooze_min
      snooze_min = input('HOW MANY MINUTES\n')
      snooze_min = int(snooze_min)
      snooze_sec = snooze_min * 60
      if snooze_min > 1:
            print('SNOOZE Set For: %s mins\n' %(snooze_min))
      else:
            print('SNOOZE Set For: %s min\n' %(snooze_min))
      time.sleep(snooze_sec)
      return winsound.PlaySound(sound_file, 1)

'''def snooze_timeout():
      try:
            
            snooze_sec = snooze_min * 60
            snooze_apex = datetime.timedelta(seconds = snooze_sec)
            current_time = datetime.datetime.now()
            remaining_time = current_time - snooze_apex
            return remaining_time
      except Exception as msg:
            print('%s' %(msg))     ''' 


def SetAlarm(hours, mins, sec):
      print('\rALARM TIME: \r', end = '')
      print('\t%s:%s:%s\n' %(hours, mins, sec))
      alarm_hour = hours
      alarm_minute = mins
      alarm_second = sec
      alert = False
      while(alert == False):
            #current_time = datetime.datetime.time(datetime.datetime.now())
            setime = time.localtime()
            if setime.tm_hour > 12:
                  current_hour = setime.tm_hour - 12
            else:
                  current_hour = setime.tm_hour
                  
            current_minute = setime.tm_min
            current_second = setime.tm_sec
            print('%s:%s:%s' %(current_hour, current_minute, current_second))
                   
            if ( (int(current_hour) == int(alarm_hour)) and (int(current_minute) == int(alarm_minute)) and (int(current_second) == int(alarm_second)) ):
                        print('\r\r\nIT\'S TIME\r\r\n')
                        alarm()
                        while(True):
                              option = input('DO YOU WANT TO SNOOZE(y/Y or n/N)\n')
                              if option == 'y' or option == 'Y':
                                    snooze()
                              else:
                                    alert = True
                                    break
            else:
                  #print(current_time)
                  time.sleep(1)
                  print('not time\n')
                  

'''
from socket import socket, AF_INET, SOCK_STREAM

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 5000))

msg = input('What is your name: ')
sock.send(bytes(msg, 'UTF-8'))
sock.recv(8192)
'''
