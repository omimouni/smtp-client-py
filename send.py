#!/usr/bin/env python3

import smtplib

sender = "Oumar Mimouni <oumar@noops.ma>"
receiver = "Test User <test2@gmail.com>"

subject = "Hello World"
message = "Hello World it's me"

body = f"""\
Subject: {subject}
To: {receiver}
From: {sender}

{message}"""

# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#   server.login("8866c5d5021bb6", "8da6c5dc7fa0cf")
#   server.sendmail(sender, receiver, message)

try:
  mysmtp = smtplib.SMTP("smtp.mailtrap.io", 2525)
  mysmtp.login("8866c5d5021bb6", "8da6c5dc7fa0cf")

  mysmtp.sendmail(sender, receiver, body)
except Exception as e:
  print(e)