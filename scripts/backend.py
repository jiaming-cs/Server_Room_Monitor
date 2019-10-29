from flask import Flask, Response, request
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

@web.rout("/subscribe/", methods = ["GET", "POST"])
def subscribe():
    getData = request.args # 利用request对象获取GET请求数据
    print('获取的GET数据为：', getData) # 打印获取到的GET数据 ImmutableMultiDict([])
    postData = request.form # 利用request对象获取POST请求数据
    print('获取的POST数据为：', postData) # 打印获取到的POST请求 ImmutableMultiDict([('username', '456'), ('password', '789')])
    #username = request.form.get('username') 
    #assword = request.form.get('password')
    #print(username,password) #456 789
    #return '这是测试页面'


