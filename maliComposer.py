# https://docs.python.org/3/library/email.examples.html
# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

import markdown

from settings import (HOST, PORT,
                      SENDER, DISPLAY_NAME, PASSWORD,
                      RECIPIENT, MESSAGE_FILE)


with open(MESSAGE_FILE) as file:
    message = file.read()


server = SMTP(host=HOST, port=PORT)
server.connect(host=HOST, port=PORT)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user=SENDER, password=PASSWORD)

multipart_msg = MIMEMultipart("alternative")

multipart_msg["Subject"] = message.splitlines()[0]
multipart_msg["From"] = DISPLAY_NAME + f' <{SENDER}>'
multipart_msg["To"] = RECIPIENT

text = message
html = markdown.markdown(text)

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

multipart_msg.attach(part1)
multipart_msg.attach(part2)


server.sendmail(SENDER, RECIPIENT, multipart_msg.as_string())

print('Sent email successfully!')