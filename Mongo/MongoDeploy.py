#!/usr/bin/env python
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://192.168.99.100:27017/')
db = client.FilRouge
collection = db.data

post = {"Faux":"Faux"}
post_id = collection.insert_one(post).inserted_id
x=post_id
result = collection.delete_one({'_id': ObjectId(x)})
print(result)