import smtplib

mailfrom = "zrg3@njit.edu"
msg = "Hello"

host = "smtp.gmail.com" 
port = 587
username = "zeelphysics@gmail.com"
password = "zrg04032545" 


email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(mailfrom,username,msg)
email_conn.quit()


from smtplib import SMTP
email_conn2 = SMTP(host,port)
email_conn2.ehlo()
email_conn2.starttls()
email_conn2.login(username,password)
email_conn2.sendmail(mailfrom,username,msg)
email_conn2.quit()


from smtplib import SMTP, SMTPAuthenticationError, SMTPException

pass_wrong = SMTP(host,port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username,"wrong_password")
    pass_wrong.sendmail(mailfrom,username,msg)
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("An error occured")
pass_wrong.quit()