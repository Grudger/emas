from __future__ import print_function
import pandas as pd
import pymongo
from bson.json_util import dumps
import statsmodels.tsa.arima_model as ari

client = pymongo.MongoClient('192.168.1.101', 2019)
db = client.emas
stream = db.stream
avg =  db.avg

cursor = dumps(db.stream.find({}, {'_id': 0}))
df = pd.read_json(cursor)
totalEntries = len(df)

df['time'] = df['time'].apply(pd.to_datetime)
df['load'] = df['volt1'] * df['cur1']


tsload = df['load']
df.index = df['time']

start = totalEntries - totalEntries + 50
end = totalEntries + 50

model = ari.ARMA(df['load'], (2, 1))
ar_res = model.fit()

a = (ar_res.predict(start, end))

b = a.tolist()
# print(b)
for item in b:
    avg.insert({'pred': item})
