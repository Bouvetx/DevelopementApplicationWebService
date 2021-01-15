#!/usr/bin/env python
from pymongo import MongoClient
import datetime , time , pprint
from bson.son import SON

client = MongoClient('mongodb://192.168.99.100:27017/')
db = client.FilRouge
collection = db.data

pipeline = [{"$match": {"SENSOR": "Temp1"}},{ "$sort" : { "DATE" : -1 } },{ "$limit" : 1 }]
pprint.pprint(list(collection.aggregate(pipeline)))

d1 = 10
# time.sleep(10)
d2 = 20

pipeline = [{"$match": {"DATE": {"$gte": d1 , "$lte": d2},"SENSOR": "Temp1"}},{"$group": {"_id": { "SENSOR" : "$SENSOR" } , "average": {"$avg": "$VALUE"}}}]
pprint.pprint(list(collection.aggregate(pipeline)))

pipeline = [{"$match": {"DATE": {"$gte": d1 , "$lte": d2},"SENSOR": "Temp1"}},{"$group": {"_id": { "SENSOR" : "$SENSOR" } , "minimum": {"$min": "$VALUE"}}}]
pprint.pprint(list(collection.aggregate(pipeline)))

