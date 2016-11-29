import pico
import pymongo
import time
from bson.json_util import dumps
from json import loads
client = pymongo.MongoClient('192.168.1.101', 2019)
db = client.emas
stream = db.stream
avg =  db.avg



def data():
    fullData = stream.find({},{'_id': 0}).sort('_id',pymongo.DESCENDING)
    json = dumps(fullData)
    return loads(json)

def cur1():
    phaseCur = stream.find({},{'cur1': 1,'_id': 0}).limit(50)
    json = dumps(phaseCur)
    return loads(json)

def cur2():
    phaseCur2 = stream.find({},{'cur2': 1,'_id': 0}).limit(50)
    json = dumps(phaseCur2)
    return loads(json)

def cur3():
    phaseCur3 = stream.find({},{'cur3': 1,'_id': 0}).limit(50)
    json = dumps(phaseCur3)
    return loads(json)


def volt1():
    phaseVolt = stream.find({},{'volt1': 1,'_id': 0}).limit(50)
    json = dumps(phaseVolt)
    return loads(json)

def volt2():
    phaseVolt2 = stream.find({},{'volt2': 1,'_id': 0}).limit(50)
    json = dumps(phaseVolt2)
    return loads(json)

def volt3():
    phaseVolt3 = stream.find({},{'volt3': 1,'_id': 0}).limit(50)
    json = dumps(phaseVolt3)
    return loads(json)


def time():
    time = stream.find({},{'time': 1,'_id': 0}).limit(50).sort('_id',pymongo.DESCENDING)
    json = dumps(time)
    return loads(json)

def pred():
    pred = avg.find({}).sort('_id',pymongo.DESCENDING)
    json = dumps(pred)
    return loads(json)



def hello():
    return "Hello World"
