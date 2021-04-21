import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://karansiamintern:1234@cluster0.4sl4c.mongodb.net/my_database?retryWrites=true&w=majority")

db = cluster["my_database"]
collection = db["my_collection"]

post = {"_id" : 0, "name" : "karan" , "hometown" : "chennai"}

collection.insert_one(post)
