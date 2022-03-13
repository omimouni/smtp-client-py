#!/usr/bin/env python3

import smtplib
from time import sleep

host = "smtp.mailtrap.io"
port = 2525
username = "8866c5d5021bb6"
password = "8da6c5dc7fa0cf"

sender = "Oumar Mimouni <oumar@noops.ma>"
receiver = [
  "test2@gmail.com",
  "test3@gmail.com",
  "test4@gmail.com",
  ]

subject = "Hello World"
message = "Hello World it's me"


mysmtp = None
body = """\
Subject: %s
Content-type: text/html
MIME-Version: 1.0
To: %s
From: %s

%s"""

try:
  mysmtp = smtplib.SMTP(host, port)
  mysmtp.login(username, password)
except Exception as e:
  print(e)

for i in range(len(receiver)):
  mysmtp.sendmail(sender, receiver[i], body % (subject, receiver[i], sender, message))
  print("sent to: " + receiver[i])
  sleep(.2)