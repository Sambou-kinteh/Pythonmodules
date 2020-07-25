import threading, time

#the main function

def classfunction(target_func):
    def wrapper_func(x, y):
        print(target_func(x, y))

    return wrapper_func
        
            
        




@classfunction
def myfunction(x, y):
    '''print("STart of a thread\n")
    time.sleep(3)
    print("eNd of the thread\n")'''
    #next()
    for i in range(x):
        print("Loop %d" % i)
        print("i is %d" % i)
        print("y is %d" % y)
        yield i*y

threads = []

#To run 5 times concurrent sessions of myfunction
for i in range(5):
    th = threading.Thread(target = myfunction(x, y))
    th.start()
    threads.append(th)

#waiting for all threads to terminate
for th in threads:
    th.join()


