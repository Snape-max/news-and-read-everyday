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
host_server = 'smtp.163.com'

sender_qq = 'wpw12138@163.com'

pwd = 'ARLYBVGDHDJELLSC'

sender_qq_mail = 'wpw12138@163.com'

receiver = 'ssnape@qq.com'
receiver1 = '2926083239@qq.com'
        
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
smtp.sendmail(sender_qq_mail,receiver1, msg.as_string())
smtp.quit()
