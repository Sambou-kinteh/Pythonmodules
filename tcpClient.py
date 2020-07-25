import socket

s = socket.socket()

def Main():
    host = '127.0.0.1'
    port = 5000

    s.connect((host, port))

    #message = input('Input: ')
    '''while (True):
        data = s.recv(1024)
        message = input('Input: ')
        s.send(bytes(message, 'ANSI'))
        data = s.recv(1024)
        print('Server:   %s' % ((data)))
        message = input('Input: ')'''

def byte_remover(data):
   ''' ex = ' b"' '
    no_b = ' '
    for i in data:
        if i not in ex:
            no_b += (i + ' ')
    return no_b'''
   if data.startswith(b):
       datalist = list(data)
       datalist[0] = ' '
       for i in datalist:
           print(i, end='')
  

def Chatting():
    while(True):
        try:
            import time

            time.sleep(1.5)

        except Exception:
            print('logCat: %s at %s' %(msg, time.ctime(time.time())))
            

        data = s.recv(1024)
        print('Server:  %s\n' %(str(data)))
        c1 = input('Input: ')
        print('Sending:  %s\n' %(c1))
        s.send(bytes((c1), 'ASCII'))

    
    s.close()


    

if __name__ == '__main__':
    Main()
    Chatting()
