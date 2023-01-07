from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import requests,bs4


url = 'https://meiriyiwen.com/random/iphone'
html = requests.get(url)
a = bs4.BeautifulSoup(html.content,features="html.parser")
b = a.select('p')
c = str(a.select('title')).replace('<title>','').replace('</title>','').replace(' @每日一文官网 ','').replace('[','').replace(']','')
k = ''
for i in b:
    k+=str(i)

k = "<style type='text/css'>p{text-indent:2em;}</style>"+k
#the smtp server, you should change to yours
host_server = 'smtp.example.com'
#sender is the sender's email 
sender = 'your-sender-email@example'
#pwd
pwd = 'your pwd'
#receiver mail
receiver = 'your-receiver-email@example.com'
#the content of the eamil
mail_content = k
#the title of the email
mail_title = c
#ssl login
smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender, pwd)

msg1 = MIMEText(mail_content, "html", 'utf-8')
msg1["Subject"] = Header(mail_title, 'utf-8')
msg1["From"] = 'Reading'
msg1["To"] = receiver

smtp.sendmail(sender_qq_mail, receiver, msg1.as_string())
smtp.quit()


