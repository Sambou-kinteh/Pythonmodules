#<---------------Do --Create a module which will connect to google and then do a search then return the results------------------------->
#lets coonect to google
import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("socket successfully created")
except socket.error as err:
	print("socket creation failed with an error %s" %(err))
#default port for the socket
port = 80

try:
	host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror as msg:
	print("there was an error resolving the host [ %s ]" % (msg))
	sys.exit()
#connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connect to google \ on port == %s" %(host_ip))

#def __init__(self, age, height, place, ids )
