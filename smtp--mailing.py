
import smtplib
import socket

sender = 'from@fromdomain.com'
receivers = 'to@todomain.com'

host = ''
port = 25
local_hostname = 'localhost'

message = '''From: From Person
<from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test


This is an e-mail message to be sent in HTML
format

<b>This is HTML message</b>
<h1>This is headline.</h1>

'''

try:
    
    smtpObj = smtplib.SMTP(local_hostname)
    smtpObj.sendmail(sender, receivers, message)

    print('Successfully sent e-mail')

except Exception as msg:
    print('Error: Unable to send e-mail due to [ %s ]' % (msg))
