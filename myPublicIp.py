import urllib.request
import json
import smtplib
import time

def getMyPublicIpAddress():
    url = 'https://httpbin.org/ip'
    response = urllib.request.urlopen(url)
    data = response.read()
    data = json.loads(data)
    return data['origin']

myPublicIp = None
newPublicIp = None

def sendNewIpAddress(ipaddr):
    senderEmail = 'gregor.wysylacz@poczta.fm'
    receiverEmail = 'rozpadek@poczta.fm'
    password = "Wojtowa#siekiera"
    hostSmtp = 'poczta.interia.pl'
    message = """From: Thermoberry <szachowicz.g@poczta.fm>
To: thermoberry <rozpadek@poczta.fm>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

<b>Nowy adres IP</b>
<h1>"""

    message += ipaddr + '</h1>'
    print(message)
    print(password)

    try:
       smtpObj = smtplib.SMTP_SSL(host=hostSmtp, port=465)
       smtpObj.login(senderEmail, password)
       smtpObj.sendmail(senderEmail, receiverEmail, message)
       print("Successfully sent email")
    except smtplib.SMTPException as ex:
       print("Error: unable to send email")
       print(ex)


while True:
    newPublicIp = getMyPublicIpAddress()
    print('adres publiczny:', newPublicIp)
    if newPublicIp != myPublicIp:
        myPublicIp = newPublicIp
        sendNewIpAddress(myPublicIp)
    time.sleep(36000)
