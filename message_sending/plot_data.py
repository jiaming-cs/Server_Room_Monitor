from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from os.path import abspath, dirname
import time
import MySQLdb
import numpy as np

def get_temp_humi(start_time:str, end_time:str):
    db = MySQLdb.connect(host = "52.43.93.127", user = "root", passwd = "ljm960704519", db = "server")
    cursor = db.cursor()
    sql = "select * from data where time > '{start}' and time < '{end}';".format(start = start_time, end = end_time)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    db.close()
    return data

    
def get_graph_data(start_time = None, end_time = None, title=None):
    if start_time == None:
        end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        start_time = time.strftime("%Y-%m-%d 00:00:00", time.localtime())
    data = get_temp_humi(start_time, end_time)
    temp = []
    humi = []
    time_str = []
    for d in data:
        temp.append(d[0])
        humi.append(d[1])
        time_str.append(d[2].strftime("%H:%M"))

    temp_max = max(temp)
    temp_min = min(temp)
    temp_mean = round(np.mean(temp))

    humi_max = max(humi)
    humi_min = min(humi)
    humi_mean = round(np.mean(humi), 2)

    critical_info = {}
    critical_info["temp_max"] = temp_max
    critical_info["temp_min"] = temp_min
    critical_info["temp_avg"] = temp_mean

    critical_info["humi_max"] = humi_max
    critical_info["humi_min"] = humi_min
    critical_info["humi_avg"] = humi_mean
    critical_info["end_time"] = end_time
    critical_info["start_time"] = start_time


    tick_spacing = int(len(data)/10)+1
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(time_str, temp, 'r', label="Temperature")
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax1.set_ylabel('Temperature / F')
    if title == None:
        title = "Sever Room Temperature and Huminity Report\n"+time.strftime("%a, %b %d, %Y", time.localtime())
    ax1.set_title(title)
    ax1.set_xlabel("Time (h:m)")
    ax2 = ax1.twinx()  
    ax2.plot(time_str, humi, 'b', label="Humidity")
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    ax2.set_ylabel('Huminity / %')
    fig.legend(loc="upper right", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.savefig(abspath(dirname(__file__))+"/graphs/"+"temp_humi_graph.png")
    
    return critical_info
    

get_graph_data()
