from flask import Flask, Response
import Adafruit_DHT
import json

web = Flask(__name__)

def c_to_f(c):
    f = round(32+1.8*c)
    return f

@web.route('/api/gettmp',methods=["GET", "POST"])
def draw_stone():
    d_hum,d_temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
    d_hum = d_hum
    d_temp = c_to_f(d_temp)
    data = [d_temp,d_hum]
    return Response(json.dumps(data),  mimetype='application/json')


@web.route('/')
def staff_page():
    return web.send_static_file('index.html')


