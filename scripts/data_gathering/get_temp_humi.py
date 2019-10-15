
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
  

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    def run(self):
        def c_to_f(c):
            f = round(32+1.8*c)
            return f
        print("Initialize the sensor... Please wait for senconds")
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        time.sleep(2) # The first data can be not accurate, we skip it
        csv_file = open(abspath(dirname(__file__))+"/data_record.csv", "a")
        csv_writer = csv.writer(csv_file)
        while True:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            self.temperature = c_to_f(self.temperature)
            if self.humidity is not None and self.temperature is not None:
                t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
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


