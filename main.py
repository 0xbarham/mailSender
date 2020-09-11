import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import config


server = smtplib.SMTP('SMTP Server Address: PORT')

server.ehlo()
server.starttls()

server.login(config.fromEmail, config.password)

msg = MIMEMultipart()

msg['From'] = "Sender's Name"
msg['To'] = config.toEmail
msg['Subject'] = 'Subject of the message'

with open('msg.txt', 'r') as f:
    message = f.read()
    
msg.attach(MIMEText(message, 'plane'))

filename = 'Test.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')

p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header("Content-Disposition", f'Attachment; filename = {filename}')

msg.attach(p)

text = msg.as_string()

server.sendmail(config.fromEmail, config.toEmail, text)