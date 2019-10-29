from message_sending.email_message import EmailSending
from message_sending.text_message_sending import  MessageSending
from data_gathering.get_temp_humi import GetTempHumi
from message_sending.plot_data import get_graph_data
import time
import threading
from backend import web

class Monitor(threading.Thread):
    """
    Main thread
    Monitor the alert variable in GetTempHumi class
    Send messages when there is an alert
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.message_sending = MessageSending()
        self.email_sending = EmailSending()
        self.sensor = GetTempHumi()
        self.delay = 120 # Delay time of every message, seconds
        
        

    def run(self):
        self.sensor.start()
        while True:
            if self.sensor.alert:
                t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
                self.message_sending.send_message(time = t, value=self.sensor.temperature)
                self.email_sending.send_alert_email(time_str = t, value=self.sensor.temperature)
                time.sleep(self.delay) # dealy for a while
                self.delay *= 2 # every time send the message, double the delay time
                

if __name__ == "__main__":

    
    monitor = Monitor()
    monitor.start()
    web.run("127.0.0.1", 5000)

    #em = EmailSending()
    #em.send_report_email(8)
    

