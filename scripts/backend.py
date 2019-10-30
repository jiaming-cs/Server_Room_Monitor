from flask import Flask, Response, request
import Adafruit_DHT
import json
import pandas as pd
from os.path import abspath, dirname
from const_ import const


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
    getData = request.args # 利用request对象获取GET请求数据
    print('获取的GET数据为：', getData) # 打印获取到的GET数据 ImmutableMultiDict([])
    postData = request.form # 利用request对象获取POST请求数据
    print('获取的POST数据为：', postData) # 打印获取到的POST请求 ImmutableMultiDict([('username', '456'), ('password', '789')])
    name = request.form.get('Name') 
    email = request.form.get('Email')
    phone_number = request.form.get('Phone Number')
    print(name)
    print(email)
    print(phone_number)
    
    return web.send_static_file('subscribe.html')


