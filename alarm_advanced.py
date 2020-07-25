import datetime, winsound, time

#alarm_hour = input('HOUR: ')
#alarm_minute = input('MINUTE: ')
#alarm_second = input('SECOND: ')
#sound file for the extraction of sound ofr your alarm
file = "C:\\Users\\Sambou\\Desktop\\W3SCHOOLS\\gggg\\www.w3schools.com\\jsref\\horse.wav"
#this is a short documentation of the alarm
about = '''This a class object that sets an alarm time for you, this SetAlarm accepts three positional arguments
and an optional last one
1. Hours: Specifies an hour input type of  integer for the alarm which is required.
2. Minutes: Specifies a minute of integer input type which must be given.
3. Seconds: Specifies a specific second to stop timing which also is required.
4. Sound_File: An optional sound file input which must be in the (.wav) file format.
The sound file needs not to be specified if wished, but if to be, then consider writing the complete
name of the sound file i.e ( C:...\\\..\\\ ... \\\ (file name).wav ) 
Lastly the dir should be seperated by two leading backslash (\\\)
Hope you benefited from Sam.tips, now you can go on and set an alarm by implementing the main class::;;
SetAlarm()
You can also enter the Browser_Info() function to invoke the web browser'''

#<____________________CLASS CODE BLOCK_________________________>

def Tips():
      print(about)

def Browser_Info():
      try:
            import webbrowser, time
            print('Redirecting You To My Page To Get Started;;;:::;;;:::\n')
            time.sleep(3)
            return webbrowser.open('www.stp.edu.gm')
      except Exception as msg:
            print(msg)


class SetAlarm:
      '''->hrs -- the hour of alarm
      ->mins -- minute of preferred alarm
      ->secs -- seconds
      ->sound_file -- optional alarm tune'''
      
      def __init__(self, hours, mins, sec = 0, sound_ref = file):
            self.hours = hours
            self.mins = mins
            self.sec = sec
            
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
                              SetAlarm.alarm(self, sound_ref)
                              while(True):
                                    option = input('DO YOU WANT TO SNOOZE(y/Y or n/N)\n')
                                    if option == 'y' or option == 'Y':
                                          SetAlarm.snooze(self, sound_ref)
                                    else:
                                          alert = True
                                          break
                  else:
                        #print(current_time)
                        time.sleep(1)
                        print('not time\n')


            
      def alarm(self, sound_file):
            self.sound_file = sound_file
            for i in range(0, 10):#while(True):
                  
                  i = winsound.PlaySound(self.sound_file , 1)
                  time.sleep(1)
                  return i

      def snooze(self, sound_file):
            self.sound_file = sound_file
            global snooze_min
            snooze_min = input('HOW MANY MINUTES\n')
            snooze_min = int(snooze_min)
            snooze_sec = snooze_min * 60
            if snooze_min > 1:
                  print('SNOOZE Set For: %s mins\n' %(snooze_min))
            else:
                  print('SNOOZE Set For: %s min\n' %(snooze_min))
            time.sleep(snooze_sec)
            return winsound.PlaySound(self.sound_file, 1)



##make a funcrtion and define in in there




         
            
