import smtplib
from email.mime.text import MIMEText
from email.header import Header

class EmailSending():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = "serverroominform.ksu@gmail.com"
        self.passwd = "seniorproject"
        self.from_email = self.username
        self.to_list = ["jli36@students.kennesaw.edu", "jiamingli9674@gmail.com"]

    def send_emai(self, time,  value, type = "tempreature"):
        msg = """
        <p1>Server Room Alert:</p1></br>
        <p2>{}</p2><br/>
        <p2>Tempterature monitor shows that the current {} is {} °C</p2></br>
        <p2>please check the server room immediately!"</p2>
        """.format(time, type, value)
        message = MIMEText(msg, "html", "utf-8")
        message["From"] = Header("Server Room Monitor")
        message["To"] = Header("Server Room Administrator")
        message["Subject"] = Header("Server Room Temprature Alert")
        try:
            email_conn = smtplib.SMTP(self.host, self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.username, self.passwd)
            email_conn.sendmail(self.from_email, self.to_list, message.as_string())
            print("Send the email meassage successfully!")
            print(msg)
        except smtplib.SMTPException:
            print ("Fail to send message")
        email_conn.quit()
