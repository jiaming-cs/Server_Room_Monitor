from flask import Flask, Response, request
import Adafruit_DHT
import json
import pandas as pd
from os.path import abspath, dirname
from const_ import const
import csv
from message_sending.email_message import EmailSending


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
    import re
    def validateEmail(email):
        if len(email) > 7:
            if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
                return True
        return False
    postData = request.form 
    name = request.form.get('Name') 
    email_addr = request.form.get('Email')
    phone = request.form.get('Phone Number')
    print(name)
    print(email_addr)
    print(phone)
    with open(abspath(dirname(__file__))+"/data_gathering/user_record.csv", "a") as csv_file:
        user_data = []
        user_data = [name, email_addr, phone]
        try:
            es = EmailSending()
            es.send_confirm_email(user_data)
            if not validateEmail(user_data[1]):
                return web.send_static_file('unsuccessful.html')
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(user_data)
            print("subscribe")
            return web.send_static_file('subscribe.html')

        except:
            print("Invalid email address!")
            return web.send_static_file('unsuccessful.html')


@web.route("/unsubscribe", methods = ["POST"])
def unsubscribe():
    
    postData = request.form 
   
    email_addr = request.form.get('Email')

    df = pd.read_csv(abspath(dirname(__file__))+"/data_gathering/user_record.csv") 
    old_row_number = df.shape[0]
    df = df[df['email'] != email_addr]
    new_row_number = df.shape[0]
    

    if(new_row_number < old_row_number):
        df.to_csv(abspath(dirname(__file__))+"/data_gathering/user_record.csv", index=0)
        return web.send_static_file('unsubscribe.html')
    else:
        print("errors!")
        return web.send_static_file('unsuccessful.html')
    
    


