import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
msg = EmailMessage()
msg["from"] = "*****"
msg["subject"] = "Hey hey"
msg["to"] = "******@gmail.com"

msg.set_content(html.substitute(name="Guy"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as s:
    s.ehlo()
    s.starttls()
    s.login("email", "password")
    s.send_message(msg)
print("Success!")
