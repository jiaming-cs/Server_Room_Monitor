import socket
import json
import csv
from os.path import abspath, dirname, exists



def get_data():
    def parse_time(time_str:str):
        m = time_str.split(":")[1]
        return int(m)

    port = 5001
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", port))
    recieved = sock.recvfrom(1024)
    received_str = recieved[0].decode("utf-8")
    received_str = received_str.replace("'", '"')
    json_obj = json.loads(received_str)
    data = json_obj["data"]
    time_str = json_obj["time"]
    
    if exists(abspath(dirname(__file__))+"/data_record.csv"):
        pre_min = 0
        now_min = 0
        with open(abspath(dirname(__file__))+"/data_record.csv", 'r', newline='') as f:
            pre_line = f.readlines()[-1]
            pre_min = parse_time(pre_line)
            now_min = parse_time(time_str)
            f.close()
        if pre_min != now_min:
            with open(abspath(dirname(__file__))+"/data_record.csv", 'a', newline='') as f:
                wt = csv.writer(f)
                wt.writerow([time_str, data['temp'], data['humidity']])
                f.close()
    else:
        with open(abspath(dirname(__file__))+"/data_record.csv", 'a', newline='') as f:
            wt = csv.writer(f)
            wt.writerow([time_str, data['temp'], data['humidity']])
            f.close()
    return data

