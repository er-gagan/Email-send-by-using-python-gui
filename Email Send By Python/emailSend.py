import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def EmailSend(emailVar,subjectVar,Msg):
    email_user = "gaganaggarwal121@gmail.com"
    email_send=emailVar
    subject=subjectVar
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject']=subject
    message = Msg
    msg.attach(MIMEText(message,'plain'))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,"AAA111...1")
    server.sendmail(email_user,email_send,text)
    server.quit()