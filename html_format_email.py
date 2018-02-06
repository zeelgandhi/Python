from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mailfrom = "zrg3@njit.edu"
msg = "<b>Hello</b></br> there is an email message"

host = "smtp.gmail.com" 
port = 587
username = "zeelphysics@gmail.com"
password = "zrg04032545" 
try:
    email_conn = smtplib.SMTP(host,port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username,password)
    the_msg = MIMEMultipart("alternative")
    the_msg["Subject"] = "Testing python"
    the_msg["From"] = mailfrom
    the_msg["To"] = username

    plain_txt = "Testing the message"
    html_txt = """
    <html>
    <head></head>
    <body>
    <p>Hey!!<br>
    Testing this email <b>message</b>, Made by Zeel!!
        </p>
    </body>
    </html>
    """
    part_1 = MIMEText(plain_txt,'plain')
    part_2 = MIMEText(html_txt,"html")
    the_msg.attach(part_1)
    the_msg.attach(part_2)
    email_conn.sendmail(mailfrom,username,the_msg.as_string())
    email_conn.quit()
except smtplib.SMTPException:
    print("Error sending message")