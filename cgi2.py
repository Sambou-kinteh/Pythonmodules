
import cgi,cgitb

form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvvalue('last_name')

