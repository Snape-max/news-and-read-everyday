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
        #qq邮箱smtp服务器
k = "<style type='text/css'>p{text-indent:2em;}</style>"+k
host_server = 'smtp.163.com'
        #sender_qq为发件人的qq号码
sender_qq = 'wpw12138@163.com'
        #pwd为qq邮箱的授权码
pwd = 'ARLYBVGDHDJELLSC'
        #发件人的邮箱
sender_qq_mail = 'wpw12138@163.com'
        #收件人邮箱
receiver = 'ssnape@qq.com'
receiver2 = '1797552779@qq.com'
        #邮件的正文内容
mail_content = k
        #邮件标题
mail_title = c

         #ssl登录
smtp = SMTP_SSL(host_server)
        #set_debuglevel()是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
smtp.set_debuglevel(0)
smtp.ehlo(host_server)
smtp.login(sender_qq_mail, pwd)

msg1 = MIMEText(mail_content, "html", 'utf-8')
msg1["Subject"] = Header(mail_title, 'utf-8')
msg1["From"] = 'Reading'
msg1["To"] = receiver

msg2 = MIMEText(mail_content, "html", 'utf-8')
msg2["Subject"] = Header(mail_title, 'utf-8')
msg2["From"] = 'Reading'
msg2["To"] = receiver2
smtp.sendmail(sender_qq_mail, receiver, msg1.as_string())
smtp.sendmail(sender_qq_mail, receiver2, msg2.as_string())
smtp.quit()


