import time, threading

exitFlag = 0


class myThread(threading.Thread):
     def __init__(self, ThreadId, name, counter):
        threading.Thread.__init__(self)

        self.ThreadId = ThreadId
        self.name = name
        self.counter = counter

     def run(self):
          print(' Starting %s ' % (self.name))
          print_name(self.name, self.counter, 5)
          print (' Exiting %s ' % (self.name))

def print_name(threadName, counter, delay):

     while counter:
          if exitFlag:
               threadName.exit()

          time.sleep(delay)
          print('%s: %s ' % (threadName, time.ctime(time.time())))

          counter -= 1

#Create new thread objects
thread1 = myThread(1, 'Thread-1', 2)
thread2 = myThread(2, 'Thread-2', 4)

#Start The process

thread1.start()
thread2.start()
thread2.is_alive()

print('Exiting Main Thread ')


               
