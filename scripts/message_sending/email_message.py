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

    def send_email(self, time,  value, type = "tempreature"):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Server Room Temprature Alert")

        text = """
        <p1>Server Room Alert:</p1></br>
        <p2>{}</p2><br/>
        <p2>Tempterature monitor shows that the current {} is {} °C</p2></br>
        <p2>please check the server room immediately!"</p2>
        """.format(time, type, value)

        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)

        try:
            graph= open(abspath(dirname(__file__))+"\\graphs\\temp_humi_graph.png", "rb").read()
            
        except e:
            print(e)
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
