'''import cgi
import HTMLParser
top = HTMLParser.HTMLParser
def test():
 print "content-type:text/html\r\n\r\n"
 print'<html>'
 print'<head>'
 print'<title> hello,world - first cgi program<title>'
 print'</head>'
 print'<boby>'
 print'<h2>Hello world! - first cgi program'
 print'</body>'
 print'</html>'
test();''''
'''# Import modules for CGI handling  
import cgi, cgitb   
# Create instance of FieldStorage  
form = cgi.FieldStorage()   
# Get data from fields 
first_name = form.getvalue('first_name') 
last_name  = form.getvalue('last_name')  
print "Content-type:text/html\r\n\r\n" 
print "<html>"'''

# Import modules for CGI handling  
import cgi, cgitb   
# Create instance of FieldStorage  
form = cgi.FieldStorage()   
# Get data from fields 
first_name = form.getvalue('first_name') 
last_name  = form.getvalue('last_name')  
print "Content-type:text/html\r\n\r\n" 
print "<html>" 
print "<head>" 
print "<title>Hello - Second CGI Program</title>" 
print "</head>" 
print "<body>" 
print "<h2>Hello %s %s</h2>" % (first_name, last_name) 
print "</body>" 
print "</html>"


'''
 ##download path
# HTTP Header 
print "Content-Type:application/octet-stream; name=\"FileName\"\r\n"; 
print "Content-Disposition: attachment; filename=\"FileName\"\r\n\n";  
# Actual File Content will go hear. 
fo = open("foo.txt", "rb")  
str = fo.read(); 
print str  
# Close opend file 
fo.close()'''
