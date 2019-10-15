
import Adafruit_DHT
import time
import threading
import sys
sys.path.append("..")
from os.path import abspath, dirname
from const_ import const
import csv

class GetTempHumi(threading.Thread):
    '''
    Using Adafruit_DTH library to collect data from the DHT11 Temprature & Humidity sensor
    '''
    def __init__(self, sensor = Adafruit_DHT.DHT11, pin = 3, alert_f_temp = 90 ):
        threading.Thread.__init__(self)
        self.sensor = sensor # set sensor type  
        self.pin = pin #set GPIO pin
        self.alert_f_temp = alert_f_temp # set threshold temprature
        self.alert = False # if temprature exceeds the threshold, set alert true
        self.temperature = None
        self.humidity = None
    '''
    def add_recode(self, data_dic:dict, time_info):
    
    def parse_time_str(self, time_str:str):
        part_1 = time_str.split("-")
        year = part_1[0]
        month = part_1[1]
        day = part_1[2]
        part_2 = time_str.split(' ')[1].split(':')
        hour = part_2[0]
        minute = part_2[1]
        second = part_2[2]
        return (int(year), int(month), int(day), int(hour), int(minute))
    '''

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    def run(self):
        def c_to_f(c):
            f = round(32+1.8*c)
            return f
        print("Initialize the sensor... Please wait for senconds")
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        time.sleep(2) # The first data can be not accurate, we skip it
        csv_file = open(abspath(dirname(__file__))+"data_recod.csv", "a")
        csv_writer = csv.writer(csv_file)
        while True:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            self.temperature = c_to_f(self.temperature)
            if self.humidity is not None and self.temperature is not None:
                t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+

                data_row = [t, self.temperature, self.humidity]
                print(data_row)
                csv_writer.writerow(data_row)
                csv_file.flush()
                if self.temperature>=self.alert_f_temp:
                    self.alert = True             # set alert true if it exceeds the threshold
                else:
                    self.alert = False
            else:
                print('Failed to get reading. Try again!')


