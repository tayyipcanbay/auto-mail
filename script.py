import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import time
import os

def read_mail_list():
    with open('mail_list.txt', 'r') as f:
        lines = f.readlines()
        mail_list = [line.strip() for line in lines]
        return mail_list

def get_sender_info():
    sender = input('Mail adresinizi giriniz: ')
    password = input('Mail şifrenizi giriniz (Uygulama Şifresi): ')
    return sender, password

def get_message_info():
    subject = input('Mail konusunu giriniz: ')
    print('Mail HTML içeriği için mail.html dosyasını düzenleyiniz.')
    time.sleep(3)
    print("Mail'e eklemek istediğiniz dosyaları attachments klasörüne ekleyiniz.")
    time.sleep(3)
    return subject

def read_attachments():
    attachments = []
    for file in os.listdir('attachments'):
        part= MIMEText(file)
        attachments.append(part)
    return attachments

def read_html():
    with open('mail.html', 'r') as f:
        html = f.read()
    return html

def create_message(subject,sender,to):
    msg= MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    html= MIMEText(read_html(), 'html')
    msg.attach(html)
    # read the files in the attachments folder and attach them to the email
    for file in os.listdir('attachments'):
        with open(f'attachments/{file}', 'rb') as f:
            part = MIMEApplication(f.read(), Name=file)
        part['Content-Disposition'] = f'attachment; filename="{file}"'
        msg.attach(part)
    return msg

def send_mail(msg,server):
    try:
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except Exception as e:
        print(e)

def init(sender,password):
    server = smtplib.SMTP ('smtp.yandex.ru', 587)
    server.ehlo () 
    server.starttls () 
    server.login (sender, password)
    server.set_debuglevel(1)
    return server

def show_time_boiii():
    sender,password=get_sender_info()
    subject=get_message_info()
    mail_list=read_mail_list()
    for mail in mail_list:
        msg=create_message(subject,sender,mail)
        server=init(sender,password)
        send_mail(msg,server)
        print(f'{mail} adresine mail gönderildi.')
        time.sleep(3)
    print('Tüm mail gönderildi.')

show_time_boiii()
