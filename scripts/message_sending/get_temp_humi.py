
import Adafruit_DHT
import time
import threading

class GetTempHumi(threading.Thread):
    '''
    Using Adafruit_DTH library to collect data from the DHT11 Temprature & Humidity sensor
    '''
    def __init__(self, sensor = Adafruit_DHT.DHT11, pin = 3, alert_c_temp = 30 ):
        threading.Thread.__init__(self)
        self.sensor = sensor # set sensor type  
        self.pin = pin #set GPIO pin
        self.alert_c_temp = alert_c_temp # set threshold temprature
        self.alert = False # if temprature exceeds the threshold, set alert true
        self.temperature = None
        self.humidity = None

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    def run(self):
        print("Initialize the sensor... Please wait for senconds")
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        time.sleep(2) # The first data can be not accurate, we skip it
        while True:
            self.humidity, self.temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            if self.humidity is not None and self.temperature is not None:
                t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+":"
                print(t)
                print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(self.temperature, self.humidity)) 
                if self.temperature>=self.alert_c_temp:
                    self.alert = True             # set alert true if it exceeds the threshold
                else:
                    self.alert = False
            else:
                print('Failed to get reading. Try again!')


