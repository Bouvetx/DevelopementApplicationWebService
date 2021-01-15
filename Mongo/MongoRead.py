#!/usr/bin/env python
from pymongo import MongoClient
import random , time , pprint

client = MongoClient('mongodb://192.168.99.100:27017/')
db = client.FilRouge
collection = db.data
pprint.pprint(collection.find_one())
time.sleep(1)
