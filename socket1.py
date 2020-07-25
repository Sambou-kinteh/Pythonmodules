 # first of all we are importing the socket library

import socket

#next create a socket object
s = socket.socket()
if s:print("socket successfully created")

#reserve a port number
port = 1456

#bind to the port
a = s.bind(('', port))
if a:print("socket binded to %s" %(port))

#put the socket into listening mode

b = s.listen(5)
if b:print("socket is listening")

#a forever loop untill we exit
#or an error occurs

while True:
	#establish connection with client
	c, addr = s.accept()
	print("got connection from", addr)
