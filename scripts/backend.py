from flask import Flask, Response
import Adafruit_DHT
import json

web = Flask(__name__)


@web.route('/api/gettmp',methods=["GET", "POST"])
def draw_stone():
    d_hum,d_temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)
    d_hum = round(d_hum,2)
    d_temp = round(d_temp,2)
    data = [d_temp,d_hum]
    return Response(json.dumps(data),  mimetype='application/json')


@web.route('/')
def staff_page():
    return web.send_static_file('index.html')


