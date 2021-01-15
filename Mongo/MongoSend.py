#!/usr/bin/env python
from pymongo import MongoClient
import datetime , random , time

client = MongoClient('mongodb://192.168.99.100:27017/')
db = client.FilRouge
collection = db.data
value=20
temps=0
while(1):
    post = {"SENSOR":"Temp1","DATE":temps, "VALUE":value}
    post_id = collection.insert_one(post).inserted_id
    print(post_id)
    value=value+random.uniform(-0.5, 0.5)
    temps=temps+1
    time.sleep(1)
