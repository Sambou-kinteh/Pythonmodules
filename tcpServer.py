import socket

s = socket.socket()
host = '127.0.0.1'
port = 5000

s.bind((host, port))

s.listen(1)
c, addr = s.accept()

def Main():
    
    print('Connection from %s' % (str(addr)))


def byte_remover(data):
    ex = ''' b" ' '''
    no_b = ' '
    for i in str(data):
        if i not in ex:
            no_b += i 
    return no_b


def Messaging():
    while(True):
        try:
            import time

            time.sleep(1)

        except Exception:
            print('logCat: %s at %s' %(msg, time.ctime(time.time())))
            
        m1 = 'What is your name User'
        print('Sending:  %s' %(m1))
        c.send(bytes((m1), 'ASCII'))
        data = c.recv(1024)
        print('%s: %s' %(byte_remover(data.upper()), data))

    
    c.close()
    
    

if __name__ == '__main__':
    Main()
    Messaging()
