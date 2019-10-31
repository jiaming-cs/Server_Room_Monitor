from flask import Flask, Response, request
import Adafruit_DHT
import json
import pandas as pd
from os.path import abspath, dirname
from const_ import const
import csv


web = Flask(__name__)




@web.route('/api/gettmp',methods=["GET", "POST"])
def draw_stone():
    csv_file = pd.read_csv(abspath(dirname(__file__))+"/data_gathering/data_record.csv")
    data_list = csv_file.tail(1).to_dict("list")
    d_temp = data_list[const.TEMPERATURE]
    d_hum = data_list[const.HUMIDITY]
    data = [d_temp,d_hum]
    return Response(json.dumps(data),  mimetype='application/json')


@web.route('/')
def staff_page():
    return web.send_static_file('index.html')

@web.route("/subscribe/", methods = ["POST"])
def subscribe():
    postData = request.form 
    name = request.form.get('Name') 
    email = request.form.get('Email')
    phone = request.form.get('Phone Number')
    print(name)
    print(email)
    print(phone)
    with open("/data/gathering/user_record.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)

    
    return web.send_static_file('subscribe.html')


