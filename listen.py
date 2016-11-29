import serial
import json
import ast
from pymongo import MongoClient
from time import gmtime, strftime

ser = serial.Serial('COM3', 9600)

client = MongoClient('192.168.1.104', 2019)
db = client.emas
stream = db.stream


def is_json(myjson):
        try:
                json_object = json.loads(myjson)
        except ValueError, e:
                return False
        return True
while 1:
        map = {}
        serialData = ser.readline().rstrip('\n\r')
        map = json.dumps(serialData)
        map = json.loads(map)
        if is_json(map):
                data = ast.literal_eval(map)
                data['time'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())  # #datetime.datetime.utcnow())
                inserted_id = stream.insert(data)
                print serialData
        


