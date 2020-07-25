import cgi
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
test();
