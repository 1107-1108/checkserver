##作者:1107
#Version Alpha1.0.0
#使用本程序请遵循MIT License

import socket
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import time
def check_port(ip, port):
    a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(200)
    try:
        a.connect((ip, int(port)))
        a.shutdown(socket.SHUT_RDWR)
        return True
    except:
        return False

#邮箱配置部分
mail_host = "smtp.163.com"
mail_sender = "114514@163.com"
mail_license  = ""#邮箱授权码不是密码
recver = [""]
mm = MIMEMultipart('related')
subject_content = "服务器检测"

#发送邮件
while True:
    localtime = time.asctime( time.localtime(time.time()) )
    a =check_port('1107.siwg.top', 80)
    if a == True:
        body_content = f"{localtime}服务器能ping到"
    elif a == False:
        body_content = f"{localtime}服务器无法连接！"
    mm = MIMEText(body_content, "plain","utf-8")
    mm["From"] = "114514@qq.com"
    mm["To"] = "receiver_1_name<114514@qq.com>"
    mm["Subject"] = Header(subject_content, 'utf-8')
    try:
        stp = smtplib.SMTP_SSL(mail_host, 994)
        stp.login(mail_sender, mail_license)
        stp.sendmail(mail_sender, recver, mm.as_string())
        print(f"{localtime}邮件发送成功")
        stp.quit()
        a = None
        time.sleep(42300)
    except:
        print(f"{localtime}邮件发送失败")