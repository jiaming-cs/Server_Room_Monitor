from flask import Flask, Response, request, render_template
import json
import pandas as pd
from os.path import abspath, dirname
from const_ import const
import csv
from message_sending.email_message import EmailSending
from data_gathering.get_temp_humi import get_data
import MySQLdb


web = Flask(__name__)

@web.route('/api/gettmp',methods=["GET", "POST"])
def draw_stone():
    data = get_data()
    print(data)
    return Response(json.dumps(data),  mimetype='application/json')
    

@web.route('/')
def staff_page():
    return render_template('/index.html')


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
    if len(name)>30:
        return render_template('/temp1.html', title="Your Nmae Is Too Long",\
        top_info = "Oops, Some Errors",\
        boto_info = "Please input another name with shorter length.")
    if not validateEmail(email_addr):
        return render_template('/temp1.html', title="Invalid Email Address",\
        top_info = "Oops, Some Errors",\
        boto_info = "{email} is not a vailid email address.".format(email_addr))
    if (not phone.isdigit()) or len(phone)!=10:
        return render_template('/temp1.html', title="Invalid Phone Number",\
        top_info = "Oops, Some Errors",\
        boto_info = "{phone} is not a vailid US phone number.".format(email_addr))
    db = MySQLdb.connect(host = "52.43.93.127", user = "root", passwd = "ljm960704519", db = "server")
    cursor = db.cursor()
    sql = "select email from users where email = '{email}';".format(email = email_addr)
    cursor.execute(sql)
    flag = len(cursor.fetchall())
    if (flag == 0):
        try:
            sql = "insert into users values('{name}','{email}','{phone}');".format(name = name, email = email_addr, phone = phone)
            cursor.execute(sql)
            db.commit()
            em = EmailSending()
            em.send_confirm_email(name, email_addr)
            db.close()
            print("subscribe")
            return render_template('/temp1.html', title="Successul",\
            top_info = "Welcome, {name}".format(name = name),\
            boto_info = "You have successfully subscribe the message notification with {email}.".format( email = email_addr))
        except:
            sql = "delet from users where email = '{email}'".format(email = email)
            cursor.execute(sql)
            db.commit()
            db.close()
            return render_template('/temp1.html', title="Unknow Error",\
            top_info = "Oops, Some Errors",\
            boto_info = "{name}, unknow errors, please subscribe again!".format(name = name))

    else:
        db.close()
        return render_template('/temp1.html', title="You Have Already Subscribed",\
        top_info = "Oops, Some Errors",\
        boto_info = "{name}, The email address {email} has alreay subscribed our notification.".format(name = name, email = email_addr))


@web.route("/unsubscribe", methods = ["POST"])
def unsubscribe():
    postData = request.form 
    email_addr = request.form.get('Email')
    db = MySQLdb.connect(host = "52.43.93.127", user = "root", passwd = "ljm960704519", db = "server")
    cursor = db.cursor()
    sql = "delete from users where email = '{email}';".format(email = email_addr)
    cursor.execute(sql)
    db.commit()
    db.close()
    return render_template('/temp1.html', title="Successul Unsubscribe",\
        top_info = "See  You  Again",\
        boto_info = "You will stop receiving messages from {email}.".format(email = email_addr))

   
if __name__ == "__main__":
    web.run("0.0.0.0", debug=True)
    
    


