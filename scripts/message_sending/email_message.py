
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
import pandas as pd
import numpy as np




class EmailSending():
    def __init__(self):
        self.host = "smtp.gmail.com"
        self.port = "587"
        self.username = const.EMAIL_USER_NAME
        self.passwd = const.EMAIL_PASS_WORD
        self.from_email = self.username
        self.to_list = ["jiamingli9674@gmail.com"]

    def send_alert_email(self, time_str, value, msg_type = const.TEMPERATURE):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Server room {msg_type} alert".format(msg_type= msg_type))

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

    def send_report_email(self, data_num):
        msg = MIMEMultipart()
        msg["From"] = Header("Server Room Monitor")
        msg["To"] = Header("Server Room Administrator")
        msg["Subject"] = Header("Server room daily report")

        csv_file = pd.read_csv(abspath(dirname(dirname(__file__)))+"/data_gathering/data_record.csv")
        data = csv_file.tail(data_num).to_dict("list")
        time_list = data[const.TIME]
        temp_list = data[const.TEMPERATURE]
        humi_list = data[const.HUMIDITY]
        get_graph_data(time_list, temp_list ,humi_list)

        temp_max = max(temp_list)
        temp_min = min(temp_list)
        temp_mean = round(np.mean(temp_list))

        humi_max = max(humi_list)
        humi_min = min(humi_list)
        humi_mean = round(np.mean(humi_list), 2)

        text = const.REPORT_TEMPLET.format(temp_avg=temp_mean, temp_max=temp_max, temp_min=temp_min,\
             humi_avg = humi_mean, humi_max=humi_max, humi_min=humi_min)
            
        text_part = MIMEText(text, "html", "utf-8")
        msg.attach(text_part)
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


