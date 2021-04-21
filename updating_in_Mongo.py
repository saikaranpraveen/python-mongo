import pymongo
from pymongo import MongoClient

my_client = MongoClient("mongodb+srv://karansiamintern:1234@cluster0.4sl4c.mongodb.net/my_database?retryWrites=true&w=majority")
my_db = my_client["my_database"]
my_collection = my_db["my_collection"]

my_query = {"name" : "karan"}
new_value = { "$set" : {"name" : "John Doe"}}

my_collection.update_one(my_query, new_value)

for x in my_collection.find(): #printing after updating
    print(x)