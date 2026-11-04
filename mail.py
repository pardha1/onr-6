#smtp --->simple mail transfer protocol

'''
import smtplib
from email.mime.text import MIMEText

#print(help(smtplib))

#to connect with server:
server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()


#user -details:
From="gopikrishna@codegnan.com"
password="sfaj poxb rnbi feqt"


#login to server
server.login(From,password)


To=["pavanipolisetty514@gmail.com","lalithaputsala03@gmail.com","kavyasri.akavarapu@gmail.com","singamsetty.lasya@gmail.com"]
subject="MURUSU"
info=" YOU got a 10 lpa job \n role: python full stack developer  "


for users in To:
    msg=MIMEText(info)
    msg["from"]=From


    msg["subject"]=subject
    msg["to"]=users


    #send to mail
    server.sendmail(From,users,msg.as_string())
    print(f"mail succefully sent  to {users}")

server.quit()
'''




