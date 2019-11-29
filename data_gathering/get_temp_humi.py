import socket
import json
import csv
from os.path import abspath, dirname, exists

def get_data():
    port = 5001
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", port))
    try:
        sock.settimeout(3.0)
        recieved = sock.recvfrom(1024)
        received_str = recieved[0].decode("utf-8")
        received_str = received_str.replace("'", '"')
        json_obj = json.loads(received_str)
        data = json_obj["data"]
    except:
        print("Time out!")
        data = {}
        data['temp'] = -1
        data['humidity'] = -1
    return data

