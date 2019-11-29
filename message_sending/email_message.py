
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from os.path import abspath, dirname
import sys
sys.path.append("..")
from message_sending.plot_data import get_graph_data
from const_ import const
import time



class EmailSending():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = const.EMAIL_USER_NAME
        self.passwd = const.EMAIL_PASS_WORD
        self.from_email = self.username
        self.to_list = []
        
    
    def get_user_list(self):
        
        db = MySQLdb.connect(host = "52.43.93.127", user = "root", passwd = "ljm960704519", db = "server")
        cursor = db.cursor()
        sql = "select * from users;"
        cursor.execute(sql)
        users_list = cursor.fetchall()
        db.close()
        email_list = []
        for u in users_list:
            email_list.append(u[1])
        self.to_list = email_list.copy()
        
        
    def send_alert_email(self, time_str, value, msg_type = const.TEMPERATURE):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Server room {msg_type} alert".format(msg_type= msg_type))
        self.get_user_list()
        text = const.ALEART_TEMPLET.format(msg_type_cap = msg_type, time_str=time_str, msg_type=msg_type, value=value)
        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)
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

    
    def send_confirm_email(self, user_name, user_eamil):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Subscribe Confirmation")
        info = get_graph_data()
        text = const.REPORT_TEMPLET.format(user_name = user_name, \
        welcome = "Welcome to subscribe message notification from server room monitor!",\
        start_time = info["start_time"],\
        end_time = info["end_time"],\
        temp_avg = info["temp_avg"],\
        temp_max = info["temp_max"],\
        temp_min = info["temp_min"],\
        humi_avg = info["humi_avg"],\
        humi_max = info["humi_max"],\
        humi_min = info["humi_min"])
            
        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)
        graph = open(abspath(dirname(__file__))+"/graphs/temp_humi_graph.png", "rb").read()
        graph_part = MIMEApplication(graph)
        graph_part['Content-Disposition'] = 'attachment; filename="Temp_Humi_graph.png"' 
        msg.attach(graph_part)

        self.to_list.clear()
        self.to_list.append(user_eamil)
        
        
        try:
            email_conn = smtplib.SMTP(self.host, self.port)
            email_conn.ehlo()
            email_conn.starttls()
            email_conn.login(self.username, self.passwd)
            email_conn.sendmail(self.from_email, user_eamil, msg.as_string())
            print("Send the email meassage successfully!")
        except smtplib.SMTPException:
            print ("Fail to send message")
            email_conn.quit()
        



        

