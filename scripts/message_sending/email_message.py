
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import abspath, dirname
import sys
sys.path.append("..")

from const_ import const




class EmailSending():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = const.EMAIL_USER_NAME
        self.passwd = const.EMAIL_PASS_WORD
        self.from_email = self.username
        self.to_list = ["jli36@students.kennesaw.edu", "jiamingli9674@gmail.com"]

    def send_email(self, time_str,  value, msg_type = "tempreature"):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Server Room {msg_type_cap} Alert".format(msg_type_cap= "Temperature"))

        text = const.ALEART_TEMPLET.format(msg_type_cap = "Temperature", time_str=time_str, msg_type=msg_type, value=value)

        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)
        print(abspath(dirname(__file__))+"/graphs/temp_humi_graph.png")
        graph = open(abspath(dirname(__file__))+"/graphs/temp_humi_graph.png", "rb").read()
            
        
        graph_part = MIMEApplication(graph)
        graph_part['Content-Disposition'] = 'attachment; filename="Temp_Humi_graph.png"' 
        msg.attach(graph_part)

        try:
            email_conn = smtplib.SMTP(self.host, self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.username, self.passwd)
            email_conn.sendmail(self.from_email, self.to_list, msg.as_string())
            print("Send the email meassage successfully!")
        except smtplib.SMTPException:
            print ("Fail to send message")
        email_conn.quit()


