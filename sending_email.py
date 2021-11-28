import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""
sender = 'szachowicz.g@poczta.fm'
receiver = 'rozpadek@poczta.fm'
try:
   smtpObj = smtplib.SMTP_SSL(host='poczta.interia.pl', port=465)
   smtpObj.login(sender, 'zolwik83.interia')
   smtpObj.sendmail(sender, receiver, message)
   print("Successfully sent email")
except smtplib.SMTPException as ex:
   print("Error: unable to send email")
   print(ex)

