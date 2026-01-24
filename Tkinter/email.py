import smtplib

sender = "sender.com"
reciever = "reciever.com"
password = "yourpassword"
subject = "Text Mail"
body = "This is Just a Test Mail, Please Do Not Reply"


message =f"""From: {sender}
To: {reciever}
Subject: {subject} \n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()


try:  
    server.login(sender, password)
    print("Logged In")
    server.sendmail(sender, reciever, message)
    print("Email has been sent")
except Exception:
    print("ERROR")