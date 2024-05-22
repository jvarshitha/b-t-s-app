import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('jyosrithamopidevi04@gmail.com','ztho owib bwpo fkmb')
    msg=EmailMessage()
    msg['From']='jyosrithamopidevi04@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()