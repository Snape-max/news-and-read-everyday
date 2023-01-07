from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
import requests,bs4
import time
url = 'https://news.china.com/'
html = requests.get(url)
a = bs4.BeautifulSoup(html.content,features="html.parser")
b = a.find_all('div',class_='focus_side')
c = str(b).replace('[','').replace(']','')
host_server = 'smtp.163.com'  # you should change to your-email-sender's host server

sender_qq = 'youremail@example.com'

pwd = 'yourpasswd' #so it is better to set your repository inprivate

sender_qq_mail = 'your-sender-email@example.com'

receiver = 'your-receiver-email@example.com'
        
mail_content = c

mail_title = 'News'


smtp = SMTP_SSL(host_server)

smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq_mail, pwd)

msg = MIMEText(mail_content, "html", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = 'News'
msg["To"] = receiver
smtp.sendmail(sender_qq_mail, receiver, msg.as_string())
smtp.quit()
